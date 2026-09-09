#!/usr/bin/env python3
"""Deterministic controller for one-chapter translation transactions."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGES = (
    "READY", "CONTEXT_READY", "DRAFTED", "REVIEWED", "REVISED",
    "CHECKPOINT_REVIEWED", "CHECKPOINT_APPLIED", "ACCEPTED", "COMMITTED",
)
HANGUL = re.compile(r"[가-힣]")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def paths(number: int) -> dict[str, Path]:
    work = ROOT / ".work" / f"{number:04d}"
    block_start = number - 4
    block_name = f"{block_start:04d}-{number:04d}"
    return {
        "work": work,
        "state": work / "workflow.json",
        "context": work / "context.md",
        "draft": work / "draft.md",
        "revised": work / "revised.md",
        "revision_context": work / "revision-context.md",
        "translation": ROOT / "translations" / f"{number:04d}.md",
        "packet": ROOT / "reviews" / "packets" / f"{number:04d}.md",
        "report": ROOT / "reviews" / "sol" / f"{number:04d}.md",
        "review_meta": ROOT / "reviews" / "sol" / f"{number:04d}.json",
        "checkpoint_summary": ROOT / "summaries" / f"{block_name}.md",
        "checkpoint_packet": ROOT / "reviews" / "packets" / f"checkpoint-{block_name}.md",
        "checkpoint_report": ROOT / "reviews" / "checkpoints" / f"{block_name}.md",
        "checkpoint_meta": ROOT / "reviews" / "checkpoints" / f"{block_name}.json",
        "checkpoint_disposition": work / "checkpoint-disposition.md",
    }


def source_hash(number: int) -> str:
    try:
        from tools.chapter import extract_chapter
    except ModuleNotFoundError:  # Direct execution from tools/.
        from chapter import extract_chapter

    try:
        source = extract_chapter(number)
    except ValueError as error:
        raise SystemExit(str(error)) from None
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def load(number: int) -> tuple[dict, dict[str, Path]]:
    p = paths(number)
    current_source_hash = source_hash(number)
    if p["state"].exists():
        state = json.loads(p["state"].read_text(encoding="utf-8"))
        if state.get("source_sha256") != current_source_hash:
            raise SystemExit("source changed after this transaction began; stop for manual reconciliation")
    else:
        completed_match = re.search(
            r"^- Last completed:\s*(\d+)\s*$",
            (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8"),
            re.MULTILINE,
        )
        already_accepted = bool(
            completed_match
            and number <= int(completed_match.group(1))
            and p["translation"].exists()
        )
        state = {
            "version": 1,
            "chapter": number,
            "stage": "COMMITTED" if already_accepted else "READY",
            "source_sha256": current_source_hash,
            "artifacts": {},
        }
        if already_accepted:
            state["artifacts"]["translation_sha256"] = digest(p["translation"])
            state["reconciled_legacy_acceptance"] = True
            state["artifacts"]["commit"] = "pre-controller checkpoint"
        atomic_json(p["state"], state)
    return state, p


def require(state: dict, *allowed: str) -> None:
    if state["stage"] not in allowed:
        raise SystemExit(f"stage is {state['stage']}; expected one of: {', '.join(allowed)}")


def save(state: dict, p: dict[str, Path], stage: str, **artifacts: str) -> None:
    state["stage"] = stage
    state["artifacts"].update(artifacts)
    atomic_json(p["state"], state)


def validate_reading_copy(path: Path, number: int) -> None:
    if not path.exists() or not path.read_text(encoding="utf-8").strip():
        raise SystemExit(f"missing or empty reading copy: {path}")
    text = path.read_text(encoding="utf-8")
    first = next((line.strip() for line in text.splitlines() if line.strip()), "")
    if first != f"# Chapter {number}":
        raise SystemExit(f"first nonblank line must be '# Chapter {number}'")
    if HANGUL.search(text):
        raise SystemExit("reading copy contains Hangul; final chapter must be English-only")


def next_action(state: dict, p: dict[str, Path]) -> str:
    number = state["chapter"]
    if state["stage"] == "REVISED" and number % 5 == 4:
        return f"update state and {p['checkpoint_summary'].relative_to(ROOT)}, then: python tools/workflow.py checkpoint {number}"
    return {
        "READY": f"python tools/workflow.py prepare {number}",
        "CONTEXT_READY": f"python tools/workflow.py draft {number}",
        "DRAFTED": f"python tools/workflow.py review {number}",
        "REVIEWED": f"python tools/workflow.py revise {number}",
        "REVISED": f"update compendium/profiles/docs/STATE.md, then: python tools/workflow.py accept {number}",
        "CHECKPOINT_REVIEWED": f"apply or disposition checkpoint findings in {p['checkpoint_disposition'].relative_to(ROOT)}, then: python tools/workflow.py checkpointed {number}",
        "CHECKPOINT_APPLIED": f"python tools/workflow.py accept {number}",
        "ACCEPTED": f"commit accepted files, then: python tools/workflow.py committed {number} --commit HEAD",
        "COMMITTED": "stop; do not begin another chapter",
    }[state["stage"]]


def command_prepare(number: int) -> None:
    state, p = load(number)
    require(state, "READY", "CONTEXT_READY")
    try:
        from tools.context import build_context
    except ModuleNotFoundError:  # Direct execution from tools/.
        from context import build_context

    packet = build_context(number)
    p["context"].parent.mkdir(parents=True, exist_ok=True)
    atomic_text(p["context"], packet)
    save(state, p, "CONTEXT_READY", context_sha256=digest(p["context"]))


def command_drafted(number: int) -> None:
    state, p = load(number)
    require(state, "CONTEXT_READY", "DRAFTED")
    validate_reading_copy(p["draft"], number)
    save(state, p, "DRAFTED", draft_sha256=digest(p["draft"]))


def run_omp(packet: Path, model: str, timeout: int) -> str:
    command = [
        "omp",
        "-p",
        "--no-session",
        "--no-tools",
        "--no-rules",
        "--no-extensions",
        "--config",
        str(ROOT / ".omp" / "review-overlay.yml"),
        "--model",
        model,
        "--max-time",
        str(timeout - 60),
        f"@{packet}",
    ]
    try:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired as error:
        raise SystemExit(f"model call timed out: {error}") from None
    if result.returncode:
        raise SystemExit(result.stderr.strip() or result.stdout.strip() or "model call failed")
    if not result.stdout.strip():
        raise SystemExit("model call returned empty output")
    return result.stdout.strip() + "\n"


def command_draft(number: int) -> None:
    state, p = load(number)
    require(state, "CONTEXT_READY")
    if digest(p["context"]) != state["artifacts"]["context_sha256"]:
        raise SystemExit("context packet changed after CONTEXT_READY; run prepare again")
    atomic_text(p["draft"], run_omp(p["context"], "openai-codex/gpt-5.6-luna:high", 960))
    command_drafted(number)


def command_review(number: int, dry_run: bool) -> None:
    state, p = load(number)
    require(state, "DRAFTED")
    if digest(p["draft"]) != state["artifacts"]["draft_sha256"]:
        raise SystemExit(f"draft changed after DRAFTED; run: python tools/workflow.py drafted {number}")
    command = [sys.executable, str(ROOT / "tools" / "review_chapter.py"), str(number), "--draft", str(p["draft"])]
    if dry_run:
        command.append("--dry-run")
    subprocess.run(command, cwd=ROOT, check=True)
    if dry_run:
        return
    meta = json.loads(p["review_meta"].read_text(encoding="utf-8"))
    if meta["draft_sha256"] != state["artifacts"]["draft_sha256"]:
        raise SystemExit("review metadata does not match the recorded draft")
    save(
        state,
        p,
        "REVIEWED",
        reviewed_draft_sha256=meta["draft_sha256"],
        report_sha256=digest(p["report"]),
    )


def command_revised(number: int) -> None:
    state, p = load(number)
    require(state, "REVIEWED", "REVISED")
    if digest(p["draft"]) != state["artifacts"]["reviewed_draft_sha256"]:
        raise SystemExit("review is stale because draft.md changed")
    validate_reading_copy(p["revised"], number)
    save(state, p, "REVISED", revised_sha256=digest(p["revised"]))


def command_revise(number: int) -> None:
    state, p = load(number)
    require(state, "REVIEWED")
    if digest(p["draft"]) != state["artifacts"]["reviewed_draft_sha256"]:
        raise SystemExit("review is stale because draft.md changed")
    if digest(p["report"]) != state["artifacts"]["report_sha256"]:
        raise SystemExit("saved review changed after REVIEWED")
    packet = f"""# Revision Task — Chapter {number}

