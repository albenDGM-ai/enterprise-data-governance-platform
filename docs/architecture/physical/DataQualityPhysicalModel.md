# Data Quality Physical Data Model

## Enterprise Data Governance Platform

**Module:** Data Quality

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

This document defines the PostgreSQL Physical Data Model for the Data Quality module.

The Physical Data Model translates the Data Quality Logical Data Model into implementable PostgreSQL database objects.

It defines:

- Physical Tables
- PostgreSQL Data Types
- Primary Keys
- Foreign Keys
- Constraints
- Indexes
- Default Values

This document serves as the implementation blueprint for SQLAlchemy ORM models, Alembic migration scripts, repository classes, Rule Engine persistence, and database deployment.

---

# 2. Scope

The Data Quality Physical Data Model consists of the following tables.

| Physical Table |
|----------------|
| data_quality_dimension |
| data_quality_rule |
| data_quality_assessment |
| data_quality_result |
| data_quality_issue |
| data_quality_exception |
| data_quality_score |
| data_quality_threshold |
| data_quality_remediation |

---

# 3. Physical Design Standards

## 3.1 Naming Standards

All database objects shall follow enterprise naming standards.

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
data_quality_rule_id UUID PRIMARY KEY
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

Every table shall support logical deletion using

```
is_active BOOLEAN DEFAULT TRUE
```

Physical deletion shall not be performed.

---

# 4. Physical Entity Mapping

| Logical Entity | Physical Table |
|----------------|----------------|
| Data Quality Dimension | data_quality_dimension |
| Data Quality Rule | data_quality_rule |
| Data Quality Assessment | data_quality_assessment |
| Data Quality Result | data_quality_result |
| Data Quality Issue | data_quality_issue |
| Data Quality Exception | data_quality_exception |
| Data Quality Score | data_quality_score |
| Data Quality Threshold | data_quality_threshold |
| Data Quality Remediation | data_quality_remediation |

---

# 5. data_quality_dimension

## 5.1 Purpose

Stores enterprise Data Quality Dimensions.

---

### Primary Key

data_quality_dimension_id

---

### Columns

| Column | PostgreSQL Type | Nullable | Notes |
|----------|----------------|----------|------|
| data_quality_dimension_id | UUID | No | Primary Key |
| dimension_name | VARCHAR(100) | No | Unique |
| display_name | VARCHAR(150) | No | |
| description | TEXT | Yes | |
| owner | VARCHAR(100) | No | |
| status | VARCHAR(30) | No | |
| created_by | VARCHAR(100) | No | |
| created_date | TIMESTAMP | No | |
| modified_by | VARCHAR(100) | Yes | |
| modified_date | TIMESTAMP | Yes | |
| is_active | BOOLEAN | No | DEFAULT TRUE |

---

### Constraints

Primary Key

- data_quality_dimension_id

Unique

- dimension_name

Indexes

- idx_dq_dimension_name
- idx_dq_dimension_status
- idx_dq_dimension_owner

---

# 6. data_quality_rule

## 6.1 Purpose

Stores enterprise Data Quality Rules.

---

### Primary Key

data_quality_rule_id

---

### Foreign Keys

data_quality_dimension_id → data_quality_dimension.data_quality_dimension_id

business_rule_id → business_rule.business_rule_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| data_quality_rule_id | UUID | No |
| data_quality_dimension_id | UUID | No |
| business_rule_id | UUID | No |
| rule_code | VARCHAR(50) | No |
| rule_name | VARCHAR(255) | No |
| target_data_asset_id | UUID | No |
| severity | VARCHAR(30) | No |
| threshold_percentage | NUMERIC(5,2) | No |
| execution_frequency | VARCHAR(50) | No |
| owner | VARCHAR(100) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- data_quality_rule_id

Foreign Keys

- data_quality_dimension_id
- business_rule_id

Unique

- rule_code

Indexes

- idx_dq_rule_code
- idx_dq_rule_dimension
- idx_dq_rule_owner
- idx_dq_rule_status

---

# 7. data_quality_assessment

## 7.1 Purpose

Stores executions of Data Quality Rules.

---

### Primary Key

data_quality_assessment_id

---

### Foreign Keys

data_quality_rule_id → data_quality_rule.data_quality_rule_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| data_quality_assessment_id | UUID | No |
| data_quality_rule_id | UUID | No |
| assessment_number | VARCHAR(50) | No |
| assessment_name | VARCHAR(255) | No |
| assessment_type | VARCHAR(50) | No |
| execution_start_time | TIMESTAMP | No |
| execution_end_time | TIMESTAMP | Yes |
| executed_by | VARCHAR(100) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- data_quality_assessment_id

Foreign Key

- data_quality_rule_id

Unique

- assessment_number

Indexes

- idx_dq_assessment_number
- idx_dq_assessment_rule
- idx_dq_assessment_status
- idx_dq_assessment_start_time

---

