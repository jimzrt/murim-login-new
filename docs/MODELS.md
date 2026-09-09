# Runtime Model Configuration

The authoritative configuration is `docs/workflow.json`.

- Draft: `openai-codex/gpt-5.6-luna:high`
- Review: `openai-codex/gpt-5.6-sol:medium`
- Revision: `openai-codex/gpt-5.6-luna:high`
- Coordinator: `openai-codex/gpt-5.6-luna:high`

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
