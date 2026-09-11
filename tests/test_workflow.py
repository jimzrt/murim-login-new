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
        (self.root / "docs" / "NAMES.md").write_text(
            "# Names\n\n| Korean | English | Notes |\n|---|---|---|\n", encoding="utf-8"
        )
        self.root_patch = patch.object(workflow, "ROOT", self.root)
        self.hash_patch = patch.object(workflow, "source_hash", return_value="source-hash")
        self.root_patch.start()
        self.hash_patch.start()

    def tearDown(self):
        self.hash_patch.stop()
        self.root_patch.stop()
        self.temporary.cleanup()
    def record_update(self, state, paths):
        files = {}
        for path in (
            self.root / "docs" / "STATE.md",
            self.root / "docs" / "CONTEXT.json",
            self.root / "docs" / "NAMES.md",
            paths["beat"],
        ):
            if path.exists():
                files[str(path.relative_to(self.root))] = workflow.digest(path)
        workflow.atomic_json(paths["update_result"], {
            "version": 1, "chapter": state["chapter"], "files": files, "update": {},
        })
        state["artifacts"]["update_result_sha256"] = workflow.digest(paths["update_result"])
        workflow.atomic_json(paths["state"], state)


    def test_accept_promotes_revised_copy_only_after_state_update(self):
        state, paths = workflow.load(1)
        paths["revised"].parent.mkdir(parents=True, exist_ok=True)
        paths["revised"].write_text("# Chapter 1\n\nFinished.\n", encoding="utf-8")
        paths["final_qa"].parent.mkdir(parents=True, exist_ok=True)
        paths["final_qa"].write_text('{"passed":true}\n', encoding="utf-8")
        state["stage"] = "REVISED"
        state["artifacts"]["revised_sha256"] = workflow.digest(paths["revised"])
        state["artifacts"]["final_qa_sha256"] = workflow.digest(paths["final_qa"])
        workflow.atomic_json(paths["state"], state)

        with self.assertRaises(SystemExit):
            workflow.command_accept(1)
        self.assertFalse(paths["translation"].exists())

        (self.root / "docs" / "STATE.md").write_text(
            "# Translation State\n\n- Last completed: 1\n- Next chapter: 2\n", encoding="utf-8"
        )
        (self.root / "docs" / "CONTEXT.json").write_text(
            json.dumps({"version":1,"safe_through":1,"continuity_sources":[1],"active_continuity":["Hook."],"open_questions":["Open."],"temporary_decisions":["Decision."]}) + "\n", encoding="utf-8"
        )
        with self.assertRaises(SystemExit):
            workflow.command_accept(1)
        paths["beat"].parent.mkdir(parents=True, exist_ok=True)
        paths["beat"].write_text(
            "# Chapter 1\n\n## Plot\n\nFinished.\n\n## Continuity\n\n- Hook.\n\n## Translation Decisions\n\n- None.\n",
            encoding="utf-8",
        )
        self.record_update(state, paths)
        workflow.command_accept(1)
        self.assertEqual(paths["translation"].read_text(encoding="utf-8"), "# Chapter 1\n\nFinished.\n")
        recorded = json.loads(paths["state"].read_text(encoding="utf-8"))
        self.assertEqual(recorded["stage"], "ACCEPTED")

    def test_accept_rejects_context_without_version(self):
        state, paths = workflow.load(1)
        paths["revised"].parent.mkdir(parents=True, exist_ok=True)
        paths["revised"].write_text("# Chapter 1\n\nFinished.\n", encoding="utf-8")
        paths["final_qa"].parent.mkdir(parents=True, exist_ok=True)
        paths["final_qa"].write_text('{"passed":true}\n', encoding="utf-8")
        paths["beat"].parent.mkdir(parents=True, exist_ok=True)
        paths["beat"].write_text(
            "# Chapter 1\n\n## Plot\n\nFinished.\n\n## Continuity\n\n- Hook.\n\n## Translation Decisions\n\n- None.\n",
            encoding="utf-8",
        )
        state["stage"] = "REVISED"
        state["artifacts"]["revised_sha256"] = workflow.digest(paths["revised"])
        state["artifacts"]["final_qa_sha256"] = workflow.digest(paths["final_qa"])
        workflow.atomic_json(paths["state"], state)
        (self.root / "docs" / "STATE.md").write_text(
            "# Translation State\n\n- Last completed: 1\n- Next chapter: 2\n", encoding="utf-8"
        )
        (self.root / "docs" / "CONTEXT.json").write_text(
            '{"safe_through":1,"continuity_sources":[1]}\n', encoding="utf-8"
        )
        self.record_update(state, paths)
        with self.assertRaises(SystemExit) as error:
            workflow.command_accept(1)
        self.assertIn("version", str(error.exception))
        self.assertFalse(paths["translation"].exists())

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
        self.assertEqual(metrics["input_bytes"], len("bounded packet"))
        self.assertEqual(metrics["packet_token_estimate"], 4)

    def test_revise_applies_exact_review_replacements_without_model_call(self):
        state, paths = workflow.load(1)
        paths["draft"].parent.mkdir(parents=True, exist_ok=True)
        paths["draft"].write_text("# Chapter 1\n\nCurrent. Keep.\n", encoding="utf-8")
        review = {
            "version": 1,
            "summary": "One fix.",
            "findings": [{
                "id": "F01",
                "severity": "major",
                "source": "원문",
                "current": "Current.",
                "replacement": "Corrected.",
                "defect": "Wrong subject.",
                "rationale": "Source-supported.",
                "confidence": 0.9,
            }],
        }
        paths["review_json"].parent.mkdir(parents=True, exist_ok=True)
        workflow.atomic_json(paths["review_json"], review)
        state["stage"] = "REVIEWED"
        state["artifacts"]["reviewed_draft_sha256"] = workflow.digest(paths["draft"])
        state["artifacts"]["report_sha256"] = workflow.digest(paths["review_json"])
        workflow.atomic_json(paths["state"], state)
        passed = {"passed": True, "errors": [], "warnings": []}
        with (
            patch.object(context, "chapter_text", return_value="source"),
            patch.object(context, "exact_glossary_entries", return_value=[]),
            patch("tools.qa.run_qa", return_value=passed),
            patch.object(workflow, "run_omp") as model,
        ):
            workflow.command_revise(1)
        model.assert_not_called()
        self.assertEqual(paths["revised"].read_text(encoding="utf-8"), "# Chapter 1\n\nCorrected. Keep.\n")
        recorded = json.loads(paths["state"].read_text(encoding="utf-8"))
        self.assertEqual(recorded["stage"], "REVISED")
        self.assertNotIn("dispositions_sha256", recorded["artifacts"])

    def test_update_generates_and_records_all_durable_state(self):
        (self.root / "docs" / "workflow.json").write_text(
            json.dumps({**workflow.DEFAULT_CONFIG, "version": 1}), encoding="utf-8"
        )
        (self.root / "docs" / "CONTEXT.json").write_text(json.dumps({
            "version": 1,
            "safe_through": 0,
            "continuity_sources": [],
            "active_continuity": ["Old."],
            "open_questions": ["Old?"],
            "temporary_decisions": [],
        }), encoding="utf-8")
        source_path = self.root / "source.txt"
        source_path.write_text("주인공은 새이름과 신규를 만났다.", encoding="utf-8")
        profile = self.root / "characters" / "Hero.md"
        profile.parent.mkdir()
        profile.write_text("""# Hero (주인공)

- **Safe through:** Chapter 0
- **Aliases:** None
- **Role:** Wanderer
- **Personality:** Quiet
- **Voice:** Direct
- **Relationships:** None
- **Continuity:** Archived.
""", encoding="utf-8")
        state, paths = workflow.load(1)
        paths["revised"].parent.mkdir(parents=True, exist_ok=True)
        paths["revised"].write_text("# Chapter 1\n\nHero met New Name.\n", encoding="utf-8")
        state["stage"] = "REVISED"
        state["artifacts"]["revised_sha256"] = workflow.digest(paths["revised"])
        workflow.atomic_json(paths["state"], state)
        response = json.dumps({
            "chapter": 1,
            "beat": {
                "plot": ["Hero met two people."],
                "continuity": ["They remain together."],
                "translation_decisions": ["새이름 is New Name."],
            },
            "context": {
                "version": 1,
                "safe_through": 1,
                "continuity_sources": [1],
                "active_continuity": ["The group is together."],
                "open_questions": ["Why did they meet?"],
                "temporary_decisions": ["Keep New Name."],
            },
            "names": [{"korean": "새이름", "english": "New Name", "notes": "New ally"}],
            "profile_updates": [{
                "path": "characters/Hero.md",
                "current": "- **Role:** Wanderer",
                "replacement": "- **Role:** Group leader",
            }],
            "profile_creations": [{
                "filename": "Recruit.md",
                "korean": "신규",
                "english": "Recruit",
                "aliases": [],
                "role": "New ally",
                "personality": "Unknown",
                "voice": "Unknown",
                "relationships": "Met Hero",
            }],
        }, ensure_ascii=False)
        metrics = {"exact": True, "requests": 1, "models": {}}
        compact = context.compact_profile(profile.read_text(encoding="utf-8"))
        patches = (
            patch.object(context, "ROOT", self.root),
            patch.object(context, "chapter_text", return_value=source_path.read_text(encoding="utf-8")),
            patch.object(context, "chapter_source_path", return_value=source_path),
            patch.object(context, "exact_glossary_entries", return_value=[]),
            patch.object(context, "profile_entries", return_value=[(profile, compact)]),
        )
        with patches[0], patches[1], patches[2], patches[3], patches[4], patch.object(
            workflow, "run_omp", return_value=(response, metrics)
        ) as model:
            before = (self.root / "docs" / "STATE.md").read_text(encoding="utf-8")
            workflow.command_update(1, True)
            self.assertEqual((self.root / "docs" / "STATE.md").read_text(encoding="utf-8"), before)
            model.assert_not_called()
            workflow.command_update(1, False)
        self.assertIn("- Last completed: 1", (self.root / "docs" / "STATE.md").read_text(encoding="utf-8"))
        self.assertIn("| 새이름 | **New Name** | New ally |", (self.root / "docs" / "NAMES.md").read_text(encoding="utf-8"))
        self.assertIn("- **Role:** Group leader", profile.read_text(encoding="utf-8"))
        self.assertIn("- **Safe through:** Chapter 1", profile.read_text(encoding="utf-8"))
        self.assertTrue((self.root / "characters" / "Recruit.md").exists())
        self.assertTrue(workflow.durable_update_valid(
            json.loads(paths["state"].read_text(encoding="utf-8")), paths
        ))

    def test_revised_block_runs_update_then_summarize_then_checkpoint(self):
        (self.root / "docs" / "STATE.md").write_text(
            "# Translation State\n\n- Last completed: 8\n- Next chapter: 9\n", encoding="utf-8"
        )
        state, paths = workflow.load(9)
        state["stage"] = "REVISED"
        self.assertEqual(workflow.next_action(state, paths), "python tools/workflow.py update 9")
        paths["beat"].parent.mkdir(parents=True, exist_ok=True)
        paths["beat"].write_text("# Chapter 9\n", encoding="utf-8")
        self.record_update(state, paths)
        self.assertEqual(workflow.next_action(state, paths), "python tools/workflow.py summarize 9")
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
            json.dumps({"version":1,"safe_through":4,"continuity_sources":[4],"active_continuity":["Hook."],"open_questions":["Open."],"temporary_decisions":["Decision."]}) + "\n", encoding="utf-8"
        )
        self.record_update(state, paths)
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
                "polish": "provider/polish:high",
                "summary": "provider/summary:high",
            }
        })
        self.assertEqual(resolved["draft_model"], "provider/draft:high")
        self.assertEqual(resolved["review_model"], "provider/review:medium")
        self.assertEqual(resolved["polish_model"], "provider/polish:high")
        self.assertEqual(resolved["summary_model"], "provider/summary:high")
        self.assertEqual(resolved["checkpoint_model"], "provider/review:medium")
        self.assertEqual(resolved["models"]["draft"], "provider/draft:high")

    def test_checkpoint_model_can_override_review(self):
        resolved = workflow.resolve_role_models({
            "models": {
                "draft": "provider/draft:high",
                "review": "provider/review:medium",
                "revision": "provider/revision:high",
                "polish": "provider/polish:high",
                "summary": "provider/summary:high",
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
                    "polish": "provider/polish:high",
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


    def test_revised_chapter_before_polish_cutoff_asks_for_generated_update(self):
        state, paths = workflow.load(1)
        state["stage"] = "REVISED"
        self.assertEqual(workflow.next_action(state, paths), "python tools/workflow.py update 1")

    def test_revised_chapter_from_cutoff_asks_for_polish(self):
        (self.root / "docs" / "STATE.md").write_text(
            "# Translation State\n\n- Last completed: 26\n- Next chapter: 27\n",
            encoding="utf-8",
        )
        (self.root / "docs" / "workflow.json").write_text(
            json.dumps({**workflow.DEFAULT_CONFIG, "version": 1}), encoding="utf-8"
        )
        state, paths = workflow.load(27)
        state["stage"] = "REVISED"
        self.assertEqual(workflow.next_action(state, paths), "python tools/workflow.py polish 27")
        state["stage"] = "POLISHED"
        self.assertEqual(workflow.next_action(state, paths), "python tools/workflow.py update 27")

    def test_accept_promotes_polished_copy_from_cutoff(self):
        (self.root / "docs" / "STATE.md").write_text(
            "# Translation State\n\n- Last completed: 26\n- Next chapter: 27\n",
            encoding="utf-8",
        )
        (self.root / "docs" / "workflow.json").write_text(
            json.dumps({**workflow.DEFAULT_CONFIG, "version": 1, "summary_interval": 100, "checkpoint_review_interval": 100}),
            encoding="utf-8",
        )
        state, paths = workflow.load(27)
        paths["revised"].parent.mkdir(parents=True, exist_ok=True)
        paths["revised"].write_text("# Chapter 27\n\nRevised.\n", encoding="utf-8")
        paths["polished"].write_text("# Chapter 27\n\nPolished.\n", encoding="utf-8")
        paths["final_qa"].parent.mkdir(parents=True, exist_ok=True)
        paths["final_qa"].write_text('{"passed":true}\n', encoding="utf-8")
        paths["beat"].parent.mkdir(parents=True, exist_ok=True)
        paths["beat"].write_text(
            "# Chapter 27\n\n## Plot\n\nFinished.\n\n## Continuity\n\n- Hook.\n\n## Translation Decisions\n\n- None.\n",
            encoding="utf-8",
        )
        state["stage"] = "POLISHED"
        state["artifacts"]["revised_sha256"] = workflow.digest(paths["revised"])
        state["artifacts"]["polished_sha256"] = workflow.digest(paths["polished"])
        state["artifacts"]["final_qa_sha256"] = workflow.digest(paths["final_qa"])
        workflow.atomic_json(paths["state"], state)
        (self.root / "docs" / "STATE.md").write_text(
            "# Translation State\n\n- Last completed: 27\n- Next chapter: 28\n",
            encoding="utf-8",
        )
        (self.root / "docs" / "CONTEXT.json").write_text(
            json.dumps({"version":1,"safe_through":27,"continuity_sources":[27],"active_continuity":["Hook."],"open_questions":["Open."],"temporary_decisions":["Decision."]}) + "\n",
            encoding="utf-8",
        )
        self.record_update(state, paths)
        workflow.command_accept(27)
        self.assertEqual(paths["translation"].read_text(encoding="utf-8"), "# Chapter 27\n\nPolished.\n")

    def test_accepted_chapter_asks_for_master_until_promoted(self):
        state, paths = workflow.load(1)
        state["stage"] = "ACCEPTED"
        self.assertEqual(workflow.next_action(state, paths), "python tools/workflow.py master 1")
        mastering = self.root / "reviews" / "mastering" / "0001"
        mastering.mkdir(parents=True)
        (mastering / "state.json").write_text(
            '{"stage":"PROMOTED","qa_passed":true}\n', encoding="utf-8"
        )
        self.assertIn("workflow.py committed 1", workflow.next_action(state, paths))

    def test_master_requires_accepted_stage(self):
        state, paths = workflow.load(1)
        state["stage"] = "REVISED"
        workflow.atomic_json(paths["state"], state)
        with self.assertRaises(SystemExit):
            workflow.command_master(1)



if __name__ == "__main__":
    unittest.main()
