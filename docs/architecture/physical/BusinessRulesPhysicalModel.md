# Business Rules Physical Data Model

## Enterprise Data Governance Platform

**Module:** Business Rules

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

This document defines the PostgreSQL Physical Data Model for the Business Rules module.

The Physical Data Model translates the Business Rules Logical Data Model into implementable PostgreSQL database objects.

It defines:

- Physical Tables
- PostgreSQL Data Types
- Primary Keys
- Foreign Keys
- Constraints
- Indexes
- Default Values

This document serves as the implementation blueprint for SQLAlchemy ORM models, Alembic migration scripts, repository classes, and database deployment.

---

# 2. Scope

The Business Rules Physical Data Model consists of the following tables.

| Physical Table |
|----------------|
| rule_category |
| rule_type |
| business_rule |
| rule_condition |
| rule_action |
| rule_version |
| rule_dependency |
| rule_execution_context |
| rule_mapping |

---

# 3. Physical Design Standards

## 3.1 Naming Standards

All database objects shall comply with enterprise naming standards.

- snake_case
- Singular table names
- Lowercase identifiers
- UUID Primary Keys
- Indexed Foreign Keys

---

## 3.2 Primary Keys

Every table shall use a UUID Primary Key.

Example

```
business_rule_id UUID PRIMARY KEY
```

---

## 3.3 Foreign Keys

Relationships shall be implemented using UUID Foreign Keys.

---

## 3.4 Audit Columns

Every table shall contain:

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
| Rule Category | rule_category |
| Rule Type | rule_type |
| Business Rule | business_rule |
| Rule Condition | rule_condition |
| Rule Action | rule_action |
| Rule Version | rule_version |
| Rule Dependency | rule_dependency |
| Rule Execution Context | rule_execution_context |
| Rule Mapping | rule_mapping |

---

# 5. rule_category

## 5.1 Purpose

Stores enterprise Business Rule Categories.

---

### Primary Key

rule_category_id

---

### Columns

| Column | PostgreSQL Type | Nullable | Notes |
|----------|----------------|----------|------|
| rule_category_id | UUID | No | Primary Key |
| category_name | VARCHAR(200) | No | Unique |
| display_name | VARCHAR(200) | No | |
| description | TEXT | Yes | |
| owner | VARCHAR(100) | No | |
| steward | VARCHAR(100) | No | |
| status | VARCHAR(30) | No | |
| created_by | VARCHAR(100) | No | |
| created_date | TIMESTAMP | No | |
| modified_by | VARCHAR(100) | Yes | |
| modified_date | TIMESTAMP | Yes | |
| is_active | BOOLEAN | No | DEFAULT TRUE |

---

### Constraints

Primary Key

- rule_category_id

Unique

- category_name

Indexes

- idx_rule_category_name
- idx_rule_category_owner
- idx_rule_category_status

---

# 6. rule_type

## 6.1 Purpose

Stores enterprise Rule Types.

---

### Primary Key

rule_type_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| rule_type_id | UUID | No |
| rule_type_name | VARCHAR(100) | No |
| display_name | VARCHAR(150) | No |
| description | TEXT | Yes |
| execution_engine | VARCHAR(100) | Yes |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- rule_type_id

Unique

- rule_type_name

Indexes

- idx_rule_type_name
- idx_rule_type_status

---

# 7. business_rule

## 7.1 Purpose

Stores enterprise Business Rules.

---

### Primary Key

business_rule_id

---

### Foreign Keys

rule_category_id → rule_category.rule_category_id

rule_type_id → rule_type.rule_type_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| business_rule_id | UUID | No |
| rule_category_id | UUID | No |
| rule_type_id | UUID | No |
| rule_code | VARCHAR(50) | No |
| rule_name | VARCHAR(255) | No |
| description | TEXT | Yes |
| severity | VARCHAR(30) | No |
| priority | INTEGER | No |
| execution_order | INTEGER | No |
| owner | VARCHAR(100) | No |
| steward | VARCHAR(100) | No |
| effective_date | DATE | No |
| expiry_date | DATE | Yes |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- business_rule_id

Foreign Keys

- rule_category_id
- rule_type_id

Unique

- rule_code

Indexes

- idx_business_rule_code
- idx_business_rule_name
- idx_business_rule_priority
- idx_business_rule_status
- idx_business_rule_owner

---

# 8. rule_condition

## 8.1 Purpose

Stores the logical conditions that determine whether a Business Rule should execute.

