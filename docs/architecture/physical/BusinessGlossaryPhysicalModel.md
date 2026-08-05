# Business Glossary Physical Data Model

## Enterprise Data Governance Platform

**Module:** Business Glossary

**Version:** 1.0

**Status:** Draft

---

Foundation Reference

This document shall be read in conjunction with:

- 00_EnterpriseArchitectureOverview.md
- 01_ProjectVision.md
- 02_BusinessRequirements.md
- 03_EnterpriseBusinessModel.md
- 04_ConceptualModel.md
- 05_LogicalModel.md
- 09_DataDictionary.md
- 10_NamingStandards.md

---

# 1. Purpose

## 1.1 Objective

This document defines the PostgreSQL Physical Data Model for the Business Glossary module.

The Physical Data Model transforms the Logical Data Model into implementable PostgreSQL database objects.

It defines:

- Physical Tables
- Columns
- PostgreSQL Data Types
- Primary Keys
- Foreign Keys
- Constraints
- Indexes
- Default Values

This document serves as the implementation blueprint for SQLAlchemy ORM models, Alembic migration scripts, repository classes, and database deployment.

---

# 2. Scope

The Business Glossary Physical Data Model consists of the following tables.

| Physical Table |
|----------------|
| business_glossary |
| business_category |
| business_term |
| business_definition |
| acronym |
| synonym |
| business_rule_association |
| business_term_relationship |

---

# 3. Physical Design Standards

## 3.1 Naming Standards

All database objects shall follow the enterprise naming standards.

- snake_case
- Singular table names
- Lowercase identifiers
- UUID primary keys
- Indexed foreign keys

---

## 3.2 Primary Keys

Every table shall use a UUID Primary Key.

Example

```
business_term_id UUID PRIMARY KEY
```

---

## 3.3 Foreign Keys

Relationships shall be implemented using UUID Foreign Keys.

---

## 3.4 Audit Columns

Every table shall include:

- created_by
- created_date
- modified_by
- modified_date

---

## 3.5 Soft Delete

Every table shall support logical deletion using:

```
is_active BOOLEAN DEFAULT TRUE
```

Physical deletion shall not be performed.

---

# 4. Physical Entity Mapping

| Logical Entity | Physical Table |
|----------------|----------------|
| Business Glossary | business_glossary |
| Business Category | business_category |
| Business Term | business_term |
| Business Definition | business_definition |
| Acronym | acronym |
| Synonym | synonym |
| Business Rule Association | business_rule_association |
| Business Term Relationship | business_term_relationship |

---

# 5. business_glossary

## 5.1 Purpose

Stores enterprise business glossaries.

---

### Primary Key

business_glossary_id

---

### Columns

| Column | PostgreSQL Type | Nullable | Notes |
|----------|----------------|----------|------|
| business_glossary_id | UUID | No | Primary Key |
| glossary_name | VARCHAR(200) | No | Unique |
| display_name | VARCHAR(200) | No | |
| description | TEXT | Yes | |
| version | VARCHAR(20) | No | |
| status | VARCHAR(30) | No | |
| owner | VARCHAR(100) | No | |
| steward | VARCHAR(100) | No | |
| created_by | VARCHAR(100) | No | |
| created_date | TIMESTAMP | No | |
| modified_by | VARCHAR(100) | Yes | |
| modified_date | TIMESTAMP | Yes | |
| is_active | BOOLEAN | No | DEFAULT TRUE |

---

### Constraints

Primary Key

- business_glossary_id

Unique

- glossary_name

Indexes

- idx_glossary_name
- idx_glossary_status
- idx_glossary_owner

---

# 6. business_category

## 6.1 Purpose

Stores Business Categories within a Business Glossary.

---

### Primary Key

business_category_id

---

### Foreign Keys

business_glossary_id → business_glossary.business_glossary_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| business_category_id | UUID | No |
| business_glossary_id | UUID | No |
| parent_category_id | UUID | Yes |
| category_name | VARCHAR(200) | No |
| display_name | VARCHAR(200) | No |
| description | TEXT | Yes |
| owner | VARCHAR(100) | No |
| steward | VARCHAR(100) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- business_category_id

Foreign Keys

- business_glossary_id
- parent_category_id (Self Reference)

