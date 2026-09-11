#!/usr/bin/env python3
"""Two-model retrospective mastering overlay for accepted translations.

Pipeline per chapter:
  accepted baseline -> GPT-5.6 Sol full master edit -> paragraph diff
  -> DeepSeek adjudication -> assembled final -> deterministic QA

The script never modifies translations/ unless `promote` is explicitly invoked.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "docs" / "mastering.json"
WORK_ROOT = ROOT / "reviews" / "mastering"
HANGUL = re.compile(r"[가-힣]")
SAFE_THROUGH = re.compile(r"Safe through:\s*Chapter\s*(\d+)", re.I)
SUMMARY_NAME = re.compile(r"^(\d{4})-(\d{4})\.md$")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as f:
        f.write(text)
        tmp = Path(f.name)
    os.replace(tmp, path)


def atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as f:
        json.dump(value, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
        tmp = Path(f.name)
    os.replace(tmp, path)


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise SystemExit(f"missing {CONFIG_PATH.relative_to(ROOT)}")
    cfg = json.loads(read_text(CONFIG_PATH))
    if cfg.get("version") != 1:
        raise SystemExit("docs/mastering.json version must be 1")
    for role in ("master", "adjudicator"):
        if not isinstance(cfg.get("models", {}).get(role), str):
            raise SystemExit(f"docs/mastering.json missing models.{role}")
    return cfg


def parse_chapters(spec: str) -> list[int]:
    out: set[int] = set()
    for raw in spec.split(","):
        part = raw.strip()
        if not part:
            continue
        if "-" in part:
            left, right = part.split("-", 1)
            start, end = int(left), int(right)
            if start <= 0 or end < start:
                raise ValueError(f"invalid chapter range: {part}")
            out.update(range(start, end + 1))
        else:
            number = int(part)
            if number <= 0:
                raise ValueError("chapter numbers must be positive")
            out.add(number)
    if not out:
        raise ValueError("no chapters selected")
    return sorted(out)


def chapter_paths(number: int) -> dict[str, Path]:
    work = WORK_ROOT / f"{number:04d}"
    return {
        "work": work,
        "state": work / "state.json",
        "source": work / "source.txt",
        "baseline": work / "baseline.md",
        "master_packet": work / "master-packet.md",
        "sol": work / "sol.md",
        "sol_qa": work / "sol-qa.json",
        "diff_json": work / "diff.json",
        "diff_md": work / "diff.md",
        "adjudicator_packet": work / "adjudicator-packet.md",
        "adjudication": work / "adjudication.json",
        "final": work / "final.md",
        "qa": work / "qa.json",
        "metrics": work / "metrics.json",
        "logs": work / "omp",
        "translation": ROOT / "translations" / f"{number:04d}.md",
    }


def current_source(number: int) -> str:
    try:
        from tools.context import chapter_text
    except ModuleNotFoundError:
        from context import chapter_text
    return chapter_text(number)


def exact_glossary(source: str) -> list[dict]:
    try:
        from tools.context import exact_glossary_entries
    except ModuleNotFoundError:
        from context import exact_glossary_entries
    return exact_glossary_entries(source)


def glossary_text(entries: list[dict]) -> str:
    return "\n".join(item.get("row", "") for item in entries if item.get("row")) or "(No exact glossary rows matched.)"


def _preferred_english():
    try:
        from tools.names import preferred_english_present, preferred_english_terms
    except ModuleNotFoundError:
        from names import preferred_english_present, preferred_english_terms
    return preferred_english_present, preferred_english_terms


def normalize_chapter(text: str) -> str:
    """Normalize outer/model whitespace while preserving Markdown blocks."""
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].strip().startswith("```") and lines[-1].strip() == "```":
            text = "\n".join(lines[1:-1]).strip()
    # Normalize blank-line whitespace and excessive blank lines. Keep line structure inside blocks.
    text = re.sub(r"\n[ \t]+\n", "\n\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip() + "\n"


def validate_chapter(text: str, number: int, label: str) -> None:
    first = next((line.strip() for line in text.splitlines() if line.strip()), "")
    if first != f"# Chapter {number}":
        raise ValueError(f"{label}: first nonblank line must be '# Chapter {number}'")
    if HANGUL.search(text):
        raise ValueError(f"{label}: output contains Hangul")


def estimated_tokens(text: str) -> int:
    return (len(text.encode("utf-8")) + 3) // 4


def enforce_budget(text: str, label: str) -> None:
    limit = int(load_config().get("packet_token_limit", 90000))
    estimate = estimated_tokens(text)
    if estimate > limit:
        raise ValueError(f"{label} packet estimate {estimate} exceeds limit {limit}")


def tail_words(text: str, limit: int) -> str:
    words = text.split()
    if len(words) <= limit:
        return text.strip()
    return "…\n" + " ".join(words[-limit:])


def latest_prior_summary(number: int) -> tuple[Path | None, str]:
    candidates: list[tuple[int, Path]] = []
    summary_dir = ROOT / "summaries"
    if summary_dir.is_dir():
        for path in summary_dir.glob("*.md"):
            m = SUMMARY_NAME.match(path.name)
            if m and int(m.group(2)) < number:
                candidates.append((int(m.group(2)), path))
    if not candidates:
        return None, "(No prior chapter summary available.)"
    path = max(candidates)[1]
    return path, read_text(path).strip()


def safe_profiles(source: str, number: int) -> list[tuple[Path, str]]:
    cfg = load_config()
    if not cfg.get("include_safe_profiles", True):
        return []
    try:
        from tools.names import profile_koreans
    except ModuleNotFoundError:
        from names import profile_koreans
    result: list[tuple[Path, str]] = []
    for path in sorted((ROOT / "characters").glob("*.md")):
        body = read_text(path)
        safe = SAFE_THROUGH.search(body)
        # Retrospective safety: a profile describing events through chapter N is
        # safe only for chapters strictly after N.
        if not safe or int(safe.group(1)) >= number:
            continue
        try:
            names = profile_koreans(body)
        except Exception:
            continue
        if any(name and name in source for name in names):
            result.append((path, body.strip()))
    return result


def continuity_bundle(number: int) -> str:
    cfg = load_config()
    count = max(0, int(cfg.get("continuity_previous_chapters", 2)))
    word_limit = max(0, int(cfg.get("continuity_tail_words", 900)))
    summary_path, summary = latest_prior_summary(number)
    parts = ["### Latest prior summary", summary]
    prior_parts: list[str] = []
    for prev in range(max(1, number - count), number):
        path = ROOT / "translations" / f"{prev:04d}.md"
        label = "accepted"
        if cfg.get("continuity_prefer_verified_mastered", True):
            mp = chapter_paths(prev)
            if mp["final"].exists() and mp["state"].exists():
                try:
                    prior_state = json.loads(read_text(mp["state"]))
                except json.JSONDecodeError:
                    prior_state = {}
                if prior_state.get("stage") in {"VERIFIED", "PROMOTED"} and prior_state.get("qa_passed"):
                    path = mp["final"]
                    label = "verified mastered"
        if path.exists():
            prior_parts.append(f"#### Chapter {prev} tail ({label})\n\n{tail_words(read_text(path), word_limit)}")
    parts.extend(["### Prior accepted reading-copy tails", "\n\n".join(prior_parts) or "(None.)"])
    return "\n\n".join(parts)


def profiles_bundle(source: str, number: int) -> str:
    profiles = safe_profiles(source, number)
    if not profiles:
        return "(No chapter-safe profiles available. This is expected for early retrospective chapters.)"
    return "\n\n".join(f"### {p.name}\n\n{body}" for p, body in profiles)


def snapshot(number: int) -> tuple[str, str, list[dict], dict[str, Path]]:
    p = chapter_paths(number)
    if not p["translation"].exists():
        raise FileNotFoundError(f"missing accepted translation: {p['translation'].relative_to(ROOT)}")
    source = current_source(number)
    baseline = normalize_chapter(read_text(p["translation"]))
    validate_chapter(baseline, number, "baseline")
    glossary = exact_glossary(source)
    return source, baseline, glossary, p


def create_or_verify_state(number: int) -> tuple[dict, dict[str, Path]]:
    source, baseline, _, p = snapshot(number)
    source_hash = sha256_text(source)
    baseline_hash = sha256_text(baseline)
    if p["state"].exists():
        state = json.loads(read_text(p["state"]))
        if state.get("source_sha256") != source_hash:
            raise ValueError(f"chapter {number}: Korean source changed since mastering began")
        if state.get("baseline_sha256") != baseline_hash:
            raise ValueError(f"chapter {number}: accepted translation changed since mastering began")
        if not p["source"].exists() or not p["baseline"].exists():
            raise ValueError(f"chapter {number}: mastering snapshots are missing")
        return state, p
    p["work"].mkdir(parents=True, exist_ok=True)
    atomic_text(p["source"], source.rstrip() + "\n")
    atomic_text(p["baseline"], baseline)
    state = {
        "version": 1,
        "chapter": number,
        "stage": "SNAPSHOTTED",
        "source_sha256": source_hash,
        "baseline_sha256": baseline_hash,
    }
    atomic_json(p["state"], state)
    return state, p


def update_state(p: dict[str, Path], state: dict, stage: str, **extra: object) -> None:
    state = dict(state)
    state["stage"] = stage
    state.update(extra)
    atomic_json(p["state"], state)


def master_packet(number: int, source: str, baseline: str, glossary: list[dict]) -> str:
    editorial = read_text(ROOT / "MASTERING_EDITORIAL.md").strip()
    rules = read_text(ROOT / "RULES.md").strip()
    polish = read_text(ROOT / "POLISH.md").strip()
    return f"""# Master Edit Task — Chapter {number}