# 8. data_quality_result

## 8.1 Purpose

Stores the detailed results produced by Data Quality Assessments.

Each record represents the outcome of executing a Data Quality Rule against a governed Data Asset.

---

### Primary Key

data_quality_result_id

---

### Foreign Keys

data_quality_assessment_id → data_quality_assessment.data_quality_assessment_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| data_quality_result_id | UUID | No |
| data_quality_assessment_id | UUID | No |
| target_data_asset_id | UUID | No |
| total_records | BIGINT | No |
| passed_records | BIGINT | No |
| failed_records | BIGINT | No |
| warning_records | BIGINT | Yes |
| quality_percentage | NUMERIC(5,2) | No |
| result_status | VARCHAR(30) | No |
| execution_duration_ms | BIGINT | Yes |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- data_quality_result_id

Foreign Key

- data_quality_assessment_id

Indexes

- idx_dq_result_assessment
- idx_dq_result_asset
- idx_dq_result_status
- idx_dq_result_quality

---

# 9. data_quality_issue

## 9.1 Purpose

Stores Data Quality Issues detected during rule execution.

---

### Primary Key

data_quality_issue_id

---

### Foreign Keys

data_quality_result_id → data_quality_result.data_quality_result_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| data_quality_issue_id | UUID | No |
| data_quality_result_id | UUID | No |
| issue_number | VARCHAR(50) | No |
| issue_type | VARCHAR(100) | No |
| severity | VARCHAR(30) | No |
| description | TEXT | No |
| business_impact | TEXT | Yes |
| owner | VARCHAR(100) | No |
| detected_date | TIMESTAMP | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- data_quality_issue_id

Foreign Key

- data_quality_result_id

Unique

- issue_number

Indexes

- idx_dq_issue_number
- idx_dq_issue_owner
- idx_dq_issue_severity
- idx_dq_issue_status

---

# 10. data_quality_exception

## 10.1 Purpose

Stores approved Data Quality Exceptions.

---

### Primary Key

data_quality_exception_id

---

### Foreign Keys

data_quality_issue_id → data_quality_issue.data_quality_issue_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| data_quality_exception_id | UUID | No |
| data_quality_issue_id | UUID | No |
| exception_number | VARCHAR(50) | No |
| exception_reason | TEXT | No |
| approved_by | VARCHAR(100) | No |
| approval_date | TIMESTAMP | No |
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

- data_quality_exception_id

Foreign Key

- data_quality_issue_id

Unique

- exception_number

Indexes

- idx_dq_exception_number
- idx_dq_exception_status
- idx_dq_exception_expiry

---

# 11. data_quality_score

## 11.1 Purpose

Stores calculated Data Quality Scores for completed assessments.

---

### Primary Key

data_quality_score_id

---

### Foreign Keys

data_quality_result_id → data_quality_result.data_quality_result_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| data_quality_score_id | UUID | No |
| data_quality_result_id | UUID | No |
| overall_score | NUMERIC(5,2) | No |
| completeness_score | NUMERIC(5,2) | No |
| accuracy_score | NUMERIC(5,2) | No |
| consistency_score | NUMERIC(5,2) | No |
| validity_score | NUMERIC(5,2) | No |
| uniqueness_score | NUMERIC(5,2) | No |
| timeliness_score | NUMERIC(5,2) | No |
| integrity_score | NUMERIC(5,2) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- data_quality_score_id

Foreign Key

- data_quality_result_id

Indexes

- idx_dq_score_result
- idx_dq_score_overall

---

# 12. data_quality_threshold

## 12.1 Purpose

Stores threshold values for Data Quality Rules.

---

### Primary Key

data_quality_threshold_id

---

### Foreign Keys

data_quality_rule_id → data_quality_rule.data_quality_rule_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| data_quality_threshold_id | UUID | No |
| data_quality_rule_id | UUID | No |
| warning_threshold | NUMERIC(5,2) | No |
| failure_threshold | NUMERIC(5,2) | No |
| measurement_unit | VARCHAR(50) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- data_quality_threshold_id

Foreign Key

- data_quality_rule_id

Indexes

- idx_dq_threshold_rule
- idx_dq_threshold_status

---

# 13. data_quality_remediation

## 13.1 Purpose

Stores remediation activities created to resolve Data Quality Issues.

---

### Primary Key

data_quality_remediation_id

---

### Foreign Keys

data_quality_issue_id → data_quality_issue.data_quality_issue_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| data_quality_remediation_id | UUID | No |
| data_quality_issue_id | UUID | No |
| remediation_number | VARCHAR(50) | No |
| assigned_to | VARCHAR(100) | No |
| target_resolution_date | DATE | No |
| actual_resolution_date | DATE | Yes |
| resolution_summary | TEXT | Yes |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- data_quality_remediation_id

Foreign Key

- data_quality_issue_id

Unique

- remediation_number

Indexes

