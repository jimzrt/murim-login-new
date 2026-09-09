import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import run_until


def write_state(root: Path, next_chapter: int) -> None:
    (root / "docs").mkdir(exist_ok=True)
    (root / "docs" / "STATE.md").write_text(
        f"# State\n\n- Last completed: {next_chapter - 1}\n- Next chapter: {next_chapter}\n",
        encoding="utf-8",
    )


class RunUntilTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        write_state(self.root, 13)
        self.root_patch = patch.object(run_until, "ROOT", self.root)
        self.incomplete_patch = patch.object(run_until, "incomplete_chapter", return_value=None)
        self.root_patch.start()
        self.incomplete_patch.start()

    def tearDown(self):
        self.incomplete_patch.stop()
        self.root_patch.stop()
        self.temporary.cleanup()

    def test_plans_remaining_chapters_from_state(self):
        self.assertEqual(run_until.planned_chapters(16), [13, 14, 15, 16])
        self.assertEqual(run_until.planned_chapters(13), [13])
        self.assertEqual(run_until.planned_chapters(12), [])

    def test_plans_from_incomplete_transaction_before_state(self):
        write_state(self.root, 15)
        self.incomplete_patch.stop()
        with patch.object(run_until, "incomplete_chapter", return_value=14):
            self.assertEqual(run_until.planned_chapters(16), [14, 15, 16])
        self.incomplete_patch.start()

    def test_dry_run_prints_plan_without_running(self):
        with patch.object(run_until, "run_next_chapter") as runner:
            with patch("sys.argv", ["run_until.py", "15", "--dry-run"]):
                self.assertEqual(run_until.main(), 0)
        runner.assert_not_called()

    def test_runs_each_chapter_and_stops_on_failure(self):
        calls: list[int] = []

        def fake_run(model):
            current = run_until.next_chapter()
            calls.append(current)
            if current == 14:
                return 7
            write_state(self.root, current + 1)
            return 0

        with patch.object(run_until, "run_next_chapter", side_effect=fake_run):
            with patch("sys.argv", ["run_until.py", "16"]):
                self.assertEqual(run_until.main(), 7)
        self.assertEqual(calls, [13, 14])
        self.assertEqual(run_until.next_chapter(), 14)

    def test_stops_if_run_next_succeeds_without_advancing_state(self):
        with patch.object(run_until, "run_next_chapter", return_value=0):
            with patch("sys.argv", ["run_until.py", "14"]):
                with self.assertRaises(SystemExit) as error:
                    run_until.main()
        self.assertIn("expected 14", str(error.exception))
        self.assertEqual(run_until.next_chapter(), 13)


if __name__ == "__main__":
    unittest.main()
