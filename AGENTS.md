# Murim Login Translation Harness

Translate exactly one explicitly requested chapter. Never start the next chapter.

## Controller Loop

For chapter `N`, run:

```bash
python tools/workflow.py status N
```

Perform only the reported next action, then run `status` again. Never infer a
stage from chat history or skip, combine, or reorder stages. Stop at `COMMITTED`,
or immediately on `ERROR`, an ambiguous source passage, a stale hash, or a
failed command.

The controller owns retrieval, artifact paths, review completion, hash checks,
promotion, recovery, and the next action. Routine chapter work must not load
`docs/WORKFLOW.md`, the bulk source, the full compendium, archive directories,
or `characters/spoilers/`.

## Model Tasks

- At `CONTEXT_READY`, run the reported `draft` command. The controller makes one
  isolated Luna call and validates `.work/NNNN/draft.md`.
- At `REVIEWED`, run the reported `revise` command. The controller gives Luna
  only the bounded context, reviewed draft, and saved findings, then validates
  `.work/NNNN/revised.md`.
- Do not invoke `omp`, `/advisor`, `/advisor-pi`, a hub, task agent, or nested
  reviewer directly. Controller model calls block until their isolated process
  exits successfully.
- At `REVISED`, update only durable terminology, affected safe profiles,
  continuity, the applicable five-chapter summary, and `docs/STATE.md`.
- For chapters ending in 4 or 9, follow the controller's checkpoint review and
  disposition stages before acceptance. Do not substitute an advisor session.

## Acceptance

`translations/NNNN.md` is an accepted reading copy, never a draft. After the
controller promotes it, inspect and commit only the accepted chapter artifacts
and relevant durable-context changes. Then register the exact commit using the
controller's reported command. Never commit `.work/`, caches, or an unaccepted
draft.

The binding translation and formatting policy is `RULES.md`. Recovery,
character-profile creation, five-chapter checkpoints, exports, and exceptional
procedures are in `docs/WORKFLOW.md`; read that file only when one applies.
