# Metadata Repository Physical Data Model

## Enterprise Data Governance Platform

**Module:** Metadata Repository

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

This document defines the PostgreSQL Physical Data Model for the Metadata Repository Module.

The Physical Data Model translates the Logical Data Model into implementable PostgreSQL database objects.

It defines:

- Tables
- Columns
- PostgreSQL Data Types
- Primary Keys
- Foreign Keys
- Constraints
- Indexes
- Default Values

---

# 2. Scope

The Metadata Repository Physical Data Model consists of the following tables.

| Table |
|---------|
| source_system |
| database |
| schema |
| table |
| column |
| view |
| file |
| api |
| data_asset |

---

# 3. Physical Design Standards

The Metadata Repository follows these standards.

## Naming

- snake_case
- Singular table names
- Lowercase
- UUID Primary Keys

---

## Primary Keys

All tables shall use UUID Primary Keys.

Example

```
source_system_id UUID PRIMARY KEY
```

---

## Foreign Keys

All relationships shall use UUID Foreign Keys.

---

## Audit Columns

Every table shall contain:

- created_by
- created_date
- modified_by
- modified_date

---

## Soft Delete

All tables shall contain:

```
is_active BOOLEAN
```

instead of physical deletion.

---

# 4. Physical Entity Model

| Logical Entity | Physical Table |
|---------------|----------------|
| Source System | source_system |
| Database | database |
| Schema | schema |
| Table | table |
| Column | column |
| View | view |
| File | file |
| API | api |
| Data Asset | data_asset |

---

## 5.1 source_system

### Purpose

Stores enterprise source systems.

### Primary Key

source_system_id

### Columns

| Column | PostgreSQL Type | Nullable | Notes |
|----------|----------------|----------|------|
| source_system_id | UUID | No | Primary Key |
| system_code | VARCHAR(50) | No | Unique |
| system_name | VARCHAR(200) | No | |
| description | TEXT | Yes | |
| system_type | VARCHAR(50) | No | |
| vendor | VARCHAR(100) | Yes | |
| business_domain | VARCHAR(100) | No | |
| environment | VARCHAR(30) | No | |
| owner | VARCHAR(100) | No | |
| steward | VARCHAR(100) | No | |
| status | VARCHAR(30) | No | |
| created_by | VARCHAR(100) | No | |
| created_date | TIMESTAMP | No | |
| modified_by | VARCHAR(100) | Yes | |
| modified_date | TIMESTAMP | Yes | |
| is_active | BOOLEAN | No | Default TRUE |

### Constraints

Primary Key

- source_system_id

Unique

- system_code

Indexes

- idx_source_system_name
- idx_source_system_domain
- idx_source_system_status

---

## 6.1 database

### Purpose

Stores enterprise databases.

### Primary Key

database_id

### Foreign Keys

source_system_id

### Columns

| Column | PostgreSQL Type | Nullable |
|----------|----------------|----------|
| database_id | UUID | No |
| source_system_id | UUID | No |
| database_name | VARCHAR(150) | No |
| database_type | VARCHAR(50) | No |
| version | VARCHAR(30) | Yes |
| description | TEXT | Yes |
| owner | VARCHAR(100) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

### Constraints

PK

database_id

FK

source_system_id

→ source_system

Unique

source_system_id + database_name

Indexes

- idx_database_name
- idx_database_type

---

# 7. Physical Table Definitions

## 7.1 database_schema

### Purpose

Stores database schemas belonging to enterprise databases.

### Primary Key

database_schema_id

### Foreign Keys

database_id → database_catalog.database_id

### Columns

| Column | PostgreSQL Type | Nullable | Notes |
|---------|-----------------|----------|------|
| database_schema_id | UUID | No | Primary Key |
| database_id | UUID | No | Foreign Key |
| schema_name | VARCHAR(150) | No | |
| description | TEXT | Yes | |
| owner | VARCHAR(100) | No | |
| status | VARCHAR(30) | No | |
| created_by | VARCHAR(100) | No | |
| created_date | TIMESTAMP | No | DEFAULT CURRENT_TIMESTAMP |
| modified_by | VARCHAR(100) | Yes | |
| modified_date | TIMESTAMP | Yes | |
| is_active | BOOLEAN | No | DEFAULT TRUE |

