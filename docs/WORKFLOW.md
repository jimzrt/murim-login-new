# Exceptional Workflows

Routine execution belongs to `tools/workflow.py`; do not use this document as a
manual substitute for controller state.

## Recovery

Run `python tools/workflow.py status N`. `.work/NNNN/workflow.json` is the
transaction record. Conversation history is not. Do not edit transaction JSON
or rebase hashes manually. Source changes, stale hashes, invalid model JSON,
packet-budget failures, QA failures, and unresolved major findings are stop
conditions. `python tools/run_next.py` resumes an in-flight transaction even
if `docs/STATE.md` already names the next chapter; do not start that later
chapter until the current one is committed. Invalid model JSON saves the raw
output under `.work/NNNN/` as `*-raw.txt`.

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

Deterministic reports live in `reviews/qa/`; exact provider-reported phase usage
and elapsed time live in `reviews/metrics/`. Run `python tools/cost_report.py`
to inspect aggregate usage and checkpoint yield.

## Routine Next-Chapter Run and Usage

From a clean Git worktree, run:

```bash
python tools/run_next.py
```

The wrapper reads `- Next chapter: N` from `docs/STATE.md`, displays coordinator
text and the full tool arguments as they run, runs exactly that chapter through
`ACCEPTED`, records the coordinator's own JSON usage, prints the chapter cost
report plus a project total, commits the accepted change set, registers the
commit, and stops. The coordinator session is bash-only (no hub or nested
agents), waits for each `workflow.py` command, and uses
`.omp/coordinator-overlay.yml` so OMP cannot auto-background those calls. On a checkpoint chapter, applied review patches to earlier
reading copies in the same block are included in `Accept Chapter N`. The inner
chapter calls and outer coordinator are therefore all attributed to the same
chapter before its checkpoint is created.

Inspect exact usage with:

```bash
python tools/cost_report.py --chapter N
python tools/cost_report.py --chapter N --json
python tools/cost_report.py --json
```

Model calls use OMP JSON events, with no additional model request or prompt
content. Missing provider usage is a hard failure. Older estimated records are
reported as unavailable and excluded rather than mixed into exact totals.

## Checkpoints and Summaries

Summary and checkpoint-review intervals are independent in
`docs/workflow.json`. After each revised chapter, write a compact beat at
`summaries/beats/NNNN.md` from that chapter only. At the summary interval,
`python tools/workflow.py summarize N` builds a bounded packet from the previous
block summary, this block's beats, and `docs/CONTEXT.json` — not the five full
reading copies — and writes `summaries/START-END.md`. Keep those compact plot
summaries at the configured interval. Initially review every five chapters. After
at least the configured evaluation window, inspect checkpoint-only finding yield:

```bash
python tools/cost_report.py
```

If checkpoint reviews repeatedly find nothing new, increase
`checkpoint_review_interval` to 10 or 20 while retaining five-chapter summaries.
If they catch meaningful drift, keep the shorter interval. A checkpoint uses
structured findings and exact structured dispositions just like chapter review.

## Retrospective Range Audit

Use this only for a targeted new pass over accepted chapters. It is deliberately
separate from normal chapter state:

```bash
python tools/audit_range.py run 0 7 --dry-run
python tools/audit_range.py run 0 7
```

The dry run performs local QA, builds bounded block packets, and reports a
packet-size budget estimate without calling a model. The full run reviews configured
blocks in parallel with Sol, merges structured findings, asks Luna once for
exact bounded replacements rather than complete chapters, applies them only
when each old span occurs exactly once and meets the configured confidence
threshold, and runs final QA. Chapters without
findings are not sent to refinement and are not changed.

Artifacts and metrics are stored under `reviews/retrofit/START-END/`; recoverable
pre-edit copies are stored under ignored `.work/retrofit/`. Inspect the Git diff
and commit one range checkpoint after `VERIFIED`. This workflow never changes
`docs/STATE.md`, `docs/CONTEXT.json`, summaries, profiles, or the ordinary
chapter transaction unless a human separately accepts a genuinely durable
terminology decision.

## New Major Character

Create `characters/<preferred-name>.md` only for recurring, plot-bearing, or
voice-sensitive characters. Record English/Korean name, safe-through chapter,
aliases, role, personality, voice, relationships, active continuity, and source
chapters. Safe profiles contain revealed facts only.

## Git Checkpoint

After `ACCEPTED`, `run_next.py` commits the promoted translation, packet,
structured review/dispositions, QA, metrics, relevant context files, and any
checkpoint patches to earlier translations in the current block. Use
`Accept Chapter N`, then register the exact commit through the controller.

## Exports

Run `python tools/build.py`; select chapters and formats as documented by
`python tools/build.py --help`. Styling lives in `tools/system-window.lua` and
`tools/book.css`.
