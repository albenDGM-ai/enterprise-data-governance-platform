# DGM Project Context

**Canonical project continuity document for AI/model handoff**

- **Project:** Enterprise Data Governance Platform (DGM)
- **Repository:** `enterprise-data-governance-platform`
- **Purpose of this file:** Provide one maintained, model-independent snapshot of the product, verified implementation progress, current repository state, decisions, and the next package-selection context.
- **Status:** ACTIVE
- **Version:** 1.0
- **Last updated:** 2026-09-30

---

## 1. How This File Must Be Used

This is the **canonical current-state context document for project continuity**.

A new AI/model should read this file first when taking over DGM work.

It should then verify the repository state before making changes.

This file is a **current-state snapshot**, not a replacement for detailed evidence, architecture documentation, test reports, or the DGM Development Operating Standard.

### Source-of-truth hierarchy

Use the following hierarchy when information conflicts:

1. Explicit human/product-owner decision
2. Current Product Requirements / Architecture documentation
3. `AGENTS.md`
4. `AI_CONTEXT/DGM_PROJECT_CONTEXT.md`
5. `AI_CONTEXT/DECISIONS.md`
6. Active work package
7. Source code and tests
8. Test reports / historical evidence
9. AI model assumptions

The repository remains the persistent project context. AI models are replaceable execution components.

Do not rely on hidden conversation memory.

---

# 2. Product: What We Are Building

## Product

**Enterprise Data Governance Platform (DGM)**

## Current product objective

Build a reliable, connected, testable, understandable governance platform containing the minimum capabilities required to understand and govern enterprise data.

The current product intentionally prioritizes a **small useful governance core** over broad enterprise functionality.

### MVP product formula

> **Metadata + Business Meaning + Data Quality + Lineage + Accountability**

Everything outside this core is either deferred or future scope unless explicitly brought back by the product owner.

---

# 3. Current MVP Product Scope

The current baseline product requirement is the **DGM Product Requirements Document v1.0**.

The MVP contains five core capabilities:

1. Metadata Repository
2. Business Glossary
3. Data Quality
4. Data Lineage
5. Basic Governance / Accountability

## 3.1 Metadata Repository

Minimum required concepts:

- Source System
- Database
- Schema
- Table
- Column
- Data Asset

Minimum behavior:

- identifiers
- names
- types
- parent relationships
- source-system relationship
- descriptions
- lifecycle/status
- owner reference where applicable
- create/read/update/delete/list behavior
- validation
- basic retrieval/filtering

**Package 03 already established initial Data Asset registration and retrieval.**

---

## 3.2 Business Glossary

Minimum required concept:

- Business Term

Minimum behavior:

- unique identifier
- term name
- definition
- status
- owner/steward reference
- connection between business meaning and relevant metadata assets

Do not introduce complex workflow, semantic search, or AI functionality unless explicitly requested.

---

## 3.3 Data Quality

Minimum required concepts:

- Data Quality Rule
- Data Quality Result

Rule should represent:

- what is checked
- applicable asset/attribute
- expected condition
- status

Result should represent:

- rule
- execution time
- status
- basic measurement/outcome

An enterprise-scale DQ execution engine is **not required for the initial MVP**.

---

## 3.4 Data Lineage

Minimum required concepts:

- Lineage Source
- Lineage Target
- Lineage Flow
- Lineage Transformation
- Lineage Mapping

Minimum behavior:

- governed source-to-target relationships
- lineage associated with metadata assets
- transformations
- mappings
- basic upstream/downstream traceability
- governed ownership/integrity

Existing lineage architecture should be reused rather than unnecessarily redesigned.

Lineage remains a governed capability and must preserve established integrity rules.

---

## 3.5 Basic Governance / Accountability

Minimum behavior:

- owner
- steward where applicable
- lifecycle/status
- basic classification where applicable

Initial lifecycle may use a simple model such as:

`Draft → Active → Retired`

