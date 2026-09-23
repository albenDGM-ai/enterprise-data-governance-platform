# WP-009 — AI Development Operating System

## Objective

Create a persistent, model-independent AI-assisted development framework
for the DGM project.

## Problem

Coding models have finite context, changing quotas, and different capabilities.
The DGM project must remain resumable when switching between models.

## Required Outcome

Any supported coding model should be able to:

1. understand the current project state
2. understand the active work package
3. understand relevant architecture decisions
4. inspect the repository
5. continue the implementation
6. validate its work
7. leave a reliable handoff for the next model

## Scope

- AI_CONTEXT
- shared agent skills
- handoff protocol
- work-package protocol
- progress tracking

## Out of Scope

- DGM application AI gateway
- model API integration
- production AI agents
- database changes
- frontend changes

## Acceptance Criteria

1. AI_CONTEXT structure exists.
2. Handoff protocol exists.
3. Project state exists.
4. Progress ledger exists.
5. Decision log exists.
6. Blocker log exists.
7. Roadmap exists.
8. Machine-readable state exists.
9. Shared skills structure exists.
10. Model-switching can be performed without relying on chat history.

## Stop Conditions

Stop if implementation requires a major architectural decision.

## Completion Artifacts

- AI_CONTEXT/*
- .agents/skills/*
- Test reports/Batch-09*
