# Murim Login Translation Harness

Translate exactly one explicitly requested chapter. Never start the next chapter.

## Routine Trigger

For the next chapter, the preferred entry point is:

```bash
python tools/run_next.py
```

It reads the exact next chapter from `docs/STATE.md`, executes each controller
action reported by `status` through `MASTERED`, creates `Accept Chapter N`,
registers that commit, and stops at `COMMITTED`. `master` runs the two-model
overlay, promotes the verified copy, and records its hashes in the same primary
transaction. The wrapper requires a clean Git worktree. An exclusive lock at
`.work/run.lock` prevents a second `run_next`/`run_until` from overlapping;
inspect it with `python tools/run_lock.py`.

## Controller Loop

For chapter `N`, run `python tools/workflow.py status N`. Perform only the
reported next action, then run `status` again. Never infer a stage from chat
history or skip, combine, or reorder stages. Stop at `COMMITTED`, or immediately
on ambiguity, stale hashes, failed QA, an over-budget packet, invalid model JSON,
or any failed command.

The controller owns retrieval, phase-specific packets, model calls, QA, review
completion, hashes, promotion, recovery, and the next action. Routine work must
not load other chapter source files, the full compendium, archive directories, or
`characters/spoilers/`.

If draft fails because the first nonblank line is not `# Chapter N`, do not
rerun the model. If `.work/NNNN/draft-raw.txt` contains the heading after a
short preamble, write the text from that heading onward into `draft.md` and run
`python tools/workflow.py drafted N`. QA reports live at
`reviews/qa/NNNN-draft.json` and `NNNN-final.json`. `translations/NNNN.md` does
not exist until `accept`.

## Model-Facing Context

- `docs/CONTEXT.json` is the bounded active state. Keep `version`, `safe_through`,
  `continuity_sources`, `active_continuity`, `open_questions`, and
  `temporary_decisions`. Keep only active continuity, unresolved questions,
  temporary decisions, and zero to two explicit `continuity_sources`. Move
  stable facts to profiles/compendium and resolved plot to summaries.
- Draft receives the source, complete rules, exact glossary matches, compact
  identity/voice/relationship fields from matching profiles, bounded active
  state, latest summary, and only the explicitly named continuity reading
  copies. Archived per-chapter profile continuity is not injected.
- Review receives the source, draft, rules, exact glossary matches, the same
  compact matching profiles, active continuity, and deterministic QA. It does
  not receive prior translations or the summary archive.
- Revision is deterministic: it applies each review finding's exact, unique
  `current` → `replacement` span to the reviewed draft. It makes no model call
  and receives no additional context.
- Summarize receives the previous block summary, this block's chapter beats,
  and bounded active state. It does not receive full reading copies.

## Gates

- The draft model drafts; deterministic QA must pass; the review model returns
  validated structured findings with exact finished replacements. Revision
  applies those replacements atomically, blocks on missing, repeated, or
  overlapping spans, and runs final QA. The mastering editor is the only
  later full-copy edit and applies `POLISH.md`.
- Reviews are durable JSON with generated Markdown reading reports. Checkpoint
  dispositions remain structured and unresolved critical or major checkpoint
  findings block acceptance.
- At `REVISED`, run
  `python tools/workflow.py update N`. Its bounded no-tools model call returns
  structured chapter facts; the controller validates and deterministically
  writes `docs/NAMES.md`, affected safe profiles, `docs/CONTEXT.json`,
  `docs/STATE.md`, and `summaries/beats/NNNN.md`. It records the packet and
  exact output under `reviews/`. Do not edit those generated updates manually.
  When status asks for it, run `python tools/workflow.py summarize N`.
- Follow configured checkpoint actions. Never substitute `/advisor`, a hub,
  task agent, nested session, or direct `omp` invocation. `run_next.py` must
  wait for each `workflow.py` command; do not background it.

## Acceptance

`accept` creates the baseline `translations/NNNN.md` and advances the primary
transaction to `ACCEPTED`. The next reported action, `master`, runs and resumes
the overlay, promotes the verified mastered copy over that file, and advances
the same transaction to `MASTERED`; the pre-master snapshot remains at
`reviews/mastering/NNNN/baseline.md`. Commit the chapter, structured review, QA,
mastering artifacts, metrics, and relevant durable-context changes only from
`MASTERED`, then register the exact commit. Never commit `.work/`, caches, or an
unaccepted draft.

Binding language policy is in `RULES.md`. Configuration is in
`docs/workflow.json`. Read `docs/WORKFLOW.md` only for recovery, profiles,
checkpoint tuning, or exports.

## Retrospective Range Audit

When the user explicitly requests a new pass over already accepted chapters,
do not reopen their normal chapter transactions. Run
`python tools/audit_range.py status START END`, follow only its reported actions,
and stop at `VERIFIED`. This maintenance flow performs deterministic QA, bounded
parallel block reviews, one patch-planning call, exact atomic replacements, and
final QA. It never advances `docs/STATE.md` or `docs/CONTEXT.json`.
