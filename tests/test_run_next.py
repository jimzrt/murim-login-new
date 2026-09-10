import io
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

    def test_checkpoint_allowlist_includes_block_translations(self):
        self.assertTrue(run_next.allowed_change("translations/0009.md", 9))
        self.assertTrue(run_next.allowed_change("translations/0005.md", 9))
        self.assertTrue(run_next.allowed_change("translations/0008.md", 9))
        self.assertTrue(run_next.allowed_change("reviews/metrics/0009.json", 9))
        self.assertFalse(run_next.allowed_change("translations/0004.md", 9))
        self.assertFalse(run_next.allowed_change("translations/0010.md", 9))
        self.assertFalse(run_next.allowed_change("translations/0005.md", 8))
        self.assertFalse(run_next.allowed_change("characters/spoilers/future.md", 9))
        self.assertFalse(run_next.allowed_change("tools/workflow.py", 9))

    def test_coordinator_command_disables_hub_and_auto_background(self):
        command = run_next.coordinator_command(14, "provider/coordinator:high")
        self.assertEqual(command[command.index("--tools") + 1], run_next.COORDINATOR_TOOLS)
        self.assertNotIn("hub", command[command.index("--tools") + 1])
        self.assertNotIn("task", command[command.index("--tools") + 1])
        self.assertEqual(command[command.index("--config") + 1], str(run_next.COORDINATOR_OVERLAY))
        self.assertEqual(command[command.index("--max-time") + 1], str(run_next.COORDINATOR_MAX_TIME))
        self.assertIn("--no-pty", command)
        self.assertIn("--no-extensions", command)
        self.assertIn("checkpoint dispositions", run_next.COORDINATOR_SYSTEM)
        self.assertIn("timeout=3600", run_next.COORDINATOR_SYSTEM)
        self.assertIn("keep every required key", run_next.COORDINATOR_SYSTEM)
        self.assertIn("temporary_decisions", run_next.COORDINATOR_SYSTEM)
        self.assertIn("do not rerun that model", run_next.COORDINATOR_SYSTEM)
        overlay = run_next.COORDINATOR_OVERLAY.read_text(encoding="utf-8")
        self.assertIn("autoBackground:\n    enabled: false", overlay)
        self.assertIn("hub: deny", overlay)
        self.assertIn("task: deny", overlay)
        self.assertIn("async:\n  enabled: false", overlay)

    def test_summarizes_workflow_and_file_tool_args(self):
        self.assertEqual(
            run_next.summarize_tool_args("bash", {"command": "python tools/workflow.py status 9"}),
            "python tools/workflow.py status 9",
        )
        self.assertEqual(
            run_next.summarize_tool_args("bash", {
                "command": "python tools/workflow.py draft 9",
                "timeout": 120,
            }),
            "python tools/workflow.py draft 9  (timeout=120)",
        )
        self.assertEqual(
            run_next.summarize_tool_args("read", {"path": ".work/0009/draft.md"}),
            "path=.work/0009/draft.md",
        )
        self.assertIn(
            "description=Apply checkpoint findings",
            run_next.summarize_tool_args("hub", {
                "description": "Apply checkpoint findings",
                "prompt": "python tools/workflow.py draft 14",
            }),
        )
        self.assertIn(
            "prompt=python tools/workflow.py draft 14",
            run_next.summarize_tool_args("hub", {
                "description": "Apply checkpoint findings",
                "prompt": "python tools/workflow.py draft 14",
            }),
        )
        self.assertEqual(
            run_next.format_tool_start("bash", {"command": "python tools/workflow.py status 9"}),
            "→ bash  python tools/workflow.py status 9",
        )
        self.assertEqual(
            run_next.format_tool_start("read", {"path": ".work/0009/draft.md"}),
            "→ read  path=.work/0009/draft.md",
        )

    def test_rejects_hub_and_task(self):
        with self.assertRaises(SystemExit) as error:
            run_next.reject_forbidden_tool({
                "type": "tool_execution_start",
                "toolName": "hub",
                "args": {
                    "description": "wait for draft",
                    "prompt": "python tools/workflow.py draft 14",
                },
            })
        self.assertIn("forbidden tool hub", str(error.exception))
        self.assertIn("python tools/workflow.py draft 14", str(error.exception))
        run_next.reject_forbidden_tool({
            "type": "tool_execution_start",
            "toolName": "bash",
            "args": {"command": "python tools/workflow.py draft 14"},
        })

    def test_progress_end_lines_include_status_command_and_elapsed(self):
        times = iter([10.0, 171.2, 200.0, 200.4])
        renderer = run_next.ProgressRenderer(clock=lambda: next(times))
        self.assertEqual(
            renderer.line({
                "type": "tool_execution_start",
                "toolCallId": "draft",
                "toolName": "bash",
                "args": {"command": "python tools/workflow.py draft 9"},
            }),
            "→ bash  python tools/workflow.py draft 9",
        )
        self.assertEqual(
            renderer.line({
                "type": "tool_execution_end",
                "toolCallId": "draft",
                "toolName": "bash",
                "isError": False,
                "result": {"content": [{"type": "text", "text": "ok"}]},
            }),
            "✓ bash  python tools/workflow.py draft 9  161s",
        )
        self.assertEqual(
            renderer.line({
                "type": "tool_execution_start",
                "toolCallId": "status",
                "toolName": "bash",
                "args": {"command": "python tools/workflow.py status 9"},
            }),
            "→ bash  python tools/workflow.py status 9",
        )
        self.assertEqual(
            renderer.line({
                "type": "tool_execution_end",
                "toolCallId": "status",
                "toolName": "bash",
                "isError": False,
                "result": {"content": [{
                    "type": "text",
                    "text": "Chapter: 9\nStage: CONTEXT_READY\nNext action: python tools/workflow.py draft 9\n",
                }]},
            }),
            "✓ CONTEXT_READY; next: python tools/workflow.py draft 9",
        )

    def test_timeout_results_are_logged(self):
        times = iter([1.0, 121.0])
        renderer = run_next.ProgressRenderer(clock=lambda: next(times))
        renderer.line({
            "type": "tool_execution_start",
            "toolCallId": "hub",
            "toolName": "hub",
            "args": {
                "description": "wait for draft",
                "prompt": "python tools/workflow.py draft 14",
            },
        })
        line = renderer.line({
            "type": "tool_execution_end",
            "toolCallId": "hub",
            "toolName": "hub",
            "isError": True,
            "result": {"content": "python tools/workflow.py draft 14 timed out after 120 seconds"},
        })
        self.assertIn("✗ hub", line)
        self.assertIn("timed out after 120 seconds", line)
        self.assertIn("120s", line)

    def test_assistant_text_does_not_glue_to_tool_lines(self):
        renderer = run_next.ProgressRenderer(clock=lambda: 0.0)
        buffer = io.StringIO()
        with patch("sys.stdout", buffer):
            run_next.render_event({
                "type": "message_update",
                "assistantMessageEvent": {"type": "text_delta", "delta": "it should wait"},
            }, renderer)
            run_next.render_event({
                "type": "tool_execution_start",
                "toolCallId": "draft",
                "toolName": "bash",
                "args": {"command": "python tools/workflow.py draft 14"},
            }, renderer)
        output = buffer.getvalue()
        self.assertIn("\nit should wait\n", output)
        self.assertIn("→ bash  python tools/workflow.py draft 14\n", output)


    def test_external_head_move_is_not_a_coordinator_commit(self):
        calls = {"rev-parse": "bbbbbbbb", "log": "Publish the HTML reader on GitHub Pages."}

        def fake_git(*args, capture=True):
            if args[:2] == ("rev-parse", "--verify"):
                return calls["rev-parse"]
            if args[:2] == ("log", "-1"):
                return calls["log"]
            raise AssertionError(args)

        with patch.object(run_next, "git", side_effect=fake_git):
            run_next.unexpected_coordinator_commit("aaaaaaaa", 17)
            calls["log"] = "Accept Chapter 17"
            with self.assertRaises(SystemExit) as error:
                run_next.unexpected_coordinator_commit("aaaaaaaa", 17)
            self.assertIn("coordinator committed unexpectedly", str(error.exception))

if __name__ == "__main__":

    unittest.main()
