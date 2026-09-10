import tempfile
import unittest
from pathlib import Path

from tools.build import BOOK_TYP, COVER, READER, TYPST_TEMPLATE, chapter_paths, pandoc_base


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

    def test_pdf_system_ornaments_exist(self):
        self.assertTrue((READER / "src" / "ornaments" / "corner.svg").is_file())
        self.assertTrue((READER / "src" / "ornaments" / "dragon.svg").is_file())
        lua = (READER.parent / "tools" / "system-window.lua").read_text(encoding="utf-8")
        self.assertIn("ornament(\"corner.svg\")", lua)
        self.assertIn("ornament(\"dragon.svg\")", lua)
        self.assertIn("murim-plaque", lua)
        self.assertTrue(BOOK_TYP.is_file())
        book = BOOK_TYP.read_text(encoding="utf-8")
        self.assertIn("#let murim-plaque", book)
        self.assertIn("Noto Sans Mono", book)
        self.assertIn("text(style: \"italic\"", book)
        self.assertIn("pagebreak(weak: true)", book)
        self.assertIn('paper: "a4"', book)
        self.assertIn("pad(x: 8%", book)
        self.assertTrue(TYPST_TEMPLATE.is_file())
        template = TYPST_TEMPLATE.read_text(encoding="utf-8")
        self.assertNotIn("  title: [$title$],", template)
        self.assertIn("#set document(title: [$title$])", template)
        self.assertIn("title: [Contents]", template)


if __name__ == "__main__":
    unittest.main()