- idx_dq_remediation_number
- idx_dq_remediation_assigned
- idx_dq_remediation_status
- idx_dq_remediation_target_date

---

# 14. Foreign Key Matrix

The following table summarizes all foreign key relationships within the Data Quality module.

| Parent Table | Child Table | Foreign Key |
|--------------|-------------|-------------|
| data_quality_dimension | data_quality_rule | data_quality_dimension_id |
| business_rule | data_quality_rule | business_rule_id |
| data_quality_rule | data_quality_assessment | data_quality_rule_id |
| data_quality_assessment | data_quality_result | data_quality_assessment_id |
| data_quality_result | data_quality_issue | data_quality_result_id |
| data_quality_result | data_quality_score | data_quality_result_id |
| data_quality_rule | data_quality_threshold | data_quality_rule_id |
| data_quality_issue | data_quality_exception | data_quality_issue_id |
| data_quality_issue | data_quality_remediation | data_quality_issue_id |

---

# 15. Referential Integrity Rules

The Data Quality module shall enforce referential integrity through foreign key constraints.

The following rules shall apply.

- A Data Quality Rule cannot exist without a Data Quality Dimension.
- A Data Quality Rule shall reference a valid Business Rule.
- A Data Quality Assessment cannot exist without a Data Quality Rule.
- A Data Quality Result cannot exist without a Data Quality Assessment.
- A Data Quality Issue cannot exist without a Data Quality Result.
- A Data Quality Score cannot exist without a Data Quality Result.
- A Data Quality Threshold cannot exist without a Data Quality Rule.
- A Data Quality Exception cannot exist without a Data Quality Issue.
- A Data Quality Remediation cannot exist without a Data Quality Issue.
- Parent records shall not be physically deleted while dependent child records exist.

---

# 16. Index Strategy

## 16.1 Purpose

Indexes shall support efficient execution of enterprise Data Quality operations.

Optimization objectives include:

- Rule execution
- Assessment processing
- Quality score retrieval
- Issue management
- Dashboard reporting
- AI-assisted analysis

---

## 16.2 Standard Indexes

Every table shall include indexes for:

- Primary Key
- Foreign Keys
- Status
- Owner / Assigned User
- Created Date

---

## 16.3 Composite Indexes

The following composite indexes are recommended.

| Table | Composite Index |
|---------|----------------|
| data_quality_rule | data_quality_dimension_id + status |
| data_quality_rule | target_data_asset_id + status |
| data_quality_assessment | data_quality_rule_id + execution_start_time |
| data_quality_result | data_quality_assessment_id + result_status |
| data_quality_issue | severity + status |
| data_quality_remediation | assigned_to + status |
| data_quality_threshold | data_quality_rule_id + status |

---

## 16.4 Search Optimization

Additional indexes should support:

- Rule Code
- Rule Name
- Assessment Number
- Issue Number
- Exception Number
- Remediation Number
- Severity
- Status
- Execution Date

These indexes improve:

- Global Search
- Executive Dashboards
- AI Retrieval
- Operational Reporting
- Trend Analysis

---

# 17. Performance Considerations

The Data Quality module shall support enterprise-scale quality assessment and monitoring.

Performance objectives include:

- High-speed rule execution
- Efficient batch assessments
- Low-latency dashboard queries
- Fast issue retrieval
- Scalable historical reporting

Future enhancements may include:

- Parallel assessment execution
- Incremental quality calculations
- Materialized reporting views
- Partitioning of assessment history
- Event-driven processing
- In-memory execution caching

---

# 18. Physical Design Standards

The Data Quality module shall follow enterprise database standards.

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

- approval_status
- approved_by
- approved_date
- execution_node
- execution_duration_ms
- rule_engine_version
- assessment_batch_id

---

# 19. Recommended Database Views

The following PostgreSQL views are recommended.

| View | Purpose |
|------|---------|
| vw_data_quality_rules | Complete Data Quality Rule information |
| vw_data_quality_assessments | Assessment execution summary |
| vw_data_quality_results | Detailed assessment results |
| vw_data_quality_scores | Current and historical quality scores |
| vw_data_quality_issues | Open and historical issues |
| vw_data_quality_remediation | Remediation progress |
| vw_data_quality_dashboard | Executive dashboard metrics |

These views simplify dashboard development, reporting, trend analysis, and AI-assisted quality insights.

---

# 20. Summary

The Data Quality Physical Data Model defines the PostgreSQL implementation of the Data Quality module.

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

The Data Quality module provides the enterprise repository for measuring, monitoring, reporting, and improving data quality while integrating with Business Rules, Metadata Repository, Business Glossary, Workflow, Reporting, and AI Services.

This document serves as the implementation blueprint for:

- PostgreSQL Database
- SQLAlchemy ORM Models
- Alembic Migration Scripts
- Repository Layer
- Data Quality Engine
- Workflow Engine
- REST APIs
- Reporting Services
- AI Services

