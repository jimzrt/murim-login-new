import unittest
from pathlib import Path

from tools import model_smoke


class ModelSmokeTest(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "smoke"
        self.source = (root / "kuunmong-opening.ko.txt").read_text(encoding="utf-8")
        self.reference = (root / "kuunmong-opening.en.md").read_text(encoding="utf-8")

    def test_gold_excerpt_covers_all_independent_facts(self):
        score = model_smoke.score_draft(self.reference, self.reference)
        self.assertTrue(score["qa_passed"])
        self.assertEqual(score["token_f1"], 1.0)
        self.assertEqual(score["fact_score"], 1.0)
        self.assertEqual(len(score["fact_hits"]), score["fact_total"])

    def test_gold_is_not_this_project_translation(self):
        self.assertIn("성진", self.source)
        self.assertIn("Song-jin", self.reference)
        self.assertNotIn("Jang Sam", self.reference)
        self.assertNotIn("Jin Taekyung", self.reference)

    def test_collapsed_draft_misses_facts(self):
        bad = "# Excerpt\n\nA monk went up a mountain.\n"
        score = model_smoke.score_draft(bad, self.reference)
        self.assertLess(score["fact_score"], 0.3)
        self.assertLess(score["token_f1"], 0.2)

    def test_planted_review_defects_are_detectable(self):
        draft, planted = model_smoke.plant_defects(self.reference)
        self.assertIn("four noted mountains", draft)
        self.assertIn("Jang Sam", draft)
        self.assertIn("위부인", draft)
        self.assertNotIn("Palace of the Waters", draft)
        findings = [
            {"current": "four noted mountains", "defect": "wrong count"},
            {"current": "was called Jang Sam", "defect": "wrong name"},
            {"current": "Queen Wee 위부인", "defect": "hangul leftover"},
            {"current": "draft drops the Palace of the Waters errand", "defect": "omission"},
        ]
        recall = model_smoke.review_recall(findings, planted)
        self.assertEqual(recall["caught"], ["count", "name", "hangul", "omission"])


if __name__ == "__main__":
    unittest.main()
