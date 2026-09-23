# DGM Database Skill

## Purpose

Provide safe database, ORM and migration practices for DGM.

## Technology

- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic where database contracts affect schemas

## Required Context

Before database changes inspect:

- AGENTS.md
- AI_CONTEXT/HANDOFF.md
- AI_CONTEXT/DECISIONS.md
- Relevant logical model
- Relevant physical model
- Existing ORM models
- Existing migration history
- Existing tests
- Relevant test reports

## Migration Safety

Never create or modify a migration casually.

Before changing schema:

1. Inspect migration history.
2. Identify the current head.
3. Understand existing-data implications.
4. Check nullability.
5. Check foreign keys.
6. Check indexes and constraints.
7. Check downgrade behavior.
8. Check migration ordering.

For existing populated tables, prefer:

Expand -> Remediate -> Enforce

Do not introduce destructive or irreversible changes merely to make tests pass.

## Relationship Integrity

Foreign-key relationships must reflect the governed domain model.

Do not weaken relationship constraints for implementation convenience.

Do not accept semantically invalid relationships merely because the database
allows them.

## Legacy Compatibility

Nullable physical columns may exist for documented transition or legacy-read
compatibility.

Do not confuse physical compatibility with the governed domain contract.

## Validation

Where possible validate:

- migration upgrade
- migration downgrade
- ORM model import
- foreign-key integrity
- relevant service behavior
- focused tests
- `git diff --check`

Never claim database validation was performed if no database was available.