### Constraints

Primary Key

- database_schema_id

Foreign Key

- database_id → database_catalog

Unique

- database_id + schema_name

Indexes

- idx_schema_name
- idx_schema_database

---

## 7.2 database_table

### Purpose

Stores enterprise database tables.

### Primary Key

database_table_id

### Foreign Keys

database_schema_id → database_schema.database_schema_id

### Columns

| Column | PostgreSQL Type | Nullable |
|---------|-----------------|----------|
| database_table_id | UUID | No |
| database_schema_id | UUID | No |
| table_name | VARCHAR(200) | No |
| display_name | VARCHAR(200) | No |
| description | TEXT | Yes |
| table_type | VARCHAR(50) | No |
| row_count | BIGINT | Yes |
| owner | VARCHAR(100) | No |
| classification | VARCHAR(50) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

### Constraints

Primary Key

- database_table_id

Foreign Key

- database_schema_id

Unique

- database_schema_id + table_name

Indexes

- idx_table_name
- idx_table_classification
- idx_table_status

---

## 7.3 table_column

### Purpose

Stores metadata for table columns.

### Primary Key

table_column_id

### Foreign Keys

database_table_id → database_table.database_table_id

### Columns

| Column | PostgreSQL Type | Nullable |
|---------|-----------------|----------|
| table_column_id | UUID | No |
| database_table_id | UUID | No |
| column_name | VARCHAR(200) | No |
| display_name | VARCHAR(200) | No |
| description | TEXT | Yes |
| logical_data_type | VARCHAR(50) | No |
| nullable | BOOLEAN | No |
| primary_key_flag | BOOLEAN | No |
| foreign_key_flag | BOOLEAN | No |
| classification | VARCHAR(50) | No |
| critical_data_element_flag | BOOLEAN | No |
| ordinal_position | INTEGER | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

### Constraints

Primary Key

- table_column_id

Foreign Key

- database_table_id

Unique

- database_table_id + column_name

Indexes

- idx_column_name
- idx_column_cde
- idx_column_datatype

---

## 7.4 database_view

### Purpose

Stores database view metadata.

### Primary Key

database_view_id

### Foreign Keys

database_schema_id → database_schema.database_schema_id

### Columns

| Column | PostgreSQL Type | Nullable |
|---------|-----------------|----------|
| database_view_id | UUID | No |
| database_schema_id | UUID | No |
| view_name | VARCHAR(200) | No |
| display_name | VARCHAR(200) | No |
| description | TEXT | Yes |
| view_type | VARCHAR(50) | No |
| sql_definition | TEXT | Yes |
| owner | VARCHAR(100) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

### Constraints

Primary Key

- database_view_id

Foreign Key

- database_schema_id

Unique

- database_schema_id + view_name

Indexes

- idx_view_name
- idx_view_status

---

# 7.5 file_asset

### Purpose

Stores metadata for enterprise files managed within the platform.

### Primary Key

file_asset_id

### Foreign Keys

source_system_id → source_system.source_system_id

### Columns

| Column | PostgreSQL Type | Nullable |
|---------|-----------------|----------|
| file_asset_id | UUID | No |
| source_system_id | UUID | No |
| file_name | VARCHAR(255) | No |
| display_name | VARCHAR(255) | No |
| description | TEXT | Yes |
| file_type | VARCHAR(50) | No |
| file_format | VARCHAR(50) | No |
| file_path | VARCHAR(1000) | Yes |
| owner | VARCHAR(100) | No |
| classification | VARCHAR(50) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

### Constraints

Primary Key

- file_asset_id

Foreign Key

- source_system_id

Unique

- source_system_id + file_name

Indexes

- idx_file_name
- idx_file_type
- idx_file_status

---

# 7.6 api_asset

### Purpose

Stores metadata for enterprise APIs.

### Primary Key

api_asset_id

### Foreign Keys

source_system_id → source_system.source_system_id

### Columns

