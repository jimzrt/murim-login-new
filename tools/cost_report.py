#!/usr/bin/env python3
"""Report exact provider-reported usage by chapter, phase, and model."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

try:
    from tools.omp_json import billing_type_for, selector_provider
except ModuleNotFoundError:
    from omp_json import billing_type_for, selector_provider

ROOT = Path(__file__).resolve().parents[1]
COUNT_FIELDS = (
    "requests", "input_tokens", "output_tokens", "cache_read_tokens",
    "cache_write_tokens", "total_tokens", "reasoning_tokens",
)
FAMILY_LABELS = {
    "luna": "Luna",
    "grok": "Grok",
    "sol": "Sol",
    "deepseek": "DeepSeek",
    "other": "Other",
}
FAMILY_ORDER = ("luna", "grok", "sol", "deepseek", "other")


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


def model_family(model_key: str) -> str:
    name = model_key.lower()
    for family in ("luna", "grok", "sol", "deepseek"):
        if family in name:
            return family
    return "other"


def stage_name(name: str) -> str:
    return name if name.endswith("_model") else f"{name}_model"


def blank_family() -> dict:
    return blank_usage()


def add_model_to_resources(resources: dict, model_key: str, usage: dict) -> None:
    provider = selector_provider(model_key)
    family = model_family(model_key)
    bucket = resources.setdefault(provider, {
        "provider": provider,
        "billing_type": billing_type_for(provider),
        "families": {},
        **blank_usage(),
    })
    add_usage(bucket, usage)
    add_usage(bucket["families"].setdefault(family, blank_family()), usage)


def finish_resources(resources: dict) -> dict:
    finished = {}
    for provider, bucket in resources.items():
        families = {
            name: finish_usage(value)
            for name, value in sorted(bucket.pop("families").items())
        }
        finished[provider] = {**finish_usage(bucket), "families": families}
    return finished


def merge_stage_map(target: dict[str, dict], stages: dict) -> None:
    for name, values in stages.items():
        target[stage_name(name)] = values


def load_chapter_stages(root: Path) -> dict[str, dict]:
    chapters: dict[str, dict] = {}
    metrics_dir = root / "reviews" / "metrics"
    for path in sorted(metrics_dir.glob("[0-9][0-9][0-9][0-9].json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        chapter = str(data.get("chapter", int(path.stem)))
        chapters[chapter] = dict(data.get("stages", {}))
    mastering_dir = root / "reviews" / "mastering"
    for path in sorted(mastering_dir.glob("[0-9][0-9][0-9][0-9]/metrics.json")):
        chapter = str(int(path.parent.name))
        existing = chapters.setdefault(chapter, {})
        if "master_model" in existing or "adjudicator_model" in existing:
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        merge_stage_map(existing, data.get("stages", {}))
    return chapters


def fetch_subscription_usage() -> dict | None:
    try:
        result = subprocess.run(
            ["omp", "usage", "--redact", "--json"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def quota_summaries(live: dict | None, provider: str) -> list[str]:
    if not isinstance(live, dict):
        return []
    lines = []
    for report in live.get("reports") or []:
        if not isinstance(report, dict) or report.get("provider") != provider:
            continue
        for limit in report.get("limits") or []:
            if not isinstance(limit, dict):
                continue
            amount = limit.get("amount")
            if not isinstance(amount, dict):
                continue
            label = str(limit.get("label") or limit.get("id") or "quota")
            unit = amount.get("unit")
            used = amount.get("used")
            cap = amount.get("limit")
            if unit == "percent" and isinstance(used, (int, float)):
                lines.append(f"{label} {used:g}% used")
            elif unit == "usd" and isinstance(used, (int, float)):
                if isinstance(cap, (int, float)):
                    lines.append(f"{label} ${used:.2f} / ${cap:.2f}")
                else:
                    lines.append(f"{label} ${used:.2f}")
            elif unit == "requests" and isinstance(used, (int, float)) and (
                used or isinstance(cap, (int, float))
            ):
                if isinstance(cap, (int, float)):
                    lines.append(f"{label} {used:g} / {cap:g} requests")
                else:
                    lines.append(f"{label} {used:g} requests")
    return lines


def build_report(*, live_usage: bool = False) -> dict:
    totals = blank_usage()
    models: dict[str, dict] = {}
    stages: dict[str, dict] = {}
    chapters: dict[str, dict] = {}
    unavailable: list[dict] = []
    resources: dict[str, dict] = {}
    for chapter, stage_map in load_chapter_stages(ROOT).items():
        chapter_totals = blank_usage()
        chapter_models: dict[str, dict] = {}
        chapter_stages: dict[str, dict] = {}
        for name, values in stage_map.items():
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
                add_model_to_resources(resources, model_name, model_usage)
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
    report = {
        "version": 3,
        "usage_source": "omp_provider_reported",
        "chapters": chapters,
        "models": {name: finish_usage(value) for name, value in sorted(models.items())},
        "stages": {name: finish_usage(value) for name, value in sorted(stages.items())},
        "totals": finish_usage(totals),
        "resources": finish_resources(resources),
        "unavailable_stages": unavailable,
        "checkpoint_reviews": checkpoint_reviews,
        "checkpoint_unique_finding_total": sum(item["findings"] for item in checkpoint_reviews),
        "retrofit_audits": retrofit_audits,
    }
    if live_usage:
        live = fetch_subscription_usage()
        if live is not None:
            report["subscription_usage"] = live
    return report


def money(value: float) -> str:
    return f"${value:.2f}"


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


def family_requests(bucket: dict, family: str) -> int:
    return int(bucket.get("families", {}).get(family, {}).get("requests", 0))


def family_cost(bucket: dict, family: str) -> float | None:
    usage = bucket.get("families", {}).get(family, {})
    if "cost_usd" not in usage:
        return None
    return float(usage["cost_usd"])


def format_resource_report(report: dict) -> str:
    resources = report.get("resources") or {}
    live = report.get("subscription_usage")
    lines = ["MURIM LOGIN RESOURCE USAGE", ""]

    openai = resources.get("openai-codex", {"families": {}, "requests": 0})
    lines.append("OpenAI subscription")
    for family, label in (("sol", "Sol calls"), ("luna", "Luna calls"), ("grok", "Grok calls")):
        count = family_requests(openai, family)
        if count:
            lines.append(f"  {label:<24}{count:,}")
    if not any(family_requests(openai, family) for family in FAMILY_ORDER):
        lines.append("  Calls:                   0")
    quota = quota_summaries(live, "openai-codex")
    lines.append(f"  Quota currently used:    {'; '.join(quota) if quota else '(unavailable)'}")
    if "cost_usd" in openai:
        lines.append(f"  API-equivalent value:    {money(openai['cost_usd'])}")
    lines.append("  Actual incremental:      $0.00")
    lines.append("")

    cursor = resources.get("cursor", {"families": {}, "requests": 0})
    lines.append("Cursor subscription")
    for family, label in (
        ("luna", "Luna calls"),
        ("grok", "Grok calls"),
        ("sol", "Sol fallback calls"),
    ):
        count = family_requests(cursor, family)
        if count or family == "sol":
            lines.append(f"  {label:<24}{count:,}")
    quota = quota_summaries(live, "cursor")
    lines.append(f"  Monthly allowance used:  {'; '.join(quota) if quota else '(unavailable)'}")
    if "cost_usd" in cursor:
        lines.append(f"  API-equivalent value:    {money(cursor['cost_usd'])}")
    lines.append("  Actual incremental:      $0.00")
    lines.append("")

    openrouter = resources.get("openrouter", {"families": {}, "requests": 0})
    lines.append("OpenRouter")
    spent = 0.0
    saw_cost = False
    for family in FAMILY_ORDER:
        cost = family_cost(openrouter, family)
        count = family_requests(openrouter, family)
        if cost is None and not count:
            continue
        label = FAMILY_LABELS[family]
        if cost is None:
            lines.append(f"  {label + ':':<24}{count:,} calls (cost unreported)")
            continue
        saw_cost = True
        spent += cost
        lines.append(f"  {label + ':':<24}{money(cost)}")
    if saw_cost:
        lines.append(f"  {'':-<24}--------")
        lines.append(f"  {'Actual token spend:':<24}{money(spent)}")
    elif not any(family_requests(openrouter, family) for family in FAMILY_ORDER):
        lines.append("  Actual token spend:      $0.00")
    return "\n".join(lines)


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
    lines = [format_resource_report(report), ""]
    lines.append(f"Chapters with metric files: {len(report['chapters'])}")
    for name, usage in report["models"].items():
        lines.append(usage_line(name, usage))
    token_total = dict(report["totals"])
    token_total.pop("cost_usd", None)
    lines.append(usage_line("Total", token_total))
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
    report = build_report(live_usage=True)
    selected: dict = report
    if args.chapter is not None:
        selected = chapter_report(report, args.chapter)
    if args.json:
        print(json.dumps(selected, indent=2, sort_keys=True))
        return 0
    print(format_report(report, args.chapter))
    if args.chapter is not None:
        print()
        print(format_resource_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
