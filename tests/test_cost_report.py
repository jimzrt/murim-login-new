import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import cost_report


class CostReportTest(unittest.TestCase):
    def test_aggregates_stage_metrics_and_checkpoint_yield(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            metrics = root / "reviews" / "metrics"
            checkpoints = root / "reviews" / "checkpoints"
            metrics.mkdir(parents=True)
            checkpoints.mkdir(parents=True)
            (metrics / "0008.json").write_text(json.dumps({
                "chapter": 8,
                "stages": {"draft_model": {
                    "exact": True,
                    "usage_source": "omp_provider_reported",
                    "requests": 1,
                    "input_tokens": 10,
                    "output_tokens": 5,
                    "cache_read_tokens": 2,
                    "cache_write_tokens": 0,
                    "total_tokens": 17,
                    "input_bytes": 400,
                    "packet_token_estimate": 100,
                    "output_bytes": 20,
                    "elapsed_seconds": 1.25,
                    "models": {"openai-codex/luna": {
                        "requests": 1,
                        "input_tokens": 10,
                        "output_tokens": 5,
                        "cache_read_tokens": 2,
                        "cache_write_tokens": 0,
                        "total_tokens": 17,
                    }},
                }}
            }), encoding="utf-8")
            (checkpoints / "0005-0009.meta.json").write_text(json.dumps({"finding_count": 2, "major_or_critical_count": 1}), encoding="utf-8")
            with patch.object(cost_report, "ROOT", root):
                report = cost_report.build_report()
        self.assertEqual(report["totals"]["input_tokens"], 10)
        self.assertEqual(report["chapters"]["8"]["models"]["openai-codex/luna"]["output_tokens"], 5)
        self.assertEqual(report["checkpoint_unique_finding_total"], 2)
        self.assertEqual(report["chapters"]["8"]["workload"]["packet_bytes"], 400)
        self.assertEqual(report["chapters"]["8"]["workload"]["packet_token_estimate"], 100)
        self.assertEqual(report["chapters"]["8"]["workload"]["elapsed_seconds"], 1.25)
        self.assertEqual(report["chapters"]["8"]["costs"]["subscription_api_equivalent_usd"], 0)
        self.assertEqual(report["chapters"]["8"]["costs"]["actual_api_cash_usd"], 0)
        text = cost_report.format_report(report, 8)
        self.assertIn("Chapter 8", text)
        self.assertIn("draft_model:", text.split("openai-codex/luna:")[0])
        self.assertIn("openai-codex/luna:", text)
        self.assertIn("Total:", text)
        full = cost_report.format_report(report)
        self.assertIn("Chapters with metric files: 1", full)
        self.assertIn("Checkpoint findings: 2 across 1 reviews", full)
        self.assertIn("MURIM LOGIN RESOURCE USAGE", full)
        self.assertIn("OpenAI subscription", full)
        self.assertIn("Luna calls", full)
        self.assertIn("Per-call cash", full)
        self.assertIn("API-equivalent value:    (unavailable for some calls)", full)

    def test_legacy_estimates_are_excluded(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            metrics = root / "reviews" / "metrics"
            metrics.mkdir(parents=True)
            (metrics / "0007.json").write_text(json.dumps({
                "chapter": 7,
                "stages": {"draft_model": {"estimated_input_tokens": 999}},
            }), encoding="utf-8")
            with patch.object(cost_report, "ROOT", root):
                report = cost_report.build_report()
        self.assertEqual(report["totals"]["input_tokens"], 0)
        self.assertEqual(len(report["unavailable_stages"]), 1)

    def test_resource_usage_keeps_subscription_value_off_openrouter_spend(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            metrics = root / "reviews" / "metrics"
            metrics.mkdir(parents=True)
            (metrics / "0063.json").write_text(json.dumps({
                "chapter": 63,
                "stages": {
                    "draft_model": {
                        "exact": True,
                        "usage_source": "omp_provider_reported",
                        "requests": 1,
                        "input_tokens": 10,
                        "output_tokens": 5,
                        "cache_read_tokens": 0,
                        "cache_write_tokens": 0,
                        "total_tokens": 15,
                        "cost_usd": 0.20,
                        "models": {"cursor/gpt-5.6-luna": {
                            "provider": "cursor",
                            "model": "gpt-5.6-luna",
                            "requests": 1,
                            "input_tokens": 10,
                            "output_tokens": 5,
                            "cache_read_tokens": 0,
                            "cache_write_tokens": 0,
                            "total_tokens": 15,
                            "cost_usd": 0.20,
                        }},
                    },
                    "review_model": {
                        "exact": True,
                        "usage_source": "omp_provider_reported",
                        "requests": 1,
                        "input_tokens": 8,
                        "output_tokens": 4,
                        "cache_read_tokens": 0,
                        "cache_write_tokens": 0,
                        "total_tokens": 12,
                        "cost_usd": 0.50,
                        "models": {"cursor/cursor-grok-4.6": {
                            "provider": "cursor",
                            "model": "cursor-grok-4.6",
                            "requests": 1,
                            "input_tokens": 8,
                            "output_tokens": 4,
                            "cache_read_tokens": 0,
                            "cache_write_tokens": 0,
                            "total_tokens": 12,
                            "cost_usd": 0.50,
                        }},
                    },
                    "master_model": {
                        "exact": True,
                        "usage_source": "omp_provider_reported",
                        "requests": 1,
                        "input_tokens": 6,
                        "output_tokens": 3,
                        "cache_read_tokens": 0,
                        "cache_write_tokens": 0,
                        "total_tokens": 9,
                        "cost_usd": 1.10,
                        "models": {"openai-codex/gpt-5.6-sol": {
                            "provider": "openai-codex",
                            "model": "gpt-5.6-sol",
                            "requests": 1,
                            "input_tokens": 6,
                            "output_tokens": 3,
                            "cache_read_tokens": 0,
                            "cache_write_tokens": 0,
                            "total_tokens": 9,
                            "cost_usd": 1.10,
                        }},
                    },
                    "adjudicator_model": {
                        "exact": True,
                        "usage_source": "omp_provider_reported",
                        "requests": 1,
                        "input_tokens": 4,
                        "output_tokens": 2,
                        "cache_read_tokens": 0,
                        "cache_write_tokens": 0,
                        "total_tokens": 6,
                        "cost_usd": 0.18,
                        "models": {"openrouter/deepseek/deepseek-v4.1-flash": {
                            "provider": "openrouter",
                            "model": "deepseek/deepseek-v4.1-flash",
                            "requests": 1,
                            "input_tokens": 4,
                            "output_tokens": 2,
                            "cache_read_tokens": 0,
                            "cache_write_tokens": 0,
                            "total_tokens": 6,
                            "cost_usd": 0.18,
                        }},
                    },
                },
            }), encoding="utf-8")
            with patch.object(cost_report, "ROOT", root):
                report = cost_report.build_report()
        resources = report["resources"]
        self.assertEqual(resources["openai-codex"]["billing_type"], "subscription")
        self.assertEqual(resources["cursor"]["families"]["luna"]["requests"], 1)
        self.assertEqual(resources["cursor"]["families"]["grok"]["requests"], 1)
        self.assertEqual(resources["openrouter"]["families"]["deepseek"]["cost_usd"], 0.18)
        self.assertEqual(resources["openai-codex"]["subscription_api_equivalent_usd"], 1.10)
        self.assertEqual(resources["cursor"]["subscription_api_equivalent_usd"], 0.70)
        self.assertEqual(resources["openrouter"]["actual_api_cash_usd"], 0.18)
        self.assertEqual(report["costs"]["actual_api_cash_usd"], 0.18)
        self.assertEqual(report["costs"]["subscription_api_equivalent_usd"], 1.80)
        text = cost_report.format_resource_report(report)
        self.assertIn("Sol calls", text)
        self.assertIn("API-equivalent value:", text)
        self.assertIn("$1.10", text)
        self.assertIn("Luna calls", text)
        self.assertIn("Grok calls", text)
        self.assertIn("DeepSeek:", text)
        self.assertIn("Actual token spend:", text)
        self.assertIn("$0.18", text)
        self.assertIn("Quota currently used:", text)
        self.assertIn("(unavailable)", text)

    def test_mastering_overlay_metrics_fill_gaps_without_double_counting(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            metrics = root / "reviews" / "metrics"
            overlay = root / "reviews" / "mastering" / "0008"
            metrics.mkdir(parents=True)
            overlay.mkdir(parents=True)
            stage = {
                "exact": True,
                "usage_source": "omp_provider_reported",
                "requests": 1,
                "input_tokens": 3,
                "output_tokens": 1,
                "cache_read_tokens": 0,
                "cache_write_tokens": 0,
                "total_tokens": 4,
                "cost_usd": 0.05,
            }
            (metrics / "0008.json").write_text(json.dumps({
                "chapter": 8,
                "stages": {
                    "draft_model": {
                        **stage,
                        "models": {"cursor/gpt-5.6-luna": {**stage, "provider": "cursor", "model": "gpt-5.6-luna"}},
                    }
                },
            }), encoding="utf-8")
            (overlay / "metrics.json").write_text(json.dumps({
                "chapter": 8,
                "stages": {
                    "master": {
                        **stage,
                        "cost_usd": 0.40,
                        "models": {"openai-codex/gpt-5.6-sol": {
                            **stage, "cost_usd": 0.40, "provider": "openai-codex", "model": "gpt-5.6-sol",
                        }},
                    }
                },
            }), encoding="utf-8")
            with patch.object(cost_report, "ROOT", root):
                report = cost_report.build_report()
            self.assertIn("master_model", report["chapters"]["8"]["stages"])
            self.assertEqual(report["resources"]["openai-codex"]["cost_usd"], 0.40)
            (metrics / "0008.json").write_text(json.dumps({
                "chapter": 8,
                "stages": {
                    "draft_model": {
                        **stage,
                        "models": {"cursor/gpt-5.6-luna": {**stage, "provider": "cursor", "model": "gpt-5.6-luna"}},
                    },
                    "master_model": {
                        **stage,
                        "cost_usd": 0.40,
                        "models": {"openai-codex/gpt-5.6-sol": {
                            **stage, "cost_usd": 0.40, "provider": "openai-codex", "model": "gpt-5.6-sol",
                        }},
                    },
                },
            }), encoding="utf-8")
            with patch.object(cost_report, "ROOT", root):
                again = cost_report.build_report()
            self.assertEqual(again["resources"]["openai-codex"]["cost_usd"], 0.40)
            self.assertEqual(again["resources"]["openai-codex"]["requests"], 1)

    def test_live_usage_is_optional(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "reviews" / "metrics").mkdir(parents=True)
            with patch.object(cost_report, "ROOT", root), patch.object(
                cost_report, "fetch_subscription_usage", return_value={"reports": []}
            ) as fetch:
                silent = cost_report.build_report()
                live = cost_report.build_report(live_usage=True)
        self.assertNotIn("subscription_usage", silent)
        fetch.assert_called_once()
        self.assertEqual(live["subscription_usage"], {"reports": []})


if __name__ == "__main__":
    unittest.main()
