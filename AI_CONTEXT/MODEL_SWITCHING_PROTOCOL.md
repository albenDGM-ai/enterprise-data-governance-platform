# DGM Model Switching Protocol

## Purpose

Allow one AI coding agent to hand work to another without losing project
context.

## Provider Independence

The workflow does not depend on:

- Gemini
- Groq
- OpenAI
- local models
- any specific model family

The repository remains the persistent context layer.

## Handoff Sequence

### Current Agent

Before stopping:

1. Finish or checkpoint the active work.
2. Record actual progress.
3. Record validation results.
4. Record blockers.
5. Update `HANDOFF.md`.
6. Update `CURRENT_WORK.md`.
7. Update `PROJECT_STATE.md` when required.
8. Produce a completion/checkpoint report.

### Next Agent

Before continuing:

1. Read `AGENTS.md`.
2. Read `HANDOFF.md`.
3. Read `PROJECT_STATE.md`.
4. Read `CURRENT_WORK.md`.
5. Read the active work package.
6. Inspect `git status`.
7. Verify the checkpoint.
8. Continue from the verified state.

## Quota Failover

If a provider reaches its quota:

1. Stop the current provider.
2. Do not reset the repository.
3. Do not restart completed work.
4. Switch provider.
5. New provider reads repository context.
6. New provider verifies current state.
7. New provider continues the active work package.

## Conflict Rule

If the new provider discovers a discrepancy:

Do not automatically rewrite previous work.

Report:

- expected state
- actual state
- discrepancy
- likely cause
- proposed resolution

Request orchestration guidance when the discrepancy is architectural.

## Context Principle

Do not depend on hidden conversation memory.

If information is required for future execution, put it in the repository.
