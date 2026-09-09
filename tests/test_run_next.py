import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import run_next


class RunNextTest(unittest.TestCase):
    def test_reads_exact_next_chapter_from_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "STATE.md").write_text(
                "# State\n\n- Last completed: 8\n- Next chapter: 9\n",
                encoding="utf-8",
            )
            with patch.object(run_next, "ROOT", root):
                self.assertEqual(run_next.next_chapter(), 9)

    def test_checkpoint_allowlist_is_chapter_scoped(self):
        self.assertTrue(run_next.allowed_change("translations/0009.md", 9))
        self.assertTrue(run_next.allowed_change("reviews/metrics/0009.json", 9))
        self.assertFalse(run_next.allowed_change("translations/0010.md", 9))
        self.assertFalse(run_next.allowed_change("characters/spoilers/future.md", 9))
        self.assertFalse(run_next.allowed_change("tools/workflow.py", 9))


if __name__ == "__main__":
    unittest.main()
