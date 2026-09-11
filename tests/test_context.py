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

    def test_review_packet_does_not_repeat_draft_only_context(self):
        with patch.object(context, "load_active_context", return_value=self.active()):
            draft_packet = context.build_draft_packet(5)
            review_packet = context.build_review_packet(5, "# Chapter 5\n\nDraft.\n", {"warnings": []})
        self.assertIn("translations/0004.md", draft_packet)
        self.assertIn("Latest completed summary", draft_packet)
        self.assertNotIn("translations/0004.md", review_packet)
        self.assertNotIn("Latest completed summary", review_packet)
        self.assertIn('"replacement": "finished exact replacement English"', review_packet)
        self.assertIn("must quote one exact, uniquely occurring draft span", review_packet)

    def test_update_packet_is_bounded_to_current_durable_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "characters").mkdir()
            (root / "docs" / "workflow.json").write_text(json.dumps({
                "continuity_source_limit": 2,
                "profile_max_bytes": 4096,
                "profile_total_max_bytes": 12288,
            }), encoding="utf-8")
            (root / "docs" / "CONTEXT.json").write_text(
                json.dumps(self.active()), encoding="utf-8"
            )
            (root / "docs" / "NAMES.md").write_text(
                "# Names\n\n| Korean | English | Notes |\n|---|---|---|\n", encoding="utf-8")
            source_path = root / "chapter.txt"
            source_path.write_text("주인공", encoding="utf-8")
            profile_path = root / "characters" / "Hero.md"
            profile = "# Hero (주인공)\n\n- **Safe through:** Chapter 4\n- **Voice:** Direct\n"
            profile_path.write_text(profile, encoding="utf-8")
            with (
                patch.object(context, "ROOT", root),
                patch.object(context, "chapter_text", return_value="주인공"),
                patch.object(context, "chapter_source_path", return_value=source_path),
                patch.object(context, "exact_glossary_entries", return_value=[]),
                patch.object(context, "profile_entries", return_value=[(profile_path, profile)]),
            ):
                packet = context.build_update_packet(5, "# Chapter 5\n\nFinal.\n")
        self.assertIn("# Durable State Update — Chapter 5", packet)
        self.assertIn("# Chapter 5\n\nFinal.", packet)
        self.assertIn('"profile_updates"', packet)
        self.assertNotIn("Latest completed summary", packet)
        self.assertNotIn("compendium.md", packet)

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
