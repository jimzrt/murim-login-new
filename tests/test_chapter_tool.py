import unittest

from tools.chapter import extract_chapter, source_chapters


class ChapterExtractorTest(unittest.TestCase):
    def test_first_and_last_chapter_boundaries(self):
        chapters = source_chapters()
        first = extract_chapter(0)
        last = extract_chapter(chapters[-1])

        self.assertTrue(first.startswith("＃0화\n"))
        self.assertNotIn("＃1화", first)
        self.assertRegex(last, rf"^\s*＃?{chapters[-1]}화\s*\n")

    def test_source_contains_every_chapter_once_in_order(self):
        chapters = source_chapters()
        self.assertTrue(chapters)
        self.assertEqual(chapters, list(range(chapters[-1] + 1)))


if __name__ == "__main__":
    unittest.main()
