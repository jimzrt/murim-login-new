# Project Context

This repository uses the deterministic chapter controller described in the
root `AGENTS.md`. `python tools/run_next.py` is the preferred clean-worktree
entry point for the next chapter. Inside a requested chapter, begin and resume
by running `python tools/workflow.py status N`; execute only its reported next
action. If the wrapper says it owns the checkpoint, stop at `ACCEPTED` without
committing.
