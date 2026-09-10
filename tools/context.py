#!/usr/bin/env python3
"""Build phase-specific, bounded packets for one chapter."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY_NAME = re.compile(r"^(\d{4})-(\d{4})\.md$")


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def workflow_config() -> dict:
    return read_json(ROOT / "docs" / "workflow.json")


def chapter_source_path(number: int) -> Path:
    try:
        from tools.chapter import chapter_path
    except ModuleNotFoundError:
        from chapter import chapter_path
    return chapter_path(number)


def chapter_text(number: int) -> str:
    try:
        from tools.chapter import extract_chapter
    except ModuleNotFoundError:
        from chapter import extract_chapter
    return extract_chapter(number)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def estimated_tokens(text: str) -> int:
    """Conservative language-agnostic estimate based on UTF-8 bytes."""
    return (len(text.encode("utf-8")) + 3) // 4


CONTEXT_REQUIRED_KEYS = (
    "version",
    "safe_through",
    "continuity_sources",
    "active_continuity",
    "open_questions",
    "temporary_decisions",
)


def durable_context_problems(value: dict, number: int, source_limit: int, *, prior: bool = False) -> list[str]:
    """Return schema problems for the durable context ledger at chapter `number`."""
    problems: list[str] = []
    missing = [key for key in CONTEXT_REQUIRED_KEYS if key not in value]
    if missing:
        problems.append("missing " + ", ".join(missing))
    if value.get("version") != 1:
        problems.append("version must be 1")
    if prior:
        expected = number - 1
        if value.get("safe_through") != expected:
            problems.append(f"safe_through must be {expected} before drafting chapter {number}")
        upper = expected
    else:
        if value.get("safe_through") != number:
            problems.append(f"safe_through must be {number}")
        upper = number
    sources = value.get("continuity_sources")
    if not isinstance(sources, list) or len(sources) > source_limit:
        problems.append("continuity_sources must be a list within the configured limit")
    elif any(not isinstance(item, int) or item < 0 or item > upper for item in sources):
        problems.append("continuity_sources must contain prior chapter numbers")
    for key in ("active_continuity", "open_questions", "temporary_decisions"):
        items = value.get(key)
        if not isinstance(items, list) or any(not isinstance(item, str) or not item.strip() for item in items):
            problems.append(f"{key} must be an array of nonempty strings")
    return problems


def load_active_context(number: int) -> dict:
    path = ROOT / "docs" / "CONTEXT.json"
    config = workflow_config()
    if path.stat().st_size > config["context_max_bytes"]:
        raise ValueError(f"{path} exceeds context_max_bytes")
    value = read_json(path)
    problems = durable_context_problems(
        value, number, config["continuity_source_limit"], prior=True,
    )
    if problems:
        raise ValueError("CONTEXT.json is invalid: " + "; ".join(problems))
    return value


def exact_glossary_entries(source: str) -> list[dict]:
    try:
        from tools.names import ledger_for_source
    except ModuleNotFoundError:
        from names import ledger_for_source
    return ledger_for_source(source)


def glossary_text(entries: list[dict]) -> str:
    return "\n".join(item["row"] for item in entries) or "(No exact compendium rows matched.)"


def profile_entries(source: str) -> list[tuple[Path, str]]:
    try:
        from tools.names import profile_koreans
    except ModuleNotFoundError:
        from names import profile_koreans
    profiles: list[tuple[Path, str]] = []
    for path in sorted((ROOT / "characters").glob("*.md")):
        body = path.read_text(encoding="utf-8")
        if any(name in source for name in profile_koreans(body)):
            profiles.append((path, body.strip()))
    return profiles


def profiles_text(profiles: list[tuple[Path, str]]) -> str:
    return "\n\n".join(f"### {path.name}\n\n{body}" for path, body in profiles) or "(No chapter-safe profiles matched.)"


def latest_summary_entry(number: int) -> tuple[Path | None, str]:
    candidates: list[tuple[int, Path]] = []
    for path in (ROOT / "summaries").glob("*.md"):
        match = SUMMARY_NAME.match(path.name)
        if match and int(match.group(2)) < number:
            candidates.append((int(match.group(2)), path))
    if not candidates:
        return None, "(No prior summary.)"
    path = max(candidates)[1]
    return path, path.read_text(encoding="utf-8").strip()


def beat_path(number: int) -> Path:
    return ROOT / "summaries" / "beats" / f"{number:04d}.md"


def validate_beat(path: Path, number: int, max_bytes: int) -> str:
    if not path.exists() or not path.read_text(encoding="utf-8").strip():
        raise ValueError(f"missing or empty chapter beat: {path}")
    text = path.read_text(encoding="utf-8")
    if len(text.encode("utf-8")) > max_bytes:
        raise ValueError(f"chapter beat exceeds beat_max_bytes: {path}")
    first = next((line.strip() for line in text.splitlines() if line.strip()), "")
    if first != f"# Chapter {number}":
        raise ValueError(f"first nonblank line must be '# Chapter {number}'")
    for heading in ("## Plot", "## Continuity", "## Translation Decisions"):
        if heading not in text:
            raise ValueError(f"chapter beat missing {heading}: {path}")
    return text.strip()


def strip_markdown_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text


def normalize_block_summary(text: str, start: int, end: int) -> str:
    text = strip_markdown_fence(text)
    first = next((line.strip() for line in text.splitlines() if line.strip()), "")
    expected = {f"# Chapters {start}–{end}", f"# Chapters {start}-{end}"}
    if first not in expected:
        raise ValueError(f"first nonblank line must be '# Chapters {start}–{end}'")
    for heading in ("## Plot", "## Continuity", "## Translation Decisions"):
        if heading not in text:
            raise ValueError(f"block summary missing {heading}")
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.strip():
            lines[index] = f"# Chapters {start}–{end}"
            break
    return "\n".join(lines).strip() + "\n"


def build_summary_packet(number: int) -> str:
    config = workflow_config()
    interval = int(config["summary_interval"])
    max_bytes = int(config["beat_max_bytes"])
    start = number - interval + 1
    previous_path, previous = latest_summary_entry(start)
    beats: list[str] = []
    used = [ROOT / "docs" / "CONTEXT.json"]
    for chapter in range(start, number + 1):
        path = beat_path(chapter)
        beats.append(f"### Chapter {chapter}\n\n{validate_beat(path, chapter, max_bytes)}")
        used.append(path)
    if previous_path:
        used.append(previous_path)
    durable = (ROOT / "docs" / "CONTEXT.json").read_text(encoding="utf-8").strip()
    body = f"""# Summary Task — Chapters {start}–{number}

