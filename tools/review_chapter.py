#!/usr/bin/env python3
"""Build a bounded chapter packet and run one non-interactive Sol review."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from context import chapter_text, exact_glossary_rows, latest_summary, present_profiles


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def build_packet(number: int, draft_path: Path) -> tuple[str, str]:
    source = chapter_text(number)
    if not draft_path.exists():
        raise FileNotFoundError(f"missing draft: {draft_path}")
    draft = draft_path.read_text(encoding="utf-8")
    draft_hash = sha256_text(draft)
    rules = (ROOT / "RULES.md").read_text(encoding="utf-8")
    state = (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8")
    packet = f"""# Bounded Sol Review Packet — Chapter {number}

Draft SHA256: `{draft_hash}`

You are the read-only final reviewer for a Korean-to-English webnovel translation.
Review only the material below. Do not use tools, read other files, infer future plot,
or edit anything. Return a finite prioritized list of actionable findings. For each
finding include: severity, exact source passage, current English, defect, recommended
correction, rationale, and confidence. Check fidelity, omissions/additions, subjects,
ambiguity, terminology, voice, hierarchy, humor, profanity, Markdown, footnotes, and
spoilers. Review tone as well as literal accuracy: the target is brisk commercial
webnovel prose, dry self-mockery, dark action-comedy, and character-specific dialogue.
Do not rewrite the chapter or give generic praise. If nothing is actionable, say exactly
`No actionable findings`.

## Korean source (Chapter {number})

```text
{source.rstrip()}
```

## Current English draft

```markdown
{draft.rstrip()}
```

## Binding translation rules

{rules.rstrip()}

## Exact glossary rows matched in this source

{exact_glossary_rows(source)}

## Chapter-safe profiles for present characters

{present_profiles(source)}

## Latest completed summary

{latest_summary(number)}

## Current state

{state.rstrip()}
"""
    return packet, draft_hash


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter", type=int, help="chapter number")
    parser.add_argument("--draft", type=Path, help="draft path (default: .work/NNNN/draft.md)")
    parser.add_argument("--dry-run", action="store_true", help="write packet without invoking omp")
    args = parser.parse_args()
    if args.chapter < 0:
        parser.error("chapter must be non-negative")

    draft_path = args.draft or ROOT / ".work" / f"{args.chapter:04d}" / "draft.md"
    if not draft_path.is_absolute():
        draft_path = (ROOT / draft_path).resolve()
    packet_dir = ROOT / "reviews" / "packets"
    report_dir = ROOT / "reviews" / "sol"
    packet_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)
    packet_path = packet_dir / f"{args.chapter:04d}.md"
    report_path = report_dir / f"{args.chapter:04d}.md"
    packet, draft_hash = build_packet(args.chapter, draft_path)
    atomic_write(packet_path, packet)

    if args.dry_run:
        print(packet_path)
        return 0

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
        "openai-codex/gpt-5.6-sol:medium",
        "--max-time",
        "600",
        f"@{packet_path}",
    ]
    try:
        result = subprocess.run(
            command, cwd=ROOT, text=True, capture_output=True, timeout=660
        )
    except subprocess.TimeoutExpired as error:
        print(f"review timed out: {error}", file=sys.stderr)
        return 124
    output = result.stdout.strip()
    if result.returncode:
        print(result.stderr.strip() or output or "review command failed", file=sys.stderr)
        return result.returncode
    if not output:
        print("review command returned an empty report", file=sys.stderr)
        return 1
    atomic_write(report_path, output + "\n")
    metadata = {
        "chapter": args.chapter,
        "draft_sha256": draft_hash,
        "packet_sha256": sha256_text(packet),
        "report_sha256": sha256_text(output + "\n"),
    }
    atomic_write(report_path.with_suffix(".json"), json.dumps(metadata, indent=2) + "\n")
    print(report_path)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
