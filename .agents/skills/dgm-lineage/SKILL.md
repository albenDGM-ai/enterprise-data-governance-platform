# DGM Lineage Skill

## Purpose

Protect the governed enterprise lineage graph and its business semantics.

## Core Model

The current governed lineage relationship is:

Source
  |
Process
  |
Flow
  |
Transformation
  |
Target
  |
Mapping

## Governing Rules

- A transformation belongs to one lineage flow.
- Transformation flow ownership is immutable after creation.
- A governed target belongs to one lineage transformation.
- A governed mapping requires a lineage target.
- Cross-flow relationships are invalid.
- Inactive parents cannot satisfy governed relationships.
- AI/discovered lineage requires appropriate human review before governed
  publication.

## Required Validation

For lineage changes inspect:

- lineage process
- lineage flow
- lineage transformation
- lineage target
- lineage mapping
- relationship validation services
- discovery services
- impact analysis
- versions
- snapshots
- API contracts
- lineage tests
- logical/physical/API/UI lineage documentation

## Graph Integrity

Never implement graph traversal that can cross unrelated flows through
inconsistent relationship paths.

The persisted relationship graph and the governed business relationship model
must agree.

## Discovery

Discovery is not equivalent to publication.

A discovered relationship may be:

- candidate
- reviewed
- approved
- rejected

Do not silently convert discovery into governed lineage.

## AI Lineage

AI-generated lineage must retain evidence and remain reviewable.

The AI must not bypass deterministic lineage controls.

## Validation

Prefer focused graph-integrity tests and service validation before broader
integration testing.
