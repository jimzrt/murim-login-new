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

from omp_json import EventCapture, OmpJsonError
from workflow import command_committed, paths, project_config, record_metric


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
    if path == f"translations/{chapter:04d}.md":
        return True
    if path.startswith("reviews/") or path.startswith("summaries/"):
        return True
    if path.startswith("characters/") and not path.startswith("characters/spoilers/"):
        return True
    return False


def render_event(event: dict) -> None:
    kind = event.get("type")
    if kind == "tool_execution_start":
        print(f"\n→ {event.get('toolName', 'tool')}", flush=True)
    elif kind == "tool_execution_end":
        marker = "✗" if event.get("isError") else "✓"
        print(f"{marker} {event.get('toolName', 'tool')}", flush=True)
    elif kind == "message_update":
        update = event.get("assistantMessageEvent", {})
        if isinstance(update, dict) and update.get("type") == "text_delta":
            print(update.get("delta", ""), end="", flush=True)


def run_coordinator(chapter: int, model: str) -> dict:
    prompt = (
        f"Complete chapter {chapter} through ACCEPTED and then stop. "
        "Do not commit and do not run workflow.py committed; the wrapper owns the checkpoint."
    )
    command = ["omp", "--mode", "json", "--no-session", "--model", model, prompt]
    capture = EventCapture(model)
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
            render_event(event)
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
    changes = changed_paths()
    unexpected = [path for path in changes if not allowed_change(path, chapter)]
    if unexpected:
        raise SystemExit("refusing to commit unexpected paths: " + ", ".join(unexpected))
    if not changes:
        raise SystemExit("workflow reached ACCEPTED without checkpointable changes")
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