{editorial}

## Binding project rules

{rules}

## Project polish guidance

{polish}

## Exact glossary matches for this Korean chapter

{glossary_text(glossary)}

## Chapter-safe character profiles

{profiles_bundle(source, number)}

## Chapter-safe bounded continuity

{continuity_bundle(number)}

## Korean source

```text
{source.rstrip()}
```

## Current accepted English baseline

```markdown
{baseline.rstrip()}
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter {number}`.
"""


def run_omp(packet_path: Path, model: str, timeout: int, log_path: Path) -> tuple[str, dict]:
    try:
        from tools.omp_json import OmpJsonError, run_json_command
    except ModuleNotFoundError:
        from omp_json import OmpJsonError, run_json_command
    cfg = load_config()
    command = [
        "omp", "--mode", "json", "--no-session", "--no-tools", "--no-rules", "--no-extensions",
    ]
    omp_config = cfg.get("omp_config")
    if omp_config:
        path = ROOT / str(omp_config)
        if path.exists():
            command += ["--config", str(path)]
    command += ["--model", model, "--max-time", str(max(60, timeout - 60)), f"@{packet_path}"]
    try:
        output, metrics = run_json_command(
            command, cwd=ROOT, requested_model=model, timeout=timeout, log_path=log_path,
        )
    except OmpJsonError as exc:
        raise RuntimeError(str(exc)) from None
    metrics["packet_bytes"] = packet_path.stat().st_size
    metrics["packet_token_estimate"] = estimated_tokens(read_text(packet_path))
    return output, metrics


def load_metrics(p: dict[str, Path]) -> dict:
    if p["metrics"].exists():
        return json.loads(read_text(p["metrics"]))
    return {"version": 1, "chapter": int(p["work"].name), "stages": {}}


def save_metric(p: dict[str, Path], stage: str, metrics: dict) -> None:
    data = load_metrics(p)
    data.setdefault("stages", {})[stage] = metrics
    atomic_json(p["metrics"], data)


def run_qa(number: int, source: str, translation: str, glossary: list[dict]) -> dict:
    try:
        from tools.qa import run_qa as project_qa
    except ModuleNotFoundError:
        from qa import run_qa as project_qa
    pairs = [(item.get("korean", ""), item.get("english", "")) for item in glossary]
    return project_qa(number, source, translation, pairs)


def invalidate_downstream(p: dict[str, Path], from_stage: str) -> None:
    if from_stage == "master":
        keys = ("diff_json", "diff_md", "adjudicator_packet", "adjudication", "final", "qa")
        metric_stages = {"adjudicator"}
    elif from_stage == "adjudicator":
        keys = ("final", "qa")
        metric_stages = set()
    else:
        return
    for key in keys:
        try:
            p[key].unlink()
        except FileNotFoundError:
            pass
    if p["metrics"].exists() and metric_stages:
        data = load_metrics(p)
        for name in metric_stages:
            data.get("stages", {}).pop(name, None)
        atomic_json(p["metrics"], data)


def command_master(number: int, force: bool = False) -> None:
    state, p = create_or_verify_state(number)
    if p["sol"].exists() and not force:
        print(f"{number:04d}: master already exists; skipping")
        return
    if force:
        invalidate_downstream(p, "master")
    source = read_text(p["source"])
    baseline = normalize_chapter(read_text(p["baseline"]))
    glossary = exact_glossary(source)
    packet = master_packet(number, source, baseline, glossary)
    enforce_budget(packet, "master")
    atomic_text(p["master_packet"], packet)
    cfg = load_config()
    model = cfg["models"]["master"]
    output, metrics = run_omp(
        p["master_packet"], model, int(cfg["timeouts"]["master"]), p["logs"] / "master.jsonl"
    )
    mastered = normalize_chapter(output)
    validate_chapter(mastered, number, "master")
    atomic_text(p["sol"], mastered)
    qa = run_qa(number, source, mastered, glossary)
    atomic_json(p["sol_qa"], qa)
    save_metric(p, "master", metrics)
    update_state(p, state, "MASTERED", sol_sha256=sha256_text(mastered))
    print(f"{number:04d}: master edit complete")


def blocks(text: str) -> list[str]:
    text = normalize_chapter(text).strip()
    return [part.strip("\n") for part in re.split(r"\n\s*\n", text) if part.strip()]


def paragraph_line_spans(text: str) -> list[tuple[int, int]]:
    """1-indexed inclusive line spans for blank-line-separated paragraphs."""
    lines = text.rstrip("\n").splitlines()
    spans: list[tuple[int, int]] = []
    start: int | None = None
    last_nonempty: int | None = None
    for idx, line in enumerate(lines, start=1):
        if line.strip():
            if start is None:
                start = idx
            last_nonempty = idx
        elif start is not None:
            spans.append((start, last_nonempty or start))
            start = None
            last_nonempty = None
    if start is not None:
        spans.append((start, last_nonempty or start))
    return spans


def format_paragraph_ref(i1: int, i2: int) -> str:
    """Format a 0-based half-open baseline block range as P# labels."""
    if i1 >= i2:
        return "before P1" if i1 <= 0 else f"after P{i1}"
    start, end = i1 + 1, i2
    return f"P{start}" if start == end else f"P{start}-P{end}"


