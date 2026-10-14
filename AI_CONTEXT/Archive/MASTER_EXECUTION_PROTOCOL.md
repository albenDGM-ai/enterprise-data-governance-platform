# DGM Master AI Execution Protocol

## 1. Purpose

This protocol defines how any AI coding agent executes work on the Enterprise
Data Governance Management Platform (DGM).

The protocol is provider-neutral.

It must work with:

- Gemini
- Groq
- OpenAI-based coding agents
- local coding models
- future AI coding systems

No AI provider is the authoritative owner of project knowledge.

The repository is the source of truth.

---

## 2. Authority Hierarchy

When information conflicts, use this order:

1. Explicit human decision
2. Current product/architecture documentation
3. AGENTS.md
4. AI_CONTEXT/DECISIONS.md
5. Active work package
6. Current source code and tests
7. Test reports/history
8. AI model assumptions

An AI model must never treat its own previous reasoning as authoritative.

---

## 3. Agent Startup Protocol

Before modifying anything, the agent MUST:

1. Read `AGENTS.md`.
2. Read `AI_CONTEXT/HANDOFF.md`.
3. Read `AI_CONTEXT/PROJECT_STATE.md`.
4. Read `AI_CONTEXT/CURRENT_WORK.md`.
5. Read the active work package.
6. Read `AI_CONTEXT/DECISIONS.md` when relevant.
7. Read relevant `AI_CONTEXT/BLOCKERS.md`.
8. Read only relevant architecture/product documentation.
9. Inspect the current Git working tree.
10. Verify that the repository state matches the stated checkpoint.

Do not assume that the previous model's description of the repository is still
correct.

---

## 4. Work Package Rule

The active work package is the execution boundary.

The agent must work only within:

- Objective
- Scope
- Acceptance criteria
- Validation requirements

The agent must not silently expand the scope.

If additional work is required, stop and report it.

---

## 5. Before Coding

The agent must:

1. Understand the objective.
2. Identify relevant files.
3. Inspect existing implementation.
4. Inspect related tests.
5. Inspect relevant architecture.
6. Identify potential architectural impact.
7. Identify database/migration impact.
8. Identify security/privacy implications.
9. Determine the smallest safe implementation.

Do not begin editing simply because a task description exists.

---

## 6. Implementation Rules

The agent must:

- preserve existing user work
- avoid destructive operations
- avoid unrelated refactoring
- preserve architecture boundaries
- preserve existing naming conventions
- preserve documented business semantics
- preserve governance controls
- preserve auditability
- preserve lineage integrity
- add tests where appropriate

Never:

- reset the repository
- clean the working tree
- delete `.before_*` files
- overwrite existing work without inspection
- create commits unless explicitly requested
- weaken constraints merely to make tests pass

---

## 7. Architecture Escalation

Stop and request orchestration guidance if the task requires:

- a major architectural change
- a new domain model decision
- destructive database changes
- changing established governance relationships
- changing immutable business semantics
- security/privacy decisions
- conflicting requirements
- materially conflicting documentation
- expanding beyond the active work package

The agent may identify a solution but must not silently make the architectural
decision.

---

## 8. Database Safety

Database changes require additional inspection.

Before changing:

- models
- migrations
- foreign keys
- indexes
- constraints
- nullability
- relationships

inspect the migration history and current database contract.

For populated databases prefer:

Expand
  ->
Remediate
  ->
Enforce

Never weaken a governed relationship simply because legacy data is difficult.

---

## 9. Data Lineage Safety

Lineage is a governed enterprise capability.

The agent must preserve:

- flow ownership
- transformation ownership
- target ownership
- mapping ownership
- graph integrity
- active-parent validation
- auditability
- versioning
- snapshots
- human review

AI-discovered lineage is a candidate until appropriately reviewed and approved.

AI must never silently publish governed lineage.

---

## 10. AI Development Safety

AI agents must distinguish:

Implemented
Partially Implemented
Planned
Future

A planned AI capability must never be described as implemented.

AI-generated recommendations must remain traceable where the product design
requires:

- provider
- model
- model version
- prompt/instruction version
- context snapshot
- evidence
- recommendation
- confidence
- reviewer
- decision
- resulting governed change

---

## 11. Validation Protocol

Every completed work package must perform the strongest practical validation
available.

Preferred order:

1. Syntax/static validation
2. Focused unit/service tests
3. API tests
4. ORM/database tests
5. Migration tests
6. Broader regression tests

Also run:

`git diff --check`

and:

`git status --short`

---

## 12. Validation Status

Every validation result must be classified as:

PASS
FAIL
BLOCKED
NOT RUN

Definitions:

PASS
The validation actually executed successfully.

FAIL
The validation executed and failed.

BLOCKED
The validation could not execute because of an environment, dependency,
database, or other external limitation.

NOT RUN
The validation was intentionally omitted.

Never convert BLOCKED into PASS.

Never claim runtime success from static inspection.

---

## 13. Completion Protocol

At completion, the agent must report:

### Summary

What was implemented.

### Files Changed

List the files changed.

### Validation

List commands/tests actually executed.

### Results

Classify each result as PASS, FAIL, BLOCKED, or NOT RUN.

### Architectural Impact

State whether architecture changed.

### Database Impact

State whether database/migrations changed.

### Risks

Identify remaining risks.

### Follow-up

Identify work that remains.

---

## 14. State Update Protocol

When the work package is complete, update the appropriate repository state:

- `AI_CONTEXT/PROJECT_STATE.md`
- `AI_CONTEXT/CURRENT_WORK.md`
- `AI_CONTEXT/HANDOFF.md`
- `AI_CONTEXT/PROGRESS_LEDGER.md`

Update only what is supported by actual completed work.

Do not mark future work as complete.

---

## 15. Model Switching Protocol

A different AI model may take over at any point.

The new model must:

1. Read the repository state.
2. Read the current handoff.
3. Read the active work package.
4. Inspect the current Git state.
5. Verify completed work.
6. Continue from the checkpoint.

It must not restart completed work merely because the provider changed.

Example:

Gemini quota exhausted
        |
        v
Repository checkpoint
        |
        v
Groq reads context
        |
        v
Groq verifies state
        |
        v
Groq continues same work package

The provider is replaceable.

The repository state is persistent.

---

## 16. ChatGPT Orchestration Role

ChatGPT acts as the project-level intelligence/orchestration layer.

ChatGPT may:

- understand the overall DGM roadmap
- define work packages
- create execution prompts
- establish acceptance criteria
- identify architectural risks
- review coding-agent output
- determine whether work is complete
- identify the next work package
- resolve cross-package dependencies
- escalate architectural decisions to the human product owner

ChatGPT does not replace repository verification.

The coding agent must independently inspect the repository.

---

## 17. Human Product Owner Role

The human product owner retains final authority over:

- major architecture
- business requirements
- scope changes
- destructive changes
- security/privacy decisions
- product priorities
- release decisions

AI agents provide implementation assistance.

They do not independently redefine the product.

---

## 18. Stop Rule

When uncertain:

STOP.

Do not guess.

Report:

1. What is known.
2. What is uncertain.
3. Why it matters.
4. What evidence is needed.
5. What decision is required.

---

## 19. Golden Rule

The agent's job is not to make the largest possible change.

The agent's job is to make the smallest safe change that satisfies the active
work package and produces verifiable evidence.
