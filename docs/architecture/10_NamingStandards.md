# Enterprise Data Governance Platform

## Naming Standards

Version: 1.0

Author: Alben David Jaypaul

Purpose

This document defines the naming standards used throughout the Enterprise Data Governance Platform to ensure consistency, maintainability, and readability across the entire solution.

All developers, architects, DBAs, and AI coding assistants must follow these standards.

# 1. General Principles

The following principles apply throughout the project.

• Use English only.

• Avoid abbreviations unless industry standard.

• Use meaningful names.

• Do not use spaces.

• Do not use special characters.

• Keep names descriptive.

• Maintain consistency.

• Prefer full words.

## Example

GOOD

customer_identifier

BAD

custid

cid

cust_no

# 2. Database Standards

Database names

## Rules

Use lowercase

Use snake_case

Use descriptive names

## Example

enterprise_governance

metadata_repository

baning_analytics

# 3. Schema Standards

## Rules

Lowercase

snake_case

Business oriented

## Examples

metadata

glossary

dq

lineage

security

audit

workflow

# 4. Table Standards

## Rules

Lowercase

snake_case

Singular nouns

No prefixes

## Examples

business_term

metadata_table

metadata_column

data_owner

data_steward

classification

# 5. Column Standards

## Rules

Lowercase

snake_case

Business friendly

## Examples

business_term_name

database_name

column_name
ata_type
description

# 6. Primary Keys

## Pattern

<table_name>_id

## Examples

domain_id

database_id

schema_id

table_id

column_id

business_term_id

# 7. Foreign Key Standards

## Rule

Foreign keys must always have the exact same name as the primary key they reference.

## Example

metadata_table

Primary Key

table_id

metadata_column

Foreign Key

table_id

## Do NOT use

tblid

parent_table

table_reference

## Why?

Using identical names makes joins easier to understand and allows developers and AI assistants to immediately identify relationships between entities.

# 8. Audit Column Standards

Every table must contain the following audit columns.

| Column | Description |
|----------|-------------|
| created_at | Record creation timestamp |
| created_by | User who created the record |
| updated_at | Last modification timestamp |
| updated_by | User who last modified the record |
| is_active | Indicates whether the record is active |
| is_deleted | Soft delete indicator |

## Why?

Enterprise systems must maintain an audit trail for governance, regulatory compliance, and troubleshooting.

# 9. Boolean Naming Standards

Boolean columns must always begin with the prefix:

is_

## Examples

is_active

is_deleted

is_pii

is_nullable

is_cde

is_mandatory

## Avoid

active

deleted

flag

status

## Why?

Boolean fields should read naturally in code and SQL.

Example

IF is_active = TRUE

# 10. Date and Timestamp Standards

Use the suffix "_at" for timestamps.

## Examples

created_at

updated_at

deleted_at

approved_at

last_profiled_at

last_scanned_at

## Why?

The "_at" suffix clearly indicates that the field stores a timestamp rather than a date-only value.

# 11. REST API Naming Standards

All APIs shall follow REST principles.

## Base URL

/api/v1/

## Examples

/api/v1/domains

/api/v1/business-terms

/api/v1/metadata/tables

/api/v1/metadata/columns

## Rules

- Use plural nouns
- Use lowercase
- Separate words using hyphens
- Never use spaces

# 12. JSON Naming Standards

JSON properties shall use snake_case.

## Example

{
    "business_term_name": "Customer Identifier",
    "description": "Unique customer number",
    "is_active": true
}

## Why?

The backend, database, and API will all use the same naming convention, reducing unnecessary mapping logic.

# 13. Python Coding Standards

## Variables

business_term

metadata_table

## Functions

create_business_term()

update_metadata_table()

delete_domain()

## Classes

BusinessTerm

MetadataTable

DataOwner

## Constants

MAX_RETRY_COUNT

DEFAULT_PAGE_SIZE

## Why?

Following PEP 8 standards improves readability and maintainability.

# 14. Docker Naming Standards

## Container Names

governance_postgres

governance_backend

governance_frontend

governance_airflow

## Volumes

postgres_data

airflow_logs

## Networks

governance_network

## Why?

Consistent naming simplifies Docker administration and troubleshooting.

# 15. Git Branch Naming Standards

Never commit directly to the main branch.

## Feature Branches

feature/business-glossary

feature/metadata-repository

feature/dq-engine

## Bug Fixes

bugfix/login

bugfix/api-validation

## Hot Fixes

hotfix/postgres-connection

## Why?

Branch naming immediately communicates the purpose of the work.

# 16. Git Commit Message Standards

Commit messages shall follow the Conventional Commits standard.

## Examples

feat: create metadata schema

feat: add business term entity

fix: resolve PostgreSQL connection issue

docs: update architecture document

test: add metadata repository unit tests

refactor: simplify repository layer

## Why?

Consistent commit messages improve project history and automate release notes.

# 17. AI Coding Standards

Every AI coding session must begin with the following instruction:

Read the following project documentation before generating any code:

01_ProjectVision.md

02_BusinessRequirements.md

03_ConceptualModel.md

09_NamingStandards.md

Follow every naming convention defined in these documents.

## Why?

Providing structured project context enables AI assistants to generate code that is consistent with the project's architecture, standards, and conventions.