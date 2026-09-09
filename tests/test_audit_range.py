import unittest

from tools.audit_range import apply_patchset, blocks


class AuditRangeTest(unittest.TestCase):
    def test_blocks_preserve_order_and_remainder(self):
        self.assertEqual(blocks(list(range(8)), 5), [list(range(5)), [5, 6, 7]])

    def test_exact_patch_is_applied_once(self):
        patchset = {"patches": [{"chapter": 1, "finding_ids": ["R1"], "old": "shook his head", "new": "nodded"}]}
        result = apply_patchset(patchset, {1: "He shook his head."})
        self.assertEqual(result[1], "He nodded.")

    def test_ambiguous_patch_is_rejected(self):
        patchset = {"patches": [{"chapter": 1, "finding_ids": ["R1"], "old": "head", "new": "face"}]}
        with self.assertRaises(ValueError):
            apply_patchset(patchset, {1: "His head met the head."})


if __name__ == "__main__":
    unittest.main()