A general-purpose workflow engine is not required for the MVP.

Approval may initially be represented through governed state rather than a complex workflow system.

---

# 4. MVP Relationship Model

The core platform should connect the five capabilities.

Conceptually:

```text
Source System
    ↓
Database
    ↓
Schema
    ↓
Table
    ↓
Column / Data Asset
    ↓
Business Term
    ↓
Data Quality Rule / Result
    ↓
Lineage
    ↓
Downstream Asset
```

Ownership/accountability and governance status apply across relevant governed objects.

The MVP is not complete merely because individual modules exist.

The relationships between them must work.

---

# 5. Minimum User Outcomes

The MVP should allow a user to answer:

1. What data assets exist?
2. Where does an asset exist technically?
3. What does the data mean?
4. Which business term describes it?
5. What data-quality rules/results apply?
6. Where did the data come from?
7. Where does it go?
8. What transformations occur?
9. Who owns or stewards it?
10. What is its current governance status?

Basic retrieval/filtering is sufficient initially.

Advanced enterprise search is deferred.

---

# 6. Product Architecture Boundary

Current architectural direction:

```text
Frontend
    ↓
FastAPI Governance APIs
    ↓
Services
    ↓
Repositories
    ↓
SQLAlchemy
    ↓
PostgreSQL
```

Frontend target:

- React
- TypeScript
- MUI

Backend:

- FastAPI
- Python
- SQLAlchemy
- Alembic
- PostgreSQL

The deterministic governance platform is the authoritative system of record.

A future AI Intelligence Layer may sit above the deterministic governance platform.

AI is **not required for the current MVP**.

---

# 7. Explicit MVP Non-Goals

The following are intentionally deferred unless the product owner explicitly changes scope:

- AI assistants
- multi-agent governance
- complex AI routing
- advanced semantic/vector search
- full workflow engine
- enterprise policy management
- comprehensive business rules engine
- CDE management
- advanced classification automation
- advanced stewardship work queues
- executive dashboards
- advanced reporting
- enterprise connector/harvesting framework
- complex notifications/SLA
- advanced RBAC/ABAC
- centralized enterprise audit/event platform
- full deployment automation
- large-scale performance optimization

These must not be introduced simply because they appeared in older roadmap documents.

---

# 8. Development Operating Contract

Development is governed by the **DGM Development Operating Standard v1.1**.

Core lifecycle:

```text
Define
  ↓
Preflight
  ↓
Implement
  ↓
Verify
  ↓
Evidence
  ↓
Review
  ↓
Fix if needed
  ↓
PR / Merge
  ↓
Local Sync
  ↓
Local Verify
  ↓
Close
```

Every work package must be bounded and independently verifiable.

The package must have:

- one primary purpose
- clear objective
- explicit scope
- explicit exclusions
- acceptance criteria
- preflight
- validation
- evidence
- Git boundary
- completion status

### Required status vocabulary

Use only:

- `PASS`
- `FAIL`
- `BLOCKED`
- `INCOMPLETE`
- `COMPLETE`

Do not convert `BLOCKED` into `PASS`.

Do not claim runtime success from static inspection.

Do not weaken the environment or test strategy simply to manufacture a passing result.

---

# 9. AI / Coding Agent Rules

Any AI coding agent must:

1. Read `AGENTS.md`.
2. Read this `DGM_PROJECT_CONTEXT.md`.
3. Inspect the current Git working tree.
4. Verify the stated checkpoint.
5. Read the active work package.
6. Read only relevant architecture/product documentation.
7. Perform required environment/database preflight.
8. Implement only the active work package.
9. Run required validation.
10. Produce evidence.
11. Update project context/state as required.
12. Report blockers rather than guessing.

The agent must preserve existing work.

The agent must not:

- reset the repository
- clean the working tree
- delete `.before_*` files
- overwrite existing work without inspection
- silently expand scope
- make destructive database changes without approval
- weaken constraints merely to make tests pass
- make major architectural decisions silently
- describe planned functionality as implemented

