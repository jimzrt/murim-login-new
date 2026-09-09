# Runtime Model Instructions

- Executor: `openai-codex/gpt-5.6-luna:high`
- Reviewer: one-shot `omp -p`, `openai-codex/gpt-5.6-sol:medium`
- Run all three model stages through `python tools/workflow.py`: isolated Luna
  draft, isolated Sol review, and isolated Luna revision.
- The runner uses `--no-session`, `--no-tools`, `--no-rules`, `--no-extensions`, and `.omp/review-overlay.yml` with `advisor.enabled: false`.
- Review writes the bounded packet to `reviews/packets/NNNN.md`, the report to
  `reviews/sol/NNNN.md`, and its content hashes to `reviews/sol/NNNN.json`.
- The reviewer must not edit files, spawn nested reviewers, or read outside the packet.
- Limit reviewer context to the current chapter/checkpoint, exact glossary rows, present-character profiles, and latest applicable state/summary. It reports prioritized, detailed, source-backed defects only.
- Review tone as well as fidelity: preserve brisk commercial-webnovel prose, Jin Taekyung’s dry self-mockery, dark humor, character-specific dialogue, and the contrast between danger and absurdity.
- The executor applies or dispositions corrections and verifies them.
- If the Sol model or `omp -p` is unavailable, stop and ask the user. Do not substitute silently.
- Never invoke the built-in `/advisor` or `/advisor-pi` for this project.

## Export Toolchain

- Pandoc CLI parses the translation Markdown and writes the per-chapter HTML site and EPUB3.
- `tools/system-window.lua` turns only explicitly headed System blockquotes into `.system-window` containers for HTML/EPUB and framed Typst blocks for PDF.
- `tools/book.css` styles System containers and chapter navigation for HTML and EPUB. PDF is generated directly from Markdown through Pandoc's Typst engine.
- `cover.jpg` is passed as the EPUB cover and rendered as the HTML contents image and direct Typst PDF cover page.
