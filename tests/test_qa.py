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