When uncertain:

> STOP — do not guess.

Report:

1. what is known
2. what is uncertain
3. why it matters
4. what evidence is needed
5. what decision is required

---

# 10. Architectural Decisions That Must Be Preserved

The following decisions are durable unless explicitly changed by the product owner.

## Lineage

### Transformation ownership

A lineage transformation belongs to one lineage flow.

### Target ownership

A governed lineage target belongs to one lineage transformation.

### Mapping ownership

A governed lineage mapping requires a lineage target.

### Transformation flow mutability

A transformation's lineage flow is immutable after creation.

### Legacy migration compatibility

Historical migrations may require nullable relationship columns to preserve legacy-read compatibility.

Hard enforcement requires governed remediation before tightening constraints.

### Lineage governance

Lineage relationships must preserve:

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

AI-discovered lineage remains a candidate until appropriately reviewed and approved.

AI must not silently publish governed lineage.

---

# 11. Development Governance Decisions

- The repository is the source of truth.
- AI models are replaceable execution components.
- Project knowledge must remain in the repository.
- Development is organized into bounded work packages.
- Major architectural decisions require human/orchestration review.
- Existing work must not be destroyed or silently replaced.
- Git commits are not created by coding agents unless explicitly requested.
- Product scope is controlled by the human product owner.
- The smallest safe change that satisfies the active work package is preferred.

---

# 12. Verified Implementation Progress

## Package 03 — Metadata Asset Registration and Retrieval

**Status: COMPLETE**

Package 03 established the initial metadata asset registration/retrieval capability.

### Approved correction

Commit:

`484a4dfb5444d80bdd4fa00b1e561db3a6f70fd9`

Message:

`Configure PostgreSQL test harness for backend tests`

Parent:

`6e5ce4440fa48026a4e10039fd4c8905b6faad88`

The parent implementation commit was:

`6e5ce4440fa48026a4e10039fd4c8905b6faad88`

Message:

`[Jules-Backend] Implement Metadata Asset Registration and Retrieval`

### Package 03 functional coverage

The package covered:

1. successful metadata asset creation
2. creation with source-system reference
3. duplicate `(asset_type, asset_identifier)` rejection → HTTP 409
4. invalid request → HTTP 422
5. retrieval by ID
6. missing asset → HTTP 404
7. listing/pagination

### Verified local tests

Targeted test command:

```bash
DATABASE_URL="postgresql+psycopg2://governance_admin:governance_password@localhost:5432/enterprise_governance_test" /home/alben/Projects/enterprise-data-governance-platform/.venv/bin/pytest -q backend/tests/test_metadata_asset.py
```

Result:

```text
7 passed, 2 warnings in 0.93s
```

Full backend regression:

```bash
DATABASE_URL="postgresql+psycopg2://governance_admin:governance_password@localhost:5432/enterprise_governance_test" /home/alben/Projects/enterprise-data-governance-platform/.venv/bin/pytest -q backend/tests
```

Result:

```text
19 passed, 1 skipped, 2 warnings in 0.88s
```

The single skip is a pre-existing framework/migration compatibility skip.

`git diff --check` was clean.

### PostgreSQL test environment

Local PostgreSQL is Docker-based.

Relevant environment:

- container: `governance_postgres`
- image: `postgres:17`
- host port: `5432`
- database: `enterprise_governance_test`
- database owner: `governance_admin`

Backend container:

- `governance_backend`
- image: `docker-backend`
- port: `8000`

### Package 03 final Git state

Final local HEAD:

`04290c28696791a699ff236322caaab83797669f`

Local:

- branch: `feature/project-foundation`
- `origin/feature/project-foundation` matched local HEAD
- ahead: 0
- behind: 0

### Package 03 PR

PR:

`#6`

Title:

`Package 03: Configure PostgreSQL test harness`

