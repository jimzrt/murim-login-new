#!/usr/bin/env python3
"""Durable Korean→English names ledger and Revised Romanization helpers."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KOREAN = re.compile(r"[가-힣]{2,}")
TABLE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|.*$")
HEADING = re.compile(r"^#\s+(.+?)\s*\(([가-힣]{2,})\)\s*$")
ALIAS_LINE = re.compile(r"^- \*\*Aliases:\*\*\s*(.+)$")
ALIAS_PAIR = re.compile(r"([^;,(]+?)\s*\(([가-힣]{2,})\)")

CHOSEONG = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "", "j", "jj", "ch", "k", "t", "p", "h"]
JUNGSEONG = [
    "a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "oe", "yo",
    "u", "wo", "we", "wi", "yu", "eu", "ui", "i",
]
JONGSEONG = [
    "", "k", "k", "k", "n", "n", "n", "t", "l", "l", "l", "l", "l", "l", "l", "l",
    "m", "p", "p", "t", "t", "ng", "t", "t", "k", "t", "p", "t",
]


def strip_english(value: str) -> str:
    return re.sub(r"[*_`]", "", value).strip()


def preferred_english_terms(english: str) -> list[str]:
    """Preferred glossary renderings; slash-separated cells are alternatives."""
    parts = [part.strip() for part in strip_english(english).split(" / ") if part.strip()]
    if len(parts) <= 1:
        return parts
    substantial = [part for part in parts if len(part) >= 3]
    return substantial or parts


def preferred_english_present(text: str, english: str) -> bool:
    folded = text.casefold()
    return any(term.casefold() in folded for term in preferred_english_terms(english))


def romanize_syllable(char: str) -> str:
    code = ord(char) - 0xAC00
    if not 0 <= code <= 11171:
        return char
    initial, rest = divmod(code, 21 * 28)
    medial, final = divmod(rest, 28)
    return CHOSEONG[initial] + JUNGSEONG[medial] + JONGSEONG[final]


def romanize(text: str) -> str:
    return "".join(romanize_syllable(char) if "가" <= char <= "힣" else char for char in text)


def profile_koreans(body: str) -> list[str]:
    names: list[str] = []
    for line in body.splitlines():
        heading = HEADING.match(line)
        if heading:
            names.append(heading.group(2))
            continue
        aliases = ALIAS_LINE.match(line)
        if aliases:
            names.extend(match.group(2) for match in ALIAS_PAIR.finditer(aliases.group(1)))
    return names


def _row(korean: str, english: str, note: str = "") -> dict:
    plain = strip_english(english)
    display = english.strip() if english.strip().startswith("**") else f"**{plain}**"
    suffix = f" | {note}" if note else ""
    return {"korean": korean, "english": display, "row": f"| {korean} | {display}{suffix} |"}


def _add(index: dict[str, dict], korean: str, english: str, *, overwrite: bool = False) -> None:
    korean = korean.strip()
    if not KOREAN.fullmatch(korean):
        return
    if korean in index and not overwrite:
        return
    index[korean] = _row(korean, english)


def _load_table(path: Path, index: dict[str, dict], *, overwrite: bool) -> None:
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        match = TABLE_ROW.match(line)
        if not match:
            continue
        korean = match.group(1).strip()
        english = match.group(2).strip()
        if not KOREAN.fullmatch(korean):
            continue
        if korean in index and not overwrite:
            continue
        index[korean] = {"korean": korean, "english": english, "row": line}


def _load_profiles(index: dict[str, dict]) -> None:
    directory = ROOT / "characters"
    if not directory.is_dir():
        return
    for path in sorted(directory.glob("*.md")):
        body = path.read_text(encoding="utf-8")
        heading_english = path.stem
        for line in body.splitlines():
            heading = HEADING.match(line)
            if heading:
                heading_english = heading.group(1).strip()
                _add(index, heading.group(2), heading_english)
                continue
            aliases = ALIAS_LINE.match(line)
            if not aliases:
                continue
            text = aliases.group(1).strip()
            if text.casefold() in {"none revealed", "name not yet revealed"}:
                continue
            for match in ALIAS_PAIR.finditer(text):
                _add(index, match.group(2), match.group(1).strip())


def load_names_ledger() -> list[dict]:
    index: dict[str, dict] = {}
    _load_table(ROOT / "compendium.md", index, overwrite=False)
    _load_profiles(index)
    _load_table(ROOT / "docs" / "NAMES.md", index, overwrite=True)
    return list(index.values())


def ledger_for_source(source: str) -> list[dict]:
    entries: list[dict] = []
    seen: set[str] = set()
    for item in load_names_ledger():
        korean = item["korean"]
        if korean in source and korean not in seen:
            entries.append(item)
            seen.add(korean)
    return entries


JOSA = (
    "에게서", "으로부터", "에서", "으로", "에게", "부터", "까지", "처럼", "보다",
    "이나", "이랑", "이란", "이", "가", "을", "를", "은", "는", "의", "도", "만", "과", "와", "로",
)
IGNORED_KOREAN = {"하하하"}


def _cores(token: str) -> list[str]:
    cores = [token]
    for josa in JOSA:
        if token.endswith(josa) and len(token) - len(josa) >= 2:
            cores.append(token[: -len(josa)])
            break
    return cores


def romanization_variants(korean: str) -> set[str]:
    syllables = [romanize_syllable(char) for char in korean if "가" <= char <= "힣"]
    joined = "".join(syllables).casefold()
    variants = {joined}
    if len(syllables) >= 2:
        variants.add("-".join(syllables).casefold())
        variants.add(" ".join(syllables).casefold())
    return {item for item in variants if item}


TOKEN = re.compile(r"[A-Za-z]+(?:-[A-Za-z]+)*")


def _english_tokens(translation: str) -> set[str]:
    tokens: set[str] = set()
    for raw in TOKEN.findall(translation):
        if not raw[0].isupper():
            continue
        folded = raw.casefold()
        tokens.add(folded)
        tokens.add(folded.replace("-", ""))
    return tokens


def _romanization_sequences(translation: str) -> set[str]:
    words = [word.casefold() for word in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", translation)]
    return {" ".join(words[index:index + size]) for size in (2, 3) for index in range(len(words) - size + 1)}


def _romanization_hit(korean: str, tokens: set[str]) -> bool:
    for item in romanization_variants(korean):
        letters = re.sub(r"[^a-z]", "", item)
        if len(letters) < 6:
            continue
        if item in tokens or item.replace("-", "").replace(" ", "") in tokens:
            return True
    return False


def novel_romanizations(source: str, translation: str, ledger: list[dict] | None = None) -> list[dict]:
    known = {item["korean"] for item in (ledger if ledger is not None else load_names_ledger())}
    tokens = _english_tokens(translation)
    sequences = _romanization_sequences(translation)
    found: list[dict] = []
    seen: set[str] = set()
    for korean in KOREAN.findall(source):
        if korean in IGNORED_KOREAN:
            continue
        if any(korean == term or korean.startswith(term) for term in known):
            continue
        for core in _cores(korean):
            if core in seen or core in known:
                continue
            variants = romanization_variants(core)
            if _romanization_hit(core, tokens) or any(
                item in sequences and len(re.sub(r"[^a-z]", "", item)) >= 6
                for item in variants
                if " " in item
            ):
                found.append({"korean": core, "romanization": romanize(core)})
                seen.add(core)
                break
    return found
