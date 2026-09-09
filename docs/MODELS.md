# Runtime Model Configuration

The authoritative configuration is `docs/workflow.json`.

- Draft: `openai-codex/gpt-5.6-luna:high`
- Review: `openai-codex/gpt-5.6-sol:medium`
- Revision: `openai-codex/gpt-5.6-luna:high`

All calls are isolated, non-interactive, tool-free, session-free, and bounded by
phase-specific packets and token ceilings. Do not silently substitute models.
Reviewer output and revision dispositions are schema-validated before workflow
state advances.

Usage figures are conservative estimates because the OMP subprocess does not
provide authoritative billing data here. Inspect them with
`python tools/cost_report.py` and use provider billing as the cost authority.
