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

PROFILE_FIELDS = ("Safe through", "Aliases", "Role", "Personality", "Voice", "Relationships")


def compact_profile(body: str) -> str:
    lines = body.strip().splitlines()
    heading = next((line.strip() for line in lines if line.startswith("# ")), "")
    fields = [
        line.strip()
        for line in lines
        if any(line.startswith(f"- **{name}:**") for name in PROFILE_FIELDS)
    ]
    if not heading:
        raise ValueError("character profile requires a Markdown heading")
    return "\n\n".join((heading, "\n".join(fields))).strip()


def bounded_profiles(profiles: list[tuple[Path, str]]) -> list[tuple[Path, str]]:
    config = workflow_config()
    per_profile = int(config.get("profile_max_bytes", 4096))
    total_limit = int(config.get("profile_total_max_bytes", 12288))
    result: list[tuple[Path, str]] = []
    total = 0
    for path, body in profiles:
        compact = compact_profile(body)
        size = len(compact.encode("utf-8"))
        if size > per_profile:
            raise ValueError(f"{path} compact profile exceeds profile_max_bytes")
        total += size
        if total > total_limit:
            raise ValueError("matched character profiles exceed profile_total_max_bytes")
        result.append((path, compact))
    return result

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
            profiles.append((path, body))
    return bounded_profiles(profiles)


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
terminology, voice, hierarchy, humor, profanity, Markdown, footnotes, and
spoilers. Treat deterministic QA warnings as leads, not proof. Every finding
must quote one exact, uniquely occurring draft span and supply its finished
replacement; do not return instructions for another editor.

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
      "replacement": "finished exact replacement English",
      "rationale": "source-supported reason",
      "confidence": 0.0
    }}
  ]
}}

Use an empty findings array when nothing is actionable. Replacement spans must
not overlap.

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


def build_update_packet(number: int, reading_copy: str) -> str:
    source = chapter_text(number)
    source_path = chapter_source_path(number)
    context_path = ROOT / "docs" / "CONTEXT.json"
    names_path = ROOT / "docs" / "NAMES.md"
    profiles = profile_entries(source)
    prior = read_json(context_path)
    body = f"""# Durable State Update — Chapter {number}

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through {number}. Keep at most
{workflow_config()["continuity_source_limit"]} continuity_sources. Use only chapter
numbers through {number}. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. Beat plot paragraphs are plain strings; continuity and translation
decisions are concise list items.

Return this exact shape:

{{
  "chapter": {number},
  "beat": {{
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  }},
  "context": {{
    "version": 1,
    "safe_through": {number},
    "continuity_sources": [{number}],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  }},
  "names": [
    {{"korean": "source spelling", "english": "English rendering", "notes": "brief note"}}
  ],
  "profile_updates": [
    {{
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }}
  ],
  "profile_creations": [
    {{
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }}
  ]
}}

Use empty arrays when no name or profile change is required.

## Prior durable context

```json
{json.dumps(prior, ensure_ascii=False, indent=2)}
```

## Existing names ledger

{names_path.read_text(encoding="utf-8").strip()}

## Exact glossary matches

{glossary_text(exact_glossary_entries(source))}

## Listed compact profiles

{profiles_text(profiles)}

## Korean source

```text
{source.rstrip()}
```

## Final English reading copy

```markdown
{reading_copy.rstrip()}
```
"""
    used = [source_path, context_path, names_path, *(path for path, _ in profiles)]
    return body.replace(
        "# Durable State Update",
        f"<!-- packet-manifest\n{manifest(used, body)}\n-->\n\n# Durable State Update",
        1,
    )






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
