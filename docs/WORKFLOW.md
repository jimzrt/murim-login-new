# Exceptional Workflows

Routine execution belongs to `tools/workflow.py`; do not use this document as a
manual substitute for controller state.

## Recovery

Run `python tools/workflow.py status N`. `.work/NNNN/workflow.json` is the
transaction record. Conversation history is not. Do not edit transaction JSON
or rebase hashes manually. Source changes, stale hashes, invalid model JSON,
packet-budget failures, QA failures, and unresolved major findings are stop
conditions.

## Bounded Context Hygiene

`docs/CONTEXT.json` is the only model-facing state ledger. Before drafting N it
must be safe through N-1; before acceptance it must be safe through N. Keep it
below `context_max_bytes` and its explicit `continuity_sources` within the
configured limit. Include a prior translation only when wording, dialogue, or a
scene directly continues. At checkpoints, move resolved facts into the summary,
compendium, or safe profiles and remove them from active context.

`docs/STATE.md` is a short human operational view, not a historical review log.
Review history belongs to the structured files under `reviews/`.

## Review and Revision

The chapter reviewer returns validated JSON at `reviews/sol/NNNN.json`; the
human view is `reviews/sol/NNNN.md`; hashes and counts are in
`reviews/sol/NNNN.meta.json`. Revision creates
`reviews/sol/NNNN.dispositions.json`. Every finding needs exactly one applied,
rejected, or unresolved disposition. Unresolved critical/major findings block.

Deterministic reports live in `reviews/qa/`; phase usage estimates and elapsed
time live in `reviews/metrics/`. Run `python tools/cost_report.py` to inspect
aggregate usage and checkpoint yield.

## Checkpoints and Summaries

Summary and checkpoint-review intervals are independent in
`docs/workflow.json`. Keep compact plot summaries at the configured summary
interval. Initially review every five chapters. After at least the configured
evaluation window, inspect checkpoint-only finding yield:

```bash
python tools/cost_report.py
```

If checkpoint reviews repeatedly find nothing new, increase
`checkpoint_review_interval` to 10 or 20 while retaining five-chapter summaries.
If they catch meaningful drift, keep the shorter interval. A checkpoint uses
structured findings and exact structured dispositions just like chapter review.

## New Major Character

Create `characters/<preferred-name>.md` only for recurring, plot-bearing, or
voice-sensitive characters. Record English/Korean name, safe-through chapter,
aliases, role, personality, voice, relationships, active continuity, and source
chapters. Safe profiles contain revealed facts only.

## Git Checkpoint

After `ACCEPTED`, inspect `git status` and commit only the promoted translation,
packet, structured review/dispositions, QA, metrics, and relevant context files.
Use `Accept Chapter N`, then register the exact commit through the controller.

## Exports

Run `python tools/build.py`; select chapters and formats as documented by
`python tools/build.py --help`. Styling lives in `tools/system-window.lua` and
`tools/book.css`.
