# Metadata Repository Logical Data Model

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
- 09_DataDictionary.md
- 10_NamingStandards.md

---

# 1. Purpose

## 1.1 Objective

This document defines the Logical Data Model for the Metadata Repository Module.

The Metadata Repository is the foundational module of the Enterprise Data Governance Platform and provides centralized management of enterprise technical metadata.

This Logical Data Model defines:

- Logical Entities
- Entity Attributes
- Entity Relationships
- Primary Keys
- Foreign Keys
- Cardinality
- Business Constraints

The Logical Data Model is technology independent and serves as the blueprint for the Physical Data Model.

---

# 2. Scope

The Metadata Repository manages technical metadata describing enterprise information assets.

The module includes the following logical entities:

- Source System
- Database
- Schema
- Table
- Column
- View
- File
- API
- Data Asset

The module provides metadata consumed by every other platform module.

---

# 3. Module Responsibilities

The Metadata Repository is responsible for:

- Registering enterprise systems
- Managing technical metadata
- Maintaining metadata hierarchy
- Supporting metadata search
- Providing metadata to downstream modules
- Supporting metadata versioning
- Supporting metadata governance
- Providing metadata for AI services

---

# 4. Logical Entity Model

The Metadata Repository consists of the following logical entities.

| Entity | Description |
|---------|-------------|
| Source System | Enterprise application or system |
| Database | Logical database |
| Schema | Database schema |
| Table | Database table |
| Column | Table column |
| View | Database view |
| File | Enterprise file asset |
| API | Enterprise API |
| Data Asset | Generic governed information asset |

---

# 5. Entity Relationships

The Metadata Repository follows the hierarchy below.

```text
Source System
      │
      ▼
Database
      │
      ▼
Schema
      │
      ▼
Table
      │
      ▼
Column

Table
   │
   ├── View
   ├── File
   └── API

All technical objects

↓

Data Asset
```

---

# 6. Logical Relationship Matrix

| Parent Entity | Child Entity | Relationship |
|---------------|-------------|--------------|
| Source System | Database | One-to-Many |
| Database | Schema | One-to-Many |
| Schema | Table | One-to-Many |
| Table | Column | One-to-Many |
| Table | View | One-to-Many |
| Source System | File | One-to-Many |
| Source System | API | One-to-Many |
| Data Asset | Table | One-to-One |
| Data Asset | View | One-to-One |
| Data Asset | File | One-to-One |
| Data Asset | API | One-to-One |

---

# 7. Logical Entity Definitions

## 7.1 Source System

### Purpose

Represents an enterprise application, platform, or system that creates, consumes, or manages enterprise data.

Examples include Core Banking, CRM, ERP, SAP, Salesforce, Data Warehouse, and external vendor systems.

---

### Primary Key

Source System Identifier

---

### Business Key

Source System Code

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Source System Identifier | Unique identifier | Yes |
| Source System Code | Business code | Yes |
| Source System Name | Business name | Yes |
| Description | Description of the system | Yes |
| System Type | Application category | Yes |
| Vendor | Software vendor | No |
| Business Domain | Owning business domain | Yes |
| Environment | Production, UAT, Development | Yes |
| Status | Lifecycle status | Yes |
| Data Owner | Business owner | Yes |
| Data Steward | Steward responsible | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Source System | Database | 1 : N |
| Source System | File | 1 : N |
| Source System | API | 1 : N |

---

### Business Rules

- Every Source System shall have a unique Source System Code.
- Every Source System shall belong to one Business Domain.
- Every Source System shall have one Data Owner.
- Every Source System shall have one lifecycle status.

---

# 7.2 Database

### Purpose

Represents a logical database hosted within a Source System.

---

### Primary Key

Database Identifier

---

### Business Key

Database Name within Source System

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Database Identifier | Unique identifier | Yes |
| Database Name | Database name | Yes |
| Database Type | PostgreSQL, Oracle, SQL Server etc. | Yes |
| Version | Database version | No |
| Description | Business description | Yes |
| Source System Identifier | Parent Source System | Yes |
| Owner | Database owner | Yes |
| Status | Lifecycle status | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Source System | Database | 1 : N |
| Database | Schema | 1 : N |

