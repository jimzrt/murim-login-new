#!/usr/bin/env python3
"""Print one chapter from the Murim Login Korean source."""

import re
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "original 1-1104.txt"
MARKER = re.compile(r"^\s*＃?(\d+)화\s*$")


def source_chapters(source: Path = SOURCE) -> list[int]:
    with source.open(encoding="utf-8") as lines:
        return [
            int(marker.group(1))
            for line in lines
            if (marker := MARKER.match(line))
        ]


def extract_chapter(number: int, source: Path = SOURCE) -> str:
    chapter: list[str] = []
    found = False

    with source.open(encoding="utf-8") as lines:
        for line in lines:
            marker = MARKER.match(line)
            if marker:
                if found:
                    break
                found = int(marker.group(1)) == number
            if found:
                chapter.append(line)

    if not chapter:
        raise ValueError(f"chapter {number} not found in {source.name}")
    return "".join(chapter).rstrip() + "\n"


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {Path(sys.argv[0]).name} CHAPTER_NUMBER", file=sys.stderr)
        return 2
    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError
        sys.stdout.write(extract_chapter(number))
    except ValueError as error:
        print(error or "chapter number must be a non-negative integer", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
