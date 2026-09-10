#!/usr/bin/env python3
"""Deterministic controller for one-chapter translation transactions."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
try:
    from tools.run_lock import hold_run_lock
except ModuleNotFoundError:
    from run_lock import hold_run_lock

STAGES = (
    "READY", "CONTEXT_READY", "DRAFTED", "REVIEWED", "REVISED", "POLISHED",
    "CHECKPOINT_REVIEWED", "CHECKPOINT_APPLIED", "ACCEPTED", "COMMITTED",
)
HANGUL = re.compile(r"[가-힣]")
MODEL_ROLES = ("draft", "review", "revision", "polish", "summary", "coordinator")
DEFAULT_CONFIG = {
    "models": {
        "draft": "openai-codex/gpt-5.6-luna:high",
        "review": "openai-codex/gpt-5.6-sol:medium",
        "revision": "openai-codex/gpt-5.6-luna:high",
        "polish": "openai-codex/gpt-5.6-luna:high",
        "summary": "openai-codex/gpt-5.6-luna:high",
        "coordinator": "openai-codex/gpt-5.6-luna:high",
    },
    "context_max_bytes": 16384,
    "continuity_source_limit": 2,
    "packet_token_limits": {
        "draft": 60000, "review": 60000, "revision": 60000, "polish": 60000,
        "checkpoint": 120000, "summary": 20000,
    },
    "summary_interval": 5,
    "beat_max_bytes": 4096,
    "checkpoint_review_interval": 5,
    "checkpoint_evaluation_window": 20,
    "polish_from_chapter": 27,
}


def resolve_role_models(value: dict) -> dict:
    models = value.get("models") if isinstance(value.get("models"), dict) else {}
    resolved: dict[str, str] = {}
    missing: list[str] = []
    for role in MODEL_ROLES:
        name = models.get(role) or value.get(f"{role}_model")
        if not isinstance(name, str) or not name.strip():
            missing.append(role)
            continue
        resolved[role] = name.strip()
    if missing:
        raise SystemExit("docs/workflow.json models must define: " + ", ".join(missing))
    value = dict(value)
    value["models"] = resolved
    for role, name in resolved.items():
        value[f"{role}_model"] = name
    checkpoint = models.get("checkpoint") or value.get("checkpoint_model")
    if isinstance(checkpoint, str) and checkpoint.strip():
        value["checkpoint_model"] = checkpoint.strip()
    else:
        value["checkpoint_model"] = value["review_model"]
    return value


def project_config() -> dict:
    path = ROOT / "docs" / "workflow.json"
    value = json.loads(path.read_text(encoding="utf-8")) if path.exists() else DEFAULT_CONFIG
    value = resolve_role_models(value)
    summary = int(value["summary_interval"])
    checkpoint = int(value["checkpoint_review_interval"])
    if summary <= 0 or checkpoint <= 0 or checkpoint % summary:
        raise SystemExit("checkpoint_review_interval must be a positive multiple of summary_interval")
    if int(value["continuity_source_limit"]) < 0 or int(value["continuity_source_limit"]) > 2:
        raise SystemExit("continuity_source_limit must be between 0 and 2")
    value["polish_from_chapter"] = int(value.get("polish_from_chapter", 27))
    if value["polish_from_chapter"] < 0:
        raise SystemExit("polish_from_chapter must be non-negative")
    return value


def estimated_tokens(text: str) -> int:
    return (len(text.encode("utf-8")) + 3) // 4


def enforce_packet_budget(phase: str, text: str) -> int:
    estimate = estimated_tokens(text)
    limit = project_config()["packet_token_limits"][phase]
    if estimate > limit:
        raise SystemExit(f"{phase} packet estimate {estimate} exceeds configured limit {limit}")
    return estimate


def interval_due(number: int, key: str) -> bool:
    interval = int(project_config()[key])
    return interval > 0 and (number + 1) % interval == 0


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def paths(number: int) -> dict[str, Path]:
    work = ROOT / ".work" / f"{number:04d}"
    checkpoint_interval = int(project_config()["checkpoint_review_interval"])
    block_start = number - checkpoint_interval + 1
    block_name = f"{block_start:04d}-{number:04d}"
    summary_interval = int(project_config()["summary_interval"])
    summary_start = number - summary_interval + 1
    summary_name = f"{summary_start:04d}-{number:04d}"
    return {
        "work": work,
        "state": work / "workflow.json",
        "context": work / "context.md",
        "draft": work / "draft.md",
        "draft_qa": ROOT / "reviews" / "qa" / f"{number:04d}-draft.json",
        "revised": work / "revised.md",
        "final_qa": ROOT / "reviews" / "qa" / f"{number:04d}-final.json",
        "revision_context": work / "revision-context.md",
        "polish_context": work / "polish-context.md",
        "polished": work / "polished.md",
        "polish_qa": ROOT / "reviews" / "qa" / f"{number:04d}-polish.json",
        "dispositions": ROOT / "reviews" / "sol" / f"{number:04d}.dispositions.json",
        "metrics": ROOT / "reviews" / "metrics" / f"{number:04d}.json",
        "translation": ROOT / "translations" / f"{number:04d}.md",
        "packet": ROOT / "reviews" / "packets" / f"{number:04d}.md",
        "report": ROOT / "reviews" / "sol" / f"{number:04d}.md",
        "review_json": ROOT / "reviews" / "sol" / f"{number:04d}.json",
        "review_meta": ROOT / "reviews" / "sol" / f"{number:04d}.meta.json",
        "beat": ROOT / "summaries" / "beats" / f"{number:04d}.md",
        "checkpoint_summary": ROOT / "summaries" / f"{summary_name}.md",
        "summary_packet": ROOT / "reviews" / "packets" / f"summary-{summary_name}.md",
        "checkpoint_packet": ROOT / "reviews" / "packets" / f"checkpoint-{block_name}.md",
        "checkpoint_report": ROOT / "reviews" / "checkpoints" / f"{block_name}.md",
        "checkpoint_json": ROOT / "reviews" / "checkpoints" / f"{block_name}.json",
        "checkpoint_meta": ROOT / "reviews" / "checkpoints" / f"{block_name}.meta.json",
        "checkpoint_disposition": ROOT / "reviews" / "checkpoints" / f"{block_name}.dispositions.json",
    }


def source_hash(number: int) -> str:
    try:
        from tools.chapter import extract_chapter
    except ModuleNotFoundError:  # Direct execution from tools/.
        from chapter import extract_chapter

    try:
        source = extract_chapter(number)
    except ValueError as error:
        raise SystemExit(str(error)) from None
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def load(number: int) -> tuple[dict, dict[str, Path]]:
    p = paths(number)
    current_source_hash = source_hash(number)
    if p["state"].exists():
        state = json.loads(p["state"].read_text(encoding="utf-8"))
        if state.get("source_sha256") != current_source_hash:
            raise SystemExit("source changed after this transaction began; stop for manual reconciliation")
    else:
        completed_match = re.search(
            r"^- Last completed:\s*(\d+)\s*$",
            (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8"),
            re.MULTILINE,
        )
        next_match = re.search(
            r"^- Next chapter:\s*(\d+)\s*$",
            (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8"),
            re.MULTILINE,
        )
        already_accepted = bool(
            completed_match
            and number <= int(completed_match.group(1))
            and p["translation"].exists()
        )
        if not already_accepted and next_match and number != int(next_match.group(1)):
            raise SystemExit(f"requested chapter {number} does not match docs/STATE.md next chapter {next_match.group(1)}")
        state = {
            "version": 1,
            "chapter": number,
            "stage": "COMMITTED" if already_accepted else "READY",
            "source_sha256": current_source_hash,
            "artifacts": {},
        }
        if already_accepted:
            state["artifacts"]["translation_sha256"] = digest(p["translation"])
            state["reconciled_legacy_acceptance"] = True
            state["artifacts"]["commit"] = "pre-controller checkpoint"
        atomic_json(p["state"], state)
    return state, p


def require(state: dict, *allowed: str) -> None:
    if state["stage"] not in allowed:
        raise SystemExit(f"stage is {state['stage']}; expected one of: {', '.join(allowed)}")


def save(state: dict, p: dict[str, Path], stage: str, **artifacts: str) -> None:
    state["stage"] = stage
    state["artifacts"].update(artifacts)
    atomic_json(p["state"], state)


IN_FLIGHT_STAGES = {
    "CONTEXT_READY", "DRAFTED", "REVIEWED", "REVISED", "POLISHED",
    "CHECKPOINT_REVIEWED", "CHECKPOINT_APPLIED",
}


def _git_tracks(relative: str) -> bool:
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", relative],
        cwd=ROOT, text=True, capture_output=True,
    )
    return result.returncode == 0


def incomplete_chapter() -> int | None:
    work = ROOT / ".work"
    if not work.is_dir():
        return None
    found: list[int] = []
    for path in sorted(work.glob("[0-9][0-9][0-9][0-9]/workflow.json")):
        try:
            state = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        number = state.get("chapter")
        stage = state.get("stage")
        if not isinstance(number, int):
            continue
        if stage in IN_FLIGHT_STAGES:
            found.append(number)
        elif stage == "ACCEPTED" and not _git_tracks(f"translations/{number:04d}.md"):
            found.append(number)
    unique = sorted(set(found))
    if len(unique) > 1:
        raise SystemExit("multiple incomplete chapter transactions: " + ", ".join(map(str, unique)))
    return unique[0] if unique else None


def record_failed_model_output(path: Path, raw: str, error: Exception) -> None:
    atomic_text(path, raw)
    raise SystemExit(f"{error}\nraw output saved: {path.relative_to(ROOT)}") from None


def record_metric(p: dict[str, Path], phase: str, **values: object) -> None:
    metrics = {"version": 2, "chapter": int(p["work"].name), "stages": {}}
    if p["metrics"].exists():
        metrics = json.loads(p["metrics"].read_text(encoding="utf-8"))
    metrics["version"] = 2
    metrics.setdefault("stages", {})[phase] = values
    atomic_json(p["metrics"], metrics)


def validate_reading_copy(path: Path, number: int) -> None:
    if not path.exists() or not path.read_text(encoding="utf-8").strip():
        raise SystemExit(f"missing or empty reading copy: {path}")
    text = path.read_text(encoding="utf-8")
    first = next((line.strip() for line in text.splitlines() if line.strip()), "")
    if first != f"# Chapter {number}":
        raise SystemExit(f"first nonblank line must be '# Chapter {number}'")
    if HANGUL.search(text):
        raise SystemExit("reading copy contains Hangul; final chapter must be English-only")


def polish_due(number: int) -> bool:
    return number >= int(project_config()["polish_from_chapter"])


def post_revision_stage(number: int) -> str:
    return "POLISHED" if polish_due(number) else "REVISED"


def reading_copy_path(p: dict[str, Path], number: int) -> Path:
    return p["polished"] if polish_due(number) else p["revised"]


def durable_next_action(number: int, p: dict[str, Path]) -> str:
    beat = p["beat"].relative_to(ROOT)
    durable = (
        f"update {beat}, docs/STATE.md, docs/CONTEXT.json "
        "(keep version, continuity_sources, active_continuity, open_questions, "
        "and temporary_decisions), and profiles from this chapter only"
    )
    if interval_due(number, "summary_interval") and not checkpoint_exists(number):
        return f"{durable}, then: python tools/workflow.py summarize {number}"
    if interval_due(number, "checkpoint_review_interval"):
        return f"python tools/workflow.py checkpoint {number}"
    return f"{durable}, then: python tools/workflow.py accept {number}"


def next_action(state: dict, p: dict[str, Path]) -> str:
    number = state["chapter"]
    if state["stage"] == "REVISED":
        if polish_due(number):
            return f"python tools/workflow.py polish {number}"
        return durable_next_action(number, p)
    if state["stage"] == "POLISHED":
        return durable_next_action(number, p)
    return {
        "READY": f"python tools/workflow.py prepare {number}",
        "CONTEXT_READY": f"python tools/workflow.py draft {number}",
        "DRAFTED": f"python tools/workflow.py review {number}",
        "REVIEWED": f"python tools/workflow.py revise {number}",
        "CHECKPOINT_REVIEWED": f"apply or disposition checkpoint findings in {p['checkpoint_disposition'].relative_to(ROOT)}, then: python tools/workflow.py checkpointed {number}",
        "CHECKPOINT_APPLIED": f"python tools/workflow.py accept {number}",
        "ACCEPTED": f"commit accepted files, then: python tools/workflow.py committed {number} --commit HEAD",
        "COMMITTED": "stop; do not begin another chapter",
    }[state["stage"]]


def command_prepare(number: int) -> None:
    state, p = load(number)
    require(state, "READY", "CONTEXT_READY")
    try:
        from tools.context import build_draft_packet
    except ModuleNotFoundError:  # Direct execution from tools/.
        from context import build_draft_packet

    try:
        packet = build_draft_packet(number)
    except (ValueError, FileNotFoundError) as error:
        raise SystemExit(str(error)) from None
    packet_tokens = enforce_packet_budget("draft", packet)
    p["context"].parent.mkdir(parents=True, exist_ok=True)
    atomic_text(p["context"], packet)
    record_metric(p, "draft_packet", packet_token_estimate=packet_tokens, input_bytes=len(packet.encode("utf-8")))
    save(state, p, "CONTEXT_READY", context_sha256=digest(p["context"]))


def command_drafted(number: int) -> None:
    state, p = load(number)
    require(state, "CONTEXT_READY", "DRAFTED")
    validate_reading_copy(p["draft"], number)
    try:
        from tools.context import chapter_text, exact_glossary_entries
        from tools.qa import run_qa
    except ModuleNotFoundError:
        from context import chapter_text, exact_glossary_entries
        from qa import run_qa
    source = chapter_text(number)
    glossary = [(item["korean"], item["english"]) for item in exact_glossary_entries(source)]
    qa = run_qa(number, source, p["draft"].read_text(encoding="utf-8"), glossary)
    atomic_json(p["draft_qa"], qa)
    if not qa["passed"]:
        raise SystemExit(f"draft failed deterministic QA; inspect {p['draft_qa']}")
    save(state, p, "DRAFTED", draft_sha256=digest(p["draft"]), draft_qa_sha256=digest(p["draft_qa"]))


def omp_log_path(number: int, phase: str) -> Path:
    return ROOT / ".work" / f"{number:04d}" / "omp" / f"{phase}.jsonl"


def run_omp(packet: Path, model: str, timeout: int, log_path: Path | None = None) -> tuple[str, dict]:
    try:
        from tools.omp_json import OmpJsonError, run_json_command
    except ModuleNotFoundError:
        from omp_json import OmpJsonError, run_json_command
    command = [
        "omp",
        "--mode",
        "json",
        "--no-session",
        "--no-tools",
        "--no-rules",
        "--no-extensions",
        "--config",
        str(ROOT / ".omp" / "review-overlay.yml"),
        "--model",
        model,
        "--max-time",
        str(timeout - 60),
        f"@{packet}",
    ]
    try:
        output, metrics = run_json_command(
            command, cwd=ROOT, requested_model=model, timeout=timeout, log_path=log_path,
        )
    except OmpJsonError as error:
        raise SystemExit(str(error)) from None
    metrics["input_bytes"] = packet.stat().st_size
    return output, metrics


def command_draft(number: int) -> None:
    state, p = load(number)
    require(state, "CONTEXT_READY")
    if digest(p["context"]) != state["artifacts"]["context_sha256"]:
        raise SystemExit("context packet changed after CONTEXT_READY; run prepare again")
    output, metrics = run_omp(
        p["context"], project_config()["draft_model"], 960, log_path=omp_log_path(number, "draft"),
    )
    atomic_text(p["work"] / "draft-raw.txt", output)
    try:
        from tools.model_io import extract_reading_copy
    except ModuleNotFoundError:
        from model_io import extract_reading_copy
    try:
        copy = extract_reading_copy(output, number)
    except ValueError as error:
        record_failed_model_output(p["work"] / "draft-raw.txt", output, error)
    atomic_text(p["draft"], copy)
    record_metric(p, "draft_model", **metrics)
    command_drafted(number)


def command_review(number: int, dry_run: bool) -> None:
    state, p = load(number)
    require(state, "DRAFTED")
    if digest(p["draft"]) != state["artifacts"]["draft_sha256"]:
        raise SystemExit(f"draft changed after DRAFTED; run: python tools/workflow.py drafted {number}")
    if digest(p["draft_qa"]) != state["artifacts"]["draft_qa_sha256"]:
        raise SystemExit("draft QA changed after DRAFTED")
    command = [
        sys.executable, str(ROOT / "tools" / "review_chapter.py"), str(number),
        "--draft", str(p["draft"]), "--qa", str(p["draft_qa"]),
    ]
    if dry_run:
        command.append("--dry-run")
    try:
        subprocess.run(command, cwd=ROOT, check=True)
    except subprocess.CalledProcessError as error:
        raise SystemExit(f"review command failed with exit code {error.returncode}") from None
    if dry_run:
        return
    meta = json.loads(p["review_meta"].read_text(encoding="utf-8"))
    if meta["draft_sha256"] != state["artifacts"]["draft_sha256"]:
        raise SystemExit("review metadata does not match the recorded draft")
    save(
        state,
        p,
        "REVIEWED",
        reviewed_draft_sha256=meta["draft_sha256"],
        report_sha256=digest(p["review_json"]),
        review_markdown_sha256=digest(p["report"]),
    )
    record_metric(
        p,
        "review_model",
        **meta["usage"],
        finding_count=meta["finding_count"],
        major_or_critical_count=meta["major_or_critical_count"],
    )


def command_revised(number: int) -> None:
    state, p = load(number)
    require(state, "REVIEWED", "REVISED")
    if digest(p["draft"]) != state["artifacts"]["reviewed_draft_sha256"]:
        raise SystemExit("review is stale because draft.md changed")
    validate_reading_copy(p["revised"], number)
    if not p["dispositions"].exists():
        raise SystemExit(f"missing structured dispositions: {p['dispositions']}")
    review = json.loads(p["review_json"].read_text(encoding="utf-8"))
    dispositions = json.loads(p["dispositions"].read_text(encoding="utf-8"))
    try:
        from tools.model_io import blocking_dispositions
        from tools.context import chapter_text, exact_glossary_entries
        from tools.qa import run_qa
    except ModuleNotFoundError:
        from model_io import blocking_dispositions
        from context import chapter_text, exact_glossary_entries
        from qa import run_qa
    if blocking_dispositions(review, dispositions):
        raise SystemExit("critical or major findings remain unresolved")
    source = chapter_text(number)
    glossary = [(item["korean"], item["english"]) for item in exact_glossary_entries(source)]
    qa = run_qa(number, source, p["revised"].read_text(encoding="utf-8"), glossary)
    atomic_json(p["final_qa"], qa)
    if not qa["passed"]:
        raise SystemExit(f"revision failed deterministic QA; inspect {p['final_qa']}")
    save(
        state,
        p,
        "REVISED",
        revised_sha256=digest(p["revised"]),
        dispositions_sha256=digest(p["dispositions"]),
        final_qa_sha256=digest(p["final_qa"]),
    )


def command_revise(number: int) -> None:
    state, p = load(number)
    require(state, "REVIEWED")
    if digest(p["draft"]) != state["artifacts"]["reviewed_draft_sha256"]:
        raise SystemExit("review is stale because draft.md changed")
    if digest(p["review_json"]) != state["artifacts"]["report_sha256"]:
        raise SystemExit("saved review changed after REVIEWED")
    try:
        from tools.context import build_revision_packet
        from tools.model_io import parse_revision_response
    except ModuleNotFoundError:
        from context import build_revision_packet
        from model_io import parse_revision_response
    review = json.loads(p["review_json"].read_text(encoding="utf-8"))
    packet = build_revision_packet(number, p["draft"].read_text(encoding="utf-8"), review)
    enforce_packet_budget("revision", packet)
    atomic_text(p["revision_context"], packet)
    raw, metrics = run_omp(
        p["revision_context"],
        project_config()["revision_model"],
        960,
        log_path=omp_log_path(number, "revision"),
    )
    atomic_text(p["work"] / "revision-raw.txt", raw)
    try:
        revision = parse_revision_response(raw, review)
    except ValueError as error:
        record_failed_model_output(p["work"] / "revision-raw.txt", raw, error)
    atomic_text(p["revised"], revision["translation"])
    canonical_dispositions = {"version": 1, "dispositions": revision["dispositions"]}
    atomic_json(p["dispositions"], canonical_dispositions)
    record_metric(p, "revision_model", **metrics)
    command_revised(number)


def command_polished(number: int) -> None:
    state, p = load(number)
    require(state, "REVISED", "POLISHED")
    if digest(p["revised"]) != state["artifacts"]["revised_sha256"]:
        raise SystemExit("polish is stale because revised.md changed")
    validate_reading_copy(p["polished"], number)
    try:
        from tools.context import chapter_text, exact_glossary_entries
        from tools.qa import run_qa
    except ModuleNotFoundError:
        from context import chapter_text, exact_glossary_entries
        from qa import run_qa
    source = chapter_text(number)
    glossary = [(item["korean"], item["english"]) for item in exact_glossary_entries(source)]
    qa = run_qa(number, source, p["polished"].read_text(encoding="utf-8"), glossary)
    atomic_json(p["polish_qa"], qa)
    atomic_json(p["final_qa"], qa)
    if not qa["passed"]:
        raise SystemExit(f"polish failed deterministic QA; inspect {p['polish_qa']}")
    save(
        state,
        p,
        "POLISHED",
        polished_sha256=digest(p["polished"]),
        final_qa_sha256=digest(p["final_qa"]),
    )


def command_polish(number: int) -> None:
    state, p = load(number)
    require(state, "REVISED")
    if not polish_due(number):
        raise SystemExit(f"polish starts at chapter {project_config()['polish_from_chapter']}")
    if digest(p["revised"]) != state["artifacts"]["revised_sha256"]:
        raise SystemExit("revised.md changed after REVISED")
    if digest(p["dispositions"]) != state["artifacts"]["dispositions_sha256"]:
        raise SystemExit("structured dispositions changed after REVISED")
    try:
        from tools.context import build_polish_packet
    except ModuleNotFoundError:
        from context import build_polish_packet
    packet = build_polish_packet(number, p["revised"].read_text(encoding="utf-8"))
    enforce_packet_budget("polish", packet)
    atomic_text(p["polish_context"], packet)
    raw, metrics = run_omp(
        p["polish_context"],
        project_config()["polish_model"],
        960,
        log_path=omp_log_path(number, "polish"),
    )
    atomic_text(p["work"] / "polish-raw.txt", raw)
    try:
        from tools.model_io import extract_reading_copy
    except ModuleNotFoundError:
        from model_io import extract_reading_copy
    try:
        copy = extract_reading_copy(raw, number)
    except ValueError as error:
        record_failed_model_output(p["work"] / "polish-raw.txt", raw, error)
    atomic_text(p["polished"], copy)
    record_metric(p, "polish_model", **metrics)
    command_polished(number)


def command_summarize(number: int) -> None:
    state, p = load(number)
    require(state, post_revision_stage(number))
    if not interval_due(number, "summary_interval"):
        raise SystemExit("this chapter does not end a summary block")
    if not state_claims_completion(number):
        raise SystemExit("update Last completed and Next chapter in docs/STATE.md before summarizing")
    if not context_claims_completion(number):
        raise SystemExit(f"update bounded docs/CONTEXT.json through chapter {number} before summarizing")
    try:
        from tools.context import build_summary_packet, normalize_block_summary
    except ModuleNotFoundError:
        from context import build_summary_packet, normalize_block_summary
    try:
        packet = build_summary_packet(number)
    except (ValueError, FileNotFoundError) as error:
        raise SystemExit(str(error)) from None
    packet_tokens = enforce_packet_budget("summary", packet)
    atomic_text(p["summary_packet"], packet)
    raw, metrics = run_omp(
        p["summary_packet"],
        project_config()["summary_model"],
        960,
        log_path=omp_log_path(number, "summary"),
    )
    atomic_text(p["work"] / "summary-raw.txt", raw)
    interval = int(project_config()["summary_interval"])
    start = number - interval + 1
    try:
        summary = normalize_block_summary(raw, start, number)
    except ValueError as error:
        raise SystemExit(str(error)) from None
    atomic_text(p["checkpoint_summary"], summary)
    record_metric(
        p,
        "summary_model",
        **metrics,
        packet_token_estimate=packet_tokens,
    )
    save(state, p, post_revision_stage(number), summary_sha256=digest(p["checkpoint_summary"]))


def state_claims_completion(number: int) -> bool:
    text = (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8")
    completed = re.search(r"^- Last completed:\s*(\d+)\s*$", text, re.MULTILINE)
    next_chapter = re.search(r"^- Next chapter:\s*(\d+)\s*$", text, re.MULTILINE)
    return bool(
        completed
        and int(completed.group(1)) == number
        and next_chapter
        and int(next_chapter.group(1)) == number + 1
    )


def context_claims_completion(number: int) -> bool:
    path = ROOT / "docs" / "CONTEXT.json"
    if not path.exists() or path.stat().st_size > project_config()["context_max_bytes"]:
        return False
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    if not isinstance(value, dict):
        return False
    try:
        from tools.context import durable_context_problems
    except ModuleNotFoundError:
        from context import durable_context_problems
    return not durable_context_problems(value, number, project_config()["continuity_source_limit"])


def checkpoint_exists(number: int) -> bool:
    if not interval_due(number, "summary_interval"):
        return True
    start = number - int(project_config()["summary_interval"]) + 1
    return (ROOT / "summaries" / f"{start:04d}-{number:04d}.md").exists()


def checkpoint_summary_paths(number: int) -> list[Path]:
    summary_interval = int(project_config()["summary_interval"])
    review_interval = int(project_config()["checkpoint_review_interval"])
    first_end = number - review_interval + summary_interval
    return [
        ROOT / "summaries" / f"{end-summary_interval+1:04d}-{end:04d}.md"
        for end in range(first_end, number + 1, summary_interval)
    ]


def command_checkpoint(number: int) -> None:
    state, p = load(number)
    require(state, post_revision_stage(number))
    if not interval_due(number, "checkpoint_review_interval"):
        raise SystemExit("this chapter does not end a five-chapter block")
    if not state_claims_completion(number):
        raise SystemExit("update Last completed and Next chapter in docs/STATE.md before checkpoint review")
    if not context_claims_completion(number):
        raise SystemExit(f"update bounded docs/CONTEXT.json through chapter {number} before checkpoint review")
    summary_paths = checkpoint_summary_paths(number)
    missing_summaries = [path for path in summary_paths if not path.exists()]
    if missing_summaries:
        raise SystemExit("missing checkpoint summaries: " + ", ".join(map(str, missing_summaries)))
    chapters: list[str] = []
    review_interval = int(project_config()["checkpoint_review_interval"])
    for chapter in range(number - review_interval + 1, number + 1):
        chapter_path = reading_copy_path(p, number) if chapter == number else ROOT / "translations" / f"{chapter:04d}.md"
        validate_reading_copy(chapter_path, chapter)
        chapters.append(f"## Chapter artifact {chapter}\n\n{chapter_path.read_text(encoding='utf-8').strip()}")
    rules = (ROOT / "RULES.md").read_text(encoding="utf-8").strip()
    durable_state = (ROOT / "docs" / "CONTEXT.json").read_text(encoding="utf-8").strip()
    summaries = "\n\n".join(path.read_text(encoding="utf-8").strip() for path in summary_paths)
    packet = f"""# Checkpoint Review — {number - review_interval + 1}–{number}

