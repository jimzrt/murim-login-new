# Exceptional Workflows

Do not load this file for a routine chapter. The routine transaction is encoded
by `tools/workflow.py` and summarized in `AGENTS.md`.

## Recovery

Run `python tools/workflow.py status N`. The durable transaction record is
`.work/NNNN/workflow.json`; conversation history is not a recovery source.

- `CONTEXT_READY`: run the isolated draft call.
- `DRAFTED`: run the review gate. A changed draft is rejected by its hash.
- `REVIEWED`: run the isolated revision call.
- `REVISED`: update durable context, then accept. `translations/` is still
  untouched at this point.
- `ACCEPTED`: the reading copy was promoted; finish the Git checkpoint.

Do not manually edit `workflow.json`. If the Korean source changed after a
transaction began, stop for manual reconciliation rather than rebasing hashes.

## Review Isolation

`python tools/workflow.py review N` verifies the recorded draft hash and calls
`tools/review_chapter.py`. The latter blocks on one non-interactive
`openai-codex/gpt-5.6-sol:medium` process with tools, rules, extensions, session
persistence, and advisor recursion disabled. It installs a report only after a
successful, nonempty response and records the draft, packet, and report SHA256
values in `reviews/sol/NNNN.json`.

Use `python tools/workflow.py review N --dry-run` to inspect packet bounds. A
dry run does not advance the stage. Never use built-in advisors or task agents
for chapter review.

## New Major Character

Create `characters/<preferred-name>.md` only for a recurring, plot-bearing, or
voice-sensitive character:

```markdown
# English Name (Korean)

- **Safe through:** Chapter N
- **Aliases:** Revealed aliases
- **Role:** Current role and affiliations
- **Personality:** Demonstrated stable traits
- **Voice:** Register, rhythm, address terms, humor, profanity
- **Relationships:** Revealed relationships
- **Continuity:** Only facts needed later
- **Sources:** Source chapters; wiki URL/date when used
```

Safe profiles contain revealed facts only. Never create or consult a spoiler
profile during routine drafting or revision.

## Five-Chapter Checkpoint

After chapters ending in 4 or 9, create `summaries/NNNN-NNNN.md` for the just
completed five-chapter block, at most 250 words, and follow the reported
`checkpoint` action. It runs one isolated Sol pass over the five English reading
copies, summary, rules, and state. Apply or disposition every finding in the
reported `.work/NNNN/checkpoint-disposition.md`, then run `checkpointed`.
Acceptance is blocked until this gate is complete.

## Git Checkpoint

After `ACCEPTED`, inspect `git status` and commit the promoted translation, its
packet/report/JSON metadata, and only the durable context changed for that
chapter. Use `Accept Chapter N`. Then register that exact commit with the
controller. `.work/` remains ignored and is never committed.

## Export Editions

Run `python tools/build.py` to build HTML, PDF, and EPUB. Build selected chapters
with `python tools/build.py 0 1 2 --format epub`. Export styling lives in
`tools/system-window.lua` and `tools/book.css`.
