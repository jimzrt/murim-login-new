from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "mastering.py"
spec = importlib.util.spec_from_file_location("mastering", MODULE_PATH)
mastering = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(mastering)


def test_parse_chapters():
    assert mastering.parse_chapters("1-3,5,3") == [1, 2, 3, 5]


def test_parse_json_object_escapes_interior_quotes():
    raw = (
        '{\n'
        '  "chapter": 2,\n'
        '  "decisions": [{\n'
        '    "hunk_id": "H044",\n'
        '    "decision": "SOL",\n'
        '    "reason": "SOL\'s \'"> **Warning**\' heading is correct."\n'
        '  }]\n'
        '}\n'
    )
    value = mastering.parse_json_object(raw)
    assert value["chapter"] == 2
    assert "Warning" in value["decisions"][0]["reason"]


def test_diff_and_assemble_sol_base_repair():
    baseline = "# Chapter 1\n\nAlpha.\n\nBeta.\n\nGamma.\n"
    sol = "# Chapter 1\n\nAlpha improved.\n\nBeta improved.\n\nGamma.\n"
    diff = mastering.build_diff(baseline, sol, [])
    assert diff["hunk_count"] >= 1
    # SequenceMatcher may group adjacent changed paragraphs into one hunk.
    decisions = []
    for h in diff["hunks"]:
        decisions.append({"hunk_id": h["hunk_id"], "decision": "REPAIR", "replacement": "Alpha repaired.\n\nBeta repaired.", "reason": "test"})
    out = mastering.assemble_from_decisions(baseline, sol, {"decisions": decisions})
    assert "Alpha repaired." in out
    assert "Beta repaired." in out
    assert out.startswith("# Chapter 1")


def test_terminology_alerts_treat_slash_terms_as_alternatives():
    glossary = [{"korean": "기세", "english": "**aura** / **momentum**"}]
    switched = mastering.build_diff(
        "# Chapter 1\n\nTheir momentum returned.\n",
        "# Chapter 1\n\nAn aura pressed down.\n",
        glossary,
    )
    assert switched["global_terminology_alerts"] == []
    assert all(not h["terminology_alerts"] for h in switched["hunks"])
    dropped = mastering.build_diff(
        "# Chapter 1\n\nTheir momentum returned.\n",
        "# Chapter 1\n\nThe pressure returned.\n",
        glossary,
    )
    assert dropped["global_terminology_alerts"][0]["preferred"] == "aura / momentum"


def test_expected_live_hash_uses_promoted_copy():
    baseline = mastering.expected_live_translation_hash({"stage": "VERIFIED", "baseline_sha256": "aaa"})
    promoted = mastering.expected_live_translation_hash({"stage": "PROMOTED", "baseline_sha256": "aaa", "promoted_sha256": "bbb"})
    assert baseline == "aaa"
    assert promoted == "bbb"


def test_finish_for_commit_skips_when_already_promoted(monkeypatch):
    calls = []

    def fake_state(_number):
        return {"stage": "PROMOTED", "qa_passed": True}

    monkeypatch.setattr(mastering, "state_for", fake_state)
    monkeypatch.setattr(mastering, "command_run", lambda _number: calls.append("run"))
    monkeypatch.setattr(mastering, "command_promote", lambda *_args: calls.append("promote"))
    mastering.command_finish_for_commit(3)
    assert calls == []


def test_validate_adjudication_requires_exact_hunks():
    diff = {"hunks": [{"hunk_id": "H001"}, {"hunk_id": "H002"}]}
    value = {
        "chapter": 7,
        "decisions": [
            {"hunk_id": "H001", "decision": "SOL", "reason": "better"},
            {"hunk_id": "H002", "decision": "BASE", "reason": "faithful"},
        ],
    }
    normalized = mastering.validate_adjudication(value, 7, diff)
    assert [d["decision"] for d in normalized["decisions"]] == ["SOL", "BASE"]


def test_normalize_strips_single_fence():
    value = "```markdown\n# Chapter 2\n\nText.\n```"
    assert mastering.normalize_chapter(value) == "# Chapter 2\n\nText.\n"


