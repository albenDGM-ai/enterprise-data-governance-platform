# Data Lineage Physical Data Model

## Enterprise Data Governance Platform

**Module:** Data Lineage

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

This document defines the PostgreSQL Physical Data Model for the Data Lineage module.

The Physical Data Model translates the Data Lineage Logical Data Model into implementable PostgreSQL database objects.

It defines:

- Physical Tables
- PostgreSQL Data Types
- Primary Keys
- Foreign Keys
- Constraints
- Indexes
- Default Values

This document serves as the implementation blueprint for SQLAlchemy ORM models, Alembic migration scripts, repository classes, the Lineage Engine, and database deployment.

---

# 2. Scope

The Data Lineage Physical Data Model consists of the following tables.

| Physical Table |
|----------------|
| lineage_source |
| lineage_target |
| lineage_flow |
| lineage_transformation |
| lineage_process |
| lineage_mapping |
| impact_analysis |
| lineage_version |
| lineage_snapshot |

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
lineage_source_id UUID PRIMARY KEY
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
| Lineage Source | lineage_source |
| Lineage Target | lineage_target |
| Lineage Flow | lineage_flow |
| Lineage Transformation | lineage_transformation |
| Lineage Process | lineage_process |
| Lineage Mapping | lineage_mapping |
| Impact Analysis | impact_analysis |
| Lineage Version | lineage_version |
| Lineage Snapshot | lineage_snapshot |

---

# 5. lineage_source

## 5.1 Purpose

Stores enterprise Lineage Sources.

---

### Primary Key

lineage_source_id

---

### Columns

| Column | PostgreSQL Type | Nullable | Notes |
|----------|----------------|----------|------|
| lineage_source_id | UUID | No | Primary Key |
| source_name | VARCHAR(255) | No | |
| source_type | VARCHAR(100) | No | |
| system_name | VARCHAR(150) | No | |
| business_domain | VARCHAR(150) | No | |
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

- lineage_source_id

Unique

- source_name + system_name

Indexes

- idx_lineage_source_name
- idx_lineage_source_type
- idx_lineage_source_system
- idx_lineage_source_status

---

# 6. lineage_target

## 6.1 Purpose

Stores enterprise Lineage Targets.

---

### Primary Key

lineage_target_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| lineage_target_id | UUID | No |
| target_name | VARCHAR(255) | No |
| target_type | VARCHAR(100) | No |
| system_name | VARCHAR(150) | No |
| business_domain | VARCHAR(150) | No |
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

- lineage_target_id

Unique

- target_name + system_name

Indexes

- idx_lineage_target_name
- idx_lineage_target_type
- idx_lineage_target_system
- idx_lineage_target_status

---

# 7. lineage_process

## 7.1 Purpose

Stores enterprise processes responsible for moving or transforming data.

---

### Primary Key

lineage_process_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| lineage_process_id | UUID | No |
| process_name | VARCHAR(255) | No |
| process_type | VARCHAR(100) | No |
| technology | VARCHAR(100) | No |
| schedule | VARCHAR(100) | Yes |
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

- lineage_process_id

Unique

- process_name

Indexes

- idx_lineage_process_name
- idx_lineage_process_type
- idx_lineage_process_status

---

# 8. lineage_flow

## 8.1 Purpose

Stores enterprise data movement between Lineage Sources and Targets.

---

### Primary Key

lineage_flow_id

---

### Foreign Keys

lineage_source_id → lineage_source.lineage_source_id

lineage_process_id → lineage_process.lineage_process_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| lineage_flow_id | UUID | No |
| lineage_source_id | UUID | No |
| lineage_process_id | UUID | No |
| flow_name | VARCHAR(255) | No |
| flow_type | VARCHAR(50) | No |
| direction | VARCHAR(30) | No |
| frequency | VARCHAR(50) | No |
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

- lineage_flow_id

Foreign Keys

- lineage_source_id
- lineage_process_id

Unique

- flow_name

Indexes

- idx_lineage_flow_name
- idx_lineage_flow_source
- idx_lineage_flow_process
- idx_lineage_flow_status

---

# 9. lineage_transformation

## 9.1 Purpose

Stores business and technical transformations applied to data during movement from Source to Target.

---

### Primary Key

lineage_transformation_id

---

### Foreign Keys