Base:

`feature/project-foundation`

Head:

`integration/package-03-correction`

Merge commit:

`04290c28696791a699ff236322caaab83797669f`

Status:

- merged
- closed
- 3 files changed
- 134 additions
- 3 deletions

Package 03 is therefore **formally COMPLETE**.

---

# 13. Existing Local Artifacts That Must Be Preserved

The verified local state contains uncommitted artifacts that must not be deleted, reset, cleaned, or stashed without explicit authorization.

Tracked deletions:

- `Test reports/Evaluation_03_DGM_Metadata_Repository_Development_Report.md`
- `Test reports/Jules-Handoff-Commit-20260925-115127.md`

Untracked:

- `Test reports/Archive/*.md`
- `Test reports/Package-03-Test-Execution-SQLite.md`
- `backend/app/models/__init__.py.before-jules-metadata-import-fix-20260925-114315`

Any future agent must inspect current `git status` rather than assuming this list remains unchanged.

---

# 14. Current Project State

The previous AI_CONTEXT documents contain historical state describing:

- Platform Foundation
- Lineage Governance
- Batch 09
- AI Development Operating System

Those documents are historical context and must not override the current MVP product direction described here.

The project has now deliberately simplified the immediate product scope.

### Current strategic direction

The next development effort should continue building the **minimum Governance Platform MVP**, not expand into the previously envisioned broad enterprise platform.

The current priority is to complete the five connected MVP capabilities:

```text
Metadata
Business Meaning
Data Quality
Lineage
Accountability
```

---

# 15. Package Sequence for the MVP

The working package sequence is:

| Package | Capability | Status |
|---|---|---|
| Package 03 | Data Asset Registration & Retrieval | COMPLETE |
| Package 04 | Core Metadata Repository Expansion | NEXT CANDIDATE |
| Package 05 | Business Glossary Core | PLANNED |
| Package 06 | Data Quality Core | PLANNED |
| Package 07 | Lineage Runtime Completion | PLANNED |
| Package 08 | Basic Governance / Ownership | PLANNED |
| Package 09 | Core Integration | PLANNED |

This sequence is a planning baseline, not permission to implement the next package blindly.

The next package must be selected only after repository verification and dependency analysis.

---

# 16. How the Next Package Must Be Selected

Before defining the next package, the orchestrating AI should:

1. Read this file.
2. Inspect the repository Git state.
3. Confirm Package 03 remains merged and locally synchronized.
4. Inspect the implemented metadata/domain model.
5. Inspect existing lineage implementation.
6. Inspect current tests and migrations.
7. Check for uncommitted user work.
8. Identify what MVP capability is genuinely missing or incomplete.
9. Identify dependencies between the missing capability and existing implementation.
10. Select the **smallest bounded package** that advances the MVP.
11. Define acceptance criteria before implementation.
12. Perform environment/database preflight.
13. Execute through the DGM Development Operating Standard v1.1.

### Critical planning rule

Do **not** select a package simply because it is the next number.

The next package must be justified by:

- current product requirements
- actual repository state
- existing implementation
- tests/evidence
- dependencies
- smallest safe increment

---

# 17. MVP Completion Gate

The Governance Platform MVP should ultimately allow a user to:

- register/retrieve a governed data asset
- understand its technical location
- associate business meaning
- associate basic data-quality rules/results
- trace lineage
- identify owner/steward
- see current governance status
- perform basic retrieval/filtering
- persist data in PostgreSQL
- use tested APIs and a basic UI

The MVP is **not complete** merely because separate modules exist.

The relationships between the capabilities must work.

---

# 18. Deferred Future Layers

After the MVP is proven, future expansion may include:

- advanced governance workflows
- advanced impact analysis
- richer audit/versioning
- enterprise search
- dashboards/reporting
- advanced data-quality execution
- connectors/harvesting
- AI governance layer
- AI gateway
- model routing
- governance assistants