| Column | PostgreSQL Type | Nullable |
|---------|-----------------|----------|
| api_asset_id | UUID | No |
| source_system_id | UUID | No |
| api_name | VARCHAR(255) | No |
| display_name | VARCHAR(255) | No |
| description | TEXT | Yes |
| api_type | VARCHAR(30) | No |
| api_version | VARCHAR(30) | No |
| base_url | VARCHAR(500) | Yes |
| owner | VARCHAR(100) | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

### Constraints

Primary Key

- api_asset_id

Foreign Key

- source_system_id

Unique

- source_system_id + api_name + api_version

Indexes

- idx_api_name
- idx_api_type
- idx_api_status

---

# 7.7 data_asset

### Purpose

Represents the common abstraction layer for all governed technical assets.

### Primary Key

data_asset_id

### Columns

| Column | PostgreSQL Type | Nullable |
|---------|-----------------|----------|
| data_asset_id | UUID | No |
| asset_type | VARCHAR(30) | No |
| asset_identifier | UUID | No |
| asset_name | VARCHAR(255) | No |
| display_name | VARCHAR(255) | No |
| description | TEXT | Yes |
| owner | VARCHAR(100) | No |
| steward | VARCHAR(100) | No |
| classification | VARCHAR(50) | No |
| critical_data_element_flag | BOOLEAN | No |
| status | VARCHAR(30) | No |
| created_by | VARCHAR(100) | No |
| created_date | TIMESTAMP | No |
| modified_by | VARCHAR(100) | Yes |
| modified_date | TIMESTAMP | Yes |
| is_active | BOOLEAN | No |

### Constraints

Primary Key

- data_asset_id

Unique

- asset_type + asset_identifier

Indexes

- idx_asset_type
- idx_asset_name
- idx_asset_classification
- idx_asset_status

---

# 8. Foreign Key Matrix

| Parent Table | Child Table | Foreign Key |
|---------------|-------------|-------------|
| source_system | database_catalog | source_system_id |
| source_system | file_asset | source_system_id |
| source_system | api_asset | source_system_id |
| database_catalog | database_schema | database_id |
| database_schema | database_table | database_schema_id |
| database_table | table_column | database_table_id |
| database_schema | database_view | database_schema_id |

---

# 9. Index Strategy

## 9.1 Objectives

Indexes shall be created to support:

- Fast searching
- Metadata discovery
- Foreign key joins
- Filtering
- Reporting
- AI-assisted search

---

## 9.2 Standard Indexes

Every table shall include indexes for:

- Primary Key
- Foreign Keys
- Name
- Status
- Classification (where applicable)

---

## 9.3 Composite Indexes

Composite indexes shall be created for common search combinations.

Examples include:

- Source System + Database Name
- Database + Schema Name
- Schema + Table Name
- Table + Column Name

---

# 10. Performance Considerations

The Metadata Repository shall support enterprise-scale metadata management.

Performance objectives include:

- Fast metadata lookup
- Efficient hierarchy traversal
- Optimized joins
- Minimal duplicate data
- Efficient indexing

Future enhancements may include:

- Table partitioning
- Read replicas
- Full-text search
- Materialized views
- Metadata caching

---

# 11. Physical Design Standards

The Metadata Repository shall adhere to the following standards.

- Third Normal Form (3NF)
- UUID Primary Keys
- Foreign Key Constraints
- Soft Deletes
- Audit Columns
- Consistent Naming Standards
- Indexed Foreign Keys
- Optimized Search Performance

---

# 12. Summary

The Metadata Repository Physical Data Model defines the PostgreSQL implementation of the Metadata Repository module.

It specifies:

- Physical Tables
- Columns
- PostgreSQL Data Types
- Primary Keys
- Foreign Keys
- Constraints
- Indexes
- Performance Standards

This document serves as the implementation blueprint for:

- PostgreSQL Database
- SQLAlchemy ORM Models
- Alembic Migration Scripts
- Repository Layer
- REST APIs
- Metadata Repository Services

The Metadata Repository provides the technical metadata foundation upon which all remaining modules of the Enterprise Data Governance Platform are built.