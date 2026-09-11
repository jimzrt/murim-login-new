import unittest

from tools.model_io import (
    apply_review_replacements,
    blocking_dispositions,
    extract_reading_copy,
    parse_json_object,
    validate_patchset,
    validate_range_review,
    validate_review,
    validate_durable_update,
)


class ModelIoTest(unittest.TestCase):
    def review(self):
        return validate_review({
            "summary": "One problem.",
            "findings": [{
                "id": "F01", "severity": "major", "source": "원문",
                "current": "Current.", "defect": "Wrong subject.",
                "replacement": "Corrected.", "rationale": "Grammar.", "confidence": 0.9,
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

    def test_review_replacements_apply_without_rewriting_unchanged_text(self):
        revised = apply_review_replacements("# Chapter 1\n\nCurrent. Keep.\n", self.review())
        self.assertEqual(revised, "# Chapter 1\n\nCorrected. Keep.\n")

    def test_review_replacement_requires_a_unique_current_span(self):
        with self.assertRaisesRegex(ValueError, "occurs 2 times"):
            apply_review_replacements("Current. Current.", self.review())

    def test_overlapping_review_replacements_are_rejected(self):
        review = self.review()
        review["findings"].append({
            "id": "F02",
            "severity": "minor",
            "source": "원문",
            "current": "rent.",
            "replacement": "vised.",
            "defect": "Overlap.",
            "rationale": "Cannot apply atomically.",
            "confidence": 0.8,
        })
        with self.assertRaisesRegex(ValueError, "overlap"):
            apply_review_replacements("Current.", review)

    def test_durable_update_rejects_multiline_profile_patch(self):
        value = {
            "chapter": 4,
            "beat": {"plot": ["Plot."], "continuity": [], "translation_decisions": []},
            "context": {
                "version": 1,
                "safe_through": 4,
                "continuity_sources": [4],
                "active_continuity": ["Fact."],
                "open_questions": ["Question?"],
                "temporary_decisions": [],
            },
            "names": [],
            "profile_updates": [{
                "path": "characters/Hero.md",
                "current": "- **Role:** Old\n- **Voice:** Old",
                "replacement": "- **Role:** New",
            }],
            "profile_creations": [],
        }
        with self.assertRaisesRegex(ValueError, "one complete line"):
            validate_durable_update(value, 4)

    def test_unresolved_major_checkpoint_finding_blocks_acceptance(self):
        review = self.review()
        dispositions = {
            "dispositions": [
                {"finding_id": "F01", "status": "unresolved", "reason": "Ambiguous."}
            ]
        }
        self.assertEqual(blocking_dispositions(review, dispositions), ["F01"])

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
