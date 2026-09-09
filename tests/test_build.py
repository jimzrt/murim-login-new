import tempfile
import unittest
from pathlib import Path

from tools.build import COVER, READER, chapter_paths, pandoc_base


class BuildToolTest(unittest.TestCase):
    def test_chapter_selection_is_numeric_and_ordered(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp)
            for number in (3, 1, 12):
                (source / f"{number:04d}.md").write_text("# Chapter\n", encoding="utf-8")
            selected = chapter_paths(source, [12, 1])
            self.assertEqual([path.stem for path in selected], ["0001", "0012"])

    def test_default_selection_ignores_non_chapter_markdown(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp)
            (source / "0000.md").write_text("# Chapter\n", encoding="utf-8")
            (source / "notes.md").write_text("# Notes\n", encoding="utf-8")
            self.assertEqual([path.stem for path in chapter_paths(source, None)], ["0000"])

    def test_combined_exports_use_file_scope_for_chapter_local_notes(self):
        command = pandoc_base([Path("0001.md"), Path("0002.md")], "epub3")
        self.assertIn("--file-scope", command)

    def test_cover_asset_exists(self):
        self.assertTrue(COVER.is_file())

    def test_html_reader_scaffold_exists(self):
        self.assertTrue((READER / "package.json").is_file())
        self.assertTrue((READER / "astro.config.ts").is_file())
        self.assertTrue((READER / "src" / "pages" / "chapter" / "[id].astro").is_file())


if __name__ == "__main__":
    unittest.main()
