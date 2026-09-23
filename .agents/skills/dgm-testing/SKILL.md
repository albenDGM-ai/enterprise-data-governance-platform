# DGM Testing Skill

## Purpose

Ensure AI coding agents verify changes honestly and systematically.

## Required Context

Read:

- AGENTS.md
- active work package
- relevant source code
- relevant architecture
- existing tests
- previous test reports

## Test Strategy

Prefer the smallest useful validation set first:

1. Syntax/static checks
2. Focused unit/service tests
3. API tests
4. ORM/database tests
5. Migration tests
6. Broader regression suite

## Evidence Rules

A test is:

- PASS only when actually executed successfully.
- FAIL when executed and unsuccessful.
- BLOCKED when it could not be executed.
- NOT RUN when deliberately omitted.

Never convert BLOCKED into PASS.

Never infer runtime success from static inspection.

## Regression Discipline

When fixing a defect:

- add or update a focused regression test where appropriate
- run the regression test
- run adjacent tests
- inspect for contract inconsistencies

## Environment Awareness

Do not install large dependency sets merely to obtain a test result.

Consider the project's Python version, available memory, database availability,
and existing virtual environment before installing dependencies.

## Final Validation

Run:

- relevant tests
- syntax/static checks
- `git diff --check`
- `git status --short`

Report exact blockers.