Write a compact plot summary for this block only. Return only the Markdown
file beginning with `# Chapters {start}–{number}` and the sections Plot,
Continuity, and Translation Decisions. Capture unresolved hooks and binding
facts a later chapter needs. Do not invent plot, quote long passages, or
include reading copies.

## Previous block summary

{previous}

## Chapter beats

{chr(10).join(beats)}

## Durable state after chapter {number}

```json
{durable}
```
"""
    return body.replace("# Summary Task", f"<!-- packet-manifest\n{manifest(used, body)}\n-->\n\n# Summary Task", 1)


def continuity_text(context: dict) -> tuple[list[Path], str]:
    paths: list[Path] = []
    parts: list[str] = []
    for number in context["continuity_sources"]:
        path = ROOT / "translations" / f"{number:04d}.md"
        if not path.exists():
            raise ValueError(f"continuity source does not exist: {path}")
        paths.append(path)
        parts.append(f"### {path.name}\n\n{path.read_text(encoding='utf-8').strip()}")
    return paths, "\n\n".join(parts) or "(No prior reading copy required.)"


def manifest(paths: list[Path], packet_without_manifest: str) -> str:
    unique: list[Path] = []
    for path in paths:
        if path and path not in unique:
            unique.append(path)
    items = [
        {
            "path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "bytes": path.stat().st_size,
        }
        for path in unique
    ]
    return json.dumps({"included": items, "estimated_tokens": estimated_tokens(packet_without_manifest)}, ensure_ascii=False, indent=2)


def build_draft_packet(number: int) -> str:
    source = chapter_text(number)
    context = load_active_context(number)
    rules_path = ROOT / "RULES.md"
    context_path = ROOT / "docs" / "CONTEXT.json"
    source_path = chapter_source_path(number)
    compendium_path = ROOT / "compendium.md"
    rules = rules_path.read_text(encoding="utf-8").strip()
    glossary = exact_glossary_entries(source)
    profiles = profile_entries(source)
    summary_path, summary = latest_summary_entry(number)
    continuity_paths, continuity = continuity_text(context)
    body = f"""# Draft Task — Chapter {number}

Translate only Chapter {number}. Return only the complete English Markdown
reading copy beginning with `# Chapter {number}`. Preserve every source beat and
ambiguity. Do not review, explain, update files, or continue to another chapter.

## Binding rules

{rules}

## Bounded active continuity

```json
{json.dumps(context, ensure_ascii=False, indent=2)}
```

## Korean source

```text
{source.rstrip()}
```

## Exact glossary matches

{glossary_text(glossary)}

## Latest completed summary

{summary}

## Explicit continuity reading copies

{continuity}

## Chapter-safe profiles present in the source

{profiles_text(profiles)}
"""
    names_path = ROOT / "docs" / "NAMES.md"
    used = [rules_path, context_path, source_path, compendium_path, names_path, *continuity_paths, *(path for path, _ in profiles)]
    if summary_path:
        used.append(summary_path)
    return body.replace("# Draft Task", f"<!-- packet-manifest\n{manifest(used, body)}\n-->\n\n# Draft Task", 1)


def build_review_packet(number: int, draft: str, qa: dict) -> str:
    source = chapter_text(number)
    context = load_active_context(number)
    rules_path = ROOT / "RULES.md"
    rules = rules_path.read_text(encoding="utf-8").strip()
    glossary = exact_glossary_entries(source)
    profiles = profile_entries(source)
    active = {key: context[key] for key in ("active_continuity", "open_questions", "temporary_decisions")}
    return f"""# Structured Review Task — Chapter {number}

