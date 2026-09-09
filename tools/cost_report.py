#!/usr/bin/env python3
"""Summarize estimated model usage and checkpoint yield."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build_report() -> dict:
    stages: dict[str, dict[str, float]] = defaultdict(lambda: {
        "calls": 0, "estimated_input_tokens": 0, "estimated_output_tokens": 0, "elapsed_seconds": 0,
    })
    chapters = 0
    for path in sorted((ROOT / "reviews" / "metrics").glob("[0-9][0-9][0-9][0-9].json")):
        chapters += 1
        data = json.loads(path.read_text(encoding="utf-8"))
        for name, values in data.get("stages", {}).items():
            if not name.endswith("_model"):
                continue
            stages[name]["calls"] += 1
            for key in ("estimated_input_tokens", "estimated_output_tokens", "elapsed_seconds"):
                stages[name][key] += values.get(key, 0)
    checkpoint_reviews = []
    for path in sorted((ROOT / "reviews" / "checkpoints").glob("*.meta.json")):
        value = json.loads(path.read_text(encoding="utf-8"))
        checkpoint_reviews.append({
            "block": path.name.removesuffix(".meta.json"),
            "findings": value.get("finding_count", 0),
            "major_or_critical": value.get("major_or_critical_count", 0),
        })
    retrofit_audits = []
    for path in sorted((ROOT / "reviews" / "retrofit").glob("[0-9]*-[0-9]*/state.json")):
        value = json.loads(path.read_text(encoding="utf-8"))
        review_metrics = value.get("review_metrics", [])
        refine_metrics = value.get("refine_metrics", {})
        retrofit_audits.append({
            "range": path.parent.name,
            "stage": value.get("stage"),
            "findings": value.get("finding_count", 0),
            "changed_chapters": value.get("changed_chapters", []),
            "estimated_review_input_tokens": sum(item.get("estimated_input_tokens", 0) for item in review_metrics) or value.get("estimated_review_input_tokens", 0),
            "estimated_refine_input_tokens": refine_metrics.get("estimated_input_tokens", 0),
        })
    totals = {
        key: sum(value[key] for value in stages.values())
        for key in ("estimated_input_tokens", "estimated_output_tokens", "elapsed_seconds")
    }
    return {
        "version": 1,
        "chapters_with_metrics": chapters,
        "stages": dict(stages),
        "totals": totals,
        "checkpoint_reviews": checkpoint_reviews,
        "checkpoint_unique_finding_total": sum(item["findings"] for item in checkpoint_reviews),
        "retrofit_audits": retrofit_audits,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = build_report()
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0
    print(f"Chapters measured: {report['chapters_with_metrics']}")
    for name, values in sorted(report["stages"].items()):
        print(f"{name}: {values['calls']} calls, ~{int(values['estimated_input_tokens'])} input tokens, ~{int(values['estimated_output_tokens'])} output tokens")
    print(f"Checkpoint findings: {report['checkpoint_unique_finding_total']} across {len(report['checkpoint_reviews'])} reviews")
    for audit in report["retrofit_audits"]:
        print(f"Retrofit {audit['range']}: {audit['stage']}, {audit['findings']} findings, ~{audit['estimated_review_input_tokens']} review input tokens, ~{audit['estimated_refine_input_tokens']} refine input tokens")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
