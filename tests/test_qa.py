import unittest

from tools.qa import run_qa


class QaTest(unittest.TestCase):
    def test_clean_copy_passes(self):
        source = "＃1화\n\n" + ("그는 말했다. " * 9) + "\n\n* * *\n\n100"
        target = '# Chapter 1\n\nHe said, “This is deliberately long enough to pass the translation ratio check.”\n\n* * *\n\n100 remained.\n'
        result = run_qa(1, source, target, [])
        self.assertTrue(result["passed"], result)

    def test_scene_break_and_hangul_errors_block(self):
        result = run_qa(2, "＃2화\n\n* * *", "# Chapter 2\n\n안녕", [])
        self.assertFalse(result["passed"])
        self.assertEqual({item["code"] for item in result["errors"]} & {"hangul", "scene_breaks"}, {"hangul", "scene_breaks"})

    def test_semantic_probes_flag_reversed_gesture_and_lost_specificity(self):
        source = "그는 조용히 고개를 끄덕였다. 큰형이 전음으로 공력을 전달했다."
        target = "# Chapter 8\n\nHe quietly shook his head. His older brother used Sound Transmission.\n"
        result = run_qa(8, source, target, [])
        messages = {item["message"] for item in result["warnings"]}
        self.assertTrue(any("nod" in message for message in messages))
        self.assertTrue(any("eldest-brother" in message for message in messages))
        self.assertTrue(any("internal energy" in message for message in messages))