def format_line_range(start: int, end: int) -> str:
    return str(start) if start == end else f"{start}-{end}"


def map_korean_lines(i1: int, i2: int, spans: list[tuple[int, int]]) -> str:
    """Map a baseline block range onto Korean source line numbers by paragraph order."""
    if not spans:
        return ""
    n_src = len(spans)
    if i1 >= i2:
        idx = min(n_src - 1, max(i1 - 1, 0))
        return format_line_range(*spans[idx])
    start_idx = min(i1, n_src - 1)
    end_idx = min(max(i2 - 1, start_idx), n_src - 1)
    return format_line_range(spans[start_idx][0], spans[end_idx][1])


def format_numbered_source(source: str) -> str:
    lines = source.rstrip("\n").splitlines()
    width = max(1, len(str(len(lines) or 1)))
    return "\n".join(f"{i:>{width}}|{line}" for i, line in enumerate(lines, start=1))


def format_numbered_baseline(baseline: str) -> str:
    return "\n\n".join(f"[P{i}]\n{para}" for i, para in enumerate(blocks(baseline), start=1))


def _similarity(left: str, right: str) -> float:
    left = re.sub(r"\s+", " ", left).strip()
    right = re.sub(r"\s+", " ", right).strip()
    if left == right:
        return 1.0
    return difflib.SequenceMatcher(None, left, right, autojunk=False).ratio()


