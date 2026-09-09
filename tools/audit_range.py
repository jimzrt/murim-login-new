#!/usr/bin/env python3
"""Targeted retrospective audit for accepted chapter ranges.

This workflow is independent of normal chapter progress. It performs free QA,
parallel bounded Sol reviews, one Luna patch-planning pass, atomic application,
and final QA without redrafting complete chapters.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

try:
    from tools.context import exact_glossary_entries, glossary_text, profile_entries, profiles_text
    from tools.model_io import (
        blocking_dispositions,
        parse_json_object,
        review_markdown,
        validate_patchset,
        validate_range_review,
    )
    from tools.qa import run_qa
    from tools.workflow import estimated_tokens, project_config, run_omp
    from tools.chapter import extract_chapter, source_chapters
except ModuleNotFoundError:
    from context import exact_glossary_entries, glossary_text, profile_entries, profiles_text
    from model_io import blocking_dispositions, parse_json_object, review_markdown, validate_patchset, validate_range_review
    from qa import run_qa
    from workflow import estimated_tokens, project_config, run_omp
    from chapter import extract_chapter, source_chapters

STAGES = ("PREPARED", "REVIEWED", "REFINED", "VERIFIED")
HANGUL = re.compile(r"[가-힣]")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def atomic_json(path: Path, value: dict) -> None:
    atomic_text(path, json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def range_name(start: int, end: int) -> str:
    return f"{start:04d}-{end:04d}"


def audit_dir(start: int, end: int) -> Path:
    return ROOT / "reviews" / "retrofit" / range_name(start, end)


def state_path(start: int, end: int) -> Path:
    return audit_dir(start, end) / "state.json"


def translation_path(number: int) -> Path:
    return ROOT / "translations" / f"{number:04d}.md"


def validate_range(start: int, end: int) -> list[int]:
    if start < 0 or end < start:
        raise SystemExit("range must satisfy 0 <= START <= END")
    chapters = list(range(start, end + 1))
    available = set(source_chapters())
    missing_source = [number for number in chapters if number not in available]
    missing_translation = [number for number in chapters if not translation_path(number).exists()]
    if missing_source:
        raise SystemExit("missing Korean source chapters: " + ", ".join(map(str, missing_source)))
    if missing_translation:
        raise SystemExit("missing accepted translations: " + ", ".join(map(str, missing_translation)))
    return chapters


def blocks(chapters: list[int], block_size: int) -> list[list[int]]:
    if block_size < 1:
        raise SystemExit("block size must be positive")
    return [chapters[index:index + block_size] for index in range(0, len(chapters), block_size)]


def qa_for(number: int, text: str | None = None) -> dict:
    source = extract_chapter(number)
    translation = text if text is not None else translation_path(number).read_text(encoding="utf-8")
    glossary = [(item["korean"], item["english"]) for item in exact_glossary_entries(source)]
    return run_qa(number, source, translation, glossary)


def build_review_packet(chapter_block: list[int]) -> str:
    rubric = (ROOT / "docs" / "RETROFIT.md").read_text(encoding="utf-8").strip()
    sections: list[str] = []
    combined_source = "\n".join(extract_chapter(number) for number in chapter_block)
    glossary = exact_glossary_entries(combined_source)
    profiles = profile_entries(combined_source)
    for number in chapter_block:
        qa = qa_for(number)
        sections.append(f"""## Chapter {number}

### Korean source

```text
{extract_chapter(number).rstrip()}
```

### Accepted English

```markdown
{translation_path(number).read_text(encoding='utf-8').rstrip()}
```

### Deterministic QA leads

```json
{json.dumps(qa, ensure_ascii=False, indent=2)}
```""")
    return f"""# Retrospective Audit — Chapters {chapter_block[0]}–{chapter_block[-1]}

Review only this packet. Do not retranslate acceptable prose, use tools, infer
future plot, or report optional synonyms. Apply the rubric strictly.

Return exactly one JSON object with no Markdown fence:

{{
  "summary": "brief block assessment",
  "findings": [
    {{
      "id": "R{chapter_block[0]:04d}-01",
      "chapter": {chapter_block[0]},
      "severity": "critical|major|minor",
      "source": "exact Korean passage",
      "current": "exact current-English span",
      "defect": "specific defect",
      "correction": "bounded recommended correction",
      "rationale": "source-supported reason",
      "confidence": 0.0
    }}
  ]
}}

Use an empty findings array when nothing is actionable. Finding IDs must be
unique. The `current` span must be copied exactly from that chapter so a later
patch stage can locate it.