These are future capabilities.

They should not drive current MVP package selection unless the product owner explicitly changes the scope.

---

# 19. Current Environment Baseline

Known development environment:

- OS: Ubuntu/Xubuntu
- Python: 3.14.4
- project-local virtual environment: `.venv`
- backend: FastAPI / Python
- ORM: SQLAlchemy
- migrations: Alembic
- database: PostgreSQL
- frontend target: React / TypeScript / MUI
- Git branch: `feature/project-foundation`

Runtime/database availability must still be verified during each relevant package preflight.

Do not assume the environment is operational merely because it was operational for a previous package.

---

# 20. Evidence and Completion Rules

A package is not complete because code exists.

Completion requires evidence covering, as applicable:

- implementation
- focused tests
- API tests
- database/migration validation
- regression tests
- `git diff --check`
- Git state
- PR/merge state
- local synchronization
- local verification
- completion report
- required documentation/context updates

Validation must be reported using:

`PASS / FAIL / BLOCKED / NOT RUN`

The completion state should only be `COMPLETE` when the required completion gate has been satisfied.

---

# 21. Context Maintenance Rules

This file must be updated after every meaningful completed work package or major product decision.

When updating it:

### Always update

- current package
- package status
- completed work
- validation evidence
- current Git checkpoint
- current blockers
- next package candidate
- important architectural/product decisions
- deferred scope if changed

### Never update based only on assumption

Do not mark something complete because:

- code appears to exist
- a previous model said it was complete
- a plan says it should be complete
- a test was intended but not executed
- a different environment passed
- a PR is expected but not merged

Only verified evidence supports completion.

---

# 22. What Supporting Documents Are For

This document is the **current continuity snapshot**.

Supporting documents retain specialized information:

### `AI_CONTEXT/MASTER_EXECUTION_PROTOCOL.md`

Defines how AI coding agents execute work, including startup, work-package, validation, handoff, and stop rules.

### `AI_CONTEXT/DECISIONS.md`

Contains durable architectural/development decisions.

### `AI_CONTEXT/BLOCKERS.md`

Contains active and historical blockers.

### `AI_CONTEXT/PROGRESS_LEDGER.md`

Contains the compact historical progress record.

### `AI_CONTEXT/WORK_PACKAGE_TEMPLATE.md`

Defines the standard structure for future packages.

### `AI_CONTEXT/AGENT_COMPLETION_REPORT.md`

Defines the completion-report structure.

### `AI_CONTEXT/ROADMAP.md`

Contains roadmap/history and should not override the current MVP product requirement.

### `AI_CONTEXT/HANDOFF.md`

Historical/compatibility handoff document. This canonical context file should contain the current checkpoint needed for continuity.

### `AI_CONTEXT/CURRENT_WORK.md`

Historical/compatibility current-work record. The canonical context file should contain the current active checkpoint.

### `AI_CONTEXT/PROJECT_STATE.md`

Historical/compatibility project-state record. The canonical context file should contain the current project state.

---

# 23. Startup Instructions for the Next AI

When a new AI/model enters this project, it should begin here.

Read:

```text
AI_CONTEXT/DGM_PROJECT_CONTEXT.md
```

Then:

```text
AGENTS.md
```

Then inspect:

```bash
git status --short
git branch --show-current
git log -5 --oneline
```

Then inspect the active package and only the relevant source/tests/docs.

Do not assume that historical AI_CONTEXT files describe the current product direction.

Do not restart completed work.

Do not broaden the MVP.

Do not create a new package until the repository state has been verified.

---

# 24. Current Checkpoint

## Product

**MVP Governance Platform**

## Core

**Metadata + Business Meaning + Data Quality + Lineage + Accountability**

## Last formally completed package

**Package 03 — Data Asset Registration & Retrieval**

## Last verified local HEAD

`04290c28696791a699ff236322caaab83797669f`

## Current branch

`feature/project-foundation`

