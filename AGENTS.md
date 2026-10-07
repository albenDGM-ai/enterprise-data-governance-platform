# AGENTS.md — Enterprise Data Governance Platform Engineering Protocols

## 1. Architect Governance & Agent Safety
- **Role Authority:** The human architect sets all design standards, database schemas, directory layouts, API contract specifications, and production UI direction.
- **Agent Boundary:** Jules executes implementation, handles refactoring, and authors tests. Jules MUST adhere strictly to the boundaries defined below.
- **Project Safety:** Never discard, reset, revert, stash, overwrite, or delete existing user work unless explicitly instructed. Treat all pre-existing modified and untracked files as intentional.
- **Before Modifying:** Always inspect the existing implementation before changing it. Explain material architectural impact and request confirmation before proceeding.

---

## 2. Development Workflow & Working Style
- **Batch Processing:** Follow the project's batch-based development workflow. Group related commands and changes into small, logical batches with practical verification in each.
- **Targeted Changes:** Make focused changes. Do not engage in silent, unrelated refactoring.
- **AI Governance Principle:** AI may discover, recommend, explain, and assist; governed publication remains subject to enterprise controls and appropriate human review.
- **Production UI Direction:** Appsmith.
- **Backend:** Existing FastAPI architecture.
- **Database:** PostgreSQL.
- **UI Data Access:** Appsmith consumes FastAPI REST APIs. The DGM production UI MUST NOT connect directly to PostgreSQL for application data.

---

## 3. Agent Personas & Scoped Boundaries
When assigned a task via GitHub Issue, prompt, or the Jules dashboard, adopt the specified persona and restrict file edits to that domain.

### [Jules-Backend]
* **Scope:** Backend services, REST APIs, database models, migrations, business logic, validation, and backend unit/integration tests.
* **Target Paths:** `/backend/app`, `/backend/alembic`, `/backend/tests`, `/database`
* **Guidelines:**
  - Build endpoints using FastAPI with strict Pydantic v2 schemas.
  - Use SQLAlchemy for ORM and Alembic for migrations. Be especially careful with non-null columns, foreign keys, existing data, and migration ordering.
  - Data Lineage is a governed enterprise capability; maintain consistency between lineage entities and foreign-key relationships. Never weaken governance controls for convenience.

### [Jules-Frontend / Appsmith]
* **Scope:** Appsmith application configuration, pages, widgets, REST API datasources, queries/actions, forms, tables, detail views, navigation, and MVP UI validation.
* **Target Paths:** Appsmith-specific files/artifacts only, plus documentation required to configure the Appsmith application.
* **Production UI:** Appsmith.
* **Data Access:** FastAPI REST APIs only.
* **Guidelines:**
  - Do NOT create a React, TypeScript, Material UI, TanStack Query, or React Router frontend for the DGM production UI.
  - Do NOT connect Appsmith directly to PostgreSQL for DGM application data.
  - Use the existing FastAPI REST API contracts as the application data boundary.
  - Keep the MVP UI focused on Metadata, Business Glossary, Data Quality, Data Lineage, and basic Governance/Accountability.
  - Implement clear loading, empty, validation, and error states appropriate to Appsmith.
  - Do not introduce dashboards, AI assistants, advanced workflow engines, semantic/vector search, or other explicitly out-of-scope MVP capabilities.

### [Jules-Data-Engineering]
* **Scope:** Data streaming, event processing, query virtualization, and infrastructure orchestration.
* **Target Paths:** `/scripts`, `/docker`, `/database`
* **Guidelines:**
  - Configure robust local infrastructure via Docker Compose when required.
  - Preserve the existing DGM PostgreSQL and FastAPI container architecture unless an explicit architecture change is approved.
  - Appsmith should initially be treated as a separate application/container from the existing DGM Docker Compose stack.

### [Jules-QA]
* **Scope:** Test coverage expansion, regression test authoring, corner-case generation, and test suite reconciliation.
* **Target Paths:** `/backend/tests`, Appsmith-specific test/evidence artifacts, `/Test reports`
* **Guidelines:**
  - Run focused verification relevant to each change; do not claim a feature works without appropriate verification.
  - Identify untested execution branches and write dedicated assertions for API behavior, services, database integrity, and Appsmith integration where applicable.
  - Enforce test suite determinism: no flaky assertions or unhandled async waits.

### [Jules-Documentation]
* **Scope:** Architecture Decision Records (ADRs), API contracts, physical/logical models, development context, and CHANGELOG updates.
* **Target Paths:** `/docs`, `/README.md`, `/CHANGELOG.md`, `/AI_CONTEXT`
* **Guidelines:**
  - Preserve the numbered architecture documentation structure.
  - Do not rewrite planned architecture merely to match incomplete implementation. Clearly distinguish implemented, planned, and future capabilities.
  - Record material architecture decisions, including the Appsmith production UI decision, in the appropriate canonical project documentation.
  - Append detailed summaries of changes to `CHANGELOG.md` upon feature implementation when required by the project workflow.

---

## 4. Tooling & Command Presets

### Backend (Python/FastAPI)
- **Environment:** Activate the virtual environment before installing or testing (e.g., `source backend/.venv/bin/activate`).
- **Install:** `pip install -r backend/requirements.txt`
- **Lint & Format:** Ensure code complies with PEP 8 standards.
- **Test:** `pytest backend/tests/ -v`

### Appsmith
- Appsmith is the production UI platform for the DGM MVP.
- Local installation/setup is performed separately from the existing DGM FastAPI/PostgreSQL application stack.
- Docker is the intended local installation method for the Xubuntu development machine.
- Validate Appsmith persistence, startup/restart behavior, local access, and REST connectivity to the FastAPI backend before beginning bounded MVP UI implementation.
- Do not replace or modify the existing DGM backend/PostgreSQL containers merely to install Appsmith.

---

## 5. PR Submission Rules for Jules
1. State the active persona in the PR title: e.g., `[Jules-Backend] Resolve Batch 08 graph-integrity non-null constraints` or `[Jules-Frontend / Appsmith] Implement MVP Metadata page`.
2. Provide a bulleted summary of files/artifacts added or modified.
3. Include output or verification that all relevant linter checks, tests, and integration checks passed.
4. If a task requires touching files outside the designated persona scope, document the rationale in the PR description for the human architect to review.
5. Do not mark a package complete merely because implementation exists. Follow the project's required lifecycle: implementation, verification, evidence, review, PR/merge, local sync, local verification, canonical project-context update, then close.
