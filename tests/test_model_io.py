import unittest

from tools.model_io import (
    blocking_dispositions,
    extract_reading_copy,
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

    def test_json_embedded_in_prose_is_extracted(self):
        value = parse_json_object('Here is the review.\n{"findings": [], "summary": "No actionable findings"}\n')
        self.assertEqual(value["summary"], "No actionable findings")

    def test_empty_response_names_the_failure(self):
        with self.assertRaises(ValueError) as error:
            parse_json_object("   ")
        self.assertIn("empty response", str(error.exception))

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

    def test_looped_revision_envelope_uses_the_first_copy(self):
        review = self.review()
        raw = """<<<TRANSLATION>>>
# Chapter 1

“Ordinary Markdown.”
<<<DISPOSITIONS>>>
{"dispositions":[{"finding_id":"F01","status":"applied","reason":"Corrected the subject."}]}
<<<END>>>
<<<TRANSLATION>>>
# Chapter 1

Repeated looping copy.
<<<DISPOSITIONS>>>
{"dispositions":[{"finding_id":"F01","status":"applied","reason":"looped"}]}
"""
        revision = parse_revision_response(raw, review)
        self.assertIn("Ordinary Markdown", revision["translation"])
        self.assertNotIn("Repeated looping copy", revision["translation"])
        self.assertEqual(revision["dispositions"][0]["reason"], "Corrected the subject.")

    def test_trailing_prose_after_json_is_ignored(self):
        value = parse_json_object(
            '{"findings": [], "summary": "No actionable findings"}\nPlease continue reviewing.\n{"findings": []}'
        )
        self.assertEqual(value["summary"], "No actionable findings")

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


class ReadingCopyExtractTest(unittest.TestCase):
    def test_extract_reading_copy_strips_same_line_preamble(self):
        raw = "Checking the chapter workflow and source so the polish pass stays faithful.# Chapter 28\n\n*Hoo.*\n"
        self.assertEqual(extract_reading_copy(raw, 28), "# Chapter 28\n\n*Hoo.*\n")

    def test_extract_reading_copy_rejects_missing_heading(self):
        with self.assertRaises(ValueError):
            extract_reading_copy("No heading here.", 28)