def align_blocks(base_blocks: list[str], sol_blocks: list[str]) -> list[tuple[str, int, int, int, int]]:
    """Fuzzy monotonic paragraph alignment.

    Exact SequenceMatcher is a poor fit for literary edits because changing every
    paragraph can turn an entire chapter into one replace hunk. This dynamic
    alignment pairs similar paragraphs by order even when their wording changed.
    """
    n, m = len(base_blocks), len(sol_blocks)
    gap = -0.35
    dp = [[float("-inf")] * (m + 1) for _ in range(n + 1)]
    back: list[list[str | None]] = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0.0
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + gap
        back[i][0] = "delete"
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + gap
        back[0][j] = "insert"
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sim = _similarity(base_blocks[i - 1], sol_blocks[j - 1])
            pair_score = dp[i - 1][j - 1] + (2.2 * sim - 0.9)
            delete_score = dp[i - 1][j] + gap
            insert_score = dp[i][j - 1] + gap
            best = max(pair_score, delete_score, insert_score)
            dp[i][j] = best
            # Prefer pairing on ties; preserving monotonic paragraph identity is
            # usually safer for edited prose than manufacturing gaps.
            if pair_score >= delete_score and pair_score >= insert_score:
                back[i][j] = "pair"
            elif delete_score >= insert_score:
                back[i][j] = "delete"
            else:
                back[i][j] = "insert"
    atomic: list[tuple[str, int, int, int, int]] = []
    i, j = n, m
    while i or j:
        step = back[i][j]
        if step == "pair":
            tag = "equal" if base_blocks[i - 1] == sol_blocks[j - 1] else "replace"
            atomic.append((tag, i - 1, i, j - 1, j))
            i -= 1
            j -= 1
        elif step == "delete":
            atomic.append(("delete", i - 1, i, j, j))
            i -= 1
        elif step == "insert":
            atomic.append(("insert", i, i, j - 1, j))
            j -= 1
        else:
            raise ValueError("internal diff alignment failure")
    atomic.reverse()
    return atomic


