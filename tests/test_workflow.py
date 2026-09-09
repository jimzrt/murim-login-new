import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import workflow
from tools import omp_json
from tools import context


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "docs").mkdir()
        (self.root / "docs" / "STATE.md").write_text(
            "# Translation State\n\n- Last completed: 0\n- Next chapter: 1\n", encoding="utf-8"
        )
        self.root_patch = patch.object(workflow, "ROOT", self.root)
        self.hash_patch = patch.object(workflow, "source_hash", return_value="source-hash")
        self.root_patch.start()
        self.hash_patch.start()

    def tearDown(self):
        self.hash_patch.stop()
        self.root_patch.stop()
        self.temporary.cleanup()

    def test_accept_promotes_revised_copy_only_after_state_update(self):
        state, paths = workflow.load(1)
        paths["revised"].parent.mkdir(parents=True, exist_ok=True)
        paths["revised"].write_text("# Chapter 1\n\nFinished.\n", encoding="utf-8")
        paths["dispositions"].parent.mkdir(parents=True, exist_ok=True)
        paths["dispositions"].write_text('{"version":1,"dispositions":[]}\n', encoding="utf-8")
        paths["final_qa"].parent.mkdir(parents=True, exist_ok=True)
        paths["final_qa"].write_text('{"passed":true}\n', encoding="utf-8")
        state["stage"] = "REVISED"
        state["artifacts"]["revised_sha256"] = workflow.digest(paths["revised"])
        state["artifacts"]["dispositions_sha256"] = workflow.digest(paths["dispositions"])
        state["artifacts"]["final_qa_sha256"] = workflow.digest(paths["final_qa"])
        workflow.atomic_json(paths["state"], state)

        with self.assertRaises(SystemExit):
            workflow.command_accept(1)
        self.assertFalse(paths["translation"].exists())

        (self.root / "docs" / "STATE.md").write_text(
            "# Translation State\n\n- Last completed: 1\n- Next chapter: 2\n", encoding="utf-8"
        )
        (self.root / "docs" / "CONTEXT.json").write_text(
            '{"safe_through":1,"continuity_sources":[1]}\n', encoding="utf-8"
        )
        with self.assertRaises(SystemExit):
            workflow.command_accept(1)
        paths["beat"].parent.mkdir(parents=True, exist_ok=True)
        paths["beat"].write_text(
            "# Chapter 1\n\n## Plot\n\nFinished.\n\n## Continuity\n\n- Hook.\n\n## Translation Decisions\n\n- None.\n",
            encoding="utf-8",
        )
        workflow.command_accept(1)
        self.assertEqual(paths["translation"].read_text(encoding="utf-8"), "# Chapter 1\n\nFinished.\n")
        recorded = json.loads(paths["state"].read_text(encoding="utf-8"))
        self.assertEqual(recorded["stage"], "ACCEPTED")

    def test_existing_completed_translation_reconciles_as_accepted(self):
        translation = self.root / "translations" / "0000.md"
        translation.parent.mkdir()
        translation.write_text("# Chapter 0\n\nAccepted.\n", encoding="utf-8")
        state, _ = workflow.load(0)
        self.assertEqual(state["stage"], "COMMITTED")
        self.assertTrue(state["reconciled_legacy_acceptance"])

    def test_reading_copy_rejects_hangul(self):
        path = self.root / "bad.md"
        path.write_text("# Chapter 2\n\n안녕\n", encoding="utf-8")
        with self.assertRaises(SystemExit):
            workflow.validate_reading_copy(path, 2)

    def test_new_transaction_must_match_next_chapter(self):
        with self.assertRaises(SystemExit):
            workflow.load(2)

    def test_model_call_uses_json_mode_and_preserves_exact_usage(self):
        packet = self.root / "packet.md"
        packet.write_text("bounded packet", encoding="utf-8")
        exact = {
            "exact": True,
            "usage_source": "omp_provider_reported",
            "input_tokens": 12,
            "output_tokens": 3,
            "cache_read_tokens": 4,
            "cache_write_tokens": 0,
            "total_tokens": 19,
            "requests": 1,
            "models": {},
        }
        with patch.object(omp_json, "run_json_command", return_value=("answer\n", exact)) as runner:
            output, metrics = workflow.run_omp(packet, "provider/model:high", 120)
        command = runner.call_args.args[0]
        self.assertIn("--mode", command)
        self.assertIn("json", command)
        self.assertNotIn("-p", command)
        self.assertEqual(output, "answer\n")
        self.assertTrue(metrics["exact"])
        self.assertEqual(metrics["input_tokens"], 12)

    def test_revised_block_asks_for_summarize_then_checkpoint(self):
        (self.root / "docs" / "STATE.md").write_text(
            "# Translation State\n\n- Last completed: 8\n- Next chapter: 9\n", encoding="utf-8"
        )
        state, paths = workflow.load(9)
        state["stage"] = "REVISED"
        action = workflow.next_action(state, paths)
        self.assertIn("summaries/beats/0009.md", action)
        self.assertIn("python tools/workflow.py summarize 9", action)
        paths["checkpoint_summary"].parent.mkdir(parents=True, exist_ok=True)
        paths["checkpoint_summary"].write_text("# Chapters 5–9\n", encoding="utf-8")
        self.assertEqual(workflow.next_action(state, paths), "python tools/workflow.py checkpoint 9")

    def test_summarize_packet_is_written_from_beats(self):
        (self.root / "docs" / "STATE.md").write_text(
            "# Translation State\n\n- Last completed: 3\n- Next chapter: 4\n", encoding="utf-8"
        )
        (self.root / "docs" / "workflow.json").write_text(
            json.dumps({**workflow.DEFAULT_CONFIG, "version": 1}), encoding="utf-8"
        )
        beats = self.root / "summaries" / "beats"
        beats.mkdir(parents=True)
        for chapter in range(5):
            (beats / f"{chapter:04d}.md").write_text(
                f"# Chapter {chapter}\n\n## Plot\n\nPlot {chapter}.\n\n## Continuity\n\n- Hook {chapter}.\n\n## Translation Decisions\n\n- Term {chapter}.\n",
                encoding="utf-8",
            )
        state, paths = workflow.load(4)
        paths["revised"].parent.mkdir(parents=True, exist_ok=True)
        state["stage"] = "REVISED"
        workflow.atomic_json(paths["state"], state)
        (self.root / "docs" / "STATE.md").write_text(
            "# Translation State\n\n- Last completed: 4\n- Next chapter: 5\n", encoding="utf-8"
        )
        (self.root / "docs" / "CONTEXT.json").write_text(
            '{"safe_through":4,"continuity_sources":[4]}\n', encoding="utf-8"
        )
        exact = {
            "exact": True,
            "usage_source": "omp_provider_reported",
            "input_tokens": 8,
            "output_tokens": 4,
            "cache_read_tokens": 0,
            "cache_write_tokens": 0,
            "total_tokens": 12,
            "requests": 1,
            "models": {},
        }
        summary = "# Chapters 0–4\n\n## Plot\n\nBlock plot.\n\n## Continuity\n\n- Hook.\n\n## Translation Decisions\n\n- Term.\n"
        with patch.object(context, "ROOT", self.root), patch.object(workflow, "run_omp", return_value=(summary, exact)):
            workflow.command_summarize(4)
        written = paths["checkpoint_summary"].read_text(encoding="utf-8")
        self.assertIn("# Chapters 0–4", written)
        packet = paths["summary_packet"].read_text(encoding="utf-8")
        self.assertIn("Plot 0", packet)
        self.assertNotIn("translations/", packet)

    def test_each_role_model_is_independent(self):
        resolved = workflow.resolve_role_models({
            "models": {
                "draft": "provider/draft:high",
                "review": "provider/review:medium",
                "revision": "provider/revision:high",
                "summary": "provider/summary:high",
                "coordinator": "provider/coordinator:high",
            }
        })
        self.assertEqual(resolved["draft_model"], "provider/draft:high")
        self.assertEqual(resolved["review_model"], "provider/review:medium")
        self.assertEqual(resolved["revision_model"], "provider/revision:high")
        self.assertEqual(resolved["summary_model"], "provider/summary:high")
        self.assertEqual(resolved["coordinator_model"], "provider/coordinator:high")
        self.assertEqual(resolved["checkpoint_model"], "provider/review:medium")
        self.assertEqual(resolved["models"]["draft"], "provider/draft:high")

    def test_checkpoint_model_can_override_review(self):
        resolved = workflow.resolve_role_models({
            "models": {
                "draft": "provider/draft:high",
                "review": "provider/review:medium",
                "revision": "provider/revision:high",
                "summary": "provider/summary:high",
                "coordinator": "provider/coordinator:high",
                "checkpoint": "provider/checkpoint:medium",
            }
        })
        self.assertEqual(resolved["review_model"], "provider/review:medium")
        self.assertEqual(resolved["checkpoint_model"], "provider/checkpoint:medium")

    def test_missing_role_model_is_a_hard_failure(self):
        with self.assertRaises(SystemExit):
            workflow.resolve_role_models({
                "models": {
                    "draft": "provider/draft:high",
                    "review": "provider/review:medium",
                    "revision": "provider/revision:high",
                    "summary": "provider/summary:high",
                }
            })

    def test_incomplete_chapter_resumes_in_flight_transaction(self):
        work = self.root / ".work"
        for number, stage in ((13, "COMMITTED"), (14, "CHECKPOINT_REVIEWED"), (15, "READY")):
            folder = work / f"{number:04d}"
            folder.mkdir(parents=True)
            (folder / "workflow.json").write_text(
                f'{{"chapter":{number},"stage":"{stage}","artifacts":{{}}}}\n',
                encoding="utf-8",
            )
        self.assertEqual(workflow.incomplete_chapter(), 14)


if __name__ == "__main__":
    unittest.main()
