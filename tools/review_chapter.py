#!/usr/bin/env python3
"""Build a phase-specific packet and run one structured Sol review."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from context import build_review_packet, estimated_tokens
from model_io import parse_json_object, review_markdown, validate_review
from workflow import project_config, run_omp


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter", type=int)
    parser.add_argument("--draft", type=Path)
    parser.add_argument("--qa", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    draft_path = args.draft or ROOT / ".work" / f"{args.chapter:04d}" / "draft.md"
    qa_path = args.qa or ROOT / ".work" / f"{args.chapter:04d}" / "draft-qa.json"
    draft = draft_path.read_text(encoding="utf-8")
    qa = json.loads(qa_path.read_text(encoding="utf-8"))
    packet = build_review_packet(args.chapter, draft, qa)
    packet_tokens = estimated_tokens(packet)
    packet_limit = project_config()["packet_token_limits"]["review"]
    if packet_tokens > packet_limit:
        print(f"review packet estimate {packet_tokens} exceeds configured limit {packet_limit}", file=sys.stderr)
        return 1
    packet_path = ROOT / "reviews" / "packets" / f"{args.chapter:04d}.md"
    report_json = ROOT / "reviews" / "sol" / f"{args.chapter:04d}.json"
    report_markdown = ROOT / "reviews" / "sol" / f"{args.chapter:04d}.md"
    metadata_path = ROOT / "reviews" / "sol" / f"{args.chapter:04d}.meta.json"
    atomic_write(packet_path, packet)
    if args.dry_run:
        print(packet_path)
        return 0
    try:
        raw, usage = run_omp(packet_path, project_config()["review_model"], 660)
    except SystemExit as error:
        print(error, file=sys.stderr)
        return 1
    try:
        review = validate_review(parse_json_object(raw))
    except ValueError as error:
        raw_path = ROOT / ".work" / f"{args.chapter:04d}" / "review-raw.txt"
        atomic_write(raw_path, raw)
        print(f"{error}\nraw output saved: {raw_path.relative_to(ROOT)}", file=sys.stderr)
        return 1
    canonical = json.dumps(review, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    atomic_write(report_json, canonical)
    atomic_write(report_markdown, review_markdown(review))
    metadata = {
        "version": 2,
        "chapter": args.chapter,
        "draft_sha256": sha256_text(draft),
        "qa_sha256": sha256_text(json.dumps(qa, ensure_ascii=False, sort_keys=True)),
        "packet_sha256": sha256_text(packet),
        "report_sha256": sha256_text(canonical),
        "finding_count": len(review["findings"]),
        "major_or_critical_count": sum(item["severity"] in {"major", "critical"} for item in review["findings"]),
        "usage": usage,
    }
    atomic_write(metadata_path, json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(report_markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
