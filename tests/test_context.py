import unittest
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
        self.assertIn("translations/0004.md", draft_packet)
        self.assertIn("Latest completed summary", draft_packet)
        self.assertNotIn("translations/0004.md", review_packet)
        self.assertNotIn("Latest completed summary", review_packet)
        self.assertNotIn("active_continuity", revision_packet)
        self.assertIn("Structured findings", revision_packet)
        self.assertIn("Semantic errors outrank stylistic improvements", review_packet)

    def test_confirmed_terms_are_retrieved_by_exact_source_match(self):
        entries = context.exact_glossary_entries("큰형 생도 삼전보 대물남 전각 전음")
        mapping = {item["korean"]: item["english"] for item in entries}
        self.assertIn("eldest brother", mapping["큰형"])
        self.assertIn("cadet", mapping["생도"])
        self.assertIn("Three-Turn Footwork", mapping["삼전보"])
        self.assertIn("Well-Endowed Man", mapping["대물남"])
        self.assertIn("pavilion", mapping["전각"])


if __name__ == "__main__":
    unittest.main()
