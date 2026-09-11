import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import call, patch

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

    def test_checkpoint_allowlist_includes_generated_state_and_block_translations(self):
        self.assertTrue(run_next.allowed_change("docs/NAMES.md", 9))
        self.assertTrue(run_next.allowed_change("translations/0009.md", 9))
        self.assertTrue(run_next.allowed_change("translations/0005.md", 9))
        self.assertTrue(run_next.allowed_change("translations/0008.md", 9))
        self.assertTrue(run_next.allowed_change("reviews/metrics/0009.json", 9))
        self.assertFalse(run_next.allowed_change("translations/0004.md", 9))
        self.assertFalse(run_next.allowed_change("translations/0010.md", 9))
        self.assertFalse(run_next.allowed_change("translations/0005.md", 8))
        self.assertFalse(run_next.allowed_change("characters/spoilers/future.md", 9))
        self.assertFalse(run_next.allowed_change("tools/workflow.py", 9))

    def test_runner_executes_only_each_reported_workflow_action(self):
        statuses = [
            {"stage": "READY", "next_action": "python tools/workflow.py prepare 14"},
            {"stage": "CONTEXT_READY", "next_action": "python tools/workflow.py draft 14"},
            {"stage": "ACCEPTED", "next_action": "python tools/workflow.py master 14"},
        ]
        lock = SimpleNamespace(update=lambda **_values: None)
        with (
            patch.object(run_next, "workflow_status", side_effect=statuses),
            patch.object(run_next, "run_workflow_command") as command,
        ):
            run_next.run_to_accepted(14, lock)
        self.assertEqual(command.call_args_list, [
            call(14, "python tools/workflow.py prepare 14"),
            call(14, "python tools/workflow.py draft 14"),
        ])

    def test_manual_checkpoint_action_stops_without_guessing(self):
        action = "apply or disposition checkpoint findings, then: python tools/workflow.py checkpointed 14"
        with self.assertRaisesRegex(SystemExit, "manual action"):
            run_next.run_workflow_command(14, action)

    def test_workflow_command_rejects_another_chapter(self):
        with self.assertRaisesRegex(SystemExit, "manual action"):
            run_next.run_workflow_command(14, "python tools/workflow.py draft 15")

    def test_workflow_command_runs_without_an_omp_coordinator(self):
        completed = SimpleNamespace(returncode=0)
        with patch.object(run_next.subprocess, "run", return_value=completed) as runner:
            run_next.run_workflow_command(14, "python tools/workflow.py draft 14")
        command = runner.call_args.args[0]
        self.assertEqual(command[-2:], ["draft", "14"])
        self.assertNotIn("omp", command)


if __name__ == "__main__":
    unittest.main()
