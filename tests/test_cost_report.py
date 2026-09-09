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


if __name__ == "__main__":
    unittest.main()
