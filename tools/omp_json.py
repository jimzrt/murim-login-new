#!/usr/bin/env python3
"""Strict parsing and aggregation for OMP JSON event streams."""

from __future__ import annotations

import json
import numbers
import subprocess
import time
from pathlib import Path
from typing import Callable, Iterable


class OmpJsonError(ValueError):
    """Raised when OMP's event stream cannot provide exact usage."""


TOKEN_FIELDS = {
    "input": "input_tokens",
    "output": "output_tokens",
    "cacheRead": "cache_read_tokens",
    "cacheWrite": "cache_write_tokens",
    "totalTokens": "total_tokens",
}


def _number(value: object, label: str) -> int | float:
    if not isinstance(value, numbers.Real) or isinstance(value, bool) or value < 0:
        raise OmpJsonError(f"OMP usage field {label} is missing or invalid")
    return value


def _message_text(message: dict) -> str:
    content = message.get("content")
    if not isinstance(content, list):
        return ""
    return "".join(
        block.get("text", "")
        for block in content
        if isinstance(block, dict) and block.get("type") == "text" and isinstance(block.get("text"), str)
    )


def _usage_record(message: dict) -> dict:
    provider = message.get("provider")
    model = message.get("model")
    usage = message.get("usage")
    if not isinstance(provider, str) or not provider or not isinstance(model, str) or not model:
        raise OmpJsonError("OMP assistant message is missing its actual provider or model")
    if not isinstance(usage, dict):
        raise OmpJsonError(f"OMP did not report usage for {provider}/{model}")
    record = {
        "provider": provider,
        "model": model,
        **{target: _number(usage.get(source), source) for source, target in TOKEN_FIELDS.items()},
    }
    reasoning = usage.get("reasoning", usage.get("reasoningTokens"))
    if reasoning is not None:
        record["reasoning_tokens"] = _number(reasoning, "reasoning")
    cost = usage.get("cost")
    if isinstance(cost, dict) and cost.get("total") is not None:
        record["cost_usd"] = _number(cost["total"], "cost.total")
    return record


class EventCapture:
    """Collect final text and exact provider usage from JSONL events."""

    def __init__(self, requested_model: str):
        self.requested_model = requested_model
        self.records: list[dict] = []
        self.final_text = ""

    def consume(self, event: dict) -> None:
        if event.get("type") != "message_end":
            return
        message = event.get("message")
        if not isinstance(message, dict) or message.get("role") != "assistant":
            return
        record = _usage_record(message)
        self.records.append(record)
        text = _message_text(message)
        if message.get("stopReason") != "error" and text.strip():
            self.final_text = text

    def finish(self, *, require_output: bool = True) -> tuple[str, dict]:
        if not self.records:
            raise OmpJsonError("OMP JSON stream contained no assistant usage records")
        if require_output and not self.final_text.strip():
            raise OmpJsonError("OMP JSON stream contained no final assistant text")
        models: dict[str, dict] = {}
        for record in self.records:
            key = f"{record['provider']}/{record['model']}"
            aggregate = models.setdefault(key, {
                "provider": record["provider"],
                "model": record["model"],
                "requests": 0,
                "input_tokens": 0,
                "output_tokens": 0,
                "cache_read_tokens": 0,
                "cache_write_tokens": 0,
                "total_tokens": 0,
                "reasoning_tokens": 0,
                "cost_usd": 0,
                "cost_reported": True,
                "reasoning_reported": True,
            })
            aggregate["requests"] += 1
            for field in (
                "input_tokens", "output_tokens", "cache_read_tokens",
                "cache_write_tokens", "total_tokens",
            ):
                aggregate[field] += record[field]
            if "reasoning_tokens" in record:
                aggregate["reasoning_tokens"] += record["reasoning_tokens"]
            else:
                aggregate["reasoning_reported"] = False
            if "cost_usd" in record:
                aggregate["cost_usd"] += record["cost_usd"]
            else:
                aggregate["cost_reported"] = False
        totals = {
            "requests": len(self.records),
            "input_tokens": sum(item["input_tokens"] for item in self.records),
            "output_tokens": sum(item["output_tokens"] for item in self.records),
            "cache_read_tokens": sum(item["cache_read_tokens"] for item in self.records),
            "cache_write_tokens": sum(item["cache_write_tokens"] for item in self.records),
            "total_tokens": sum(item["total_tokens"] for item in self.records),
        }
        if all("reasoning_tokens" in item for item in self.records):
            totals["reasoning_tokens"] = sum(item["reasoning_tokens"] for item in self.records)
        if all("cost_usd" in item for item in self.records):
            totals["cost_usd"] = sum(item["cost_usd"] for item in self.records)
        for aggregate in models.values():
            if not aggregate.pop("cost_reported"):
                aggregate.pop("cost_usd")
            if not aggregate.pop("reasoning_reported"):
                aggregate.pop("reasoning_tokens")
        metrics = {
            "exact": True,
            "usage_source": "omp_provider_reported",
            "requested_model": self.requested_model,
            **totals,
            "models": models,
        }
        return self.final_text.strip() + ("\n" if self.final_text.strip() else ""), metrics


def parse_json_lines(lines: Iterable[str], requested_model: str, on_event: Callable[[dict], None] | None = None) -> tuple[str, dict]:
    capture = EventCapture(requested_model)
    for line_number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as error:
            raise OmpJsonError(f"invalid OMP JSON event on line {line_number}: {error}") from None
        if not isinstance(event, dict):
            raise OmpJsonError(f"OMP JSON event on line {line_number} is not an object")
        capture.consume(event)
        if on_event:
            on_event(event)
    return capture.finish()


def run_json_command(
    command: list[str],
    *,
    cwd: Path,
    requested_model: str,
    timeout: int,
) -> tuple[str, dict]:
    started = time.monotonic()
    try:
        result = subprocess.run(command, cwd=cwd, text=True, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired as error:
        raise OmpJsonError(f"model call timed out: {error}") from None
    if result.returncode:
        raise OmpJsonError(result.stderr.strip() or result.stdout.strip() or "model call failed")
    output, metrics = parse_json_lines(result.stdout.splitlines(), requested_model)
    metrics.update({
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "output_bytes": len(output.encode("utf-8")),
    })
    return output, metrics
