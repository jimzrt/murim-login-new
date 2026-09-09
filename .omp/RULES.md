# Sticky Harness Invariants

- Process exactly one explicitly requested chapter; never advance automatically.
- Ask `python tools/workflow.py status N` what to do next.
- Never infer, skip, combine, or reorder workflow stages.
- Read only the artifact named by the current action.
- Never read bulk archives or `characters/spoilers/` during chapter work.
- Never write a draft to `translations/`.
- A review is valid only for the recorded draft SHA256.
- Model-facing state comes only from bounded `docs/CONTEXT.json`.
- Deterministic QA and structured finding dispositions must pass.
- Unresolved critical or major findings block acceptance.
- Run chapter review only through `python tools/workflow.py review N`.
- Never start nested agents or reviewer sessions.
- Under `tools/run_next.py`, stop at `ACCEPTED`; the wrapper records coordinator usage and commits.
- Stop on command failure, stale hashes, ambiguity, or `COMMITTED`.
- For accepted-range re-audits, use `tools/audit_range.py`; never reopen normal chapter transactions.
