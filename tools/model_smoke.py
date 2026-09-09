#!/usr/bin/env python3
"""Compare cheap draft/review models against an independent published KR–EN pair."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from model_io import parse_json_object, validate_review
from workflow import atomic_text, run_omp

FIXTURE = ROOT / "tests" / "fixtures" / "smoke"
KO = FIXTURE / "kuunmong-opening.ko.txt"
EN = FIXTURE / "kuunmong-opening.en.md"
HEADING = "# Excerpt"
HANGUL = re.compile(r"[가-힣]")
WORD = re.compile(r"[A-Za-z']+")
# old, new, recall needle. Spans must remain unique in the Gale gold.
PLANTED = (
    ("count", "five noted mountains", "four noted mountains", "four noted mountains"),
    ("name", "was called Song-jin", "was called Jang Sam", "jang sam"),
    ("hangul", "named Queen Wee,", "named Queen Wee 위부인,", "위부인"),
    (
        "omission",
        "Who among you will go for me to the Palace of the Waters and pay my respects to the Dragon King?",
        "",
        "palace of the waters",
    ),
)
# Accept Gale's 1922 spellings and ordinary modern romanizations.
FACTS = (
    ("five_mountains", re.compile(r"\bfive\b.{0,80}\b(?:mountain|peak)s?\b|\b(?:mountain|peak)s?\b.{0,80}\bfive\b", re.I | re.S)),
    ("tai_san", re.compile(r"tai-?san|taishan|tae-?san|mount tai|\bgreat mountain\b", re.I)),
    ("hyong_san", re.compile(r"hyong-?san|hyeong-?san|heng-?san|hengshan|mount heng|\bscales\b", re.I)),
    ("queen_wee", re.compile(r"queen wee|\blady wee\b|\bwee of the southern\b|\blady wei\b|\blady wi\b|wei fu", re.I)),
    ("qin", re.compile(r"\bqin\b|chin see|\bchin dynasty\b", re.I)),
    ("tang", re.compile(r"\btang\b", re.I)),
    ("india", re.compile(r"\bindia\b|tianzhu|cheonchuk|western regions", re.I)),
    ("lotus", re.compile(r"lotus peak|yeonhwa|yonhwa|lianhua", re.I)),
    ("yook_kwan", re.compile(r"yook-?kwan|yuk-?gwan|yukgwan|liuguan|six[- ](?:temptation|gate|contemplation|crown|remainder)", re.I)),
    ("song_jin", re.compile(r"song-?jin|seong-?jin|sung-?jin", re.I)),
    ("dongting", re.compile(r"tong-?jong|dongting|dong jeong", re.I)),
    ("dragon_king", re.compile(r"dragon king", re.I)),
    ("white_clothes", re.compile(r"white (?:clothes|robes|clad)|old man.{0,40}white|white.{0,40}old man", re.I | re.S)),
    ("volunteers", re.compile(r"volunteer|offered (?:to )?(?:go|himself)|i (?:will|shall) go|will (?:obey|receive|accept).{0,60}\bgo\b|command and (?:will )?go", re.I)),
)

DRAFT_BRIEF = """Translate only this bounded excerpt of classical Korean narrative into
contemporary literary English. Return only the complete English Markdown
reading copy beginning with `# Excerpt`. Preserve every named person, place,
count, and plot beat, including the master's request and the disciple's
acceptance. Do not imitate 1922 diction, add a preface, review the text, or
continue past the excerpt."""

REVIEW_BRIEF = """Review only this packet. Do not use tools or rewrite the excerpt.
Flag leftover Hangul, wrong names or counts, and omitted plot beats.

Return exactly one JSON object and no Markdown fence:

{
  "summary": "brief assessment or No actionable findings",
  "findings": [
    {
      "id": "F01",
      "severity": "critical|major|minor",
      "source": "exact Korean passage",
      "current": "exact current English",
      "defect": "specific defect",
      "correction": "recommended correction",
      "rationale": "source-supported reason",
      "confidence": 0.0
    }
  ]
}

