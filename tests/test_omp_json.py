import json
import unittest

from tools.omp_json import OmpJsonError, parse_json_lines


def event(model="gpt-test", input_tokens=100, output_tokens=20, text="done"):
    return json.dumps({
        "type": "message_end",
        "message": {
            "role": "assistant",
            "provider": "openai-codex",
            "model": model,
            "content": [{"type": "text", "text": text}],
            "usage": {
                "input": input_tokens,
                "output": output_tokens,
                "Vrij": "ignored",
                "cacheRead": 30,
                "cacheWrite": 0,
                "totalTokens": input_tokens + output_tokens + 30,
                "reasoning": 7,
                "cost": {"total": 0.0123},
            },
            "stopReason": "stop",
        },
    })


class OmpJsonTest(unittest.TestCase):
    def test_extracts_output_and_exact_usage(self):
        output, usage = parse_json_lines([event()], "requested/high")
        self.assertEqual(output, "done\n")
        self.assertTrue(usage["exact"])
        self.assertEqual(usage["input_tokens"], 100)
        self.assertEqual(usage["output_tokens"], 20)
        self.assertEqual(usage["cache_read_tokens"], 30)
        self.assertEqual(usage["reasoning_tokens"], 7)
        self.assertEqual(usage["models"]["openai-codex/gpt-test"]["requests"], 1)

    def test_aggregates_every_assistant_request_by_actual_model(self):
        _, usage = parse_json_lines([
            event("gpt-a", 100, 20, "intermediate"),
            event("gpt-b", 40, 5, "final"),
        ], "requested/high")
        self.assertEqual(usage["requests"], 2)
        self.assertEqual(usage["input_tokens"], 140)
        self.assertEqual(set(usage["models"]), {"openai-codex/gpt-a", "openai-codex/gpt-b"})

    def test_missing_usage_is_a_hard_failure(self):
        bad = json.dumps({"type": "message_end", "message": {
            "role": "assistant", "provider": "openai-codex", "model": "gpt-test",
            "content": [{"type": "text", "text": "done"}], "stopReason": "stop",
        }})
        with self.assertRaises(OmpJsonError):
            parse_json_lines([bad], "requested/high")


if __name__ == "__main__":
    unittest.main()