A Business Rule may consist of one or more Rule Conditions evaluated in sequence.

---

### Primary Key

rule_condition_id

---

### Foreign Keys

business_rule_id → business_rule.business_rule_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| rule_condition_id | UUID | No |
| business_rule_id | UUID | No |
| sequence_number | INTEGER | No |
| left_operand | VARCHAR(255) | No |
| operator | VARCHAR(50) | No |
| right_operand | VARCHAR(255) | No |
| logical_operator | VARCHAR(10) | Yes |
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

- rule_condition_id

Foreign Key

- business_rule_id

Unique

- business_rule_id + sequence_number

Indexes

- idx_rule_condition_rule
- idx_rule_condition_sequence
- idx_rule_condition_status

---

# 9. rule_action

## 9.1 Purpose

Stores actions executed when a Business Rule evaluates successfully.

---

### Primary Key

rule_action_id

---

### Foreign Keys

business_rule_id → business_rule.business_rule_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| rule_action_id | UUID | No |
| business_rule_id | UUID | No |
| sequence_number | INTEGER | No |
| action_type | VARCHAR(100) | No |
| action_parameters | JSONB | Yes |
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

- rule_action_id

Foreign Key

- business_rule_id

Unique

- business_rule_id + sequence_number

Indexes

- idx_rule_action_rule
- idx_rule_action_type
- idx_rule_action_status

---

# 10. rule_version

## 10.1 Purpose

Maintains version history for Business Rules.

---

### Primary Key

rule_version_id

---

### Foreign Keys

business_rule_id → business_rule.business_rule_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| rule_version_id | UUID | No |
| business_rule_id | UUID | No |
| version_number | VARCHAR(20) | No |
| change_summary | TEXT | No |
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

- rule_version_id

Foreign Key

- business_rule_id

Unique

- business_rule_id + version_number

Indexes

- idx_rule_version_rule
- idx_rule_version_number
- idx_rule_version_status

---

# 11. rule_dependency

## 11.1 Purpose

Stores execution dependencies between Business Rules.

---

### Primary Key

rule_dependency_id

---

### Foreign Keys

parent_business_rule_id → business_rule.business_rule_id

dependent_business_rule_id → business_rule.business_rule_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| rule_dependency_id | UUID | No |
| parent_business_rule_id | UUID | No |
| dependent_business_rule_id | UUID | No |
| dependency_type | VARCHAR(50) | No |
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

- rule_dependency_id

Foreign Keys

- parent_business_rule_id
- dependent_business_rule_id

Unique

- parent_business_rule_id + dependent_business_rule_id

Indexes

- idx_rule_dependency_parent
- idx_rule_dependency_child
- idx_rule_dependency_status

---

# 12. rule_execution_context

## 12.1 Purpose

Stores execution contexts for Business Rules.

---

### Primary Key

rule_execution_context_id

---

### Foreign Keys

business_rule_id → business_rule.business_rule_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| rule_execution_context_id | UUID | No |
| business_rule_id | UUID | No |
| context_name | VARCHAR(100) | No |
| trigger_event | VARCHAR(100) | No |
| execution_frequency | VARCHAR(50) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- rule_execution_context_id

Foreign Key

- business_rule_id

Unique

- business_rule_id + context_name

Indexes

- idx_execution_context_rule
- idx_execution_context_name
- idx_execution_context_status

---

# 13. rule_mapping

## 13.1 Purpose

Stores mappings between Business Rules and enterprise governance objects.

Mappings enable end-to-end traceability between rules and the assets they govern.

---

### Primary Key

rule_mapping_id

---

### Foreign Keys

business_rule_id → business_rule.business_rule_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| rule_mapping_id | UUID | No |
| business_rule_id | UUID | No |
| target_object_type | VARCHAR(50) | No |
| target_object_identifier | UUID | No |
| mapping_type | VARCHAR(50) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- rule_mapping_id

Foreign Key

- business_rule_id

Unique

- business_rule_id + target_object_type + target_object_identifier

Indexes

- idx_rule_mapping_rule
- idx_rule_mapping_target
- idx_rule_mapping_type
- idx_rule_mapping_status

---

# 14. Foreign Key Matrix

The following table summarizes all foreign key relationships within the Business Rules module.

