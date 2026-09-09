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
COORDINATOR_OVERLAY = ROOT / ".omp" / "coordinator-overlay.yml"
COORDINATOR_MAX_TIME = 7200
COORDINATOR_TOOLS = "bash,read,write,edit"
FORBIDDEN_TOOLS = {"hub", "task"}
RESULT_LIMIT = 800
GENERIC_ARG_LIMIT = 4000
COORDINATOR_SYSTEM = (
    "Run only the exact next python tools/workflow.py command reported by status. "
    "Wait for each bash command to finish. Never background a command, never use hub "
    "or task, and never start a nested agent. Do not commit and do not run "
    "workflow.py committed."
)


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


def truncate(text: str, limit: int) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def first_string(args: dict, *keys: str) -> str:
    for key in keys:
        value = args.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def event_args(event: dict) -> dict:
    for key in ("args", "arguments", "input", "params"):
        value = event.get(key)
        if isinstance(value, dict):
            return value
    return {}


def workflow_label(command: str) -> str | None:
    match = WORKFLOW_RE.search(command)
    if not match:
        return None
    label = f"workflow {match.group(1)}"
    if match.group(2):
        label += f" {match.group(2)}"
    return label


def format_scalar_extras(args: dict, skip: set[str] | None = None) -> str:
    bits: list[str] = []
    ignored = skip or set()
    names = (
        ("timeout", "timeout"),
        ("timeout_ms", "timeout_ms"),
        ("timeoutMs", "timeout_ms"),
        ("timeoutSeconds", "timeout_s"),
        ("cwd", "cwd"),
        ("working_directory", "cwd"),
        ("background", "background"),
        ("block_until_ms", "block_until_ms"),
        ("wait", "wait"),
        ("wait_ms", "wait_ms"),
    )
    seen: set[str] = set()
    for key, label in names:
        if key in ignored or key not in args or key in seen:
            continue
        value = args[key]
        if value in (None, "", False):
            continue
        seen.add(key)
        bits.append(f"{label}={value}")
    return ", ".join(bits)


def format_generic_args(args: dict) -> str:
    parts: list[str] = []
    for key in sorted(args):
        value = args[key]
        if value is None or value == "":
            continue
        if isinstance(value, bool):
            parts.append(f"{key}={str(value).lower()}")
        elif isinstance(value, (int, float)):
            parts.append(f"{key}={value}")
        elif isinstance(value, str):
            text = value.strip()
            if "\n" in text or len(text) > 160:
                indented = "\n    ".join(text.splitlines())
                parts.append(f"{key}:\n    {indented}")
            else:
                parts.append(f"{key}={collapse(text)}")
        else:
            parts.append(f"{key}={truncate(json.dumps(value, ensure_ascii=False, default=str), 500)}")
    return truncate("\n  ".join(parts), GENERIC_ARG_LIMIT)


def format_tool_detail(tool: str, args: object) -> str:
    if not isinstance(args, dict) or not args:
        return ""
    name = (tool or "tool").lower()
    if name == "bash":
        command = first_string(args, "command")
        extra = format_scalar_extras(args, skip={"command"})
        if command and extra:
            return f"{command}  ({extra})"
        return command or extra
    return format_generic_args(args)


def summarize_tool_args(tool: str, args: object) -> str:
    return format_tool_detail(tool, args)


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
    if isinstance(result.get("error"), str):
        return result["error"]
    return truncate(json.dumps(result, ensure_ascii=False, default=str), RESULT_LIMIT)


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


def result_needs_snippet(text: str, is_error: bool) -> bool:
    if not text.strip():
        return False
    if is_error:
        return True
    lowered = text.lower()
    return any(token in lowered for token in ("timed out", "timeout", "background", "still running", "error"))


def format_tool_start(tool: str, args: dict) -> str:
    detail = format_tool_detail(tool, args)
    if not detail:
        return f"→ {tool}"
    if "\n" in detail:
        return f"→ {tool}\n  {detail}"
    return f"→ {tool}  {detail}"