def build_diff(baseline: str, sol: str, glossary: list[dict], source: str = "") -> dict:
    present, terms_of = _preferred_english()
    base_blocks = blocks(baseline)
    sol_blocks = blocks(sol)
    opcodes = align_blocks(base_blocks, sol_blocks)
    korean_spans = paragraph_line_spans(source)
    hunks: list[dict] = []
    hunk_num = 0
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == "equal":
            continue
        hunk_num += 1
        base_text = "\n\n".join(base_blocks[i1:i2])
        sol_text = "\n\n".join(sol_blocks[j1:j2])
        alerts: list[dict] = []
        for item in glossary:
            english = str(item.get("english", ""))
            if present(base_text, english) and not present(sol_text, english):
                alerts.append({
                    "korean": item.get("korean", ""),
                    "preferred": " / ".join(terms_of(english)),
                    "message": "preferred glossary term appears in BASE but not SOL for this hunk",
                })
        hunks.append({
            "hunk_id": f"H{hunk_num:03d}",
            "tag": tag,
            "baseline_range": [i1, i2],
            "sol_range": [j1, j2],
            "baseline_paragraphs": format_paragraph_ref(i1, i2),
            "korean_lines": map_korean_lines(i1, i2, korean_spans),
            "baseline": base_text,
            "sol": sol_text,
            "terminology_alerts": alerts,
        })
    global_alerts: list[dict] = []
    for item in glossary:
        english = str(item.get("english", ""))
        if present(baseline, english) and not present(sol, english):
            global_alerts.append({"korean": item.get("korean", ""), "preferred": " / ".join(terms_of(english))})
    return {
        "version": 1,
        "baseline_sha256": sha256_text(normalize_chapter(baseline)),
        "sol_sha256": sha256_text(normalize_chapter(sol)),
        "baseline_blocks": len(base_blocks),
        "sol_blocks": len(sol_blocks),
        "hunk_count": len(hunks),
        "global_terminology_alerts": global_alerts,
        "hunks": hunks,
    }


def diff_markdown(diff: dict) -> str:
    lines = [f"# Mastering Diff — {diff['hunk_count']} changed hunks", ""]
    if diff.get("global_terminology_alerts"):
        lines += ["## Global terminology alerts", ""]
        for alert in diff["global_terminology_alerts"]:
            lines.append(f"- `{alert['korean']}` → `{alert['preferred']}` is present in BASE but absent from SOL.")
        lines.append("")
    for h in diff["hunks"]:
        lines += [f"## {h['hunk_id']} ({h['tag']})", ""]
        lines.append(f"Baseline paragraphs: {h.get('baseline_paragraphs', '')}")
        if h.get("korean_lines"):
            lines.append(f"Korean lines: {h['korean_lines']}")
        lines.append("")
        for alert in h.get("terminology_alerts", []):
            lines.append(f"**Terminology alert:** `{alert['korean']}` → `{alert['preferred']}`")
            lines.append("")
        lines += ["BASE:", "", h["baseline"] or "*(empty)*", "", "SOL:", "", h["sol"] or "*(empty)*", ""]
    return "\n".join(lines).rstrip() + "\n"


def format_hunk_for_packet(h: dict) -> str:
    parts = [
        f"### {h['hunk_id']} — {h['tag']}",
        f"Baseline paragraphs: {h.get('baseline_paragraphs', '')}",
    ]
    if h.get("korean_lines"):
        parts.append(f"Korean lines: {h['korean_lines']}")
    for alert in h.get("terminology_alerts", []):
        parts.append(
            f"Terminology alert: `{alert['korean']}` → `{alert['preferred']}` present in BASE, absent from SOL."
        )
    parts += [
        "",
        "BASE:",
        h["baseline"] or "(empty)",
        "",
        "SOL:",
        h["sol"] or "(empty)",
        "",
    ]
    return "\n".join(parts)


def adjudicator_packet(number: int, source: str, baseline: str, sol: str, glossary: list[dict], diff: dict) -> str:
    brief = read_text(ROOT / "MASTERING_ADJUDICATOR.md").strip()
    rules = read_text(ROOT / "RULES.md").strip()
    hunk_parts = [format_hunk_for_packet(h) for h in diff["hunks"]]
    global_alerts = diff.get("global_terminology_alerts", [])
    global_text = "\n".join(f"- `{a['korean']}` → `{a['preferred']}`" for a in global_alerts) or "(none)"
    return f"""# Adjudication Task — Chapter {number}

## Korean source

```text
{format_numbered_source(source)}
```

## Complete BASELINE English

```markdown
{format_numbered_baseline(baseline)}
```

## Complete SOL English

```markdown
{sol.rstrip()}
```

## Exact glossary matches for this Korean chapter

{glossary_text(glossary)}

## Adjudicator rules

{brief}

## Critical binding translation rules

{rules}

## Global protected-term risks introduced by SOL

{global_text}

## Numbered diff hunks

Each hunk is the changed span only. Neighboring unchanged English is in the numbered baseline and complete SOL above; use the P# labels and Korean line numbers to look up surrounding context.

{chr(10).join(hunk_parts)}

Return exactly the JSON object required by the adjudicator brief, with chapter set to {number} and exactly one decision for each of the {diff['hunk_count']} hunks.
"""