lineage_flow_id → lineage_flow.lineage_flow_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| lineage_transformation_id | UUID | No |
| lineage_flow_id | UUID | No |
| sequence_number | INTEGER | No |
| transformation_name | VARCHAR(255) | No |
| transformation_type | VARCHAR(100) | No |
| description | TEXT | Yes |
| expression | TEXT | Yes |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- lineage_transformation_id

Foreign Key

- lineage_flow_id

Unique

- lineage_flow_id + sequence_number

Indexes

- idx_lineage_transformation_flow
- idx_lineage_transformation_sequence
- idx_lineage_transformation_type
- idx_lineage_transformation_status

---

# 10. lineage_mapping

## 10.1 Purpose

Stores attribute-level mappings between Lineage Sources and Lineage Targets.

This table provides the foundation for column-level lineage.

---

### Primary Key

lineage_mapping_id

---

### Foreign Keys

lineage_flow_id → lineage_flow.lineage_flow_id

lineage_transformation_id → lineage_transformation.lineage_transformation_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| lineage_mapping_id | UUID | No |
| lineage_flow_id | UUID | No |
| lineage_transformation_id | UUID | Yes |
| source_attribute | VARCHAR(255) | No |
| target_attribute | VARCHAR(255) | No |
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

- lineage_mapping_id

Foreign Keys

- lineage_flow_id
- lineage_transformation_id

Unique

- lineage_flow_id + source_attribute + target_attribute

Indexes

- idx_lineage_mapping_flow
- idx_lineage_mapping_source
- idx_lineage_mapping_target
- idx_lineage_mapping_status

---

# 11. impact_analysis

## 11.1 Purpose

Stores results of enterprise Impact Analysis.

---

### Primary Key

impact_analysis_id

---

### Foreign Keys

lineage_mapping_id → lineage_mapping.lineage_mapping_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| impact_analysis_id | UUID | No |
| lineage_mapping_id | UUID | No |
| analysis_number | VARCHAR(50) | No |
| source_asset | VARCHAR(255) | No |
| impact_scope | VARCHAR(100) | No |
| affected_objects | INTEGER | No |
| analysis_date | TIMESTAMP | No |
| requested_by | VARCHAR(100) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- impact_analysis_id

Foreign Key

- lineage_mapping_id

Unique

- analysis_number

Indexes

- idx_impact_analysis_number
- idx_impact_analysis_scope
- idx_impact_analysis_date
- idx_impact_analysis_status

---

# 12. lineage_version

## 12.1 Purpose

Maintains version history of Lineage Flows.

---

### Primary Key

lineage_version_id

---

### Foreign Keys

lineage_flow_id → lineage_flow.lineage_flow_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| lineage_version_id | UUID | No |
| lineage_flow_id | UUID | No |
| version_number | VARCHAR(20) | No |
| change_summary | TEXT | No |
| effective_date | DATE | No |
| approved_by | VARCHAR(100) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- lineage_version_id

Foreign Key

- lineage_flow_id

Unique

- lineage_flow_id + version_number

Indexes

- idx_lineage_version_flow
- idx_lineage_version_number
- idx_lineage_version_status

---

# 13. lineage_snapshot

## 13.1 Purpose

Stores point-in-time snapshots of enterprise Lineage.

Snapshots support auditing, historical comparison, compliance, and rollback.

---

### Primary Key

lineage_snapshot_id

---

### Foreign Keys

lineage_flow_id → lineage_flow.lineage_flow_id

---

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| lineage_snapshot_id | UUID | No |
| lineage_flow_id | UUID | No |
| snapshot_name | VARCHAR(255) | No |
| snapshot_date | TIMESTAMP | No |
| created_by | VARCHAR(100) | No |
| status | VARCHAR(30) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

---

### Constraints

Primary Key

- lineage_snapshot_id

Foreign Key

- lineage_flow_id

Unique

- lineage_flow_id + snapshot_name

Indexes

- idx_lineage_snapshot_flow
- idx_lineage_snapshot_name
- idx_lineage_snapshot_date
- idx_lineage_snapshot_status

---

# 14. Foreign Key Matrix

The following table summarizes all foreign key relationships within the Data Lineage module.

