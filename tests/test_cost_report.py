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
                "stages": {"draft_model": {"estimated_input_tokens": 10, "estimated_output_tokens": 5, "elapsed_seconds": 2}}
            }), encoding="utf-8")
            (checkpoints / "0005-0009.meta.json").write_text(json.dumps({"finding_count": 2, "major_or_critical_count": 1}), encoding="utf-8")
            with patch.object(cost_report, "ROOT", root):
                report = cost_report.build_report()
        self.assertEqual(report["totals"]["estimated_input_tokens"], 10)
        self.assertEqual(report["checkpoint_unique_finding_total"], 2)


if __name__ == "__main__":
    unittest.main()