Review only this bounded packet. Check the English reading copies, summaries,
and active state for voice drift, terminology drift, dropped hooks, formatting
differences, internal contradiction, and accidental spoilers. Do not redo the
source-fidelity reviews and do not rewrite files. Return exactly one JSON object
using the chapter-review schema: summary plus a findings array. Use stable IDs
`C01`, `C02`, and so on; source identifies the chapter/location, current quotes
the exact English, correction gives the action, and confidence is 0 through 1.
Use an empty findings array when nothing is actionable.

Return this exact shape with no Markdown fence:

{{
  "summary": "brief assessment",
  "findings": [
    {{
      "id": "C01",
      "severity": "critical|major|minor",
      "source": "chapter and location",
      "current": "exact current English",
      "defect": "specific defect",
      "correction": "recommended action",
      "rationale": "specific reason",
      "confidence": 0.0
    }}
  ]
}}

## Binding rules

{rules}

## Checkpoint summary

{summaries}

## Durable state

{durable_state}

## Reading copies

{chr(10).join(chapters)}
"""
    enforce_packet_budget("checkpoint", packet)
    atomic_text(p["checkpoint_packet"], packet)
    raw_report, metrics = run_omp(
        p["checkpoint_packet"],
        project_config()["checkpoint_model"],
        960,
        log_path=omp_log_path(number, "checkpoint"),
    )
    atomic_text(p["work"] / "checkpoint-raw.txt", raw_report)
    try:
        from tools.model_io import parse_json_object, review_markdown, validate_review
    except ModuleNotFoundError:
        from model_io import parse_json_object, review_markdown, validate_review
    try:
        report = validate_review(parse_json_object(raw_report))
    except ValueError as error:
        record_failed_model_output(p["work"] / "checkpoint-raw.txt", raw_report, error)
    atomic_json(p["checkpoint_json"], report)
    atomic_text(p["checkpoint_report"], review_markdown(report))
    record_metric(
        p,
        "checkpoint_model",
        **metrics,
        finding_count=len(report["findings"]),
        major_or_critical_count=sum(item["severity"] in {"major", "critical"} for item in report["findings"]),
    )
    metadata = {
        "chapter": number,
        "packet_sha256": digest(p["checkpoint_packet"]),
        "report_sha256": digest(p["checkpoint_json"]),
        "finding_count": len(report["findings"]),
        "major_or_critical_count": sum(item["severity"] in {"major", "critical"} for item in report["findings"]),
        "revised_sha256": digest(reading_copy_path(p, number)),
        "summary_sha256": {str(path.relative_to(ROOT)): digest(path) for path in summary_paths},
    }
    atomic_json(p["checkpoint_meta"], metadata)
    save(state, p, "CHECKPOINT_REVIEWED", checkpoint_report_sha256=metadata["report_sha256"])


def command_checkpointed(number: int) -> None:
    state, p = load(number)
    require(state, "CHECKPOINT_REVIEWED")
    if digest(p["checkpoint_json"]) != state["artifacts"]["checkpoint_report_sha256"]:
        raise SystemExit("checkpoint report changed after review")
    if not p["checkpoint_disposition"].exists():
        raise SystemExit("write checkpoint-disposition.json before continuing")
    try:
        disposition_object = json.loads(p["checkpoint_disposition"].read_text(encoding="utf-8"))
        from tools.model_io import blocking_dispositions, validate_dispositions
    except ModuleNotFoundError:
        from model_io import blocking_dispositions, validate_dispositions
    except json.JSONDecodeError as error:
        raise SystemExit(f"invalid checkpoint disposition JSON: {error}") from None
    checkpoint_review = json.loads(p["checkpoint_json"].read_text(encoding="utf-8"))
    try:
        normalized = validate_dispositions(disposition_object.get("dispositions"), checkpoint_review)
    except ValueError as error:
        raise SystemExit(str(error)) from None
    normalized_object = {"version": 1, "dispositions": normalized}
    if blocking_dispositions(checkpoint_review, normalized_object):
        raise SystemExit("critical or major checkpoint findings remain unresolved")
    atomic_json(p["checkpoint_disposition"], normalized_object)
    copy = reading_copy_path(p, number)
    validate_reading_copy(copy, number)
    try:
        from tools.context import chapter_text, exact_glossary_entries
        from tools.qa import run_qa
    except ModuleNotFoundError:
        from context import chapter_text, exact_glossary_entries
        from qa import run_qa
    source = chapter_text(number)
    glossary = [(item["korean"], item["english"]) for item in exact_glossary_entries(source)]
    qa = run_qa(number, source, copy.read_text(encoding="utf-8"), glossary)
    atomic_json(p["final_qa"], qa)
    if not qa["passed"]:
        raise SystemExit(f"checkpoint revision failed deterministic QA; inspect {p['final_qa']}")
    artifacts = {
        "revised_sha256": digest(copy),
        "checkpoint_disposition_sha256": digest(p["checkpoint_disposition"]),
        "final_qa_sha256": digest(p["final_qa"]),
    }
    if polish_due(number):
        artifacts["polished_sha256"] = digest(copy)
    save(state, p, "CHECKPOINT_APPLIED", **artifacts)


def command_accept(number: int) -> None:
    state, p = load(number)
    expected = "CHECKPOINT_APPLIED" if interval_due(number, "checkpoint_review_interval") else post_revision_stage(number)
    require(state, expected)
    copy = reading_copy_path(p, number)
    validate_reading_copy(copy, number)
    copy_key = "polished_sha256" if polish_due(number) else "revised_sha256"
    if digest(copy) != state["artifacts"][copy_key]:
        raise SystemExit("reading copy changed after the last recorded stage; record it again before acceptance")
    if digest(p["dispositions"]) != state["artifacts"]["dispositions_sha256"]:
        raise SystemExit("structured dispositions changed after REVISED")
    if digest(p["final_qa"]) != state["artifacts"]["final_qa_sha256"]:
        raise SystemExit("final QA changed after the last recorded stage")
    if not state_claims_completion(number):
        raise SystemExit(
            f"docs/STATE.md must say '- Last completed: {number}' and '- Next chapter: {number + 1}' before acceptance"
        )
    if not context_claims_completion(number):
        raise SystemExit(
            f"docs/CONTEXT.json must stay bounded, keep version and required keys, "
            f"and set safe_through to {number}"
        )
    if not checkpoint_exists(number):
        raise SystemExit("five-chapter summary is missing for this checkpoint chapter")
    if not p["beat"].exists():
        raise SystemExit(f"write {p['beat'].relative_to(ROOT)} before acceptance")
    p["translation"].parent.mkdir(parents=True, exist_ok=True)
    temporary = p["translation"].with_suffix(".md.tmp")
    shutil.copyfile(copy, temporary)
    os.replace(temporary, p["translation"])
    save(state, p, "ACCEPTED", translation_sha256=digest(p["translation"]))


def command_committed(number: int, commit: str) -> None:
    state, p = load(number)
    require(state, "ACCEPTED")
    resolved = subprocess.run(
        ["git", "rev-parse", "--verify", commit], cwd=ROOT, text=True, capture_output=True, check=True
    ).stdout.strip()
    names = subprocess.run(
        ["git", "show", "--format=", "--name-only", resolved], cwd=ROOT, text=True, capture_output=True, check=True
    ).stdout.splitlines()
    required = {
        str(p["translation"].relative_to(ROOT)),
        str(p["report"].relative_to(ROOT)),
        str(p["review_meta"].relative_to(ROOT)),
        str(p["beat"].relative_to(ROOT)),
    }
    if interval_due(number, "summary_interval"):
        required.update(
            {
                str(p["checkpoint_summary"].relative_to(ROOT)),
                str(p["summary_packet"].relative_to(ROOT)),
            }
        )
    if interval_due(number, "checkpoint_review_interval"):
        required.update(
            {
                str(p["checkpoint_packet"].relative_to(ROOT)),
                str(p["checkpoint_report"].relative_to(ROOT)),
                str(p["checkpoint_json"].relative_to(ROOT)),
                str(p["checkpoint_meta"].relative_to(ROOT)),
                str(p["checkpoint_disposition"].relative_to(ROOT)),
            }
        )
    required.update(
        {
            str(p["review_json"].relative_to(ROOT)),
            str(p["review_meta"].relative_to(ROOT)),
            str(p["dispositions"].relative_to(ROOT)),
            str(p["draft_qa"].relative_to(ROOT)),
            str(p["final_qa"].relative_to(ROOT)),
            str(p["metrics"].relative_to(ROOT)),
        }
    )
    if polish_due(number):
        required.add(str(p["polish_qa"].relative_to(ROOT)))
    missing = required.difference(names)
    if missing:
        raise SystemExit("commit is missing: " + ", ".join(sorted(missing)))
    save(state, p, "COMMITTED", commit=resolved)


def command_status(number: int, as_json: bool) -> None:
    state, p = load(number)
    result = {**state, "next_action": next_action(state, p)}
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(f"Chapter: {number}\nStage: {state['stage']}\nNext action: {result['next_action']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in (
        "status", "prepare", "draft", "drafted", "review", "revise",
        "revised", "polish", "polished", "summarize", "checkpoint", "checkpointed", "accept",
    ):
        item = sub.add_parser(name)
        item.add_argument("chapter", type=int)
        if name == "status":
            item.add_argument("--json", action="store_true")
        if name == "review":
            item.add_argument("--dry-run", action="store_true")
    committed = sub.add_parser("committed")
    committed.add_argument("chapter", type=int)
    committed.add_argument("--commit", required=True)
    args = parser.parse_args()
    if args.chapter < 0:
        parser.error("chapter must be non-negative")
    if args.command == "status":
        command_status(args.chapter, args.json)
        return 0
    if args.command == "review" and getattr(args, "dry_run", False):
        command_review(args.chapter, True)
        return 0
    with hold_run_lock(ROOT, holder="workflow", chapter=args.chapter, stage=args.command):
        if args.command == "prepare":
            command_prepare(args.chapter)
        elif args.command == "drafted":
            command_drafted(args.chapter)
        elif args.command == "draft":
            command_draft(args.chapter)
        elif args.command == "review":
            command_review(args.chapter, args.dry_run)
        elif args.command == "revised":
            command_revised(args.chapter)
        elif args.command == "revise":
            command_revise(args.chapter)
        elif args.command == "polished":
            command_polished(args.chapter)
        elif args.command == "polish":
            command_polish(args.chapter)
        elif args.command == "summarize":
            command_summarize(args.chapter)
        elif args.command == "checkpoint":
            command_checkpoint(args.chapter)
        elif args.command == "checkpointed":
            command_checkpointed(args.chapter)
        elif args.command == "accept":
            command_accept(args.chapter)
        else:
            command_committed(args.chapter, args.commit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
