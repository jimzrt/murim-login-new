# Murim Login Translation Harness

Translate exactly one explicitly requested chapter. Never start the next chapter.

## Controller Loop

For chapter `N`, run `python tools/workflow.py status N`. Perform only the
reported next action, then run `status` again. Never infer a stage from chat
history or skip, combine, or reorder stages. Stop at `COMMITTED`, or immediately
on ambiguity, stale hashes, failed QA, an over-budget packet, invalid model JSON,
or any failed command.

The controller owns retrieval, phase-specific packets, model calls, QA, review
completion, hashes, promotion, recovery, and the next action. Routine work must
not load the bulk source, full compendium, archive directories, or
`characters/spoilers/`.

## Model-Facing Context

- `docs/CONTEXT.json` is the bounded active state. Keep only active continuity,
  unresolved questions, temporary decisions, and zero to two explicit
  `continuity_sources`. Move stable facts to profiles/compendium and resolved
  plot to summaries.
- Draft receives the source, complete rules, exact glossary matches, matching
  profiles, bounded active state, latest summary, and only the explicitly named
  continuity reading copies.
- Review receives the source, draft, rules, exact glossary matches, matching
  profiles, active continuity, and deterministic QA. It does not receive prior
  translations or the summary archive.
- Revision receives the source, draft, structured findings, rules, glossary,
  and matching profiles. It does not receive draft-only history or state.

## Gates

- Luna drafts; deterministic QA must pass; Sol returns validated structured
  findings; Luna returns the revised reading copy plus one disposition per
  finding; final QA must pass.
- Unresolved critical or major findings block acceptance. Reviews and
  dispositions are durable JSON with generated Markdown reading reports.
- At `REVISED`, update durable terminology, affected safe profiles,
  `docs/CONTEXT.json`, `docs/STATE.md`, and the applicable summary.
- Follow configured checkpoint actions. Never substitute `/advisor`, a hub,
  task agent, nested session, or direct `omp` invocation.

## Acceptance

`translations/NNNN.md` contains accepted reading copies only. After promotion,
commit the chapter, structured review/dispositions, QA reports, metrics, and
relevant durable-context changes. Register the exact commit with the reported
command. Never commit `.work/`, caches, or an unaccepted draft.

Binding language policy is in `RULES.md`. Configuration is in
`docs/workflow.json`. Read `docs/WORKFLOW.md` only for recovery, profiles,
checkpoint tuning, or exports.