def test_fuzzy_alignment_does_not_collapse_fully_edited_chapter():
    baseline = "# Chapter 1\n\nThe hunter walked home.\n\nHe opened the door.\n\nThe room was empty.\n"
    sol = "# Chapter 1\n\nThe hunter headed home.\n\nHe pushed the door open.\n\nNo one was inside.\n"
    diff = mastering.build_diff(baseline, sol, [])
    # Heading remains an anchor and edited prose is adjudicable in small units.
    assert diff["hunk_count"] == 3
    assert all(len(h["baseline_range"]) == 2 for h in diff["hunks"])


def test_master_packet_owns_full_copy_polish():
    packet = mastering.master_packet(
        1,
        "＃1화\n\n원문.\n",
        "# Chapter 1\n\nBaseline.\n",
        [],
    )
    assert "## Project polish guidance" in packet
    assert "Translate the thought, not the Korean sentence structure" in packet
    assert "## Current accepted English baseline" in packet


def test_adjudicator_packet_is_compact():
    source = "＃1화\n\n“쓰레기네.”\n\n진호가 말했다.\n"
    baseline = "# Chapter 1\n\n“It’s garbage.”\n\nJinho spoke.\n"
    sol = "# Chapter 1\n\n“It’s garbage.”\n\nJinho said it.\n"
    diff = mastering.build_diff(baseline, sol, [], source)
    assert diff["hunk_count"] == 1
    hunk = diff["hunks"][0]
    assert hunk["baseline_paragraphs"] == "P3"
    assert hunk["korean_lines"] == "5"
    assert "context_before_baseline" not in hunk
    packet = mastering.adjudicator_packet(1, source, baseline, sol, [], diff)
    assert "## Complete SOL English" in packet
    assert "BASE context before" not in packet
    assert "SOL context after" not in packet
    assert "Baseline paragraphs: P3" in packet
    assert "Korean lines: 5" in packet
    assert "[P1]" in packet
    assert "1|＃1화" in packet
    assert packet.count("Jinho spoke.") == 2
    assert packet.count("Jinho said it.") == 2
    sections = [
        "## Korean source",
        "## Complete BASELINE English",
        "## Complete SOL English",
        "## Exact glossary matches for this Korean chapter",
        "## Adjudicator rules",
        "## Critical binding translation rules",
        "## Numbered diff hunks",
    ]
    indexes = [packet.index(name) for name in sections]
    assert indexes == sorted(indexes)


def test_expected_live_hash_uses_promoted_copy():
    baseline = mastering.expected_live_translation_hash({"stage": "VERIFIED", "baseline_sha256": "aaa"})
    promoted = mastering.expected_live_translation_hash(
        {"stage": "PROMOTED", "baseline_sha256": "aaa", "promoted_sha256": "bbb"}
    )
    assert baseline == "aaa"
    assert promoted == "bbb"


def test_finish_for_commit_skips_when_already_promoted():
    calls: list[str] = []
    with patch.object(mastering, "state_for", return_value={"stage": "PROMOTED", "qa_passed": True}):
        with patch.object(mastering, "command_run", lambda _number: calls.append("run")):
            with patch.object(mastering, "command_promote", lambda *_args: calls.append("promote")):
                mastering.command_finish_for_commit(3)
    assert calls == []


def test_adjudicator_run_omp_passes_deepseek_overlay():
    work = Path(tempfile.mkdtemp())
    packet = work / "packet.md"
    packet.write_text("x", encoding="utf-8")
    captured: dict[str, list[str]] = {}

    def fake_run(command, **_kwargs):
        captured["command"] = command
        return "# Chapter 1\n", {"exact": True}

    with patch("tools.omp_json.run_json_command", fake_run):
        mastering.run_omp(
            packet,
            "cursor/cursor-grok-4.6:low",
            120,
            work / "log.jsonl",
            extra_configs=[".omp/adjudicator-overlay.yml"],
        )
    configs = [item for i, item in enumerate(captured["command"]) if captured["command"][i - 1] == "--config"]
    assert any(str(item).endswith("review-overlay.yml") for item in configs)
    assert any(str(item).endswith("adjudicator-overlay.yml") for item in configs)
    assert captured["command"][captured["command"].index("--model") + 1] == "cursor/cursor-grok-4.6:low"
