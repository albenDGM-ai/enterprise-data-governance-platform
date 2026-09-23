# DGM Product Context — Current Progress

**Product:** Enterprise Data Governance Platform (DGM)  
**Document:** Product Context and Progress Baseline  
**Status:** Living project-context document  
**Last Updated:** 19 September 2026

---

## 1. Purpose

This document captures the current product context, implementation maturity, architectural direction, and progress baseline for the Enterprise Data Governance Platform (DGM).

It is intended to provide a stable context source for future development work, coding-agent sessions, architecture decisions, AI implementation, testing, and roadmap planning.

Completion percentages are **indicative product-capability estimates**, not formal project-management KPIs. They represent approximate usable capability across requirements, architecture, data model, backend behavior, API foundation, validation, and testing.

---

## 2. Product Vision

DGM is intended to be an enterprise data-governance platform providing a governed system of record for:

- enterprise metadata
- business meaning
- data quality
- ownership
- stewardship
- policies
- business rules
- critical data elements
- data lineage
- governance workflows
- auditability
- search
- reporting
- AI-assisted governance

The platform is intended to combine deterministic governance controls with AI capabilities rather than allowing AI to bypass governance controls.

### AI governance principle

> AI may discover, recommend, explain, and assist; governed publication remains subject to enterprise controls and appropriate human review.

---

## 3. Core Product Capability Areas

1. Metadata Management
2. Business Glossary Management
3. Enterprise Business Modeling
4. Data Governance
5. Data Ownership
6. Data Stewardship
7. Data Classification
8. Policy Management
9. Business Rules Management
10. Critical Data Element (CDE) Management
11. Data Quality Management
12. Data Lineage
13. Workflow Management
14. Audit Management
15. Security Management
16. Reporting and Dashboards
17. Enterprise Search

These capabilities are intended to operate as an integrated governance platform rather than as independent applications.

---

## 4. Current Product Architecture Direction

The intended architecture separates the deterministic governance platform from the AI intelligence layer.

```text
                    Enterprise DGM
                          |
          +---------------+---------------+
          |                               |
   Deterministic Governance          AI Intelligence
          |                               |
   PostgreSQL                         SLM / LLM
   SQLAlchemy                         Embeddings
   Alembic                            Retrieval / RAG
   FastAPI                            AI Agents
   Governance APIs                    Recommendations
   Audit / Controls                   Explanations
          |                               |
          +---------------+---------------+
                          |
                  Human Governance
                   / Review / Approval
```

The deterministic layer is the system of record. AI operates as a governed intelligence layer over enterprise metadata and the governance graph.

---

## 5. Current Technical Foundation

### Main technology direction

- Python / FastAPI
- SQLAlchemy ORM
- Pydantic
- Alembic
- PostgreSQL
- Docker Compose
- pytest
- Git

### Development branch

`feature/project-foundation`

### Current lineage migration head

`e2d453a0ad03`

---

## 6. Documentation Baseline

The established architecture documentation sequence is:

```text
01_ProjectVision.md
02_BusinessRequirements.md
03_EnterpriseBusinessModel.md
04_ConceptualModel.md
05_LogicalModel.md
06_PhysicalModel.md
07_API_Design.md
08_UI_Design.md
09_DataDictionary.md
10_NamingStandards.md
```

Lineage-specific architecture documentation includes:

```text
docs/architecture/logical/DataLineageLogicalModel.md
docs/architecture/physical/DataLineagePhysicalModel.md
docs/architecture/api/DataLineageAPI.md
docs/architecture/ui/DataLineageUI.md
```

This document is a product-context supplement and does not replace the architecture baseline.

---

# 7. Capability Progress Baseline

| Capability | Indicative maturity | Current position |
|---|---:|---|
| Metadata Management | 25–30% | Core objective and architecture direction established; ingestion/catalog/operational management remain |
| Business Glossary Management | 15–20% | Identified core capability; glossary model, lifecycle, UI and workflows remain |
| Enterprise Business Modeling | 40–50% | Domain/capability modeling and enterprise context substantially defined; operational implementation remains |
| Data Governance | 30–35% | Governance is the central product purpose; operational governance framework remains |
| Data Ownership | 15–20% | Ownership concepts/fields established; owner registry and lifecycle workflows remain |
| Data Stewardship | 15–20% | Stewardship recognized as core role; assignments/work queues/workflows remain |
| Data Classification | 5–10% | Capability identified; implementation largely future, including AI assistance |
| Policy Management | 5–10% | Target capability identified; repository/lifecycle/approval remain |
| Business Rules Management | 10–15% | Concept established; repository/lifecycle/evaluation remain |
| CDE Management | 5–10% | Capability identified; repository and lifecycle remain |
| Data Quality Management | 15–20% | Central capability direction established; profiling/rules/scorecards/issues remain |
| **Data Lineage** | **70–80%** | Most mature area: models, migrations, services, validation, discovery, mapping, impact/version/snapshot foundations and tests |
| Workflow Management | 10–15% | Governance workflow direction established; engine and approvals remain |
| Audit Management | 15–20% | Auditability is an architectural principle; central audit/event framework remains |
| Security Management | 10–15% | Enterprise security recognized; authentication/RBAC/authorization remain |
| Reporting and Dashboards | 5–10% | Target capability identified; reporting/KPI/dashboard implementation remains |
| Enterprise Search | 5–10% | Target capability identified; unified/semantic search remains |