Unique

- business_glossary_id + category_name

Indexes

- idx_category_name
- idx_category_owner
- idx_category_status

---

# 7. business_term

## 7.1 Purpose

Stores approved enterprise Business Terms.

---

### Primary Key

business_term_id

---

### Foreign Keys

business_category_id → business_category.business_category_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| business_term_id | UUID | No |
| business_category_id | UUID | No |
| business_term_name | VARCHAR(255) | No |
| display_name | VARCHAR(255) | No |
| preferred_definition | TEXT | No |
| business_domain | VARCHAR(100) | No |
| business_capability | VARCHAR(100) | Yes |
| owner | VARCHAR(100) | No |
| steward | VARCHAR(100) | No |
| classification | VARCHAR(50) | Yes |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- business_term_id

Foreign Key

- business_category_id

Unique

- business_category_id + business_term_name

Indexes

- idx_business_term_name
- idx_business_domain
- idx_business_term_owner
- idx_business_term_status

---

# 8. business_definition

## 8.1 Purpose

Stores formal business definitions for Business Terms.

A Business Term may have multiple historical definitions through versioning, however only one definition may be active at any point in time.

---

### Primary Key

business_definition_id

---

### Foreign Keys

business_term_id → business_term.business_term_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| business_definition_id | UUID | No |
| business_term_id | UUID | No |
| definition_text | TEXT | No |
| definition_source | VARCHAR(255) | Yes |
| version | VARCHAR(20) | No |
| effective_date | DATE | No |
| expiry_date | DATE | Yes |
| approved_by | VARCHAR(100) | No |
| approved_date | TIMESTAMP | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- business_definition_id

Foreign Key

- business_term_id

Indexes

- idx_definition_term
- idx_definition_status
- idx_definition_version

---

# 9. acronym

## 9.1 Purpose

Stores approved acronyms for Business Terms.

---

### Primary Key

acronym_id

---

### Foreign Keys

business_term_id → business_term.business_term_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| acronym_id | UUID | No |
| business_term_id | UUID | No |
| acronym | VARCHAR(50) | No |
| description | TEXT | Yes |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- acronym_id

Foreign Key

- business_term_id

Unique

- acronym

Indexes

- idx_acronym
- idx_acronym_status

---

# 10. synonym

## 10.1 Purpose

Stores approved alternate business names for Business Terms.

---

### Primary Key

synonym_id

---

### Foreign Keys

business_term_id → business_term.business_term_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| synonym_id | UUID | No |
| business_term_id | UUID | No |
| synonym | VARCHAR(255) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- synonym_id

Foreign Key

- business_term_id

Indexes

- idx_synonym
- idx_synonym_status

---

# 11. business_rule_association

## 11.1 Purpose

Stores relationships between Business Terms and Business Rules.

---

### Primary Key

business_rule_association_id

---

### Foreign Keys

business_term_id → business_term.business_term_id

business_rule_id → business_rule.business_rule_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| business_rule_association_id | UUID | No |
| business_term_id | UUID | No |
| business_rule_id | UUID | No |
| relationship_type | VARCHAR(50) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- business_rule_association_id

Foreign Keys

- business_term_id
- business_rule_id

Unique

- business_term_id + business_rule_id

Indexes

- idx_rule_association_term
- idx_rule_association_rule
- idx_rule_association_status

---

# 12. business_term_relationship

## 12.1 Purpose

Stores semantic relationships between Business Terms.

---

### Primary Key

business_term_relationship_id

---

### Foreign Keys

source_business_term_id → business_term.business_term_id

target_business_term_id → business_term.business_term_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| business_term_relationship_id | UUID | No |
| source_business_term_id | UUID | No |
| target_business_term_id | UUID | No |
| relationship_type | VARCHAR(50) | No |
| description | TEXT | Yes |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- business_term_relationship_id

Foreign Keys

- source_business_term_id
- target_business_term_id

Unique

- source_business_term_id + relationship_type + target_business_term_id

Indexes

- idx_relationship_source
- idx_relationship_target
- idx_relationship_type
- idx_relationship_status

---

# 13. Foreign Key Matrix

The following table summarizes all foreign key relationships within the Business Glossary module.

