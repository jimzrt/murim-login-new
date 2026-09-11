# Murim Login Translation Harness

Translate exactly one explicitly requested chapter. Never start the next chapter.

## Routine Trigger

For the next chapter, the preferred entry point is:

```bash
python tools/run_next.py
```

It reads the exact next chapter from `docs/STATE.md`, runs the controller through
`ACCEPTED`, records the coordinator's exact OMP JSON usage, runs the two-model
mastering overlay, promotes the verified mastered copy into `translations/`,
creates `Accept Chapter N`, registers that commit, and stops at `COMMITTED`. It
requires a clean Git worktree. An exclusive lock at `.work/run.lock` prevents a
second `run_next`/`run_until` from overlapping; inspect it with
`python tools/run_lock.py`. When invoked by this wrapper, stop at `ACCEPTED`;
never master, commit, or run `workflow.py committed` yourself.

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

If draft or polish fails because the first nonblank line is not `# Chapter N`,
do not rerun the model. The raw output is `.work/NNNN/draft-raw.txt` or
`polish-raw.txt`. If that file contains the heading after a short preamble,
write the text from the heading onward into `draft.md`/`polished.md` and run
`python tools/workflow.py drafted N` or `polished N`. QA reports live at
`reviews/qa/NNNN-draft.json`, `NNNN-polish.json`, and `NNNN-final.json`.
`translations/NNNN.md` does not exist until `accept`.

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
- Revision receives the source, draft, structured findings, rules, glossary,
  and compact matching profiles. It does not receive draft-only history or
  state.
- Polish receives the source, revised reading copy, `POLISH.md`, rules,
  glossary, and compact matching profiles. It does not receive review findings,
  the summary archive, or prior translations. Chapters before
  `polish_from_chapter` skip this stage.
- Summarize receives the previous block summary, this block's chapter beats,
  and bounded active state. It does not receive full reading copies.

## Gates

- The draft model drafts; deterministic QA must pass; the review model returns
  validated structured findings; the revision model returns the revised reading
  copy plus one disposition per finding; from `polish_from_chapter` onward the
  polish model returns a complete reading copy using `POLISH.md`; final QA
  must pass.
- Unresolved critical or major findings block acceptance. Reviews and
  dispositions are durable JSON with generated Markdown reading reports.
- At `POLISHED`, or at `REVISED` when polish is skipped, update durable
  terminology in `docs/NAMES.md` or the compendium, affected safe profiles,
  `docs/CONTEXT.json`, `docs/STATE.md`, and `summaries/beats/NNNN.md` from this
  chapter only. Each beat's first nonblank line must be exactly `# Chapter N`,
  followed by `## Plot`, `## Continuity`, and `## Translation Decisions`. Do not
  use `# Chapter N Beat`. Do not load other reading copies to summarize. When
  status asks for it, run `python tools/workflow.py summarize N`.
- Follow configured checkpoint actions. Never substitute `/advisor`, a hub,
  task agent, nested session, or direct `omp` invocation. `run_next.py` must
  wait for each `workflow.py` command; do not background it.

## Acceptance

`translations/NNNN.md` contains accepted reading copies only. After acceptance,
the wrapper runs mastering and promotes the verified mastered copy over that
file; the pre-master snapshot remains at `reviews/mastering/NNNN/baseline.md`.
After promotion, commit the chapter, structured review/dispositions, QA reports,
mastering artifacts, metrics, and relevant durable-context changes. Register the
exact commit with the reported command. The `run_next.py` wrapper performs
mastering, promotion, commit, and registration itself. Never commit `.work/`,
caches, or an unaccepted draft.

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
