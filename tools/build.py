#!/usr/bin/env python3
"""Build HTML, PDF, and EPUB editions from translation Markdown files.

Pandoc parses Markdown for every format. HTML is emitted as a navigable site
with one chapter per subdirectory; PDF is generated directly from Markdown
through Typst, and EPUB uses Pandoc's file-scope mode.
"""

from __future__ import annotations

import argparse
import html
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "translations"
DEFAULT_OUTPUT = ROOT / "build"
FILTER = ROOT / "tools" / "system-window.lua"
STYLESHEET = ROOT / "tools" / "book.css"
COVER = ROOT / "cover.jpg"
TITLE = "Murim Login"


def chapter_paths(source: Path, selected: list[int] | None) -> list[Path]:
    paths = sorted(source.glob("[0-9][0-9][0-9][0-9].md"))
    if selected is None:
        return paths
    wanted = {f"{number:04d}" for number in selected}
    return [path for path in paths if path.stem in wanted]


def require_binary(name: str, install_hint: str) -> str:
    binary = shutil.which(name)
    if binary is None:
        raise RuntimeError(f"{name} is required. Install it with: {install_hint}")
    return binary


def pandoc_base(paths: list[Path], output_format: str) -> list[str]:
    pandoc = require_binary("pandoc", "sudo pacman -S pandoc-cli")
    return [
        pandoc,
        *(str(path.resolve()) for path in paths),
        "--from=markdown",
        f"--to={output_format}",
        f"--lua-filter={FILTER}",
        "--file-scope",
        "--standalone",
        "--metadata=lang=en",
    ]


def run_pandoc(
    paths: list[Path],
    output: Path,
    output_format: str,
    css: Path | None = None,
    *,
    css_ref: str | None = None,
    epub_cover: Path | None = None,
    title: str = TITLE,
    pdf: bool = False,
) -> None:
    command = pandoc_base(paths, output_format)
    command.append(f"--metadata=title={title}")
    if css is not None:
        command.append(f"--css={css_ref or css.name}")
    if epub_cover is not None:
        command.append(f"--epub-cover-image={epub_cover.resolve()}")
    if pdf:
        command.extend(
            [
                "--pdf-engine=typst",
                "--variable=papersize:a5",
                "--variable=margin-left:18mm",
                "--variable=margin-right:16mm",
                "--variable=margin-top:18mm",
                "--variable=margin-bottom:20mm",
            ]
        )
    output = output.resolve()
    command.extend(["--output", str(output)])
    subprocess.run(command, cwd=output.parent, check=True)


def build_html(paths: list[Path], output: Path, css: Path) -> list[Path]:
    html_root = output / "html"
    html_root.mkdir(parents=True, exist_ok=True)
    result: list[Path] = []
    for index, path in enumerate(paths):
        chapter_dir = html_root / f"chapter-{path.stem}"
        chapter_dir.mkdir(parents=True, exist_ok=True)
        target = chapter_dir / "index.html"
        run_pandoc(
            [path],
            target,
            "html5",
            css,
            css_ref="../../book.css",
            title=f"{TITLE} — Chapter {int(path.stem)}",
        )
        add_navigation(target, index, paths)
        result.append(target)
    write_html_index(html_root, paths)
    return result


def navigation_html(index: int, paths: list[Path]) -> str:
    links = []
    if index:
        links.append(f'<a href="../chapter-{paths[0].stem}/index.html">First</a>')
        links.append(f'<a href="../chapter-{paths[index - 1].stem}/index.html">Previous</a>')
    links.append('<a href="../index.html">Contents</a>')
    if index + 1 < len(paths):
        links.append(f'<a href="../chapter-{paths[index + 1].stem}/index.html">Next</a>')
        links.append(f'<a href="../chapter-{paths[-1].stem}/index.html">Last</a>')
    position = f'<span class="chapter-position">Chapter {index + 1} of {len(paths)}</span>'
    return '<nav class="chapter-nav" aria-label="Chapter navigation">' + " · ".join(links) + " " + position + "</nav>"


def add_navigation(path: Path, index: int, paths: list[Path]) -> None:
    document = path.read_text(encoding="utf-8")
    marker = "<body>"
    if marker not in document:
        raise ValueError(f"Pandoc HTML has no body tag: {path}")
    navigation = navigation_html(index, paths)
    document = document.replace(marker, marker + "\n" + navigation, 1)
    if "</body>" not in document:
        raise ValueError(f"Pandoc HTML has no closing body tag: {path}")
    document = document.replace("</body>", navigation + "\n</body>", 1)
    path.write_text(document, encoding="utf-8")


def write_html_index(html_root: Path, paths: list[Path]) -> Path:
    items = "\n".join(
        f'<li><a href="chapter-{path.stem}/index.html">Chapter {int(path.stem)}</a></li>'
        for path in paths
    )
    index = html_root / "index.html"
    index.write_text(
        f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(TITLE)} — Contents</title>
<link rel="stylesheet" href="../book.css">
</head>
<body>
<main class="book contents">
<img class="cover-image" src="../cover.jpg" alt="Murim Login cover">
<h1>{html.escape(TITLE)}</h1>
<ol>
{items}
</ol>
</main>
</body>
</html>
""",
        encoding="utf-8",
    )
    return index


def write_pdf_cover(output: Path) -> Path:
    cover_markdown = output / ".cover.md"
    image = "cover.jpg"
    cover_markdown.write_text(
        f"""```{{=typst}}
#page(paper: "a5", margin: 0pt)[
  #image("{image}", width: 100%, height: 100%, fit: "cover")
]
#pagebreak()
```
""",
        encoding="utf-8",
    )
    return cover_markdown


def build_pdf(paths: list[Path], output: Path) -> Path:
    target = output / "murim-login.pdf"
    cover_markdown = write_pdf_cover(output)
    try:
        run_pandoc([cover_markdown, *paths], target, "pdf", title=TITLE, pdf=True)
    finally:
        cover_markdown.unlink(missing_ok=True)
    return target


def build_epub(paths: list[Path], output: Path, css: Path) -> Path:
    target = output / "murim-login.epub"
    run_pandoc(paths, target, "epub3", css, epub_cover=output / "cover.jpg", title=TITLE)
    return target


def build(args: argparse.Namespace) -> list[Path]:
    paths = chapter_paths(args.source, args.chapters or None)
    if not paths:
        raise ValueError("no translation files selected")

    args.output.mkdir(parents=True, exist_ok=True)
    css = args.output / "book.css"
    shutil.copyfile(STYLESHEET, css)
    shutil.copyfile(COVER, args.output / "cover.jpg")
    produced: list[Path] = []

    if args.format in {"all", "html"}:
        produced.extend(build_html(paths, args.output, css))
    if args.format in {"all", "pdf"}:
        produced.append(build_pdf(paths, args.output))
    if args.format in {"all", "epub"}:
        produced.append(build_epub(paths, args.output, css))
    return produced


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapters", nargs="*", type=int, help="chapter numbers; default: all translation files")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--format", choices=("all", "html", "pdf", "epub"), default="all")
    args = parser.parse_args(argv)
    try:
        for path in build(args):
            print(path)
    except (OSError, RuntimeError, subprocess.CalledProcessError, ValueError) as error:
        print(f"build failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
