import tempfile
import unittest
from pathlib import Path

from tools.chapter import chapter_path, extract_chapter, source_chapters, split_bulk


class ChapterSourceTest(unittest.TestCase):
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
        for number in chapters:
            self.assertTrue(chapter_path(number).is_file())

    def test_split_bulk_writes_normalized_chapter_files(self):
        bulk = (
            "preamble ignored\n"
            "＃0화\n\nfirst\n\n"
            "2화\n\nsecond\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dump = root / "bulk.txt"
            dump.write_text(bulk, encoding="utf-8")
            source_dir = root / "source"
            chapters = split_bulk(dump, source_dir)
            self.assertEqual(chapters, [0, 2])
            self.assertEqual(extract_chapter(0, source_dir), "＃0화\n\nfirst\n")
            self.assertEqual(extract_chapter(2, source_dir), "2화\n\nsecond\n")
            self.assertEqual(source_chapters(source_dir), [0, 2])


if __name__ == "__main__":
    unittest.main()
