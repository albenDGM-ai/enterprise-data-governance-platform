# DGM AI Handoff

## Purpose

This document allows one AI coding agent to hand DGM development to another
AI coding agent without losing project context.

## Mission

Continue development of the Enterprise Data Governance Platform.

## Current Phase

Platform Foundation

## Current Workstream

Lineage Governance

## Current Work Package

WP-009 — AI Development Operating System

## Last Completed Major Work

Batch 08 established lineage graph integrity and corrected the transformation
API update contract. WP-009.3 successfully verified and aligned the Batch-07
compatibility test with the strict NOT NULL Batch-08 contract (13 tests passing
successfully), followed by a scope-integrity audit confirming `env.py` formatting
provenance.

## Current Objective

Establish the model-independent AI development operating system.

## Important Architectural Rules

1. Preserve the existing DGM documentation structure.
2. Preserve existing business, conceptual, logical, physical, API, and UI
   separation.
3. Do not destroy or reset existing work.
4. Do not overwrite `.before_*` files.
5. Do not make destructive database changes without explicit approval.
6. Lineage relationships must preserve governed graph integrity.
7. Transformation flow ownership is immutable after creation.
8. Governed lineage records must have valid active parent relationships.
9. Physical migration compatibility may require nullable legacy columns.
10. AI-generated lineage must remain subject to human governance/review.

## Current Development Method

Development is organized into small bounded work packages.

Each work package must define:

- objective
- scope
- exclusions
- acceptance criteria
- validation
- stop conditions
- completion artifacts

## Model Switching Protocol

A coding agent must:

1. Read AGENTS.md.
2. Read this HANDOFF.md.
3. Read PROJECT_STATE.md.
4. Read CURRENT_WORK.md.
5. Read the active work package.
6. Read only the relevant architecture/product documentation.
7. Inspect the current repository state.
8. Verify the stated state before modifying anything.
9. Implement only the active work package.
10. Run the required validation.
11. Update the handoff/state documents.
12. Produce a concise completion report.

## Escalate Instead of Guessing

Stop and request orchestration guidance when:

- requirements conflict
- architecture is unclear
- a destructive migration is required
- a major domain model decision is required
- existing documentation conflicts materially with code
- security/privacy implications are unclear
- the requested change exceeds the current work package

## Handoff Rule

The next AI must continue from the current checkpoint.

It must not restart completed work merely because it is a different model.