## Audit rubric

{rubric}

## Exact glossary matches for this block

{glossary_text(glossary)}

## Relevant safe profiles

{profiles_text(profiles)}

{chr(10).join(sections)}
"""


def prepare(start: int, end: int, block_size: int) -> dict:
    chapters = validate_range(start, end)
    directory = audit_dir(start, end)
    directory.mkdir(parents=True, exist_ok=True)
    initial: dict[str, dict] = {}
    for number in chapters:
        qa = qa_for(number)
        atomic_json(directory / f"qa-before-{number:04d}.json", qa)
        if not qa["passed"]:
            raise SystemExit(f"accepted chapter {number} fails blocking QA before audit")
        initial[str(number)] = {
            "source_sha256": hashlib.sha256(extract_chapter(number).encode("utf-8")).hexdigest(),
            "translation_sha256": digest(translation_path(number)),
        }
    block_records = []
    total_tokens = 0
    limit = int(project_config()["retrofit_review_token_limit"])
    for chapter_block in blocks(chapters, block_size):
        packet = build_review_packet(chapter_block)
        tokens = estimated_tokens(packet)
        if tokens > limit:
            raise SystemExit(f"audit packet {chapter_block[0]}-{chapter_block[-1]} estimate {tokens} exceeds {limit}")
        packet_path = directory / f"packet-{chapter_block[0]:04d}-{chapter_block[-1]:04d}.md"
        atomic_text(packet_path, packet)
        block_records.append({
            "start": chapter_block[0], "end": chapter_block[-1],
            "chapters": chapter_block, "packet": packet_path.name,
            "packet_sha256": digest(packet_path), "estimated_input_tokens": tokens,
        })
        total_tokens += tokens
    state = {
        "version": 1, "range": [start, end], "stage": "PREPARED",
        "normal_workflow_untouched": True, "initial": initial,
        "blocks": block_records, "estimated_review_input_tokens": total_tokens,
        "changed_chapters": [],
    }
    atomic_json(state_path(start, end), state)
    return state


def load_state(start: int, end: int) -> dict:
    path = state_path(start, end)
    if not path.exists():
        raise SystemExit("audit is not prepared")
    state = json.loads(path.read_text(encoding="utf-8"))
    if state.get("range") != [start, end] or state.get("stage") not in STAGES:
        raise SystemExit("invalid retrospective audit state")
    return state


def verify_initial_hashes(state: dict) -> None:
    for text_number, hashes in state["initial"].items():
        number = int(text_number)
        source_hash = hashlib.sha256(extract_chapter(number).encode("utf-8")).hexdigest()
        if source_hash != hashes["source_sha256"]:
            raise SystemExit(f"source chapter {number} changed after audit preparation")
        if state["stage"] in {"PREPARED", "REVIEWED"} and digest(translation_path(number)) != hashes["translation_sha256"]:
            raise SystemExit(f"translation chapter {number} changed before refinement")


def run_block_review(directory: Path, block: dict) -> tuple[dict, dict]:
    packet_path = directory / block["packet"]
    raw, metrics = run_omp(packet_path, project_config()["review_model"], 960)
    review = validate_range_review(parse_json_object(raw), set(block["chapters"]))
    return review, metrics


def review(start: int, end: int, jobs: int) -> dict:
    state = load_state(start, end)
    if state["stage"] != "PREPARED":
        raise SystemExit(f"audit stage is {state['stage']}; expected PREPARED")
    verify_initial_hashes(state)
    directory = audit_dir(start, end)
    results: dict[int, tuple[dict, dict]] = {}
    with ThreadPoolExecutor(max_workers=max(1, min(jobs, len(state["blocks"])))) as executor:
        futures = {executor.submit(run_block_review, directory, block): index for index, block in enumerate(state["blocks"])}
        for future in as_completed(futures):
            index = futures[future]
            try:
                results[index] = future.result()
            except (ValueError, SystemExit) as error:
                raise SystemExit(f"audit block {index + 1} failed: {error}") from None
    merged_findings: list[dict] = []
    metrics_records: list[dict] = []
    for index, block in enumerate(state["blocks"]):
        block_name = f"{block['start']:04d}-{block['end']:04d}"
        block_review, metrics = results[index]
        atomic_json(directory / f"review-{block_name}.json", block_review)
        atomic_text(directory / f"review-{block_name}.md", review_markdown(block_review))
        merged_findings.extend(block_review["findings"])
        metrics_records.append({"block": block_name, **metrics, "finding_count": len(block_review["findings"])})
    identifiers = [item["id"] for item in merged_findings]
    if len(identifiers) != len(set(identifiers)):
        raise SystemExit("review blocks returned duplicate finding IDs")
    merged = {"version": 1, "summary": f"{len(merged_findings)} findings across {len(state['blocks'])} blocks", "findings": merged_findings}
    atomic_json(directory / "findings.json", merged)
    state["stage"] = "REVIEWED"
    state["review_metrics"] = metrics_records
    state["finding_count"] = len(merged_findings)
    atomic_json(state_path(start, end), state)
    return state


def build_refine_packet(start: int, end: int, review_data: dict) -> str:
    rubric = (ROOT / "docs" / "RETROFIT.md").read_text(encoding="utf-8").strip()
    affected = sorted({finding["chapter"] for finding in review_data["findings"]})
    chapters: list[str] = []
    for number in affected:
        chapters.append(f"""## Chapter {number}

