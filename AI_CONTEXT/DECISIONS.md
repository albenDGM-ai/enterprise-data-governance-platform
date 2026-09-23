# DGM Architecture and Development Decisions

## Purpose

Record durable decisions that coding agents must not silently reverse.

## Lineage

### Transformation Ownership

A lineage transformation belongs to one lineage flow.

### Target Ownership

A governed lineage target belongs to one lineage transformation.

### Mapping Ownership

A governed lineage mapping requires a lineage target.

### Transformation Flow Mutability

A transformation's lineage flow is immutable after creation.

### Legacy Migration Strategy

New relationship columns may remain nullable during the initial migration
phase to preserve legacy-read compatibility.

Hard enforcement requires governed remediation before tightening constraints.

## Development

### Repository as Source of Truth

AI models are replaceable execution components.

Project knowledge must remain in the repository.

### Work Package Model

AI coding work must be bounded by explicit work packages and acceptance
criteria.

### Human Architectural Control

Major architectural decisions require human/orchestration review.

### Git

Do not create commits unless explicitly requested.
