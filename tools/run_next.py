#!/usr/bin/env python3
"""Run the next chapter, show live progress, record exact usage, and checkpoint it."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from cost_report import build_report, format_report, usage_line
from omp_json import EventCapture, OmpJsonError
from workflow import command_committed, interval_due, paths, project_config, record_metric

TRANSLATION_RE = re.compile(r"^translations/(\d{4})\.md$")
WORKFLOW_RE = re.compile(r"(?:python\s+)?tools/workflow\.py\s+(\S+)(?:\s+(\d+))?")
DETAIL_LIMIT = 160
HUB_LIMIT = 80


def next_chapter() -> int:
    state = (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8")
    match = re.search(r"^- Next chapter:\s*(\d+)\s*$", state, re.MULTILINE)
    if not match:
        raise SystemExit("docs/STATE.md has no exact '- Next chapter: N' line")
    return int(match.group(1))


def git(*args: str, capture: bool = True) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True,
        capture_output=capture, check=True,
    )
    return result.stdout.strip() if capture else ""


def require_clean_repository() -> str:
    try:
        head = git("rev-parse", "--verify", "HEAD")
        dirty = git("status", "--porcelain")
    except subprocess.CalledProcessError as error:
        raise SystemExit(error.stderr.strip() or "project must be an initialized Git repository") from None
    if dirty:
        raise SystemExit("working tree must be clean before run_next; commit or stash existing changes")
    return head


def changed_paths() -> list[str]:
    tracked = git("diff", "--name-only").splitlines()
    untracked = git("ls-files", "--others", "--exclude-standard").splitlines()
    return sorted(set(filter(None, tracked + untracked)))


def allowed_change(path: str, chapter: int) -> bool:
    if path in {"docs/STATE.md", "docs/CONTEXT.json", "compendium.md"}:
        return True
    match = TRANSLATION_RE.fullmatch(path)
    if match:
        other = int(match.group(1))
        if other == chapter:
            return True
        if not interval_due(chapter, "checkpoint_review_interval"):
            return False
        start = chapter - int(project_config()["checkpoint_review_interval"]) + 1
        return start <= other <= chapter
    if path.startswith("reviews/") or path.startswith("summaries/"):
        return True
    if path.startswith("characters/") and not path.startswith("characters/spoilers/"):
        return True
    return False


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def truncate(text: str, limit: int = DETAIL_LIMIT) -> str:
    text = collapse(text)
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def first_string(args: dict, *keys: str) -> str:
    for key in keys:
        value = args.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def workflow_label(command: str) -> str | None:
    match = WORKFLOW_RE.search(command)
    if not match:
        return None
    label = f"workflow {match.group(1)}"
    if match.group(2):
        label += f" {match.group(2)}"
    return label


def summarize_tool_args(tool: str, args: object) -> str:
    if not isinstance(args, dict):
        return ""
    name = (tool or "tool").lower()
    if name == "bash":
        command = first_string(args, "command")
        return workflow_label(command) or truncate(command)
    if name in {"read", "write", "edit"}:
        return first_string(args, "path", "file_path", "target_notebook")
    if name == "grep":
        return truncate(f"{first_string(args, 'pattern')} {first_string(args, 'path')}".strip())
    if name == "glob":
        return first_string(args, "glob_pattern", "pattern")
    if name == "hub":
        return truncate(first_string(args, "description", "prompt", "task", "message", "query"), HUB_LIMIT)
    for key in ("path", "command", "query", "pattern", "glob_pattern", "description"):
        value = first_string(args, key)
        if value:
            return truncate(value)
    return ""


def result_text(result: object) -> str:
    if isinstance(result, str):
        return result
    if not isinstance(result, dict):
        return ""
    content = result.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict) and isinstance(block.get("text"), str):
                parts.append(block["text"])
        return "".join(parts)
    if isinstance(result.get("output"), str):
        return result["output"]
    return ""


def format_status_result(text: str) -> str | None:
    stage = None
    next_action = None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Stage:"):
            stage = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Next action:"):
            next_action = stripped.split(":", 1)[1].strip()
    if not stage:
        return None
    if next_action:
        return f"{stage}; next: {next_action}"
    return stage


def format_elapsed(seconds: float | None) -> str:
    if seconds is None or seconds < 1:
        return ""
    return f"{round(seconds)}s"


def format_tool_start(event: dict) -> str:
    tool = event.get("toolName") or "tool"
    detail = summarize_tool_args(tool, event.get("args"))
    if detail.startswith("workflow "):
        return f"→ {detail}"
    if detail:
        return f"→ {tool}  {detail}"
    return f"→ {tool}"


class ProgressRenderer:
    """Turn OMP tool events into one-line progress records."""

    def __init__(self, clock=time.monotonic):
        self._clock = clock
        self._started: dict[str, float] = {}
        self._bash: dict[str, str] = {}

    def line(self, event: dict) -> str | None:
        kind = event.get("type")
        if kind == "tool_execution_start":
            call_id = event.get("toolCallId")
            args = event.get("args") if isinstance(event.get("args"), dict) else {}
            if isinstance(call_id, str):
                self._started[call_id] = self._clock()
                command = args.get("command")
                if isinstance(command, str):
                    self._bash[call_id] = command
            return format_tool_start(event)
        if kind == "tool_execution_end":
            return self._end_line(event)
        return None

    def _end_line(self, event: dict) -> str:
        tool = event.get("toolName") or "tool"
        marker = "✗" if event.get("isError") else "✓"
        call_id = event.get("toolCallId")
        elapsed = None
        command = ""
        if isinstance(call_id, str):
            started = self._started.pop(call_id, None)
            if started is not None:
                elapsed = self._clock() - started
            command = self._bash.pop(call_id, "")
        time_bit = format_elapsed(elapsed)
        label = workflow_label(command)
        if label and label.split()[1] == "status":
            status = format_status_result(result_text(event.get("result")))
            if status:
                return f"{marker} {status}" + (f"  {time_bit}" if time_bit else "")
        if label:
            return f"{marker} {time_bit}" if time_bit else f"{marker} {label}"
        if time_bit:
            return f"{marker} {tool}  {time_bit}"
        return f"{marker} {tool}"


def render_event(event: dict, renderer: ProgressRenderer | None = None) -> None:
    kind = event.get("type")
    if kind == "message_update":
        update = event.get("assistantMessageEvent", {})
        if isinstance(update, dict) and update.get("type") == "text_delta":
            print(update.get("delta", ""), end="", flush=True)
        return
    active = renderer or ProgressRenderer()
    line = active.line(event)
    if line:
        prefix = "\n" if kind == "tool_execution_start" else ""
        print(f"{prefix}{line}", flush=True)


def print_cost_report(chapter: int) -> None:
    report = build_report()
    print(flush=True)
    print(format_report(report, chapter), flush=True)
    print(usage_line("Project total", report["totals"]), flush=True)


def run_coordinator(chapter: int, model: str) -> dict:
    prompt = (
        f"Complete chapter {chapter} through ACCEPTED and then stop. "
        "Do not commit and do not run workflow.py committed; the wrapper owns the checkpoint."
    )
    command = ["omp", "--mode", "json", "--no-session", "--model", model, prompt]
    capture = EventCapture(model)
    renderer = ProgressRenderer()
    started = time.monotonic()
    process = subprocess.Popen(command, cwd=ROOT, text=True, stdout=subprocess.PIPE)
    assert process.stdout is not None
    try:
        for line_number, line in enumerate(process.stdout, 1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as error:
                process.terminate()
                raise OmpJsonError(f"invalid OMP JSON event on line {line_number}: {error}") from None
            if not isinstance(event, dict):
                process.terminate()
                raise OmpJsonError(f"OMP JSON event on line {line_number} is not an object")
            capture.consume(event)
            render_event(event, renderer)
    except BaseException:
        process.terminate()
        raise
    finally:
        return_code = process.wait()
    if return_code:
        raise SystemExit(f"OMP coordinator failed with exit code {return_code}")
    _, metrics = capture.finish()
    metrics["elapsed_seconds"] = round(time.monotonic() - started, 3)
    return metrics


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=project_config().get("coordinator_model", project_config()["draft_model"]))
    args = parser.parse_args()
    chapter = next_chapter()
    starting_head = require_clean_repository()
    print(f"Chapter {chapter}: starting", flush=True)
    try:
        metrics = run_coordinator(chapter, args.model)
    except OmpJsonError as error:
        raise SystemExit(str(error)) from None
    if git("rev-parse", "--verify", "HEAD") != starting_head:
        raise SystemExit("coordinator committed unexpectedly; exact coordinator usage was not checkpointed")
    transaction = json.loads(paths(chapter)["state"].read_text(encoding="utf-8"))
    if transaction.get("stage") != "ACCEPTED":
        raise SystemExit(f"coordinator stopped at {transaction.get('stage')}; expected ACCEPTED")
    record_metric(paths(chapter), "coordinator_model", **metrics)
    print_cost_report(chapter)
    changes = changed_paths()
    unexpected = [path for path in changes if not allowed_change(path, chapter)]
    if unexpected:
        raise SystemExit("refusing to commit unexpected paths: " + ", ".join(unexpected))
    if not changes:
        raise SystemExit("workflow reached ACCEPTED without checkpointable changes")
    print(f"Committing {len(changes)} files:", flush=True)
    for path in changes:
        print(f"  {path}", flush=True)
    git("add", "-A")
    git("commit", "-m", f"Accept Chapter {chapter}", capture=False)
    command_committed(chapter, "HEAD")
    print(
        f"Chapter {chapter}: COMMITTED — {metrics['input_tokens']} input, "
        f"{metrics['output_tokens']} output coordinator tokens",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