def _escape_interior_json_quotes(text: str) -> str:
    """Escape unescaped double quotes inside JSON string values."""
    out: list[str] = []
    in_string = False
    escape = False
    closers = set(',}]:')
    for i, ch in enumerate(text):
        if not in_string:
            if ch == '"':
                in_string = True
            out.append(ch)
            continue
        if escape:
            out.append(ch)
            escape = False
            continue
        if ch == "\\":
            out.append(ch)
            escape = True
            continue
        if ch == '"':
            j = i + 1
            while j < len(text) and text[j] in " \t\n\r":
                j += 1
            if j >= len(text) or text[j] in closers:
                in_string = False
                out.append(ch)
            else:
                out.append('\\"')
            continue
        out.append(ch)
    return "".join(out)


def parse_json_object(raw: str) -> dict:
    text = raw.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if len(lines) >= 2 and lines[-1].strip() == "```":
            text = "\n".join(lines[1:-1]).strip()
    candidates = [text]
    start, end = text.find("{"), text.rfind("}")
    if start >= 0 and end > start:
        sliced = text[start:end + 1]
        if sliced != text:
            candidates.append(sliced)
        candidates.append(_escape_interior_json_quotes(sliced))
    last_exc: json.JSONDecodeError | None = None
    for candidate in candidates:
        try:
            value = json.loads(candidate)
            break
        except json.JSONDecodeError as exc:
            last_exc = exc
    else:
        raise ValueError(f"adjudicator output has invalid JSON: {last_exc}") from None
    if not isinstance(value, dict):
        raise ValueError("adjudicator output must be one JSON object")
    return value


def validate_adjudication(value: dict, number: int, diff: dict) -> dict:
    if value.get("chapter") != number:
        raise ValueError(f"adjudicator chapter must be {number}")
    decisions = value.get("decisions")
    if not isinstance(decisions, list):
        raise ValueError("adjudicator decisions must be an array")
    expected = [h["hunk_id"] for h in diff["hunks"]]
    found: list[str] = []
    normalized: list[dict] = []
    for item in decisions:
        if not isinstance(item, dict):
            raise ValueError("each adjudicator decision must be an object")
        hid = item.get("hunk_id")
        decision = str(item.get("decision", "")).upper()
        reason = item.get("reason")
        if not isinstance(hid, str) or not hid:
            raise ValueError("decision missing hunk_id")
        if decision not in {"SOL", "BASE", "REPAIR"}:
            raise ValueError(f"{hid}: decision must be SOL, BASE, or REPAIR")
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f"{hid}: nonempty reason is required")
        out = {"hunk_id": hid, "decision": decision, "reason": reason.strip()}
        if decision == "REPAIR":
            replacement = item.get("replacement")
            if not isinstance(replacement, str) or not replacement.strip():
                raise ValueError(f"{hid}: REPAIR requires a nonempty replacement")
            replacement = replacement.strip()
            if HANGUL.search(replacement):
                raise ValueError(f"{hid}: REPAIR replacement contains Hangul")
            out["replacement"] = replacement
        found.append(hid)
        normalized.append(out)
    if found != expected:
        raise ValueError(f"adjudicator hunk IDs/order mismatch; expected {expected}, got {found}")
    return {"version": 1, "chapter": number, "decisions": normalized}


