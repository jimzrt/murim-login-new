#!/usr/bin/env python3
"""Build HTML, PDF, and EPUB editions from translation Markdown files.

HTML is an Astro reader in ``reader/``. PDF and EPUB still go through Pandoc:
PDF uses Typst, and EPUB uses Pandoc's file-scope mode with the book stylesheet.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "translations"
DEFAULT_OUTPUT = ROOT / "build"
FILTER = ROOT / "tools" / "system-window.lua"
STYLESHEET = ROOT / "tools" / "book.css"
BOOK_TYP = ROOT / "tools" / "book.typ"
TYPST_TEMPLATE = ROOT / "tools" / "typst-template.typ"
COVER = ROOT / "cover.jpg"
READER = ROOT / "reader"
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
    include_before: list[Path] | None = None,
) -> None:
    command = pandoc_base(paths, output_format)
    command.append(f"--metadata=title={title}")
    if css is not None:
        command.append(f"--css={css_ref or css.name}")
    if epub_cover is not None:
        command.append(f"--epub-cover-image={epub_cover.resolve()}")
    for prelude in include_before or ():
        command.append(f"--include-before-body={prelude.resolve()}")
    if pdf:
        command.extend(
            [
                "--pdf-engine=typst",
                "--pdf-engine-opt=--root=/",
                f"--template={TYPST_TEMPLATE}",
                "--toc",
                "--toc-depth=1",
                "--variable=papersize:a4",
                "--variable=fontsize:11.5pt",
                "--variable=mainfont:Noto Serif",
                "--variable=margin-left:26mm",
                "--variable=margin-right:24mm",
                "--variable=margin-top:26mm",
                "--variable=margin-bottom:24mm",
            ]
        )
    output = output.resolve()
    command.extend(["--output", str(output)])
    subprocess.run(command, cwd=output.parent, check=True)


def ensure_reader_dependencies(npm: str) -> None:
    if not (READER / "node_modules" / "astro").exists():
        subprocess.run([npm, "install"], cwd=READER, check=True)


def build_html(output: Path, selected: list[int] | None) -> list[Path]:
    npm = require_binary("npm", "install Node.js from https://nodejs.org")
    ensure_reader_dependencies(npm)
    html_root = output / "html"
    env = os.environ.copy()
    env["ASTRO_OUT_DIR"] = str(html_root.resolve())
    if selected:
        env["MURIM_CHAPTERS"] = ",".join(str(number) for number in selected)
    else:
        env.pop("MURIM_CHAPTERS", None)
    subprocess.run([npm, "run", "build"], cwd=READER, check=True, env=env)
    index = html_root / "index.html"
    if not index.is_file():
        raise RuntimeError("Astro build did not produce html/index.html")
    chapters = sorted((html_root / "chapter").glob("*/index.html"))
    return [index, *chapters]


def write_pdf_cover(output: Path) -> Path:
    cover_image = (output / "cover.jpg").resolve()
    cover_typ = output / ".cover.typ"
    cover_typ.write_text(
        f"""#set page(paper: "a4", margin: 0pt, header: none, footer: none, numbering: none, fill: black)
#image("{cover_image}", width: 100%, height: 100%, fit: "cover")
#pagebreak()
#counter(page).update(1)
""",
        encoding="utf-8",
    )
    return cover_typ


def build_pdf(paths: list[Path], output: Path) -> Path:
    target = output / "murim-login.pdf"
    cover_typ = write_pdf_cover(output)
    try:
        run_pandoc(
            paths,
            target,
            "pdf",
            title=TITLE,
            pdf=True,
            include_before=[cover_typ, BOOK_TYP],
        )
    finally:
        cover_typ.unlink(missing_ok=True)
    return target


def build_epub(paths: list[Path], output: Path, css: Path) -> Path:
    target = output / "murim-login.epub"
    run_pandoc(paths, target, "epub3", css, epub_cover=output / "cover.jpg", title=TITLE)
    return target


def copy_book_assets(output: Path) -> Path:
    css = output / "book.css"
    shutil.copyfile(STYLESHEET, css)
    shutil.copyfile(COVER, output / "cover.jpg")
    return css


def build(args: argparse.Namespace) -> list[Path]:
    paths = chapter_paths(args.source, args.chapters or None)
    if not paths:
        raise ValueError("no translation files selected")

    args.output.mkdir(parents=True, exist_ok=True)
    produced: list[Path] = []

    if args.format in {"all", "html"}:
        produced.extend(build_html(args.output, args.chapters or None))
    if args.format in {"all", "pdf", "epub"}:
        css = copy_book_assets(args.output)
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
