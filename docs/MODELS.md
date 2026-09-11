# Runtime Model Configuration

Translation roles live in `models` in [`docs/workflow.json`](workflow.json):

- `draft`
- `review` (chapter review and retrofit review)
- `revision` (chapter revision and retrofit refinement)
- `summary`
- `coordinator`
- `checkpoint` (optional; five-chapter checkpoint review; defaults to `review`)
- `polish`

Mastering roles live in `models` in [`docs/mastering.json`](mastering.json):

- `master`
- `adjudicator`

Do not copy those IDs into docs or defaults elsewhere. Call sites read the resolved
`draft_model`, `review_model`, `revision_model`, `summary_model`,
`coordinator_model`, and `checkpoint_model` keys from `project_config()`, and
mastering selectors from `docs/mastering.json`.

Ordered provider fallbacks for the translation and mastering selectors are in
[`.omp/config.yml`](../.omp/config.yml). OpenAI models prefer the Codex
subscription, then Cursor, then OpenRouter. OMP switches providers on quota,
rate limits, and outages without changing the validated model. The adjudicator
requests Cursor Grok and uses DeepSeek only as that stage's overflow.

All calls are isolated, non-interactive, tool-free, session-free, and bounded by
phase-specific packets and token ceilings. Do not silently substitute models in
the workflow. Reviewer output and revision dispositions are schema-validated
before workflow state advances.

Every model subprocess uses OMP JSON mode. Each assistant `message_end` must
contain provider-reported usage; a missing or malformed usage record is a hard
failure. Metrics retain the requested model, the actual provider/model OMP used,
whether a fallback fired, and billing type (`subscription` vs `api`). JSON mode
changes process output framing and does not add a model request or prompt content.

Packet token estimates are used only to enforce pre-call context ceilings. They
are never reported as consumed tokens. Inspect exact captured usage with
`python tools/cost_report.py`. That report keeps subscription quota and
API-equivalent value separate from OpenRouter cash spend. Legacy calls without
JSON usage are explicitly unavailable and excluded.
