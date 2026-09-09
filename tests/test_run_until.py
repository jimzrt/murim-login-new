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

    def test_dry_run_does_not_take_the_run_lock(self):
        with patch.object(run_until, "run_next_chapter") as runner:
            with patch("sys.argv", ["run_until.py", "15", "--dry-run"]):
                self.assertEqual(run_until.main(), 0)
        runner.assert_not_called()
        self.assertFalse((self.root / ".work" / "run.lock").exists())

    def test_existing_run_lock_blocks_run_until(self):
        import subprocess
        import sys
        import time
        from tools.run_lock import read_payload, lock_path

        repo = Path(__file__).resolve().parents[1]
        holder = subprocess.Popen(
            [
                sys.executable,
                "-c",
                "import sys, time\n"
                "from pathlib import Path\n"
                "sys.path.insert(0, sys.argv[1])\n"
                "from tools.run_lock import hold_run_lock\n"
                "with hold_run_lock(Path(sys.argv[2]), holder='run_next', chapter=12, stage='coordinator'):\n"
                "    time.sleep(30)\n",
                str(repo),
                str(self.root),
            ],
            cwd=repo,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            deadline = time.time() + 5
            payload = {}
            while time.time() < deadline:
                payload = read_payload(lock_path(self.root))
                if payload.get("holder") == "run_next":
                    break
                if holder.poll() is not None:
                    self.fail(holder.stderr.read())
                time.sleep(0.05)
            self.assertEqual(payload.get("holder"), "run_next")
            with patch.object(run_until, "run_next_chapter") as runner:
                with patch("sys.argv", ["run_until.py", "16"]):
                    with self.assertRaises(SystemExit) as error:
                        run_until.main()
            runner.assert_not_called()
            self.assertIn("already in progress", str(error.exception))
            self.assertIn("run_next", str(error.exception))
        finally:
            holder.terminate()
            holder.wait(timeout=5)
            if holder.stderr:
                holder.stderr.close()

    def test_nested_run_next_joins_run_until_lock(self):
        from tools.run_lock import hold_run_lock, read_payload, lock_path

        def fake_run(model):
            with hold_run_lock(self.root, holder="run_next", chapter=13, stage="coordinator"):
                payload = read_payload(lock_path(self.root))
                self.assertEqual(payload["holder"], "run_until")
                self.assertEqual(payload["stage"], "coordinator")
            write_state(self.root, 14)
            return 0

        with patch.object(run_until, "run_next_chapter", side_effect=fake_run):
            with patch("sys.argv", ["run_until.py", "13"]):
                self.assertEqual(run_until.main(), 0)
        payload = read_payload(lock_path(self.root))
        self.assertEqual(payload["stage"], "released")



if __name__ == "__main__":
    unittest.main()
