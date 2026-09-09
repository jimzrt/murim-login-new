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

    def test_summarizes_workflow_and_file_tool_args(self):
        self.assertEqual(
            run_next.summarize_tool_args("bash", {"command": "python tools/workflow.py status 9"}),
            "workflow status 9",
        )
        self.assertEqual(
            run_next.summarize_tool_args("bash", {"command": "python tools/workflow.py draft 9"}),
            "workflow draft 9",
        )
        self.assertEqual(
            run_next.summarize_tool_args("read", {"path": ".work/0009/draft.md"}),
            ".work/0009/draft.md",
        )
        self.assertEqual(
            run_next.summarize_tool_args("grep", {"pattern": "Jin Wikyung", "path": "translations"}),
            "Jin Wikyung translations",
        )
        self.assertEqual(
            run_next.summarize_tool_args("glob", {"glob_pattern": "reviews/sol/*.json"}),
            "reviews/sol/*.json",
        )
        self.assertEqual(
            run_next.summarize_tool_args("hub", {"description": "Apply checkpoint findings"}),
            "Apply checkpoint findings",
        )
        self.assertEqual(
            run_next.format_tool_start({
                "toolName": "bash",
                "args": {"command": "python tools/workflow.py status 9"},
            }),
            "→ workflow status 9",
        )
        self.assertEqual(
            run_next.format_tool_start({
                "toolName": "read",
                "args": {"path": ".work/0009/draft.md"},
            }),
            "→ read  .work/0009/draft.md",
        )

    def test_progress_end_lines_include_status_and_elapsed(self):
        times = iter([10.0, 171.2, 200.0, 200.4])
        renderer = run_next.ProgressRenderer(clock=lambda: next(times))
        self.assertEqual(
            renderer.line({
                "type": "tool_execution_start",
                "toolCallId": "draft",
                "toolName": "bash",
                "args": {"command": "python tools/workflow.py draft 9"},
            }),
            "→ workflow draft 9",
        )
        self.assertEqual(
            renderer.line({
                "type": "tool_execution_end",
                "toolCallId": "draft",
                "toolName": "bash",
                "isError": False,
                "result": {"content": [{"type": "text", "text": "ok"}]},
            }),
            "✓ 161s",
        )
        self.assertEqual(
            renderer.line({
                "type": "tool_execution_start",
                "toolCallId": "status",
                "toolName": "bash",
                "args": {"command": "python tools/workflow.py status 9"},
            }),
            "→ workflow status 9",
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


if __name__ == "__main__":
    unittest.main()