Return only the complete revised English Markdown reading copy beginning with
`# Chapter {number}`. Apply only source-supported review findings. Preserve
meaning and ambiguity, then make the natural-English collocation pass required
by the binding rules. Do not describe changes or include audit notes.

## Bounded chapter context

{p['context'].read_text(encoding='utf-8').rstrip()}

## Draft reviewed

```markdown
{p['draft'].read_text(encoding='utf-8').rstrip()}
```

## Reviewer findings

{p['report'].read_text(encoding='utf-8').rstrip()}
"""
    atomic_text(p["revision_context"], packet)
    atomic_text(p["revised"], run_omp(p["revision_context"], "openai-codex/gpt-5.6-luna:high", 960))
    command_revised(number)


def state_claims_completion(number: int) -> bool:
    text = (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8")
    completed = re.search(r"^- Last completed:\s*(\d+)\s*$", text, re.MULTILINE)
    next_chapter = re.search(r"^- Next chapter:\s*(\d+)\s*$", text, re.MULTILINE)
    return bool(
        completed
        and int(completed.group(1)) == number
        and next_chapter
        and int(next_chapter.group(1)) == number + 1
    )


def checkpoint_exists(number: int) -> bool:
    if number % 5 != 4:
        return True
    start = number - 4
    return (ROOT / "summaries" / f"{start:04d}-{number:04d}.md").exists()


def command_checkpoint(number: int) -> None:
    state, p = load(number)
    require(state, "REVISED")
    if number % 5 != 4:
        raise SystemExit("this chapter does not end a five-chapter block")
    if not state_claims_completion(number):
        raise SystemExit("update Last completed and Next chapter in docs/STATE.md before checkpoint review")
    if not p["checkpoint_summary"].exists():
        raise SystemExit(f"missing checkpoint summary: {p['checkpoint_summary']}")
    chapters: list[str] = []
    for chapter in range(number - 4, number + 1):
        chapter_path = p["revised"] if chapter == number else ROOT / "translations" / f"{chapter:04d}.md"
        validate_reading_copy(chapter_path, chapter)
        chapters.append(f"## Chapter artifact {chapter}\n\n{chapter_path.read_text(encoding='utf-8').strip()}")
    rules = (ROOT / "RULES.md").read_text(encoding="utf-8").strip()
    durable_state = (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8").strip()
    packet = f"""# Five-Chapter Checkpoint — {number - 4}–{number}

