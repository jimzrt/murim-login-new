#!/usr/bin/env python3
"""Run the next chapter deterministically, master it, and checkpoint it."""

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

from cost_report import build_report, format_report, format_resource_report
from run_lock import hold_run_lock
from workflow import command_committed, command_master, incomplete_chapter, interval_due, paths, project_config

TRANSLATION_RE = re.compile(r"^translations/(\d{4})\.md$")
WORKFLOW_ACTION_RE = re.compile(r"^python tools/workflow\.py ([a-z]+) (\d+)$")


def next_chapter() -> int:
    state = (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8")
    match = re.search(r"^- Next chapter:\s*(\d+)\s*$", state, re.MULTILINE)
    if not match:
        raise SystemExit("docs/STATE.md has no exact '- Next chapter: N' line")
    return int(match.group(1))


def git(*args: str, capture: bool = True) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=capture, check=True,
    )
    return result.stdout.strip() if capture else ""


def changed_paths() -> list[str]:
    tracked = git("diff", "--name-only").splitlines()
    untracked = git("ls-files", "--others", "--exclude-standard").splitlines()
    return sorted(set(filter(None, tracked + untracked)))


def allowed_change(path: str, chapter: int) -> bool:
    if path in {"docs/STATE.md", "docs/CONTEXT.json", "docs/NAMES.md", "compendium.md"}:
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
    return path.startswith("characters/") and not path.startswith("characters/spoilers/")


def require_repository(chapter: int, *, resume: bool) -> None:
    try:
        git("rev-parse", "--verify", "HEAD")
        dirty = changed_paths()
    except subprocess.CalledProcessError as error:
        raise SystemExit(error.stderr.strip() or "project must be an initialized Git repository") from None
    if not resume and dirty:
        raise SystemExit("working tree must be clean before run_next; commit or stash existing changes")
    unexpected = [path for path in dirty if not allowed_change(path, chapter)]
    if unexpected:
        raise SystemExit("working tree has unexpected changes: " + ", ".join(unexpected))


def workflow_status(chapter: int) -> dict:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "workflow.py"), "status", str(chapter), "--json"],
        cwd=ROOT, text=True, capture_output=True,
    )
    if result.returncode:
        raise SystemExit(result.stderr.strip() or result.stdout.strip() or "workflow status failed")
    try:
        value = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise SystemExit(f"workflow status returned invalid JSON: {error}") from None
    if not isinstance(value, dict):
        raise SystemExit("workflow status must return one JSON object")
    return value


def run_workflow_command(chapter: int, action: str) -> None:
    match = WORKFLOW_ACTION_RE.fullmatch(action)
    if not match or int(match.group(2)) != chapter:
        raise SystemExit(
            f"workflow requires manual action before it can continue:\n{action}\n"
            f"Complete it, then rerun python tools/run_next.py."
        )
    command = match.group(1)
    if command in {"status", "master", "committed"}:
        raise SystemExit(f"workflow returned forbidden automatic action: {action}")
    print(f"→ workflow {command} {chapter}", flush=True)
    started = time.monotonic()
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "workflow.py"), command, str(chapter)],
        cwd=ROOT,
    )
    elapsed = round(time.monotonic() - started)
    if result.returncode:
        raise SystemExit(f"workflow {command} failed with exit code {result.returncode}")
    print(f"✓ workflow {command} {chapter}  {elapsed}s", flush=True)


def run_to_accepted(chapter: int, lock) -> None:
    for _ in range(32):
        status = workflow_status(chapter)
        stage = status.get("stage")
        if stage == "ACCEPTED":
            return
        if stage == "COMMITTED":
            raise SystemExit(f"chapter {chapter} is already committed")
        action = status.get("next_action")
        if not isinstance(action, str) or not action:
            raise SystemExit("workflow status returned no next action")
        lock.update(stage=str(stage))
        run_workflow_command(chapter, action)
    raise SystemExit("workflow exceeded 32 deterministic transitions")


def print_cost_report(chapter: int) -> None:
    report = build_report(live_usage=True)
    print(flush=True)
    print(format_report(report, chapter), flush=True)
    print(flush=True)
    print(format_resource_report(report), flush=True)


def commit_accepted(chapter: int) -> None:
    transaction = json.loads(paths(chapter)["state"].read_text(encoding="utf-8"))
    if transaction.get("stage") != "ACCEPTED":
        raise SystemExit(f"workflow stopped at {transaction.get('stage')}; expected ACCEPTED")
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
    print(f"Chapter {chapter}: COMMITTED", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    in_progress = incomplete_chapter()
    chapter = in_progress if in_progress is not None else next_chapter()
    state_path = paths(chapter)["state"]
    stage = json.loads(state_path.read_text(encoding="utf-8")).get("stage") if state_path.exists() else None
    label = "resume" if in_progress is not None else "starting"
    with hold_run_lock(ROOT, holder="run_next", chapter=chapter, stage=stage or label) as lock:
        require_repository(chapter, resume=in_progress is not None)
        print(f"Chapter {chapter}: {label}", flush=True)
        if stage != "ACCEPTED":
            run_to_accepted(chapter, lock)
        print(f"Chapter {chapter}: mastering", flush=True)
        lock.update(stage="mastering")
        command_master(chapter)
        print_cost_report(chapter)
        lock.update(stage="committing")
        commit_accepted(chapter)
        lock.update(stage="COMMITTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
