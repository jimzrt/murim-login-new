import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import context


class ContextPacketTest(unittest.TestCase):
    def active(self):
        return {
            "version": 1,
            "safe_through": 4,
            "continuity_sources": [4],
            "active_continuity": ["Current hook."],
            "open_questions": ["Open question."],
            "temporary_decisions": ["Temporary decision."],
        }

    def test_phase_packets_do_not_repeat_draft_only_context(self):
        with patch.object(context, "load_active_context", return_value=self.active()):
            draft_packet = context.build_draft_packet(5)
            review_packet = context.build_review_packet(5, "# Chapter 5\n\nDraft.\n", {"warnings": []})
            revision_packet = context.build_revision_packet(5, "# Chapter 5\n\nDraft.\n", {"findings": []})
            polish_packet = context.build_polish_packet(5, "# Chapter 5\n\nRevised.\n")
        self.assertIn("translations/0004.md", draft_packet)
        self.assertIn("Latest completed summary", draft_packet)
        self.assertNotIn("translations/0004.md", review_packet)
        self.assertNotIn("Latest completed summary", review_packet)
        self.assertNotIn("active_continuity", revision_packet)
        self.assertIn("Structured findings", revision_packet)
        self.assertIn("Semantic errors outrank stylistic improvements", review_packet)
        self.assertLess(revision_packet.find("## Korean source"), revision_packet.find("<<<TRANSLATION>>>"))
        self.assertIn("<<<END>>>", revision_packet)
        self.assertIn("After <<<END>>>, stop immediately.", revision_packet)
        self.assertIn("Polish brief", polish_packet)
        self.assertIn("first nonblank line must be exactly", polish_packet)
        self.assertIn("Translate the thought, not the Korean sentence structure", polish_packet)
        self.assertIn("Revised reading copy", polish_packet)
        self.assertNotIn("Structured findings", polish_packet)
        self.assertNotIn("Latest completed summary", polish_packet)
        self.assertNotIn("<<<TRANSLATION>>>", polish_packet)

    def test_compact_profiles_keep_voice_and_drop_archived_continuity(self):
        body = """# Jin Taekyung (진태경)

- **Safe through:** Chapter 63
- **Aliases:** Sleeping Dragon
- **Role:** Protagonist
- **Personality:** Dryly observant
- **Voice:** Casual and sarcastic
- **Relationships:** Jin family
- **Continuity:** Resolved plot history
- **Chapter 63 continuity:** More resolved plot history
- **Sources:** Chapters 1–63
"""
        compact = context.compact_profile(body)
        self.assertIn("Casual and sarcastic", compact)
        self.assertIn("Jin family", compact)
        self.assertNotIn("resolved plot history", compact.casefold())
        self.assertNotIn("Sources", compact)

    def test_profile_packet_budget_rejects_oversized_identity_data(self):
        body = "# Character (인물)\\n\\n- **Voice:** " + "x" * 20
        limits = {"profile_max_bytes": 16, "profile_total_max_bytes": 32}
        with patch.object(context, "workflow_config", return_value=limits):
            with self.assertRaisesRegex(ValueError, "profile_max_bytes"):
                context.bounded_profiles([(Path("character.md"), body)])

    def test_durable_context_requires_version(self):
        problems = context.durable_context_problems(
            {"safe_through": 18, "continuity_sources": [18]},
            18,
            2,
        )
        self.assertTrue(any("version" in item for item in problems))
        problems = context.durable_context_problems(self.active() | {"safe_through": 5}, 5, 2)
        self.assertEqual(problems, [])

    def test_confirmed_terms_are_retrieved_by_exact_source_match(self):

        entries = context.exact_glossary_entries("큰형 생도 삼전보 대물남 전각 전음")
        mapping = {item["korean"]: item["english"] for item in entries}
        self.assertIn("eldest brother", mapping["큰형"])
        self.assertIn("cadet", mapping["생도"])
        self.assertIn("Three-Turn Footwork", mapping["삼전보"])
        self.assertIn("Well-Endowed Man", mapping["대물남"])
        self.assertIn("pavilion", mapping["전각"])

    def test_names_ledger_aliases_are_retrieved_by_source_korean(self):
        entries = context.exact_glossary_entries("천력부 천관일")
        mapping = {item["korean"]: item["english"] for item in entries}
        self.assertIn("Heavenly Axe", mapping["천력부"])
        self.assertIn("Sky-Piercing Strike", mapping["천관일"])

    def test_summary_packet_uses_beats_not_reading_copies(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "workflow.json").write_text(json.dumps({
                "summary_interval": 5,
                "beat_max_bytes": 4096,
                "context_max_bytes": 16384,
                "continuity_source_limit": 2,
            }), encoding="utf-8")
            (root / "docs" / "CONTEXT.json").write_text(
                '{"safe_through":9,"continuity_sources":[9]}\n', encoding="utf-8"
            )
            (root / "summaries").mkdir()
            (root / "summaries" / "0000-0004.md").write_text("# Chapters 0–4\n\nPrior block.\n", encoding="utf-8")
            beats = root / "summaries" / "beats"
            beats.mkdir()
            for chapter in range(5, 10):
                (beats / f"{chapter:04d}.md").write_text(
                    f"# Chapter {chapter}\n\n## Plot\n\nPlot {chapter}.\n\n## Continuity\n\n- Hook {chapter}.\n\n## Translation Decisions\n\n- Term {chapter}.\n",
                    encoding="utf-8",
                )
            with patch.object(context, "ROOT", root):
                packet = context.build_summary_packet(9)
        self.assertIn("## Chapter beats", packet)
        self.assertIn("Plot 5", packet)
        self.assertIn("Plot 9", packet)
        self.assertIn("Prior block.", packet)
        self.assertNotIn("translations/", packet)
        self.assertNotIn("# Chapter 5\n\nOnce upon", packet)
        summary = context.normalize_block_summary(
            "```markdown\n# Chapters 5-9\n\n## Plot\n\nP.\n\n## Continuity\n\n- C.\n\n## Translation Decisions\n\n- T.\n```",
            5,
            9,
        )
        self.assertTrue(summary.startswith("# Chapters 5–9\n"))


if __name__ == "__main__":
    unittest.main()
