# DGM AI Agent Skill

## Purpose

Define how AI coding agents operate as replaceable execution components within
the DGM development operating system.

## Core Principle

The repository owns DGM knowledge.

The AI model is an execution component, not the authoritative owner of project
context.

Gemini, Groq, OpenAI-based agents, local models, or other coding agents must
follow the same repository-resident operating protocol.

## Startup Protocol

Before work:

1. Read AGENTS.md.
2. Read AI_CONTEXT/HANDOFF.md.
3. Read AI_CONTEXT/PROJECT_STATE.md.
4. Read AI_CONTEXT/CURRENT_WORK.md.
5. Read the active work package.
6. Read AI_CONTEXT/DECISIONS.md when relevant.
7. Read only the relevant product/architecture documentation.
8. Inspect repository state.
9. Verify that the stated checkpoint matches reality.

## Execution Protocol

1. Understand the work package.
2. Identify files likely to change.
3. Inspect existing implementation.
4. Implement only the bounded scope.
5. Preserve existing work.
6. Run required validation.
7. Update project state/handoff if the work package requires it.
8. Produce a concise completion report.

## Model Switching

A new model must:

- continue from the repository checkpoint
- not restart completed work
- not assume previous model reasoning is authoritative
- verify current state independently
- preserve established decisions
- report discrepancies

## Escalation

Stop and request orchestration guidance when:

- requirements conflict
- architecture is unclear
- destructive database changes are required
- a major domain decision is required
- documentation and implementation materially conflict
- security/privacy implications are unclear
- scope exceeds the active work package

## Security

Never expose:

- API keys
- passwords
- credentials
- tokens
- secrets
- production-sensitive data

Do not send real enterprise confidential data to external AI providers unless
explicitly authorized and governed.

## Provider Neutrality

Do not assume a particular AI provider.

The skill must work with Gemini, Groq, OpenAI-based agents, local runtimes,
and future coding models.
