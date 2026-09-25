# WP-010 — Jules Development Handoff

## Objective

Prepare the Enterprise Data Governance Management (DGM) repository as the
authoritative development handoff for Jules.

Jules must be able to continue development from the repository itself without
depending on prior ChatGPT conversation history.

## Scope

- Establish the current repository/project-control baseline.
- Preserve the existing DGM architecture and documentation structure.
- Preserve the AI Development Operating System.
- Make the current development state explicit.
- Define Jules execution and validation rules.
- Define the immediate development objective after handoff.
- Record the known test baseline.
- Preserve historical tooling experiments as history, not active dependencies.

## Current Architecture

Backend:
- FastAPI
- Python
- SQLAlchemy
- Alembic
- PostgreSQL

Frontend:
- React
- TypeScript
- Material UI
- React Router
- TanStack

AI architecture:
- Provider-neutral AI architecture.
- OpenAI API as a cloud provider.
- Gemini/Groq experimentation documented separately.
- Ollama remains an optional local runtime.
- LangChain may be used where appropriate.
- LangGraph only where genuinely required.

## Repository Governance

Jules MUST:

1. Read `AGENTS.md` before making changes.
2. Read the relevant files under `AI_CONTEXT/`.
3. Read the active work package before implementation.
4. Inspect existing implementation and tests before modifying them.
5. Make the smallest safe change that satisfies the work package.
6. Preserve the numbered documentation structure.
7. Preserve architectural separation between:
   - Business Requirements
   - Enterprise Business Model
   - Conceptual Model
   - Logical Model
   - Physical Model
   - API Design
   - UI Design
8. Preserve lineage governance, traceability, ownership, auditability,
   versioning and reviewability.
9. Never reset, revert, checkout, stash, clean, delete or overwrite existing
   work unless explicitly authorized.
10. Never create a Git commit unless explicitly requested.
11. Validate every implementation change with appropriate tests/checks.
12. Produce evidence in `Test reports/`.

## Current Development State

The repository is on:

`feature/project-foundation`

The current Git baseline has already been synchronized with:

`origin/feature/project-foundation`

The repository contains the AI Development Operating System under:

- `AI_CONTEXT/`
- `.agents/skills/`
- `AGENTS.md`

The DGM lineage foundation is currently the most mature implementation area.

The current governed relationship model is:

Source → Process → Flow → Transformation → Target → Mapping

## Test Baseline

The restored backend pytest invocation uses the repository-level
`pytest.ini` to provide the backend import context.

The established baseline is:

- Batch 07: 5/5
- Batch 08: 8/8
- Combined: 13/13 passing

This baseline must be re-established before substantial new implementation.

## Historical Development Context

OpenCode, Groq and Gemini were investigated as development-agent options.

These experiments are historical development context and are NOT a requirement
for Jules to reproduce.

In particular:

- Groq TPM limitations made it unsuitable as the primary repository-aware
  OpenCode execution agent.
- OpenCode local plugin dependency resolution was investigated.
- Gemini was configured and tested through OpenCode.
- ChatGPT Work/Codex availability was exhausted during this development phase.

Jules should not spend implementation time reproducing these experiments unless
a future work package explicitly requires it.

## Immediate Priority

Restore and maintain a green backend baseline, then continue the DGM product
foundation from the repository state.

Before introducing a new feature, Jules must:

1. Establish the current test baseline.
2. Inspect relevant architecture and implementation.
3. Identify the smallest bounded work package.
4. Implement only that package.
5. Run focused tests.
6. Run the relevant broader regression tests.
7. Update required documentation/state.
8. Create a timestamped test report.
9. Stop and escalate if architecture or governance assumptions conflict.

## Stop Conditions

Jules MUST stop and report instead of making autonomous architectural changes
when:

- Existing architecture conflicts with the requested work.
- A database migration could destroy or invalidate existing data.
- A lineage relationship contract must be changed.
- A destructive operation is required.
- Existing user work would need to be discarded.
- Security/privacy implications are unclear.
- Requirements conflict with existing authoritative documentation.
- The required scope cannot be completed safely within the work package.

## Completion Contract

Every Jules work package must report:

### Status
PASS / FAIL / BLOCKED / NOT RUN

### Changes
Files changed and purpose of each change.

### Validation
Commands executed and their results.

### Tests
Focused tests and broader regression results.

### Documentation
Documentation/state files updated.

### Risks
Known unresolved risks or limitations.

### Next Step
The smallest logical next work package.

## Definition of Done

A Jules work package is complete only when:

- Scope is satisfied.
- Existing behavior is preserved unless intentionally changed.
- Tests pass or failures are explicitly explained.
- Documentation/state is synchronized.
- A test report exists.
- No unauthorized destructive operation occurred.
- No commit is created unless explicitly requested.