| Parent Table | Child Table | Foreign Key |
|--------------|-------------|-------------|
| lineage_source | lineage_flow | lineage_source_id |
| lineage_process | lineage_flow | lineage_process_id |
| lineage_flow | lineage_transformation | lineage_flow_id |
| lineage_flow | lineage_mapping | lineage_flow_id |
| lineage_transformation | lineage_mapping | lineage_transformation_id |
| lineage_mapping | impact_analysis | lineage_mapping_id |
| lineage_flow | lineage_version | lineage_flow_id |
| lineage_flow | lineage_snapshot | lineage_flow_id |

---

# 15. Referential Integrity Rules

The Data Lineage module shall enforce referential integrity through foreign key constraints.

The following rules shall apply.

- A Lineage Flow cannot exist without a Lineage Source.
- A Lineage Flow cannot exist without a Lineage Process.
- A Lineage Transformation cannot exist without a Lineage Flow.
- A Lineage Mapping cannot exist without a Lineage Flow.
- A Lineage Mapping may optionally reference a Lineage Transformation.
- An Impact Analysis cannot exist without a Lineage Mapping.
- A Lineage Version cannot exist without a Lineage Flow.
- A Lineage Snapshot cannot exist without a Lineage Flow.
- Parent records shall not be physically deleted while dependent child records exist.

---

# 16. Index Strategy

## 16.1 Purpose

Indexes shall support efficient enterprise lineage discovery and traversal.

Optimization objectives include:

- Lineage visualization
- Impact analysis
- Source-to-target tracing
- Column-level lineage
- Transformation lookup
- AI-assisted lineage discovery
- Regulatory reporting

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
| lineage_flow | lineage_source_id + lineage_process_id |
| lineage_flow | flow_type + status |
| lineage_transformation | lineage_flow_id + sequence_number |
| lineage_mapping | lineage_flow_id + source_attribute |
| lineage_mapping | lineage_flow_id + target_attribute |
| impact_analysis | source_asset + analysis_date |
| lineage_version | lineage_flow_id + version_number |
| lineage_snapshot | lineage_flow_id + snapshot_date |

---

## 16.4 Search Optimization

Additional indexes should support:

- Source Name
- Target Name
- Process Name
- Flow Name
- Business Domain
- System Name
- Transformation Type
- Mapping Type
- Analysis Number
- Snapshot Name

These indexes improve:

- Global Search
- Lineage Visualization
- Impact Analysis
- Regulatory Reporting
- AI Retrieval

---

# 17. Performance Considerations

The Data Lineage module shall support enterprise-scale lineage management.

Performance objectives include:

- Fast lineage traversal
- Efficient impact analysis
- Low-latency visualization
- Rapid dependency discovery
- High-performance column-level lineage

Future enhancements may include:

- Recursive query optimization
- Materialized lineage paths
- Graph cache
- Incremental lineage discovery
- Parallel lineage analysis
- Event-driven lineage updates

---

# 18. Physical Design Standards

The Data Lineage module shall follow enterprise database standards.

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

- discovery_method
- discovery_confidence
- scan_job_id
- scan_timestamp
- parser_version
- lineage_engine_version
- graph_node_identifier

---

# 19. Recommended Database Views

The following PostgreSQL views are recommended.

| View | Purpose |
|------|---------|
| vw_lineage_sources | Enterprise lineage sources |
| vw_lineage_targets | Enterprise lineage targets |
| vw_lineage_flows | Complete source-to-target lineage |
| vw_lineage_transformations | Transformation catalog |
| vw_lineage_mappings | Column-level lineage |
| vw_lineage_versions | Version history |
| vw_lineage_snapshots | Historical lineage snapshots |
| vw_impact_analysis | Impact analysis results |
| vw_lineage_dashboard | Executive lineage dashboard |

These views simplify dashboard development, lineage visualization, regulatory reporting, AI-assisted discovery, and operational analysis.

---

# 20. Summary

The Data Lineage Physical Data Model defines the PostgreSQL implementation of the Data Lineage module.

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

The Data Lineage module provides the enterprise repository for discovering, managing, visualizing, and governing data lineage while integrating with the Metadata Repository, Business Glossary, Business Rules, Data Quality, Workflow, Reporting, and AI Services.

This document serves as the implementation blueprint for:

- PostgreSQL Database
- SQLAlchemy ORM Models
- Alembic Migration Scripts
- Repository Layer
- Lineage Engine
- Impact Analysis Engine
- REST APIs
- Reporting Services
- AI Services

