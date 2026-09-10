#!/usr/bin/env python3
"""Read one Korean source chapter, or split a bulk dump into per-chapter files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "source"
BULK_SOURCE = ROOT / "original 1-1104.txt"
CHAPTER_FILE = re.compile(r"^(\d{4})\.txt$")
MARKER = re.compile(r"^\s*＃?(\d+)화\s*$")


def chapter_path(number: int, source_dir: Path = SOURCE_DIR) -> Path:
    if number < 0:
        raise ValueError("chapter number must be a non-negative integer")
    return source_dir / f"{number:04d}.txt"


def extract_chapter(number: int, source_dir: Path = SOURCE_DIR) -> str:
    path = chapter_path(number, source_dir)
    if not path.is_file():
        raise ValueError(f"chapter {number} not found in {path}")
    return path.read_text(encoding="utf-8").rstrip() + "\n"


def source_chapters(source_dir: Path = SOURCE_DIR) -> list[int]:
    if not source_dir.is_dir():
        return []
    return sorted(
        int(match.group(1))
        for path in source_dir.iterdir()
        if (match := CHAPTER_FILE.fullmatch(path.name))
    )


def split_bulk(source: Path = BULK_SOURCE, source_dir: Path = SOURCE_DIR) -> list[int]:
    if not source.is_file():
        raise ValueError(f"bulk source not found: {source}")
    source_dir.mkdir(parents=True, exist_ok=True)
    written: dict[int, None] = {}
    current_number: int | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_number, current_lines
        if current_number is None:
            return
        if current_number in written:
            raise ValueError(f"duplicate chapter {current_number} in {source.name}")
        chapter_path(current_number, source_dir).write_text(
            "".join(current_lines).rstrip() + "\n",
            encoding="utf-8",
        )
        written[current_number] = None
        current_number = None
        current_lines = []

    with source.open(encoding="utf-8") as lines:
        for line in lines:
            marker = MARKER.match(line)
            if marker:
                flush()
                current_number = int(marker.group(1))
            if current_number is not None:
                current_lines.append(line)
        flush()

    if not written:
        raise ValueError(f"no chapters found in {source.name}")
    return sorted(written)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter", nargs="?", type=int, help="print one prepared chapter")
    parser.add_argument(
        "--split",
        nargs="?",
        const=str(BULK_SOURCE),
        metavar="BULK_FILE",
        help="split a bulk dump into source/NNNN.txt (default: original 1-1104.txt)",
    )
    args = parser.parse_args()
    try:
        if args.split is not None and args.chapter is not None:
            raise ValueError("pass either a chapter number or --split, not both")
        if args.split is not None:
            chapters = split_bulk(Path(args.split))
            print(f"wrote {len(chapters)} chapters ({chapters[0]}-{chapters[-1]}) to {SOURCE_DIR}", file=sys.stderr)
            return 0
        if args.chapter is None:
            parser.print_usage(sys.stderr)
            return 2
        if args.chapter < 0:
            raise ValueError("chapter number must be a non-negative integer")
        sys.stdout.write(extract_chapter(args.chapter))
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