---

### Business Rules

- Every Database belongs to one Source System.
- Database Names shall be unique within a Source System.
- Every Database shall contain one or more Schemas.

---

# 7.3 Schema

### Purpose

Represents a logical grouping of database objects.

---

### Primary Key

Schema Identifier

---

### Business Key

Schema Name

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Schema Identifier | Unique identifier | Yes |
| Schema Name | Schema name | Yes |
| Description | Description | Yes |
| Database Identifier | Parent Database | Yes |
| Owner | Owner | Yes |
| Status | Lifecycle status | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Database | Schema | 1 : N |
| Schema | Table | 1 : N |

---

### Business Rules

- Every Schema belongs to one Database.
- Schema Names shall be unique within a Database.
- Every Schema shall contain one or more Tables.

---

# 7.4 Table

### Purpose

Represents a logical database table.

---

### Primary Key

Table Identifier

---

### Business Key

Schema + Table Name

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Table Identifier | Unique identifier | Yes |
| Table Name | Table name | Yes |
| Display Name | Friendly name | Yes |
| Description | Business description | Yes |
| Table Type | Base, Temporary, External | Yes |
| Schema Identifier | Parent Schema | Yes |
| Row Count | Approximate record count | No |
| Data Owner | Owner | Yes |
| Classification | Security classification | Yes |
| Status | Lifecycle status | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Schema | Table | 1 : N |
| Table | Column | 1 : N |
| Table | View | 1 : N |

---

### Business Rules

- Every Table belongs to one Schema.
- Table Names shall be unique within a Schema.
- Every Table shall contain one or more Columns.
- Every Table shall be represented as a Data Asset.

---

# 7.5 Column

### Purpose

Represents an individual attribute within a database table.

---

### Primary Key

Column Identifier

---

### Business Key

Schema + Table + Column Name

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Column Identifier | Unique identifier | Yes |
| Column Name | Column name | Yes |
| Display Name | Friendly name | Yes |
| Description | Business description | Yes |
| Logical Data Type | Enterprise data type | Yes |
| Nullable | Indicates null support | Yes |
| Primary Key Flag | Indicates PK | Yes |
| Foreign Key Flag | Indicates FK | Yes |
| Table Identifier | Parent Table | Yes |
| Classification | Data classification | Yes |
| Critical Data Element Flag | Indicates CDE | No |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Table | Column | 1 : N |

---

### Business Rules

- Every Column belongs to one Table.
- Column Names shall be unique within a Table.
- Every Column shall have a Logical Data Type.
- Every Column shall inherit ownership from its parent Table unless explicitly overridden.

---

# 7.6 View

### Purpose

Represents a logical database view that exposes data derived from one or more database tables.

Views simplify data access, reporting, and analytics without duplicating underlying data.

---

### Primary Key

View Identifier

---

### Business Key

Schema + View Name

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| View Identifier | Unique identifier | Yes |
| View Name | View name | Yes |
| Display Name | Friendly display name | Yes |
| Description | Business description | Yes |
| View Type | Standard, Materialized, System | Yes |
| Schema Identifier | Parent Schema | Yes |
| SQL Definition | View definition | No |
| Owner | Business owner | Yes |
| Status | Lifecycle status | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Schema | View | 1 : N |
| View | Data Asset | 1 : 1 |

---

### Business Rules

- Every View belongs to one Schema.
- View Names shall be unique within a Schema.
- Every View shall be represented as a Data Asset.

---

# 7.7 File

### Purpose

Represents a structured or semi-structured enterprise file managed within the platform.

Examples include CSV, Excel, XML, JSON, Parquet, and Avro files.

---

### Primary Key

File Identifier

---

### Business Key

