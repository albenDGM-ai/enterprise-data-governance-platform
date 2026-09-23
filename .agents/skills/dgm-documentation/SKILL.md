# DGM Documentation Skill

## Purpose

Maintain architecture and implementation documentation without allowing
documentation drift or accidental rewriting of the product model.

## Required Context

Read:

- AGENTS.md
- AI_CONTEXT/PROJECT_STATE.md
- AI_CONTEXT/HANDOFF.md
- relevant ProductContext
- relevant architecture documents
- relevant implementation/tests

## Documentation Rules

Preserve the numbered architecture sequence:

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

Preserve module-level logical, physical, API and UI documentation.

## Documentation Truth

Clearly label:

- Implemented
- Partially implemented
- Planned
- Future

Do not rewrite architecture merely to match incomplete implementation.

If code and documentation disagree, investigate before changing either.

## Change Discipline

Documentation changes should be:

- focused
- traceable to the work package
- consistent with existing terminology
- aligned with business semantics

Do not duplicate large sections of existing documentation unnecessarily.

## Validation

Check:

- internal consistency
- terminology
- links/references where practical
- `git diff --check`