def command_adjudicate(number: int, force: bool = False) -> None:
    state, p = create_or_verify_state(number)
    if not p["sol"].exists():
        raise ValueError(f"chapter {number}: run master first")
    if p["adjudication"].exists() and not force:
        print(f"{number:04d}: adjudication already exists; skipping")
        return
    if force:
        invalidate_downstream(p, "adjudicator")
    source = read_text(p["source"])
    baseline = normalize_chapter(read_text(p["baseline"]))
    sol = normalize_chapter(read_text(p["sol"]))
    glossary = exact_glossary(source)
    diff = build_diff(baseline, sol, glossary, source)
    atomic_json(p["diff_json"], diff)
    atomic_text(p["diff_md"], diff_markdown(diff))
    if diff["hunk_count"] == 0:
        adjudication = {"version": 1, "chapter": number, "decisions": []}
        atomic_json(p["adjudication"], adjudication)
        update_state(p, state, "ADJUDICATED", hunk_count=0)
        print(f"{number:04d}: no changes; adjudication skipped")
        return
    packet = adjudicator_packet(number, source, baseline, sol, glossary, diff)
    enforce_budget(packet, "adjudicator")
    atomic_text(p["adjudicator_packet"], packet)
    cfg = load_config()
    model = cfg["models"]["adjudicator"]
    output, metrics = run_omp(
        p["adjudicator_packet"], model, int(cfg["timeouts"]["adjudicator"]), p["logs"] / "adjudicator.jsonl"
    )
    raw_path = p["logs"] / "adjudicator-output.txt"
    atomic_text(raw_path, output)
    value = validate_adjudication(parse_json_object(output), number, diff)
    atomic_json(p["adjudication"], value)
    save_metric(p, "adjudicator", metrics)
    counts = {k: sum(1 for d in value["decisions"] if d["decision"] == k) for k in ("SOL", "BASE", "REPAIR")}
    update_state(p, state, "ADJUDICATED", hunk_count=diff["hunk_count"], decisions=counts)
    print(f"{number:04d}: adjudicated {diff['hunk_count']} hunks — {counts}")


def assemble_from_decisions(baseline: str, sol: str, adjudication: dict) -> str:
    base_blocks = blocks(baseline)
    sol_blocks = blocks(sol)
    opcodes = align_blocks(base_blocks, sol_blocks)
    decision_map = {item["hunk_id"]: item for item in adjudication["decisions"]}
    output: list[str] = []
    hunk_num = 0
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == "equal":
            output.extend(base_blocks[i1:i2])
            continue
        hunk_num += 1
        hid = f"H{hunk_num:03d}"
        item = decision_map.get(hid)
        if item is None:
            raise ValueError(f"missing decision for {hid}")
        decision = item["decision"]
        if decision == "BASE":
            output.extend(base_blocks[i1:i2])
        elif decision == "SOL":
            output.extend(sol_blocks[j1:j2])
        elif decision == "REPAIR":
            output.extend(blocks(item["replacement"]))
        else:
            raise ValueError(f"unknown decision for {hid}: {decision}")
    return normalize_chapter("\n\n".join(output))


def command_assemble(number: int) -> None:
    state, p = create_or_verify_state(number)
    if not p["sol"].exists() or not p["adjudication"].exists():
        raise ValueError(f"chapter {number}: master and adjudication are required")
    baseline = normalize_chapter(read_text(p["baseline"]))
    sol = normalize_chapter(read_text(p["sol"]))
    adjudication = json.loads(read_text(p["adjudication"]))
    final = assemble_from_decisions(baseline, sol, adjudication)
    validate_chapter(final, number, "final")
    atomic_text(p["final"], final)
    update_state(p, state, "ASSEMBLED", final_sha256=sha256_text(final))
    print(f"{number:04d}: final chapter assembled")


def command_qa(number: int) -> None:
    state, p = create_or_verify_state(number)
    if not p["final"].exists():
        raise ValueError(f"chapter {number}: assemble final first")
    source = read_text(p["source"])
    final = normalize_chapter(read_text(p["final"]))
    glossary = exact_glossary(source)
    qa = run_qa(number, source, final, glossary)
    atomic_json(p["qa"], qa)
    update_state(p, state, "VERIFIED" if qa["passed"] else "QA_FAILED", qa_passed=bool(qa["passed"]))
    status = "PASS" if qa["passed"] else "FAIL"
    print(f"{number:04d}: QA {status} — {len(qa['errors'])} errors, {len(qa['warnings'])} warnings")


def command_run(number: int) -> None:
    command_master(number)
    command_adjudicate(number)
    command_assemble(number)
    command_qa(number)


def state_for(number: int) -> dict:
    p = chapter_paths(number)
    if not p["state"].exists():
        return {"chapter": number, "stage": "NOT_STARTED"}
    return json.loads(read_text(p["state"]))


def command_status(chapters: Iterable[int]) -> None:
    print("chapter\tstage\thunks\tSOL\tBASE\tREPAIR\tqa")
    for number in chapters:
        state = state_for(number)
        decisions = state.get("decisions", {})
        print("\t".join([
            f"{number:04d}", str(state.get("stage", "?")), str(state.get("hunk_count", "")),
            str(decisions.get("SOL", "")), str(decisions.get("BASE", "")), str(decisions.get("REPAIR", "")),
            str(state.get("qa_passed", "")),
        ]))


def metric_cost(stage: dict) -> float:
    value = stage.get("cost_usd")
    if isinstance(value, (int, float)):
        return float(value)
    total = 0.0
    for model in stage.get("models", {}).values() if isinstance(stage.get("models"), dict) else []:
        if isinstance(model, dict) and isinstance(model.get("cost_usd"), (int, float)):
            total += float(model["cost_usd"])
    return total