Review only this packet. Do not use tools, infer future plot, rewrite the chapter,
or give praise. Check fidelity, omissions, additions, subjects, ambiguity,
terminology, voice, hierarchy, humor, profanity, Markdown, footnotes, and spoilers.
Treat deterministic QA warnings as leads, not proof.

Audit in this order: (1) reversed or altered actions, negation, subjects, kinship,
quantities, and causal/mechanical explanations; (2) omitted pragmatic cues and
register shifts, including euphemisms made more explicit; (3) terminology and
natural English. Semantic errors outrank stylistic improvements. Severity means:
`critical` reverses or changes a scene fact, action, identity, negation, or plot
consequence; `major` loses meaningful hierarchy, mechanism, characterization,
or register; `minor` is localized wording or polish without changed meaning.

Return exactly one JSON object and no Markdown fence:

{{
  "summary": "brief assessment or No actionable findings",
  "findings": [
    {{
      "id": "F01",
      "severity": "critical|major|minor",
      "source": "exact Korean passage",
      "current": "exact current English",
      "defect": "specific defect",
      "correction": "recommended correction",
      "rationale": "source-supported reason",
      "confidence": 0.0
    }}
  ]
}}

Use an empty findings array when nothing is actionable.

## Korean source

```text
{source.rstrip()}
```

## Draft

```markdown
{draft.rstrip()}
```

## Binding rules

{rules}

## Exact glossary matches

{glossary_text(glossary)}

## Present-character profiles

{profiles_text(profiles)}

## Relevant active continuity

```json
{json.dumps(active, ensure_ascii=False, indent=2)}
```

## Deterministic QA

```json
{json.dumps(qa, ensure_ascii=False, indent=2)}
```
"""


def build_revision_packet(number: int, draft: str, review: dict) -> str:
    source = chapter_text(number)
    rules = (ROOT / "RULES.md").read_text(encoding="utf-8").strip()
    glossary = exact_glossary_entries(source)
    profiles = profile_entries(source)
    return f"""# Structured Revision Task — Chapter {number}

Revise the reviewed draft. Apply only source-supported findings, preserve meaning
and ambiguity, and perform the required natural-English collocation pass.
Fidelity has priority over punchier prose. Preserve exact actions, kinship,
mechanisms, pragmatic cues, and the source's level of euphemism or profanity.

Start from the reviewed draft. Change only what the findings require, plus the
collocation pass. Do not retranslate the chapter from scratch.

## Korean source

```text
{source.rstrip()}
```

## Reviewed draft

```markdown
{draft.rstrip()}
```

## Structured findings

```json
{json.dumps(review, ensure_ascii=False, indent=2)}
```

## Binding rules

{rules}

## Exact glossary matches

{glossary_text(glossary)}

## Present-character profiles

{profiles_text(profiles)}

## Output format

Reply with only the envelope below. Keep the translation as ordinary Markdown;
only dispositions are JSON. Do not copy the Korean source, draft, findings,
rules, glossary, profiles, or these instructions into the output. Do not wrap
the envelope in a Markdown fence. After <<<END>>>, stop immediately.

<<<TRANSLATION>>>
# Chapter {number}
<complete revised reading copy>
<<<DISPOSITIONS>>>
{{"dispositions":[{{"finding_id":"F01","status":"applied|rejected|unresolved","reason":"specific reason"}}]}}
<<<END>>>

Include exactly one disposition for every finding. Do not put audit notes inside
the translation section.
"""


def build_polish_packet(number: int, revised: str) -> str:
    source = chapter_text(number)
    rules_path = ROOT / "RULES.md"
    handoff_path = ROOT / "POLISH.md"
    source_path = chapter_source_path(number)
    compendium_path = ROOT / "compendium.md"
    names_path = ROOT / "docs" / "NAMES.md"
    rules = rules_path.read_text(encoding="utf-8").strip()
    handoff = handoff_path.read_text(encoding="utf-8").strip()
    glossary = exact_glossary_entries(source)
    profiles = profile_entries(source)
    body = f"""# Polish Task — Chapter {number}

Edit only this revised reading copy. Return only the complete English Markdown
reading copy beginning with `# Chapter {number}`. Do not review, explain,
update files, or continue to another chapter.

Follow the polish brief below. Start from the revised copy; do not
retranslate from scratch. Preserve meaning, pacing, humor, character voice,
System terminology, names, and Korean/Murim cultural content. Check the
Korean source before changing an idiom, metaphor, joke, or cultural phrasing.

## Polish brief

{handoff}

## Binding rules

{rules}

## Korean source

```text
{source.rstrip()}
```

## Revised reading copy

```markdown
{revised.rstrip()}
```

## Exact glossary matches

{glossary_text(glossary)}

## Present-character profiles

{profiles_text(profiles)}
"""
    used = [rules_path, handoff_path, source_path, compendium_path, names_path, *(path for path, _ in profiles)]
    return body.replace("# Polish Task", f"<!-- packet-manifest\n{manifest(used, body)}\n-->\n\n# Polish Task", 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    packet = build_draft_packet(args.chapter)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(packet, encoding="utf-8")
        print(args.output)
    else:
        print(packet, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
