import tempfile
import unittest
from pathlib import Path

from tools.build import COVER, add_navigation, chapter_paths, navigation_html, pandoc_base


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

    def test_html_navigation_links_previous_and_next_chapters(self):
        paths = [Path("0001.md"), Path("0002.md"), Path("0003.md")]
        first = navigation_html(0, paths)
        middle = navigation_html(1, paths)
        last = navigation_html(2, paths)
        self.assertNotIn("Previous", first)
        self.assertIn("Last", first)
        self.assertIn('chapter-0002/index.html', first)
        self.assertIn("Chapter 1 of 3", first)
        self.assertIn('chapter-0001/index.html', middle)
        self.assertIn('chapter-0003/index.html', middle)
        self.assertIn("First", middle)
        self.assertNotIn("Next", last)
        self.assertIn("First", last)

    def test_cover_asset_exists(self):
        self.assertTrue(COVER.is_file())

    def test_html_navigation_is_repeated_at_bottom(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "chapter.html"
            path.write_text("<body><main>Text</main></body>", encoding="utf-8")
            add_navigation(path, 1, [Path("0000.md"), Path("0001.md"), Path("0002.md")])
            document = path.read_text(encoding="utf-8")
            self.assertEqual(document.count('aria-label="Chapter navigation"'), 2)


if __name__ == "__main__":
    unittest.main()
