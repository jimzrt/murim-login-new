# Project Context

This repository uses the deterministic chapter controller described in the
root `AGENTS.md`. `python tools/run_next.py` is the preferred clean-worktree
entry point for the next chapter. Inside a requested chapter, begin and resume
by running `python tools/workflow.py status N`; execute only its reported next
action through `MASTERED`; the wrapper owns commit and registration.
