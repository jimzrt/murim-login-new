#!/usr/bin/env python3
"""Parse and validate structured model responses."""

from __future__ import annotations

import json
import re

SEVERITIES = {"critical", "major", "minor"}
DISPOSITIONS = {"applied", "rejected", "unresolved"}


def parse_json_object(raw: str) -> dict:
    text = raw.strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    if fenced:
        text = fenced.group(1)
    try:
        value = json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError(f"model did not return valid JSON: {error}") from None
    if not isinstance(value, dict):
        raise ValueError("model response must be one JSON object")
    return value


def validate_review(value: dict) -> dict:
    findings = value.get("findings")
    if not isinstance(findings, list):
        raise ValueError("review response requires a findings array")
    normalized: list[dict] = []
    seen: set[str] = set()
    required = ("id", "severity", "source", "current", "defect", "correction", "rationale")
    for position, finding in enumerate(findings, 1):
        if not isinstance(finding, dict):
            raise ValueError(f"finding {position} must be an object")
        for key in required:
            if not isinstance(finding.get(key), str) or not finding[key].strip():
                raise ValueError(f"finding {position} requires nonempty {key}")
        identifier = finding["id"].strip()
        if identifier in seen:
            raise ValueError(f"duplicate finding id: {identifier}")
        seen.add(identifier)
        severity = finding["severity"].lower().strip()
        if severity not in SEVERITIES:
            raise ValueError(f"invalid severity for {identifier}: {severity}")
        confidence = finding.get("confidence")
        if not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not 0 <= confidence <= 1:
            raise ValueError(f"confidence for {identifier} must be between 0 and 1")
        normalized.append({
            **finding,
            "id": identifier,
            "severity": severity,
            "confidence": float(confidence),
        })
    summary = value.get("summary", "No actionable findings" if not normalized else "")
    if not isinstance(summary, str):
        raise ValueError("review summary must be a string")
    return {"version": 1, "summary": summary.strip(), "findings": normalized}


def validate_dispositions(dispositions: object, review: dict) -> list[dict]:
    if not isinstance(dispositions, list):
        raise ValueError("response requires a dispositions array")
    expected = {finding["id"] for finding in review["findings"]}
    normalized: list[dict] = []
    seen: set[str] = set()
    for item in dispositions:
        if not isinstance(item, dict):
            raise ValueError("every disposition must be an object")
        identifier = item.get("finding_id")
        status = item.get("status")
        reason = item.get("reason")
        if identifier not in expected or identifier in seen:
            raise ValueError(f"unknown or duplicate disposition id: {identifier}")
        if status not in DISPOSITIONS:
            raise ValueError(f"invalid disposition for {identifier}: {status}")
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f"disposition {identifier} requires a reason")
        seen.add(identifier)
        normalized.append({"finding_id": identifier, "status": status, "reason": reason.strip()})
    missing = expected.difference(seen)
    if missing:
        raise ValueError("missing dispositions: " + ", ".join(sorted(missing)))
    return normalized


def validate_revision(value: dict, review: dict) -> dict:
    translation = value.get("translation")
    if not isinstance(translation, str) or not translation.strip():
        raise ValueError("revision response requires a nonempty translation")
    normalized = validate_dispositions(value.get("dispositions"), review)
    return {"version": 1, "translation": translation.strip() + "\n", "dispositions": normalized}


def parse_revision_response(raw: str, review: dict) -> dict:
    """Parse a low-overhead Markdown + JSON envelope, with JSON fallback."""
    text = raw.strip()
    if text.startswith("{") or text.startswith("```json"):
        return validate_revision(parse_json_object(text), review)
    translation_marker = "<<<TRANSLATION>>>"
    disposition_marker = "<<<DISPOSITIONS>>>"
    if not text.startswith(translation_marker) or disposition_marker not in text:
        raise ValueError("revision response is missing required envelope markers")
    translation, separator, disposition_text = text[len(translation_marker):].partition(disposition_marker)
    if not separator or not translation.strip():
        raise ValueError("revision response has an empty translation or disposition section")
    disposition_object = parse_json_object(disposition_text)
    normalized = validate_dispositions(disposition_object.get("dispositions"), review)
    return {"version": 1, "translation": translation.strip() + "\n", "dispositions": normalized}


def blocking_dispositions(review: dict, revision: dict) -> list[str]:
    severities = {finding["id"]: finding["severity"] for finding in review["findings"]}
    return [
        item["finding_id"]
        for item in revision["dispositions"]
        if item["status"] == "unresolved" and severities[item["finding_id"]] in {"critical", "major"}
    ]


def review_markdown(review: dict) -> str:
    if not review["findings"]:
        return "# Review\n\nNo actionable findings.\n"
    sections = ["# Review", "", review["summary"]]
    for finding in review["findings"]:
        sections.extend([
            "", f"## {finding['id']} — {finding['severity'].title()}", "",
            f"- **Confidence:** {finding['confidence']:.2f}",
            f"- **Source:** {finding['source']}",
            f"- **Current:** {finding['current']}",
            f"- **Defect:** {finding['defect']}",
            f"- **Correction:** {finding['correction']}",
            f"- **Rationale:** {finding['rationale']}",
        ])
    return "\n".join(sections).rstrip() + "\n"
