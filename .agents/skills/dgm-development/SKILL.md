# DGM Development Skill

## Purpose

Provide the standard execution discipline for AI coding agents working on the
Enterprise Data Governance Management Platform (DGM).

## Required Context

Before making changes, read:

1. AGENTS.md
2. AI_CONTEXT/HANDOFF.md
3. AI_CONTEXT/PROJECT_STATE.md
4. AI_CONTEXT/CURRENT_WORK.md
5. The active work package
6. Relevant architecture/product documentation
7. Relevant source code and tests

Do not load the entire repository unnecessarily.

## Execution Rules

- Work only within the active work package.
- Inspect existing implementation before changing it.
- Preserve existing user work.
- Never delete or overwrite `.before_*` files.
- Never reset, clean, stash, or revert the working tree.
- Do not silently change architecture.
- Do not create commits unless explicitly requested.
- Prefer small, focused changes.
- Preserve separation between requirements, architecture, implementation, tests,
  and AI intelligence.

## Work Package Discipline

Every implementation task must be bounded by:

- Objective
- Scope
- Exclusions
- Acceptance criteria
- Validation
- Stop conditions
- Completion artifacts

If the requested change exceeds the work package, stop and report the scope
expansion rather than silently continuing.

## Validation

Before completion:

1. Run focused tests relevant to the change.
2. Run static/syntax validation where applicable.
3. Run `git diff --check`.
4. Inspect `git status --short`.
5. Report tests that could not be executed and why.

Never claim validation passed when it was not actually executed.

## Completion Report

Report:

- What changed
- Files changed
- Validation performed
- Validation blocked
- Decisions made
- Remaining risks
- Recommended next step
