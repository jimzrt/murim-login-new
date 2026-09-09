#!/usr/bin/env python3
"""Build deterministic, bounded context packets for one chapter."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KOREAN = re.compile(r"[가-힣]{2,}")
TABLE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|([^|]*)\|.*$")
PROFILE_NAME = re.compile(r"\(([가-힣]{2,})\)")
SUMMARY_NAME = re.compile(r"^(\d{4})-(\d{4})\.md$")


def chapter_text(number: int) -> str:
    try:
        from tools.chapter import extract_chapter
    except ModuleNotFoundError:  # Direct execution from tools/.
        from chapter import extract_chapter

    return extract_chapter(number)


def exact_glossary_rows(source: str) -> str:
    """Return unique table rows whose Korean key occurs in the source."""
    rows: list[str] = []
    seen: set[str] = set()
    for line in (ROOT / "compendium.md").read_text(encoding="utf-8").splitlines():
        match = TABLE_ROW.match(line)
        if not match:
            continue
        korean = match.group(1).strip()
        if KOREAN.fullmatch(korean) and korean in source and korean not in seen:
            rows.append(line)
            seen.add(korean)
    return "\n".join(rows) or "(No exact compendium rows matched.)"


def present_profiles(source: str) -> str:
    """Return chapter-safe profiles whose declared Korean name occurs."""
    profiles: list[str] = []
    character_dir = ROOT / "characters"
    for path in sorted(character_dir.glob("*.md")):
        body = path.read_text(encoding="utf-8")
        if any(name in source for name in PROFILE_NAME.findall(body)):
            profiles.append(f"### {path.name}\n\n{body.strip()}")
    return "\n\n".join(profiles) or "(No chapter-safe profiles matched.)"


def latest_summary(number: int) -> str:
    candidates: list[tuple[int, Path]] = []
    for path in (ROOT / "summaries").glob("*.md"):
        match = SUMMARY_NAME.match(path.name)
        if match and int(match.group(2)) < number:
            candidates.append((int(match.group(2)), path))
    if not candidates:
        return "(No prior summary.)"
    path = max(candidates)[1]
    return f"### {path.name}\n\n{path.read_text(encoding='utf-8').strip()}"


def previous_translations(number: int, limit: int = 1) -> str:
    items: list[str] = []
    for previous in range(max(0, number - limit), number):
        path = ROOT / "translations" / f"{previous:04d}.md"
        if path.exists():
            items.append(f"### {path.name}\n\n{path.read_text(encoding='utf-8').strip()}")
    return "\n\n".join(items) or "(No prior translations.)"


def build_context(number: int) -> str:
    source = chapter_text(number)
    rules = (ROOT / "RULES.md").read_text(encoding="utf-8").strip()
    state = (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8").strip()
    return f"""# Draft Context Packet — Chapter {number}

Translate only Chapter {number}. Return only the complete English Markdown reading
copy beginning with `# Chapter {number}`. Do not describe your work, update files,
review the translation, or continue to another chapter.

## Binding rules

{rules}

## Current state

{state}

## Korean source

```text
{source.rstrip()}
```

## Exact glossary matches

{exact_glossary_rows(source)}

## Latest completed summary

{latest_summary(number)}

## Previous reading copy

{previous_translations(number)}

## Chapter-safe profiles present in the source

{present_profiles(source)}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.chapter < 0:
        parser.error("chapter must be non-negative")
    packet = build_context(args.chapter)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(packet, encoding="utf-8")
        print(args.output)
    else:
        print(packet, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
