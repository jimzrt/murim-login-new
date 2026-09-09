#!/usr/bin/env python3
"""Report exact provider-reported usage by chapter, phase, and model."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COUNT_FIELDS = (
    "requests", "input_tokens", "output_tokens", "cache_read_tokens",
    "cache_write_tokens", "total_tokens", "reasoning_tokens",
)


def blank_usage() -> dict:
    return {
        **{field: 0 for field in COUNT_FIELDS},
        "cost_usd": 0.0,
        "cost_complete": True,
        "reasoning_complete": True,
    }


def add_usage(target: dict, source: dict) -> None:
    for field in COUNT_FIELDS[:-1]:
        target[field] += source.get(field, 0)
    if "reasoning_tokens" in source:
        target["reasoning_tokens"] += source["reasoning_tokens"]
    else:
        target["reasoning_complete"] = False
    if "cost_usd" in source:
        target["cost_usd"] += source["cost_usd"]
    else:
        target["cost_complete"] = False


def finish_usage(value: dict) -> dict:
    result = dict(value)
    if not result.pop("cost_complete"):
        result.pop("cost_usd")
    if not result.pop("reasoning_complete"):
        result.pop("reasoning_tokens")
    return result


def build_report() -> dict:
    totals = blank_usage()
    models: dict[str, dict] = {}
    stages: dict[str, dict] = {}
    chapters: dict[str, dict] = {}
    unavailable: list[dict] = []
    metrics_dir = ROOT / "reviews" / "metrics"
    for path in sorted(metrics_dir.glob("[0-9][0-9][0-9][0-9].json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        chapter = str(data.get("chapter", int(path.stem)))
        chapter_totals = blank_usage()
        chapter_models: dict[str, dict] = {}
        chapter_stages: dict[str, dict] = {}
        for name, values in data.get("stages", {}).items():
            if not name.endswith("_model"):
                continue
            if values.get("exact") is not True or values.get("usage_source") != "omp_provider_reported":
                unavailable.append({"chapter": int(chapter), "stage": name, "reason": "legacy_or_missing_exact_usage"})
                continue
            phase = blank_usage()
            add_usage(phase, values)
            chapter_stages[name] = finish_usage(phase)
            add_usage(stages.setdefault(name, blank_usage()), values)
            add_usage(chapter_totals, values)
            add_usage(totals, values)
            for model_name, model_usage in values.get("models", {}).items():
                add_usage(chapter_models.setdefault(model_name, blank_usage()), model_usage)
                add_usage(models.setdefault(model_name, blank_usage()), model_usage)
        chapters[chapter] = {
            "totals": finish_usage(chapter_totals),
            "models": {name: finish_usage(value) for name, value in sorted(chapter_models.items())},
            "stages": chapter_stages,
        }
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
        usage = blank_usage()
        exact_calls = 0
        for metric in [*value.get("review_metrics", []), value.get("refine_metrics", {})]:
            if metric and metric.get("exact") is True:
                add_usage(usage, metric)
                exact_calls += 1
        retrofit_audits.append({
            "range": path.parent.name,
            "stage": value.get("stage"),
            "findings": value.get("finding_count", 0),
            "changed_chapters": value.get("changed_chapters", []),
            "exact_model_calls": exact_calls,
            "usage": finish_usage(usage),
        })
    return {
        "version": 2,
        "usage_source": "omp_provider_reported",
        "chapters": chapters,
        "models": {name: finish_usage(value) for name, value in sorted(models.items())},
        "stages": {name: finish_usage(value) for name, value in sorted(stages.items())},
        "totals": finish_usage(totals),
        "unavailable_stages": unavailable,
        "checkpoint_reviews": checkpoint_reviews,
        "checkpoint_unique_finding_total": sum(item["findings"] for item in checkpoint_reviews),
        "retrofit_audits": retrofit_audits,
    }


def usage_line(label: str, usage: dict) -> str:
    cost = f", ${usage['cost_usd']:.4f}" if "cost_usd" in usage else ""
    reasoning = f", {usage['reasoning_tokens']} reasoning" if usage.get("reasoning_tokens") else ""
    return (
        f"{label}: {usage['requests']} requests, {usage['input_tokens']} input, "
        f"{usage['output_tokens']} output, {usage['cache_read_tokens']} cache-read, "
        f"{usage['cache_write_tokens']} cache-write{reasoning}{cost}"
    )


def chapter_report(report: dict, chapter: int) -> dict:
    selected = report["chapters"].get(str(chapter))
    if selected is None:
        raise SystemExit(f"no usage metrics for chapter {chapter}")
    if not selected["stages"]:
        raise SystemExit(f"exact usage is unavailable for chapter {chapter}")
    return selected


def format_report(report: dict, chapter: int | None = None) -> str:
    if chapter is not None:
        selected = chapter_report(report, chapter)
        lines = [f"Chapter {chapter}"]
        for name, usage in selected["stages"].items():
            lines.append(usage_line(name, usage))
        for name, usage in selected["models"].items():
            lines.append(usage_line(name, usage))
        lines.append(usage_line("Total", selected["totals"]))
        return "\n".join(lines)
    lines = [f"Chapters with metric files: {len(report['chapters'])}"]
    for name, usage in report["models"].items():
        lines.append(usage_line(name, usage))
    lines.append(usage_line("Total", report["totals"]))
    if report["unavailable_stages"]:
        lines.append(
            f"Exact usage unavailable for {len(report['unavailable_stages'])} legacy stages; they were excluded."
        )
    lines.append(
        f"Checkpoint findings: {report['checkpoint_unique_finding_total']} across {len(report['checkpoint_reviews'])} reviews"
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = build_report()
    selected: dict = report
    if args.chapter is not None:
        selected = chapter_report(report, args.chapter)
    if args.json:
        print(json.dumps(selected, indent=2, sort_keys=True))
        return 0
    print(format_report(report, args.chapter))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
