# DGM Architecture Skill

## Purpose

Protect the DGM enterprise architecture and prevent coding agents from
silently weakening or bypassing established architectural decisions.

## Required Context

Read:

- AGENTS.md
- AI_CONTEXT/HANDOFF.md
- AI_CONTEXT/PROJECT_STATE.md
- AI_CONTEXT/DECISIONS.md
- AI_CONTEXT/ROADMAP.md
- docs/architecture/ProductContext.md when relevant
- Relevant numbered architecture documents
- Relevant module-level logical, physical, API and UI documents

## Architecture Layers

Preserve the distinction between:

1. Project Vision
2. Business Requirements
3. Enterprise Business Model
4. Conceptual Model
5. Logical Model
6. Physical Model
7. API Design
8. UI Design
9. Data Dictionary
10. Naming Standards

Also preserve module-level architecture documentation.

## Core Rule

Do not make implementation decisions that silently redefine the documented
business or architectural model.

When implementation and architecture disagree:

1. Identify the discrepancy.
2. Determine whether it is intentional, transitional, or a defect.
3. Do not silently rewrite either side.
4. Escalate material architectural decisions.

## Implemented vs Planned

Always distinguish:

- Implemented
- Partially implemented
- Documented/planned
- Future

Never describe planned architecture as implemented functionality.

## AI Architecture

The deterministic governance platform remains the system of record.

AI is a governed intelligence layer.

AI may:

- discover
- recommend
- explain
- assist

AI must not silently publish governed changes.

Human governance/review remains required where defined by the product architecture.