## Immediate next planning task

**Inspect the verified repository state and define the smallest appropriate next MVP work package.**

The likely candidate is:

**Package 04 — Core Metadata Repository Expansion**

but this must be verified against the actual repository before implementation.

## Current blocker

No known active blocker recorded.

## Current product-level constraint

**Do not allow the Governance Platform to grow back into the previously broad enterprise scope during MVP development.**

---

# 25. Golden Rule

> **Build the smallest reliable governance platform that connects Metadata, Business Meaning, Data Quality, Lineage, and Accountability.**

> **Verify the repository before planning the next package.**

> **Use evidence—not assumptions—to describe project progress.**

> **The next AI continues from the verified checkpoint; it does not restart the project.**
---
# VERIFIED PROJECT CHECKPOINT — 2026-10-01

## Package 04 — Core Metadata Repository Expansion

**Status: COMPLETE**

Package 04 established the minimum technical metadata hierarchy: Source System → Database → Schema → Table → Column → Data Asset.

### Verification

- Package-specific tests: **12 passed, 2 warnings**
- Full backend regression: **31 passed, 1 skipped, 2 warnings**
- PostgreSQL verification completed
- `git diff --check`: **PASS**
- Jules verification evidence: 31 passing tests
- Evidence artifact: `package-04-verification-report.zip`

### Git

- Branch: `feature/package-04-metadata-repository-expansion`
- Verified HEAD: `f4688c6439685c583800caa38bf0b1084e53a7ca`
- PR #7: **MERGED**
- Local/remote synchronization: **0 ahead / 0 behind**

### Completion

Package 04 implementation, verification, evidence, merge, local synchronization, and local verification are complete.

**PACKAGE 04: COMPLETE**

### Next Package Candidate

**Package 05 — Business Glossary Core** is the current next-package candidate. Before implementation, perform repository and dependency preflight against the PRD, DGM Development Operating Standard v1.1, current source code, existing glossary-related models/APIs/tests, Package 04 dependencies, and the smallest safe MVP increment.

### Continuity Rule

Every concluded build/work package must update `AI_CONTEXT/DGM_PROJECT_CONTEXT.md` before that package is considered closed.

Required sequence: Implement → Verify → Evidence → PR/Merge → Local Sync → Local Verify → Update DGM_PROJECT_CONTEXT.md → Close.
---
# VERIFIED PROJECT CHECKPOINT — 2026-10-01

## Package 04 — Core Metadata Repository Expansion

**Status: COMPLETE**

Package 04 established the minimum technical metadata hierarchy: Source System → Database → Schema → Table → Column → Data Asset.

### Verification

- Package-specific tests: **12 passed, 2 warnings**
- Full backend regression: **31 passed, 1 skipped, 2 warnings**
- PostgreSQL verification completed
- `git diff --check`: **PASS**
- Jules verification evidence: 31 passing tests
- Evidence: `package-04-verification-report.zip`

### Git

- Branch: `feature/package-04-metadata-repository-expansion`
- HEAD: `f4688c6439685c583800caa38bf0b1084e53a7ca`
- PR #7: **MERGED**
- Local/remote synchronization: **0 ahead / 0 behind**

### Completion

Package 04 implementation, verification, evidence, merge, local synchronization, and local verification are complete.

**PACKAGE 04: COMPLETE**

### Next Package Candidate

**Package 05 — Business Glossary Core** is the current next-package candidate. Before implementation, perform repository and dependency preflight against the PRD, DGM Development Operating Standard v1.1, current source code, existing glossary models/APIs/tests, Package 04 dependencies, and the smallest safe MVP increment.

### Continuity Rule

Every concluded build/work package must update `AI_CONTEXT/DGM_PROJECT_CONTEXT.md` before that package is considered closed.

Required sequence: Implement → Verify → Evidence → PR/Merge → Local Sync → Local Verify → Update DGM_PROJECT_CONTEXT.md → Close.