Review only this bounded packet. Check the five English reading copies, summary,
and active state for voice drift, terminology drift, dropped hooks, formatting
differences, internal contradiction, and accidental spoilers. Do not redo the
source-fidelity reviews and do not rewrite files. Return a finite prioritized
list of exact actionable findings, or exactly `No actionable findings`.

## Binding rules

{rules}

## Checkpoint summary

{p['checkpoint_summary'].read_text(encoding='utf-8').strip()}

## Durable state

{durable_state}

## Reading copies

{chr(10).join(chapters)}
"""
    atomic_text(p["checkpoint_packet"], packet)
    atomic_text(
        p["checkpoint_report"],
        run_omp(p["checkpoint_packet"], "openai-codex/gpt-5.6-sol:medium", 960),
    )
    metadata = {
        "chapter": number,
        "packet_sha256": digest(p["checkpoint_packet"]),
        "report_sha256": digest(p["checkpoint_report"]),
        "revised_sha256": digest(p["revised"]),
        "summary_sha256": digest(p["checkpoint_summary"]),
    }
    atomic_json(p["checkpoint_meta"], metadata)
    save(state, p, "CHECKPOINT_REVIEWED", checkpoint_report_sha256=metadata["report_sha256"])


def command_checkpointed(number: int) -> None:
    state, p = load(number)
    require(state, "CHECKPOINT_REVIEWED")
    if digest(p["checkpoint_report"]) != state["artifacts"]["checkpoint_report_sha256"]:
        raise SystemExit("checkpoint report changed after review")
    if not p["checkpoint_disposition"].exists() or not p["checkpoint_disposition"].read_text(encoding="utf-8").strip():
        raise SystemExit("write a nonempty checkpoint disposition before continuing")
    validate_reading_copy(p["revised"], number)
    save(
        state,
        p,
        "CHECKPOINT_APPLIED",
        revised_sha256=digest(p["revised"]),
        checkpoint_disposition_sha256=digest(p["checkpoint_disposition"]),
    )


def command_accept(number: int) -> None:
    state, p = load(number)
    expected = "CHECKPOINT_APPLIED" if number % 5 == 4 else "REVISED"
    require(state, expected)
    validate_reading_copy(p["revised"], number)
    if digest(p["revised"]) != state["artifacts"]["revised_sha256"]:
        raise SystemExit("revised.md changed after REVISED; record it again before acceptance")
    if not state_claims_completion(number):
        raise SystemExit(
            f"docs/STATE.md must say '- Last completed: {number}' and '- Next chapter: {number + 1}' before acceptance"
        )
    if not checkpoint_exists(number):
        raise SystemExit("five-chapter summary is missing for this checkpoint chapter")
    p["translation"].parent.mkdir(parents=True, exist_ok=True)
    temporary = p["translation"].with_suffix(".md.tmp")
    shutil.copyfile(p["revised"], temporary)
    os.replace(temporary, p["translation"])
    save(state, p, "ACCEPTED", translation_sha256=digest(p["translation"]))


def command_committed(number: int, commit: str) -> None:
    state, p = load(number)
    require(state, "ACCEPTED")
    resolved = subprocess.run(
        ["git", "rev-parse", "--verify", commit], cwd=ROOT, text=True, capture_output=True, check=True
    ).stdout.strip()
    names = subprocess.run(
        ["git", "show", "--format=", "--name-only", resolved], cwd=ROOT, text=True, capture_output=True, check=True
    ).stdout.splitlines()
    required = {
        str(p["translation"].relative_to(ROOT)),
        str(p["report"].relative_to(ROOT)),
        str(p["review_meta"].relative_to(ROOT)),
    }
    if number % 5 == 4:
        required.update(
            {
                str(p["checkpoint_summary"].relative_to(ROOT)),
                str(p["checkpoint_packet"].relative_to(ROOT)),
                str(p["checkpoint_report"].relative_to(ROOT)),
                str(p["checkpoint_meta"].relative_to(ROOT)),
            }
        )
    missing = required.difference(names)
    if missing:
        raise SystemExit("commit is missing: " + ", ".join(sorted(missing)))
    save(state, p, "COMMITTED", commit=resolved)


def command_status(number: int, as_json: bool) -> None:
    state, p = load(number)
    result = {**state, "next_action": next_action(state, p)}
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(f"Chapter: {number}\nStage: {state['stage']}\nNext action: {result['next_action']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in (
        "status", "prepare", "draft", "drafted", "review", "revise",
        "revised", "checkpoint", "checkpointed", "accept",
    ):
        item = sub.add_parser(name)
        item.add_argument("chapter", type=int)
        if name == "status":
            item.add_argument("--json", action="store_true")
        if name == "review":
            item.add_argument("--dry-run", action="store_true")
    committed = sub.add_parser("committed")
    committed.add_argument("chapter", type=int)
    committed.add_argument("--commit", required=True)
    args = parser.parse_args()
    if args.chapter < 0:
        parser.error("chapter must be non-negative")
    if args.command == "status":
        command_status(args.chapter, args.json)
    elif args.command == "prepare":
        command_prepare(args.chapter)
    elif args.command == "drafted":
        command_drafted(args.chapter)
    elif args.command == "draft":
        command_draft(args.chapter)
    elif args.command == "review":
        command_review(args.chapter, args.dry_run)
    elif args.command == "revised":
        command_revised(args.chapter)
    elif args.command == "revise":
        command_revise(args.chapter)
    elif args.command == "checkpoint":
        command_checkpoint(args.chapter)
    elif args.command == "checkpointed":
        command_checkpointed(args.chapter)
    elif args.command == "accept":
        command_accept(args.chapter)
    else:
        command_committed(args.chapter, args.commit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