Source System + File Name

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| File Identifier | Unique identifier | Yes |
| File Name | File name | Yes |
| Display Name | Friendly display name | Yes |
| Description | Business description | Yes |
| File Type | CSV, Excel, JSON, XML, etc. | Yes |
| File Format | Physical format | Yes |
| Source System Identifier | Parent Source System | Yes |
| File Path | Logical storage location | No |
| Owner | Business owner | Yes |
| Classification | Security classification | Yes |
| Status | Lifecycle status | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Source System | File | 1 : N |
| File | Data Asset | 1 : 1 |

---

### Business Rules

- Every File belongs to one Source System.
- Every File shall have one File Type.
- Every File shall be represented as a Data Asset.

---

# 7.8 API

### Purpose

Represents an enterprise interface used for exchanging information between applications.

Both internal and external APIs are supported.

---

### Primary Key

API Identifier

---

### Business Key

API Name

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| API Identifier | Unique identifier | Yes |
| API Name | API name | Yes |
| Display Name | Friendly display name | Yes |
| Description | Business description | Yes |
| API Type | REST, SOAP, GraphQL | Yes |
| API Version | Version number | Yes |
| Base URL | Endpoint URL | No |
| Source System Identifier | Parent Source System | Yes |
| Owner | Business owner | Yes |
| Status | Lifecycle status | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Source System | API | 1 : N |
| API | Data Asset | 1 : 1 |

---

### Business Rules

- Every API belongs to one Source System.
- Every API shall have one Version.
- Every API shall be represented as a Data Asset.

---

# 7.9 Data Asset

### Purpose

Represents a generic governed information asset within the Enterprise Data Governance Platform.

The Data Asset provides a common abstraction layer that allows governance capabilities to operate consistently across different technical asset types.

Supported Data Asset types include:

- Table
- View
- File
- API

---

### Primary Key

Data Asset Identifier

---

### Business Key

Asset Type + Asset Name

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Data Asset Identifier | Unique identifier | Yes |
| Asset Name | Business name | Yes |
| Display Name | Friendly display name | Yes |
| Asset Type | Table, View, File, API | Yes |
| Description | Business description | Yes |
| Owner | Business owner | Yes |
| Steward | Data steward | Yes |
| Classification | Security classification | Yes |
| Critical Data Element Flag | Indicates CDE | No |
| Status | Lifecycle status | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Data Asset | Business Term | M : N |
| Data Asset | Data Quality Rule | 1 : N |
| Data Asset | Lineage | 1 : N |
| Data Asset | Policy | M : N |
| Data Asset | Classification | N : 1 |

---

### Business Rules

- Every governed technical object shall be represented as a Data Asset.
- A Data Asset may be linked to multiple Business Terms.
- A Data Asset may have multiple Data Quality Rules.
- A Data Asset may participate in one or more Lineage relationships.
- Every Data Asset shall have a Classification.
- Every Data Asset shall have an Owner.

---

# 8. Metadata Repository Logical Constraints

The Metadata Repository shall enforce the following logical constraints.

## 8.1 Uniqueness

- Source System Codes shall be unique.
- Database Names shall be unique within a Source System.
- Schema Names shall be unique within a Database.
- Table Names shall be unique within a Schema.
- Column Names shall be unique within a Table.
- View Names shall be unique within a Schema.
- File Names shall be unique within a Source System.
- API Names shall be unique within a Source System.

---

## 8.2 Ownership

Every logical entity shall have:

- One Data Owner
- One Data Steward
- One Lifecycle Status

---

## 8.3 Governance

Every Data Asset shall:

- Be classified.
- Be auditable.
- Support versioning.
- Support workflow approvals.
- Support AI-assisted metadata enrichment.

---

# 9. Summary

The Metadata Repository Logical Data Model defines the logical structure of the foundational module within the Enterprise Data Governance Platform.

It establishes the logical entities, relationships, constraints, and governance principles required to manage enterprise technical metadata.

The Metadata Repository serves as the authoritative source of technical metadata for all other platform modules, including Business Glossary, Data Quality, Data Lineage, Governance, Workflow, Reporting, and AI Services.

This logical model provides the blueprint for the Metadata Repository Physical Data Model, PostgreSQL schema, REST APIs, user interface, and implementation.