def command_report(chapters: Iterable[int]) -> None:
    rows: list[dict] = []
    for number in chapters:
        p = chapter_paths(number)
        metrics = load_metrics(p)
        state = state_for(number)
        master = metrics.get("stages", {}).get("master", {})
        judge = metrics.get("stages", {}).get("adjudicator", {})
        row = {
            "chapter": number,
            "stage": state.get("stage"),
            "hunks": state.get("hunk_count", 0),
            "decisions": state.get("decisions", {}),
            "master_cost_usd": metric_cost(master),
            "adjudicator_cost_usd": metric_cost(judge),
        }
        row["total_cost_usd"] = row["master_cost_usd"] + row["adjudicator_cost_usd"]
        rows.append(row)
    totals = {
        "chapters": len(rows),
        "master_cost_usd": sum(r["master_cost_usd"] for r in rows),
        "adjudicator_cost_usd": sum(r["adjudicator_cost_usd"] for r in rows),
        "total_cost_usd": sum(r["total_cost_usd"] for r in rows),
        "hunks": sum(int(r["hunks"] or 0) for r in rows),
        "SOL": sum(int(r["decisions"].get("SOL", 0)) for r in rows),
        "BASE": sum(int(r["decisions"].get("BASE", 0)) for r in rows),
        "REPAIR": sum(int(r["decisions"].get("REPAIR", 0)) for r in rows),
    }
    payload = {"version": 1, "rows": rows, "totals": totals}
    if rows:
        report_path = WORK_ROOT / f"report-{rows[0]['chapter']:04d}-{rows[-1]['chapter']:04d}.json"
        atomic_json(report_path, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def command_promote(number: int, confirm: str) -> None:
    if confirm != "REPLACE_TRANSLATIONS":
        raise ValueError("promotion requires --confirm REPLACE_TRANSLATIONS")
    state, p = create_or_verify_state(number)
    if state.get("stage") != "VERIFIED" or not state.get("qa_passed"):
        raise ValueError(f"chapter {number}: only VERIFIED chapters can be promoted")
    final = normalize_chapter(read_text(p["final"]))
    validate_chapter(final, number, "final")
    # create_or_verify_state already proved translations/<chapter>.md still matches snapshot.
    atomic_text(p["translation"], final)
    update_state(p, state, "PROMOTED", promoted_sha256=sha256_text(final))
    print(f"{number:04d}: promoted final -> translations/{number:04d}.md")


def command_doctor() -> None:
    required = [
        CONFIG_PATH, ROOT / "MASTERING_EDITORIAL.md", ROOT / "MASTERING_ADJUDICATOR.md",
        ROOT / "RULES.md", ROOT / "POLISH.md", ROOT / "compendium.md",
        ROOT / "tools" / "omp_json.py", ROOT / "tools" / "qa.py", ROOT / "tools" / "context.py",
    ]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    if missing:
        raise ValueError("missing required project files: " + ", ".join(missing))
    if shutil.which("omp") is None:
        raise ValueError("omp executable not found on PATH")
    cfg = load_config()
    print("Mastering overlay OK")
    print(f"master:       {cfg['models']['master']}")
    print(f"adjudicator:  {cfg['models']['adjudicator']}")
    omp_config = cfg.get("omp_config")
    print(f"OMP config:   {omp_config or '(none)'}")
    print("No model call was made.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("doctor", help="validate installation without making model calls")
    for name in ("run", "master", "adjudicate", "assemble", "qa", "status", "report"):
        p = sub.add_parser(name)
        p.add_argument("chapters", help="chapter spec, e.g. 1, 1-10, or 1,5,10")
        if name in {"master", "adjudicate"}:
            p.add_argument("--force", action="store_true", help="rerun this paid model stage")
    p = sub.add_parser("promote", help="replace accepted translations with VERIFIED mastered copies")
    p.add_argument("chapters")
    p.add_argument("--confirm", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "doctor":
            command_doctor()
            return 0
        chapters = parse_chapters(args.chapters)
        if args.command == "status":
            command_status(chapters)
        elif args.command == "report":
            command_report(chapters)
        else:
            for number in chapters:
                if args.command == "run":
                    command_run(number)
                elif args.command == "master":
                    command_master(number, args.force)
                elif args.command == "adjudicate":
                    command_adjudicate(number, args.force)
                elif args.command == "assemble":
                    command_assemble(number)
                elif args.command == "qa":
                    command_qa(number)
                elif args.command == "promote":
                    command_promote(number, args.confirm)
        return 0
    except (ValueError, FileNotFoundError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