### Korean source

```text
{extract_chapter(number).rstrip()}
```

### Current accepted English

```markdown
{translation_path(number).read_text(encoding='utf-8').rstrip()}
```""")
    return f"""# Retrospective Patch Plan — Chapters {start}–{end}

Create bounded exact-text patches; do not return complete chapters. Every `old`
string must occur exactly once in the identified current chapter. `new` must be
finished replacement prose. Combine adjacent findings when useful, never alter
unreported text, and disposition every finding.

Return exactly one JSON object with no Markdown fence:

{{
  "summary": "brief patch summary",
  "patches": [
    {{"chapter": 1, "finding_ids": ["R0000-01"], "old": "exact old text", "new": "exact replacement"}}
  ],
  "dispositions": [
    {{"finding_id": "R0000-01", "status": "applied|rejected|unresolved", "reason": "specific reason"}}
  ]
}}

Reject a finding only when its proposed change is not supported by the supplied
source. Leave genuinely uncertain findings unresolved. Do not intensify or
sanitize register.

## Audit rubric

{rubric}

## Structured findings

```json
{json.dumps(review_data, ensure_ascii=False, indent=2)}
```

{chr(10).join(chapters)}
"""


def apply_patchset(patchset: dict, originals: dict[int, str]) -> dict[int, str]:
    revised = dict(originals)
    for patch in patchset["patches"]:
        number = patch["chapter"]
        if number not in revised:
            raise ValueError(f"patch targets unavailable chapter {number}")
        count = revised[number].count(patch["old"])
        if count != 1:
            raise ValueError(f"patch for chapter {number} old text occurs {count} times")
        revised[number] = revised[number].replace(patch["old"], patch["new"], 1)
    return revised


def refine(start: int, end: int) -> dict:
    state = load_state(start, end)
    if state["stage"] != "REVIEWED":
        raise SystemExit(f"audit stage is {state['stage']}; expected REVIEWED")
    verify_initial_hashes(state)
    directory = audit_dir(start, end)
    review_data = json.loads((directory / "findings.json").read_text(encoding="utf-8"))
    if not review_data["findings"]:
        state["stage"] = "REFINED"
        state["changed_chapters"] = []
        atomic_json(directory / "patchset.json", {"version": 1, "summary": "No findings", "patches": [], "dispositions": []})
        atomic_json(state_path(start, end), state)
        return state
    packet = build_refine_packet(start, end, review_data)
    limit = int(project_config()["retrofit_refine_token_limit"])
    tokens = estimated_tokens(packet)
    if tokens > limit:
        raise SystemExit(f"refinement packet estimate {tokens} exceeds {limit}")
    packet_path = directory / "refine-packet.md"
    atomic_text(packet_path, packet)
    raw, metrics = run_omp(packet_path, project_config()["revision_model"], 960)
    try:
        patchset = validate_patchset(parse_json_object(raw), review_data)
    except ValueError as error:
        raise SystemExit(str(error)) from None
    confidence = {item["id"]: item["confidence"] for item in review_data["findings"]}
    minimum = float(project_config()["retrofit_min_auto_confidence"])
    low_confidence_applied = [
        item["finding_id"]
        for item in patchset["dispositions"]
        if item["status"] == "applied" and confidence[item["finding_id"]] < minimum
    ]
    if low_confidence_applied:
        raise SystemExit(
            f"findings below auto-apply confidence {minimum} cannot be applied automatically: "
            + ", ".join(low_confidence_applied)
        )
    blockers = blocking_dispositions(review_data, patchset)
    if blockers:
        raise SystemExit("critical or major findings remain unresolved: " + ", ".join(blockers))
    originals = {number: translation_path(number).read_text(encoding="utf-8") for number in range(start, end + 1)}
    try:
        revised = apply_patchset(patchset, originals)
    except ValueError as error:
        raise SystemExit(str(error)) from None
    changed = sorted(number for number in originals if revised[number] != originals[number])
    qa_results: dict[str, dict] = {}
    for number in changed:
        if HANGUL.search(revised[number]):
            raise SystemExit(f"planned revision for chapter {number} contains Hangul")
        qa = qa_for(number, revised[number])
        qa_results[str(number)] = qa
        if not qa["passed"]:
            raise SystemExit(f"planned revision for chapter {number} fails deterministic QA")
    backup_dir = ROOT / ".work" / "retrofit" / range_name(start, end) / "before"
    for number in changed:
        atomic_text(backup_dir / f"{number:04d}.md", originals[number])
    for number in changed:
        atomic_text(translation_path(number), revised[number])
        atomic_json(directory / f"qa-after-{number:04d}.json", qa_results[str(number)])
    atomic_json(directory / "patchset.json", patchset)
    state["stage"] = "REFINED"
    state["changed_chapters"] = changed
    state["refine_metrics"] = {**metrics, "estimated_input_tokens": tokens}
    atomic_json(state_path(start, end), state)
    return state


def verify(start: int, end: int) -> dict:
    state = load_state(start, end)
    if state["stage"] != "REFINED":
        raise SystemExit(f"audit stage is {state['stage']}; expected REFINED")
    for number in range(start, end + 1):
        qa = qa_for(number)
        if not qa["passed"]:
            raise SystemExit(f"chapter {number} fails final retrospective QA")
    state["stage"] = "VERIFIED"
    state["final_translation_sha256"] = {str(number): digest(translation_path(number)) for number in range(start, end + 1)}
    atomic_json(state_path(start, end), state)
    return state


def status(start: int, end: int) -> None:
    path = state_path(start, end)
    if not path.exists():
        print(f"Range: {start}-{end}\nStage: READY\nNext action: python tools/audit_range.py prepare {start} {end}")
        return
    state = load_state(start, end)
    next_actions = {
        "PREPARED": f"python tools/audit_range.py review {start} {end}",
        "REVIEWED": f"python tools/audit_range.py refine {start} {end}",
        "REFINED": f"python tools/audit_range.py verify {start} {end}",
        "VERIFIED": "inspect git diff, commit the retrospective change set, and stop",
    }
    print(f"Range: {start}-{end}\nStage: {state['stage']}\nFindings: {state.get('finding_count', 0)}\nChanged chapters: {state.get('changed_chapters', [])}\nNext action: {next_actions[state['stage']]}")


def run_all(start: int, end: int, block_size: int, jobs: int, dry_run: bool) -> None:
    path = state_path(start, end)
    state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else prepare(start, end, block_size)
    if dry_run:
        print(f"Prepared {len(state['blocks'])} packets; estimated review input: {state['estimated_review_input_tokens']} tokens")
        return
    while state["stage"] != "VERIFIED":
        if state["stage"] == "PREPARED":
            state = review(start, end, jobs)
        elif state["stage"] == "REVIEWED":
            state = refine(start, end)
        elif state["stage"] == "REFINED":
            state = verify(start, end)
        else:
            raise SystemExit(f"cannot continue from stage {state['stage']}")
    status(start, end)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("status", "prepare", "review", "refine", "verify", "run"):
        item = sub.add_parser(name)
        item.add_argument("start", type=int)
        item.add_argument("end", type=int)
        if name in {"prepare", "run"}:
            item.add_argument("--block-size", type=int, default=project_config()["retrofit_block_size"])
        if name in {"review", "run"}:
            item.add_argument("--jobs", type=int, default=project_config()["retrofit_parallel_jobs"])
        if name == "run":
            item.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.command == "status":
        status(args.start, args.end)
    elif args.command == "prepare":
        prepare(args.start, args.end, args.block_size)
        status(args.start, args.end)
    elif args.command == "review":
        review(args.start, args.end, args.jobs)
        status(args.start, args.end)
    elif args.command == "refine":
        refine(args.start, args.end)
        status(args.start, args.end)
    elif args.command == "verify":
        verify(args.start, args.end)
        status(args.start, args.end)
    else:
        run_all(args.start, args.end, args.block_size, args.jobs, args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
