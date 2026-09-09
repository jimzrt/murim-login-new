import unittest

from tools.model_io import (
    blocking_dispositions,
    parse_json_object,
    parse_revision_response,
    validate_patchset,
    validate_range_review,
    validate_review,
    validate_revision,
)


class ModelIoTest(unittest.TestCase):
    def review(self):
        return validate_review({
            "summary": "One problem.",
            "findings": [{
                "id": "F01", "severity": "major", "source": "원문",
                "current": "Current.", "defect": "Wrong subject.",
                "correction": "Corrected.", "rationale": "Grammar.", "confidence": 0.9,
            }],
        })

    def test_fenced_json_is_accepted_but_normalized(self):
        value = parse_json_object('```json\n{"findings": [], "summary": "No actionable findings"}\n```')
        self.assertEqual(validate_review(value)["findings"], [])

    def test_revision_requires_exactly_one_disposition_per_finding(self):
        review = self.review()
        with self.assertRaises(ValueError):
            validate_revision({"translation": "# Chapter 1\n", "dispositions": []}, review)

    def test_unresolved_major_finding_blocks_acceptance(self):
        review = self.review()
        revision = validate_revision({
            "translation": "# Chapter 1\n\nText.\n",
            "dispositions": [{"finding_id": "F01", "status": "unresolved", "reason": "Ambiguous."}],
        }, review)
        self.assertEqual(blocking_dispositions(review, revision), ["F01"])

    def test_revision_envelope_keeps_markdown_outside_json(self):
        review = self.review()
        raw = '''<<<TRANSLATION>>>
# Chapter 1

“Ordinary Markdown.”
<<<DISPOSITIONS>>>
{"dispositions":[{"finding_id":"F01","status":"applied","reason":"Corrected the subject."}]}'''
        revision = parse_revision_response(raw, review)
        self.assertTrue(revision["translation"].startswith("# Chapter 1"))
        self.assertEqual(revision["dispositions"][0]["status"], "applied")

    def test_range_review_requires_chapter_and_patch_coverage(self):
        value = self.review()
        value["findings"][0]["chapter"] = 3
        review = validate_range_review(value, {3, 4})
        patchset = validate_patchset({
            "summary": "Fixed.",
            "patches": [{"chapter": 3, "finding_ids": ["F01"], "old": "Current.", "new": "Corrected."}],
            "dispositions": [{"finding_id": "F01", "status": "applied", "reason": "Corrected."}],
        }, review)
        self.assertEqual(patchset["patches"][0]["chapter"], 3)
