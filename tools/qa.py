#!/usr/bin/env python3
"""Cheap deterministic checks for translation artifacts."""

from __future__ import annotations

import re

HANGUL = re.compile(r"[가-힣]")
FOOTNOTE_REF = re.compile(r"\[\^([^\]]+)\](?!:)")
FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)
ARABIC_NUMBER = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*(?!\w)")


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
    source_numbers = set(ARABIC_NUMBER.findall(source))
    target_numbers = set(ARABIC_NUMBER.findall(translation))
    missing_numbers = sorted(source_numbers - target_numbers)
    if missing_numbers:
        warnings.append(finding("numbers", "Arabic numerals from the source are absent", values=missing_numbers))
    for korean, english in glossary:
        plain = re.sub(r"[*_`]", "", english).strip()
        if korean in source and plain and plain.casefold() not in translation.casefold():
            warnings.append(finding("terminology", "matched preferred term is absent", korean=korean, preferred=plain))
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