| Parent Table | Child Table | Foreign Key |
|--------------|-------------|-------------|
| business_glossary | business_category | business_glossary_id |
| business_category | business_term | business_category_id |
| business_term | business_definition | business_term_id |
| business_term | acronym | business_term_id |
| business_term | synonym | business_term_id |
| business_term | business_rule_association | business_term_id |
| business_rule | business_rule_association | business_rule_id |
| business_term | business_term_relationship | source_business_term_id |
| business_term | business_term_relationship | target_business_term_id |

---

# 14. Referential Integrity Rules

The Business Glossary module shall enforce referential integrity through foreign key constraints.

The following rules shall apply.

- A Business Category cannot exist without a Business Glossary.
- A Business Term cannot exist without a Business Category.
- A Business Definition cannot exist without a Business Term.
- An Acronym cannot exist without a Business Term.
- A Synonym cannot exist without a Business Term.
- A Business Rule Association cannot exist without both a Business Term and a Business Rule.
- A Business Term Relationship shall reference two valid Business Terms.
- Physical deletion of parent records shall be prevented while dependent child records exist.

---

# 15. Index Strategy

## 15.1 Purpose

Indexes shall be created to optimize:

- Business Term search
- Business Glossary navigation
- Auto-complete
- AI semantic search
- Reporting
- Relationship traversal

---

## 15.2 Standard Indexes

Every table shall contain indexes for:

- Primary Key
- Foreign Keys
- Name Columns
- Status
- Owner

---

## 15.3 Composite Indexes

The following composite indexes are recommended.

| Table | Composite Index |
|---------|----------------|
| business_category | business_glossary_id + category_name |
| business_term | business_category_id + business_term_name |
| business_definition | business_term_id + version |
| business_rule_association | business_term_id + business_rule_id |
| business_term_relationship | source_business_term_id + relationship_type + target_business_term_id |

---

## 15.4 Search Optimization

Additional indexes should support:

- Business Term Name
- Display Name
- Acronym
- Synonym
- Business Domain
- Classification

These indexes will improve:

- Global Search
- AI Retrieval
- Auto-complete
- Metadata Discovery

---

# 16. Performance Considerations

The Business Glossary shall support enterprise-scale business metadata management.

Performance objectives include:

- Fast Business Term search
- Efficient relationship traversal
- Optimized joins
- Low query latency
- High read performance

Future enhancements may include:

- Full-text search
- Semantic vector search
- Metadata caching
- Materialized views
- Read replicas

---

# 17. Physical Design Standards

The Business Glossary module shall follow the enterprise database standards.

## Database Design

- Third Normal Form (3NF)
- UUID Primary Keys
- Indexed Foreign Keys
- Soft Deletes
- Audit Columns
- Optimistic Locking
- Version Management

---

## Naming Standards

All database objects shall comply with:

- 10_NamingStandards.md

Including:

- Tables
- Columns
- Indexes
- Constraints
- Foreign Keys

---

## Audit Requirements

Every table shall include:

- created_by
- created_date
- modified_by
- modified_date
- is_active

Future releases may introduce:

- version_number
- row_version
- approval_status
- approved_by
- approved_date

---

# 18. Recommended Database Views

The following PostgreSQL views are recommended for reporting and search.

| View | Purpose |
|------|---------|
| vw_business_terms | Complete Business Term information |
| vw_business_glossary | Business Glossary summary |
| vw_business_relationships | Business Term relationships |
| vw_business_search | Optimized search view |
| vw_business_metadata_links | Business Terms linked to technical metadata |

These views simplify reporting and improve query performance for dashboards and AI services.

---

# 19. Summary

The Business Glossary Physical Data Model defines the PostgreSQL implementation of the Business Glossary module.

The model includes:

- Physical Tables
- Columns
- PostgreSQL Data Types
- Primary Keys
- Foreign Keys
- Constraints
- Indexes
- Referential Integrity Rules
- Performance Standards

The Business Glossary provides the enterprise vocabulary used across all governance capabilities and establishes traceability between business concepts and technical metadata.

This document serves as the implementation blueprint for:

- PostgreSQL Database
- SQLAlchemy ORM Models
- Alembic Migration Scripts
- Repository Layer
- Business Glossary Services
- REST APIs
- AI Knowledge Base