| Parent Table | Child Table | Foreign Key |
|--------------|-------------|-------------|
| rule_category | business_rule | rule_category_id |
| rule_type | business_rule | rule_type_id |
| business_rule | rule_condition | business_rule_id |
| business_rule | rule_action | business_rule_id |
| business_rule | rule_version | business_rule_id |
| business_rule | rule_execution_context | business_rule_id |
| business_rule | rule_mapping | business_rule_id |
| business_rule | rule_dependency | parent_business_rule_id |
| business_rule | rule_dependency | dependent_business_rule_id |

---

# 15. Referential Integrity Rules

The Business Rules module shall enforce referential integrity using foreign key constraints.

The following rules shall apply.

- A Business Rule cannot exist without a Rule Category.
- A Business Rule cannot exist without a Rule Type.
- A Rule Condition cannot exist without a Business Rule.
- A Rule Action cannot exist without a Business Rule.
- A Rule Version cannot exist without a Business Rule.
- A Rule Execution Context cannot exist without a Business Rule.
- A Rule Mapping cannot exist without a Business Rule.
- Rule Dependencies shall reference valid Business Rules.
- Parent records shall not be physically deleted while dependent records exist.

---

# 16. Index Strategy

## 16.1 Purpose

Indexes shall support efficient retrieval and execution of Business Rules.

Optimization objectives include:

- Rule execution
- Rule search
- Rule approval
- Rule dependency traversal
- Governance reporting
- AI-assisted rule discovery

---

## 16.2 Standard Indexes

Every table shall include indexes for:

- Primary Key
- Foreign Keys
- Status
- Owner
- Created Date

---

## 16.3 Composite Indexes

The following composite indexes are recommended.

| Table | Composite Index |
|---------|----------------|
| business_rule | rule_category_id + status |
| business_rule | rule_type_id + priority |
| rule_condition | business_rule_id + sequence_number |
| rule_action | business_rule_id + sequence_number |
| rule_version | business_rule_id + version_number |
| rule_dependency | parent_business_rule_id + dependent_business_rule_id |
| rule_mapping | business_rule_id + target_object_type |

---

## 16.4 Search Optimization

Additional indexes should support:

- Rule Code
- Rule Name
- Category
- Rule Type
- Owner
- Status
- Effective Date

These indexes improve:

- Rule Search
- AI Retrieval
- Rule Engine Performance
- Reporting

---

# 17. Performance Considerations

The Business Rules module shall support enterprise-scale rule management and execution.

Performance objectives include:

- Low-latency rule retrieval
- Efficient rule evaluation
- Optimized dependency resolution
- Fast version lookup
- Scalable rule execution

Future enhancements may include:

- Rule execution caching
- Materialized reporting views
- Distributed rule execution
- Event-driven rule processing
- Rule execution metrics

---

# 18. Physical Design Standards

The Business Rules module shall follow enterprise database standards.

## Database Design

- Third Normal Form (3NF)
- UUID Primary Keys
- Indexed Foreign Keys
- Soft Deletes
- Audit Columns
- Version Management
- Optimistic Locking

---

## Naming Standards

All database objects shall comply with:

- 10_NamingStandards.md

Including:

- Tables
- Columns
- Constraints
- Indexes
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

- approval_status
- approved_by
- approved_date
- execution_count
- last_execution_date
- last_execution_result

---

# 19. Recommended Database Views

The following PostgreSQL views are recommended.

| View | Purpose |
|------|---------|
| vw_business_rules | Complete Business Rule information |
| vw_active_business_rules | Active rules available for execution |
| vw_rule_conditions | Rule Conditions with parent rule details |
| vw_rule_dependencies | Rule dependency hierarchy |
| vw_rule_execution_contexts | Rule execution contexts |
| vw_rule_mappings | Rule-to-asset mappings |
| vw_rule_versions | Rule version history |

These views simplify reporting, dashboard development, rule analysis, and AI-assisted rule discovery.

---

# 20. Summary

The Business Rules Physical Data Model defines the PostgreSQL implementation of the Business Rules module.

The model includes:

- Physical Tables
- PostgreSQL Data Types
- Primary Keys
- Foreign Keys
- Constraints
- Referential Integrity Rules
- Index Strategy
- Performance Standards
- Recommended Database Views

The Business Rules module provides the enterprise repository for governing business logic and enables consistent rule management across business processes, data quality, workflows, regulatory compliance, and AI-driven decision support.

This document serves as the implementation blueprint for:

- PostgreSQL Database
- SQLAlchemy ORM Models
- Alembic Migration Scripts
- Repository Layer
- Rules Engine
- Workflow Engine
- REST APIs
- AI Services