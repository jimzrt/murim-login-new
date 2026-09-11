import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import names


class NamesLedgerTest(unittest.TestCase):
    def test_slash_separated_english_cells_are_alternatives(self):
        self.assertEqual(names.preferred_english_terms("**aura** / **momentum**"), ["aura", "momentum"])
        self.assertEqual(names.preferred_english_terms("**Heavenly Axe**"), ["Heavenly Axe"])
        self.assertTrue(names.preferred_english_present("Their momentum returned.", "**aura** / **momentum**"))
        self.assertTrue(names.preferred_english_present("An aura pressed down.", "**aura** / **momentum**"))
        self.assertFalse(names.preferred_english_present("The pressure returned.", "**aura** / **momentum**"))
        self.assertNotIn("I", names.preferred_english_terms("**I / this lord** only when deliberately grandiose"))

    def test_romanizes_cheonryeokbu_and_cheongwanil(self):
        self.assertEqual(names.romanize("천력부"), "cheonryeokbu")
        self.assertEqual(names.romanize("천관일"), "cheongwanil")
        self.assertEqual(len(names.JONGSEONG), 28)
        self.assertEqual(names.romanize("놓다"), "notda")

    def test_source_match_injects_alias_and_form(self):
        mapping = {item["korean"]: names.strip_english(item["english"]) for item in names.ledger_for_source("천력부 장삼 천관일")}
        self.assertEqual(mapping["천력부"], "Heavenly Axe")
        self.assertEqual(mapping["장삼"], "Jang Sam")
        self.assertEqual(mapping["천관일"], "Sky-Piercing Strike")

    def test_profile_aliases_join_the_ledger(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "characters").mkdir()
            (root / "characters" / "Jang Sam.md").write_text(
                "# Jang Sam (장삼)\n\n- **Aliases:** Heavenly Axe (천력부)\n",
                encoding="utf-8",
            )
            (root / "docs").mkdir()
            (root / "compendium.md").write_text("", encoding="utf-8")
            with patch.object(names, "ROOT", root):
                mapping = {item["korean"]: names.strip_english(item["english"]) for item in names.load_names_ledger()}
                attached = names.profile_koreans((root / "characters" / "Jang Sam.md").read_text(encoding="utf-8"))
        self.assertEqual(mapping["장삼"], "Jang Sam")
        self.assertEqual(mapping["천력부"], "Heavenly Axe")
        self.assertEqual(attached, ["장삼", "천력부"])

    def test_names_file_overrides_compendium(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "characters").mkdir()
            (root / "compendium.md").write_text("| 천력부 | **Cheonryeokbu** |\n", encoding="utf-8")
            (root / "docs" / "NAMES.md").write_text("| 천력부 | **Heavenly Axe** |\n", encoding="utf-8")
            with patch.object(names, "ROOT", root):
                mapping = {item["korean"]: names.strip_english(item["english"]) for item in names.load_names_ledger()}
        self.assertEqual(mapping["천력부"], "Heavenly Axe")

    def test_novel_romanization_flags_unlisted_source_term(self):
        hits = names.novel_romanizations(
            "가나다라마가 나타났다.",
            "Ganadarama appeared.",
            ledger=[],
        )
        self.assertEqual(hits[0]["korean"], "가나다라마")
        self.assertEqual(hits[0]["romanization"], "ganadarama")

    def test_listed_term_is_not_a_novel_romanization(self):
        hits = names.novel_romanizations(
            "천력부가 나타났다.",
            "Cheonryeokbu appeared.",
            ledger=[{"korean": "천력부", "english": "**Heavenly Axe**"}],
        )
        self.assertEqual(hits, [])

    def test_romanization_is_token_not_substring(self):
        hits = names.novel_romanizations(
            "천배로 갚으리라.",
            "Lee Cheonbaek will repay it a thousand times.",
            ledger=[],
        )
        self.assertEqual(hits, [])

    def test_hyphenated_romanization_is_detected(self):
        hits = names.novel_romanizations(
            "천관일",
            "He used Cheongwan-il.",
            ledger=[],
        )
        self.assertEqual(hits[0]["korean"], "천관일")

    def test_spaced_romanization_is_detected(self):
        hits = names.novel_romanizations("천력부", "He mentioned Cheon Ryeok Bu.", ledger=[])
        self.assertEqual(hits[0]["korean"], "천력부")

    def test_lowercase_common_word_is_not_reported_as_a_name(self):
        self.assertEqual(
            names.novel_romanizations("파노라마가 보였다.", "A panorama appeared.", ledger=[]),
            [],
        )

    def test_laughter_is_not_reported_as_a_name(self):
        self.assertEqual(
            names.novel_romanizations("하하하.", "Hahaha.", ledger=[]),
            [],
        )