These estimates are directional and should be updated as implementation progresses.

---

# 8. Data Lineage — Current Most Mature Capability

**Indicative maturity: 70–80%**

### Implemented or established

- Lineage Process
- Lineage Flow
- Lineage Transformation
- Lineage Target
- Lineage Mapping
- Foreign-key relationships
- Relationship validation services
- Lineage discovery service foundation
- Impact analysis foundation
- Version foundation
- Snapshot foundation
- CRUD/service architecture
- Discovery filtering
- Governance-oriented validation
- API foundation
- Lineage architecture documentation
- Automated graph-integrity tests

### Current relationship model

```text
Source
  |
  v
Process
  |
  v
Flow
  |
  v
Transformation
  |
  v
Target
  |
  v
Mapping
```

Target → Transformation and Mapping → Target are now required relationships in the ORM/database contract.

### Current validation state

- Alembic migration graph: clean
- Current migration head: `e2d453a0ad03`
- Alembic check: clean
- Batch 08 graph-integrity tests: **8/8 passing**
- PostgreSQL relationship columns: `NOT NULL`

### Current issue

Batch 07 contains a historical transition-compatibility test that still expects the ORM relationship columns to be nullable. The current Batch 08 and database contract require them to be non-nullable.

This is a **test-contract reconciliation issue**, not a reason to weaken the current governed database relationship.

Response schemas retain nullable typing where required for legacy-read/discovery compatibility.

---

# 9. Other Capability Context

## Metadata Management — 25–30%

### Established

- Metadata repository is a core DGM objective.
- Metadata is intended to feed lineage, search, governance, and AI.

### Remaining

- Metadata harvesting/connectors
- Catalog APIs
- Metadata lifecycle
- Metadata UI
- Technical/business metadata reconciliation
- Metadata versioning

## Business Glossary — 15–20%

### Established

- Identified as a core DGM capability.
- Intended to connect business meaning with metadata and business modeling.

### Remaining

- Term model
- Definitions/synonyms
- Ownership/stewardship
- Data-asset relationships
- Approval lifecycle
- UI/search

## Enterprise Business Modeling — 40–50%

### Established

- Enterprise Business Model is part of the architecture baseline.
- Business Domain Catalog and Business Capability Catalog are established concepts.

### Remaining

- Full operational repository
- APIs
- UI visualization
- Relationships to glossary/metadata/CDE/policies/lineage
- Lifecycle governance

## Data Governance — 30–35%

### Established

- Central product purpose.
- Governance principles.
- Ownership, stewardship, lineage, versioning, auditability and reviewability treated as governance concerns.

### Remaining

- Operational governance framework
- Governance workflows
- Governance issue management
- Governance dashboards
- End-to-end lifecycle

## Data Ownership — 15–20%

Ownership is represented in governance-oriented structures, but owner registry, assignment/change workflows, delegation and accountability views remain.

## Data Stewardship — 15–20%

Stewardship is a core governance role, but steward registry, assignments, work queues, actions, approvals and metrics remain.

## Data Classification — 5–10%

Classification is a target capability and future AI-assisted area. Taxonomy, repository, rules, AI classification, human review and audit remain.

## Policy Management — 5–10%

Policy governance is a target capability. Repository, lifecycle, ownership, applicability, versioning, approval and policy-to-control relationships remain.

## Business Rules — 10–15%

Rules are intended to connect data quality, policies, metadata and governance controls. Repository, lifecycle, evaluation and ownership remain.

## CDE Management — 5–10%

CDEs are intended to connect business meaning, classification, quality, ownership and lineage. Dedicated CDE repository/lifecycle/monitoring remain.

## Data Quality — 15–20%

DQ is intended as a central platform capability. Rule repository, profiling, dimensions, scorecards, measurements, exceptions, remediation and dashboards remain.

## Workflow — 10–15%