Use an empty findings array when nothing is actionable."""


def tokenize(text: str) -> Counter:
    return Counter(WORD.findall(text.lower()))


def token_f1(candidate: str, reference: str) -> float:
    predicted = tokenize(candidate)
    gold = tokenize(reference)
    overlap = sum((predicted & gold).values())
    if not predicted or not gold:
        return 0.0
    precision = overlap / sum(predicted.values())
    recall = overlap / sum(gold.values())
    if precision + recall == 0:
        return 0.0
    return round(2 * precision * recall / (precision + recall), 3)


def fact_coverage(candidate: str) -> dict:
    hits = [name for name, pattern in FACTS if pattern.search(candidate)]
    return {
        "fact_hits": hits,
        "fact_total": len(FACTS),
        "fact_score": round(len(hits) / len(FACTS), 3),
    }


def smoke_qa(candidate: str) -> dict:
    errors: list[str] = []
    first = next((line.strip() for line in candidate.splitlines() if line.strip()), "")
    if first != HEADING:
        errors.append("heading")
    if HANGUL.search(candidate):
        errors.append("hangul")
    if candidate.lstrip().startswith("```") or re.match(r"^(Here is|I translated|Translation:)", candidate.lstrip(), re.I):
        errors.append("wrapper")
    return {"qa_passed": not errors, "qa_errors": errors}


def score_draft(candidate: str, reference: str) -> dict:
    return {
        **smoke_qa(candidate),
        **fact_coverage(candidate),
        "token_f1": token_f1(candidate, reference),
        "length_ratio": round(len(candidate) / max(1, len(reference)), 3),
    }


def plant_defects(reference: str) -> tuple[str, list[dict]]:
    draft = reference
    expected: list[dict] = []
    for code, old, new, needle in PLANTED:
        if old not in draft:
            raise SystemExit(f"gold excerpt no longer contains planted span: {old}")
        draft = draft.replace(old, new, 1)
        expected.append({"id": code, "needle": needle})
    return draft, expected


def review_recall(findings: list[dict], planted: list[dict]) -> dict:
    blob = json.dumps(findings, ensure_ascii=False).casefold()
    caught = [item["id"] for item in planted if item["needle"].casefold() in blob or item["id"] in blob]
    return {"caught": caught, "planted": [item["id"] for item in planted], "recall": round(len(caught) / len(planted), 3)}


def draft_packet(source: str) -> str:
    return f"""# Draft smoke excerpt — 구운몽 opening

{DRAFT_BRIEF}

## Korean source

```text
{source.rstrip()}
```
"""


def review_packet(source: str, draft: str) -> str:
    return f"""# Structured Review Task — 구운몽 excerpt

{REVIEW_BRIEF}

## Korean source

```text
{source.rstrip()}
```

## Draft

```markdown
{draft.rstrip()}
```
"""


def run_models(task: str, models: list[str]) -> dict:
    source = KO.read_text(encoding="utf-8")
    reference = EN.read_text(encoding="utf-8")
    out_dir = ROOT / "reviews" / "smoke"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []
    for model in models:
        safe = re.sub(r"[^A-Za-z0-9._-]+", "_", model)
        if task == "draft":
            packet_path = out_dir / f"draft-{safe}.packet.md"
            atomic_text(packet_path, draft_packet(source))
            text, metrics = run_omp(packet_path, model, 720)
            atomic_text(out_dir / f"draft-{safe}.md", text)
            row = {"model": model, "task": "draft", **score_draft(text, reference), "usage": {
                "input_tokens": metrics.get("input_tokens"),
                "output_tokens": metrics.get("output_tokens"),
                "cost_usd": metrics.get("cost_usd"),
                "elapsed_seconds": metrics.get("elapsed_seconds"),
            }}
        else:
            planted_draft, planted = plant_defects(reference)
            packet_path = out_dir / f"review-{safe}.packet.md"
            atomic_text(packet_path, review_packet(source, planted_draft))
            text, metrics = run_omp(packet_path, model, 720)
            atomic_text(out_dir / f"review-{safe}.raw.txt", text)
            findings: list[dict] = []
            error = None
            try:
                parsed = parse_json_object(text)
                findings = parsed.get("findings") if isinstance(parsed.get("findings"), list) else []
                review = validate_review(parsed)
            except ValueError as exc:
                error = str(exc)
                review = None
            if review is not None:
                atomic_text(out_dir / f"review-{safe}.json", json.dumps(review, ensure_ascii=False, indent=2) + "\n")
                findings = review["findings"]
            row = {
                "model": model,
                "task": "review",
                "schema_valid": review is not None,
                "finding_count": len(findings),
                **review_recall(findings, planted),
                "usage": {
                    "input_tokens": metrics.get("input_tokens"),
                    "output_tokens": metrics.get("output_tokens"),
                    "cost_usd": metrics.get("cost_usd"),
                    "elapsed_seconds": metrics.get("elapsed_seconds"),
                },
            }
            if error:
                row["error"] = error
        rows.append(row)
        print(json.dumps(row, ensure_ascii=False), flush=True)
    report = {"task": task, "gold": "tests/fixtures/smoke/kuunmong-opening", "results": rows}
    (out_dir / f"{task}-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", choices=("draft", "review"))
    parser.add_argument("--models", required=True, help="comma-separated OMP model IDs")
    args = parser.parse_args()
    models = [item.strip() for item in args.models.split(",") if item.strip()]
    if not models:
        raise SystemExit("provide at least one model")
    run_models(args.task, models)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
