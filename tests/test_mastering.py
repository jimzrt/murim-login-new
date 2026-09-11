from __future__ import annotations

import importlib.util
from pathlib import Path

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
