#!/usr/bin/env python3
"""Cheap deterministic checks for translation artifacts."""

from __future__ import annotations

import re

HANGUL = re.compile(r"[가-힣]")
FOOTNOTE_REF = re.compile(r"\[\^([^\]]+)\](?!:)")
FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)
SYSTEM_RANK_FIELD = re.compile(r"^>\s*\*\*Rank:\*\*", re.MULTILINE)
SKILL_REDISTRIBUTE_OBJECTIVE = re.compile(
    r"\bCheck and Redistribute Skill Window Points complete\b",
    re.IGNORECASE,
)
ARABIC_NUMBER = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*(?!\w)")
SEMANTIC_PROBES = (
    (re.compile(r"끄덕"), re.compile(r"\bnod(?:s|ded|ding)?\b", re.I), "source contains a nod but the translation has no form of 'nod'"),
    (re.compile(r"큰형"), re.compile(r"\beldest (?:older )?brother\b", re.I), "큰형 should preserve eldest-brother specificity"),
    (re.compile(r"생도"), re.compile(r"\bcadets?\b", re.I), "생도 should use the established term 'cadet'"),
    (re.compile(r"삼전보"), re.compile(r"\bThree-Turn Footwork\b", re.I), "삼전보 should use 'Three-Turn Footwork'"),
    (re.compile(r"대물남"), re.compile(r"\bWell-Endowed Man\b", re.I), "대물남 should retain the euphemistic rendering 'Well-Endowed Man'"),
    (re.compile(r"시침\s*뚝\s*떼"), re.compile(r"\b(?:as if nothing|pretend\w*|nothing had happened|act\w* as (?:if|though))\b", re.I), "시침 뚝 떼고 carries an acting-as-if-nothing-happened nuance"),
    (re.compile(r"수더분"), re.compile(r"\b(?:friendly|approachable|mild|unassuming|easygoing|open)\b", re.I), "수더분 describes a mild, approachable, or unassuming impression, not mere plainness"),
)


def finding(code: str, message: str, **details: object) -> dict:
    return {"code": code, "message": message, "details": details}


def run_qa(number: int, source: str, translation: str, glossary: list[tuple[str, str]]) -> dict:
    errors: list[dict] = []
    warnings: list[dict] = []
    first = next((line.strip() for line in translation.splitlines() if line.strip()), "")
    if first != f"# Chapter {number}":
        errors.append(finding("heading", f"first nonblank line must be '# Chapter {number}'"))
    if HANGUL.search(translation):
        errors.append(finding("hangul", "reading copy contains Hangul"))
    if translation.lstrip().startswith("```") or re.match(r"^(Here is|I translated|Translation:)", translation.lstrip(), re.I):
        errors.append(finding("wrapper", "reading copy contains a model wrapper or audit preface"))
    if translation.count("“") != translation.count("”"):
        errors.append(finding("quotes", "curly double quotation marks are unbalanced"))
    source_breaks = source.count("* * *")
    target_breaks = translation.count("* * *")
    if source_breaks != target_breaks:
        errors.append(finding("scene_breaks", "scene-break count differs", source=source_breaks, target=target_breaks))
    refs = set(FOOTNOTE_REF.findall(translation))
    definitions = set(FOOTNOTE_DEF.findall(translation))
    if refs != definitions:
        errors.append(finding("footnotes", "footnote references and definitions differ", missing_definitions=sorted(refs-definitions), unused_definitions=sorted(definitions-refs)))
    ratio = len(translation) / max(1, len(source))
    if ratio < 1.25 or ratio > 3.4:
        errors.append(finding("length_ratio", "translation length is outside the expected safety range", ratio=round(ratio, 3)))
    system_lines = translation.splitlines()
    for index, line in enumerate(system_lines):
        if line.strip() == "> **System**":
            cursor = index + 1
            while cursor < len(system_lines) and (not system_lines[cursor].strip() or system_lines[cursor].lstrip().startswith(">")):
                if "[" in system_lines[cursor] or "]" in system_lines[cursor]:
                    warnings.append(finding("system_brackets", "System window contains square brackets", line=cursor + 1))
                cursor += 1
    for match in SYSTEM_RANK_FIELD.finditer(translation):
        errors.append(finding(
            "system_grade",
            "System UI uses Rank; use Grade for the 등급 field",
            line=translation.count("\n", 0, match.start()) + 1,
        ))
    for match in SKILL_REDISTRIBUTE_OBJECTIVE.finditer(translation):
        errors.append(finding(
            "quest_terminology",
            "Skill Window points are unassigned here; use Distribute, not Redistribute",
            line=translation.count("\n", 0, match.start()) + 1,
        ))
    source_numbers = set(ARABIC_NUMBER.findall(source))
    target_numbers = set(ARABIC_NUMBER.findall(translation))
    missing_numbers = sorted(source_numbers - target_numbers)
    if missing_numbers:
        warnings.append(finding("numbers", "Arabic numerals from the source are absent", values=missing_numbers))
    for source_pattern, target_pattern, message in SEMANTIC_PROBES:
        if source_pattern.search(source) and not target_pattern.search(translation):
            warnings.append(finding("semantic_probe", message))
    if "전음" in source and "공력" in source and not re.search(r"\b(?:internal energy|qi)\b", translation, re.I):
        warnings.append(finding("mechanism", "source explains Sound Transmission through internal energy, but that mechanism is absent"))
    try:
        from tools.names import novel_romanizations, preferred_english_present, preferred_english_terms
    except ModuleNotFoundError:
        from names import novel_romanizations, preferred_english_present, preferred_english_terms
    for korean, english in glossary:
        terms = preferred_english_terms(english)
        if korean in source and terms and not preferred_english_present(translation, english):
            warnings.append(finding(
                "terminology",
                "matched preferred term is absent",
                korean=korean,
                preferred=" / ".join(terms),
            ))
    for item in novel_romanizations(source, translation):
        warnings.append(finding(
            "novel_name",
            "source term was romanized without a ledger entry; use the established English or footnote the first use",
            korean=item["korean"],
            romanization=item["romanization"],
        ))
    source_paragraphs = len([part for part in re.split(r"\n\s*\n", source) if part.strip()])
    target_paragraphs = len([part for part in re.split(r"\n\s*\n", translation) if part.strip()])
    paragraph_ratio = target_paragraphs / max(1, source_paragraphs)
    if paragraph_ratio < 0.55 or paragraph_ratio > 1.8:
        warnings.append(finding("paragraph_coverage", "paragraph-count ratio is unusual", source=source_paragraphs, target=target_paragraphs, ratio=round(paragraph_ratio, 3)))
    return {
        "version": 1,
        "chapter": number,
        "passed": not errors,
        "metrics": {
            "source_characters": len(source),
            "translation_characters": len(translation),
            "length_ratio": round(ratio, 3),
            "source_paragraphs": source_paragraphs,
            "translation_paragraphs": target_paragraphs,
        },
        "errors": errors,
        "warnings": warnings,
    }