Governance workflow and human review are architectural requirements. Generic workflow engine, assignments, approvals, escalation, notifications and SLA tracking remain.

## Audit — 15–20%

Auditability is a core governance principle. Versioning and snapshots provide foundations, but a central immutable audit/event framework remains.

## Security — 10–15%

Security is an enterprise requirement. Authentication, RBAC/ABAC, object/domain permissions, masking and administration remain.

## Reporting and Dashboards — 5–10%

Reporting is a target capability. KPI framework, governance/DQ/lineage/stewardship dashboards and executive reporting remain.

## Enterprise Search — 5–10%

Search is a target capability spanning metadata, glossary, lineage, policies and rules. Unified indexing, relevance, facets, semantic/vector search and AI search remain.

---

# 10. Overall Product Maturity

A single percentage would be misleading because the capabilities are at very different stages.

A more useful planning picture is:

```text
Platform / Engineering Foundation       ~65%
Governance Capability Foundation        ~25–35%
Data Lineage                            ~70–80%
AI Runtime Capability                   ~5%
```

These are directional estimates, not formal KPIs.

---

# 11. AI Implementation Direction

AI is intended to be a governed intelligence layer rather than a standalone chatbot.

## First major AI target

**AI-assisted Lineage and Metadata Discovery**

```text
Enterprise Metadata / SQL / ETL / Governance Context
                         |
                         v
                    AI Engine
                         |
                         v
                Candidate Lineage
                         |
             +-----------+-----------+
             |                       |
       Confidence                 Evidence
             |                       |
             +-----------+-----------+
                         |
                         v
                   Human Review
                  /            \
             APPROVE           REJECT
                 |
                 v
          Governed DGM Lineage
```

AI should discover, recommend and explain lineage, but should not silently publish governed lineage.

---

# 12. AI Capability Roadmap

1. AI-assisted lineage discovery
2. AI mapping recommendations
3. Transformation detection
4. Metadata classification
5. Business glossary suggestions
6. AI-assisted CDE identification
7. Data-quality rule suggestions
8. Impact-analysis explanations
9. Governance copilot/search
10. Multi-agent governance workflows

The deterministic metadata/lineage foundation should remain the governed source of context for these capabilities.

---

# 13. AI Governance Requirements

AI-generated governance recommendations should be traceable through:

- model/provider
- model version
- prompt/instruction version where applicable
- metadata/context snapshot
- evidence
- recommendation
- confidence
- status
- reviewer
- review timestamp
- approval/rejection decision
- resulting governed change

This supports auditability and controlled human review.

---

# 14. Recommended Development Sequence

```text
1. Finish Lineage foundation and regression stabilization
                     |
                     v
2. Metadata Management
                     |
                     v
3. Business Glossary
                     |
                     v
4. Data Quality
                     |
                     v
5. CDE + Classification
                     |
                     v
6. Ownership + Stewardship
                     |
                     v
7. Policies + Business Rules
                     |
                     v
8. Workflow + Audit
                     |
                     v
9. Search + Reporting
                     |
                     v
10. Expand AI capabilities
```

AI should not necessarily wait until every governance module is complete. Once metadata, glossary and lineage are sufficiently stable, the first AI feature can begin in parallel.

---

# 15. Immediate Priority

1. Resolve the Batch 07/Batch 08 compatibility-test contract.
2. Restore the complete backend test suite to green.
3. Preserve the current database governance constraints.
4. Stabilize the metadata/governance foundation.
5. Introduce the AI abstraction and first AI-assisted lineage/metadata capability.

---

# 16. Development-Agent Context

Any coding agent working on DGM should use this document together with:

- `AGENTS.md`
- project vision
- business requirements
- architecture documentation
- logical/physical/API/UI designs
- current migrations
- automated tests
- test reports

Agents must clearly distinguish:

- **Implemented**
- **Partially implemented**
- **Documented/planned**
- **Future AI**

Planned capabilities must not be represented as implemented capabilities.

---

# 17. Current Baseline Summary

As of 19 September 2026:

- DGM has a functioning backend/platform foundation.
- Data Lineage is the most mature product capability.
- The lineage graph has explicit governed relationship constraints.
- Batch 08 graph-integrity tests pass 8/8.
- Current Alembic lineage head is `e2d453a0ad03`.
- The remaining Batch 07 failure is a historical test-contract mismatch with the newer governed relationship contract.
- Most broader governance capabilities have architecture/requirements direction but still require substantial implementation.
- The AI runtime layer has not yet been implemented.
- The intended first AI feature is AI-assisted lineage and metadata discovery with human review.

This document should be updated whenever a major capability moves from planned to implemented or its maturity materially changes.
