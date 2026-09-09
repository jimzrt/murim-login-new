#!/usr/bin/env python3
"""Build phase-specific, bounded packets for one chapter."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KOREAN = re.compile(r"[가-힣]{2,}")
TABLE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|.*$")
PROFILE_NAME = re.compile(r"\(([가-힣]{2,})\)")
SUMMARY_NAME = re.compile(r"^(\d{4})-(\d{4})\.md$")


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def workflow_config() -> dict:
    return read_json(ROOT / "docs" / "workflow.json")


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


def load_active_context(number: int) -> dict:
    path = ROOT / "docs" / "CONTEXT.json"
    config = workflow_config()
    if path.stat().st_size > config["context_max_bytes"]:
        raise ValueError(f"{path} exceeds context_max_bytes")
    value = read_json(path)
    required = {"version", "safe_through", "continuity_sources", "active_continuity", "open_questions", "temporary_decisions"}
    missing = required.difference(value)
    if missing:
        raise ValueError("CONTEXT.json is missing: " + ", ".join(sorted(missing)))
    if value["safe_through"] != number - 1:
        raise ValueError(f"CONTEXT.json safe_through must be {number - 1} before drafting chapter {number}")
    sources = value["continuity_sources"]
    if not isinstance(sources, list) or len(sources) > config["continuity_source_limit"]:
        raise ValueError("continuity_sources must be a list within the configured limit")
    if any(not isinstance(item, int) or item < 0 or item >= number for item in sources):
        raise ValueError("continuity_sources must contain prior chapter numbers")
    for key in ("active_continuity", "open_questions", "temporary_decisions"):
        if not isinstance(value[key], list) or any(not isinstance(item, str) or not item.strip() for item in value[key]):
            raise ValueError(f"{key} must be an array of nonempty strings")
    return value


def exact_glossary_entries(source: str) -> list[dict]:
    entries: list[dict] = []
    seen: set[str] = set()
    for line in (ROOT / "compendium.md").read_text(encoding="utf-8").splitlines():
        match = TABLE_ROW.match(line)
        if not match:
            continue
        korean = match.group(1).strip()
        english = match.group(2).strip()
        if KOREAN.fullmatch(korean) and korean in source and korean not in seen:
            entries.append({"korean": korean, "english": english, "row": line})
            seen.add(korean)
    return entries


def glossary_text(entries: list[dict]) -> str:
    return "\n".join(item["row"] for item in entries) or "(No exact compendium rows matched.)"


def profile_entries(source: str) -> list[tuple[Path, str]]:
    profiles: list[tuple[Path, str]] = []
    for path in sorted((ROOT / "characters").glob("*.md")):
        body = path.read_text(encoding="utf-8")
        if any(name in source for name in PROFILE_NAME.findall(body)):
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
    source_path = ROOT / "original 1-1104.txt"
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
    used = [rules_path, context_path, source_path, compendium_path, *continuity_paths, *(path for path, _ in profiles)]
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

Return exactly this two-part envelope with no surrounding Markdown fence. Keep
the translation as ordinary Markdown; only dispositions are JSON:

<<<TRANSLATION>>>
# Chapter {number}

Complete revised reading copy here.
<<<DISPOSITIONS>>>
{{
  "dispositions": [
    {{"finding_id": "F01", "status": "applied|rejected|unresolved", "reason": "specific reason"}}
  ]
}}

Include exactly one disposition for every finding. Do not put audit notes inside
the translation section.

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
"""


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
