import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import workflow
from tools import omp_json


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


if __name__ == "__main__":
    unittest.main()