def reject_forbidden_tool(event: dict) -> None:
    if event.get("type") != "tool_execution_start":
        return
    name = str(event.get("toolName") or "").lower()
    if name not in FORBIDDEN_TOOLS:
        return
    detail = format_tool_detail(name, event_args(event)) or "(no arguments)"
    raise SystemExit(f"coordinator used forbidden tool {name}: {collapse(detail)}")


def coordinator_command(chapter: int, model: str) -> list[str]:
    prompt = (
        f"Complete chapter {chapter} through ACCEPTED and then stop. "
        "Do not commit and do not run workflow.py committed; the wrapper owns the checkpoint."
    )
    return [
        "omp",
        "--mode",
        "json",
        "--no-session",
        "--no-extensions",
        "--no-skills",
        "--no-lsp",
        "--no-pty",
        "--tools",
        COORDINATOR_TOOLS,
        "--config",
        str(COORDINATOR_OVERLAY),
        "--model",
        model,
        "--max-time",
        str(COORDINATOR_MAX_TIME),
        "--auto-approve",
        "--append-system-prompt",
        COORDINATOR_SYSTEM,
        prompt,
    ]


class ProgressRenderer:
    """Turn OMP tool events into one-line progress records."""

    def __init__(self, clock=time.monotonic):
        self._clock = clock
        self._started: dict[str, float] = {}
        self._calls: dict[str, tuple[str, dict]] = {}
        self._in_text = False

    def write_text(self, delta: str) -> None:
        if not delta:
            return
        if not self._in_text:
            print("\n", end="", flush=True)
            self._in_text = True
        print(delta, end="", flush=True)

    def finish_text(self) -> None:
        if self._in_text:
            print(flush=True)
            self._in_text = False

    def line(self, event: dict) -> str | None:
        kind = event.get("type")
        if kind == "tool_execution_start":
            self.finish_text()
            call_id = event.get("toolCallId")
            args = event_args(event)
            tool = str(event.get("toolName") or "tool")
            if isinstance(call_id, str):
                self._started[call_id] = self._clock()
                self._calls[call_id] = (tool, args)
            return format_tool_start(tool, args)
        if kind == "tool_execution_end":
            self.finish_text()
            return self._end_line(event)
        return None

    def _end_line(self, event: dict) -> str:
        call_id = event.get("toolCallId")
        tool = str(event.get("toolName") or "tool")
        args: dict = {}
        if isinstance(call_id, str):
            started = self._started.pop(call_id, None)
            recorded = self._calls.pop(call_id, None)
            elapsed = None if started is None else self._clock() - started
            if recorded:
                tool, args = recorded
        else:
            elapsed = None
        is_error = bool(event.get("isError"))
        marker = "✗" if is_error else "✓"
        command = first_string(args, "command")
        label = workflow_label(command)
        time_bit = format_elapsed(elapsed)
        result = result_text(event.get("result"))
        if label and label.split()[1] == "status":
            status = format_status_result(result)
            if status:
                line = f"{marker} {status}"
                return f"{line}  {time_bit}" if time_bit else line
        detail = command or format_tool_detail(tool, args)
        line = f"{marker} {tool}"
        if detail:
            line += f"  {detail}"
        if time_bit:
            line += f"  {time_bit}"
        if result_needs_snippet(result, is_error):
            snippet = truncate(result, RESULT_LIMIT)
            indented = "\n  ".join(snippet.splitlines())
            return f"{line}\n  {indented}"
        return line


def render_event(event: dict, renderer: ProgressRenderer | None = None) -> None:
    active = renderer or ProgressRenderer()
    kind = event.get("type")
    if kind == "message_update":
        update = event.get("assistantMessageEvent", {})
        if isinstance(update, dict) and update.get("type") == "text_delta":
            active.write_text(update.get("delta", "") or "")
        return
    line = active.line(event)
    if line:
        print(line, flush=True)


def print_cost_report(chapter: int) -> None:
    report = build_report()
    print(flush=True)
    print(format_report(report, chapter), flush=True)
    print(usage_line("Project total", report["totals"]), flush=True)


def run_coordinator(chapter: int, model: str) -> dict:
    command = coordinator_command(chapter, model)
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
            reject_forbidden_tool(event)
    except BaseException:
        process.terminate()
        raise
    finally:
        return_code = process.wait()
    renderer.finish_text()
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
