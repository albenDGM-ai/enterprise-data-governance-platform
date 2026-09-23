# DGM API Skill

## Purpose

Build consistent, governed FastAPI APIs aligned with DGM architecture and
service contracts.

## Technology

- FastAPI
- Pydantic
- SQLAlchemy services
- PostgreSQL persistence

## Required Context

Read:

- AGENTS.md
- AI_CONTEXT/HANDOFF.md
- AI_CONTEXT/PROJECT_STATE.md
- Relevant API architecture
- Relevant logical/physical model
- Relevant ORM models
- Relevant services
- Existing API tests

## API Rules

- Keep routes thin.
- Put business validation in services/domain logic where appropriate.
- Keep Pydantic contracts aligned with actual service behavior.
- Do not expose mutable fields that the service intentionally treats as
  immutable.
- Validate semantic relationships, not only database foreign keys.
- Preserve active/inactive governance rules.
- Preserve audit and review requirements.

## PUT vs PATCH

Treat PUT and PATCH contracts explicitly.

For immutable fields:

- do not silently accept mutation
- either exclude them from the update schema or explicitly reject changes

PATCH semantics must distinguish:

- field omitted
- field explicitly set to null
- field intentionally cleared

## Errors

Use stable, meaningful API errors for validation failures.

Do not convert domain validation failures into unexplained database errors.

## Validation

Run focused API/service tests and syntax/static checks.

Report unavailable integration tests explicitly.
