# Runtime Model Configuration

The only place to set models is `models` in [`docs/workflow.json`](workflow.json):

- `draft`
- `review` (chapter review, checkpoint review, and retrofit review)
- `revision` (chapter revision and retrofit refinement)
- `summary`
- `coordinator`

Do not copy those IDs into docs or defaults elsewhere. Call sites read the resolved
`draft_model`, `review_model`, `revision_model`, `summary_model`, and
`coordinator_model` keys from `project_config()`.

All calls are isolated, non-interactive, tool-free, session-free, and bounded by
phase-specific packets and token ceilings. Do not silently substitute models.
Reviewer output and revision dispositions are schema-validated before workflow
state advances.

Every model subprocess uses OMP JSON mode. Each assistant `message_end` must
contain provider-reported usage; a missing or malformed usage record is a hard
failure. Metrics retain the requested model and aggregate every actual
provider/model reported by OMP. JSON mode changes process output framing and
does not add a model request or prompt content.

Packet token estimates are used only to enforce pre-call context ceilings. They
are never reported as consumed tokens. Inspect exact captured usage with
`python tools/cost_report.py`; legacy calls without JSON usage are explicitly
unavailable and excluded.
