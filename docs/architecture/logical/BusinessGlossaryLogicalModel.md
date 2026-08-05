# Business Glossary Logical Data Model

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
- 09_DataDictionary.md
- 10_NamingStandards.md

---

# 1. Purpose

## 1.1 Objective

This document defines the Logical Data Model for the Business Glossary module.

The Business Glossary provides a centralized repository for managing enterprise business terminology, definitions, classifications, ownership, and relationships between business concepts and technical metadata.

The logical model defines:

- Logical Entities
- Entity Attributes
- Entity Relationships
- Primary Keys
- Business Keys
- Business Rules
- Cardinality
- Logical Constraints

This model serves as the blueprint for the Physical Data Model, REST APIs, User Interface, and implementation.

---

# 2. Scope

The Business Glossary module manages enterprise business metadata.

The module consists of the following logical entities.

- Business Glossary
- Business Category
- Business Term
- Acronym
- Synonym
- Business Definition
- Business Rule Association
- Business Term Relationship

The module integrates with:

- Metadata Repository
- Governance
- Data Quality
- Data Lineage
- AI Services

---

# 3. Module Responsibilities

The Business Glossary module is responsible for:

- Managing business terminology
- Maintaining enterprise definitions
- Standardizing business language
- Managing synonyms and acronyms
- Linking business concepts to technical metadata
- Supporting enterprise search
- Providing metadata for AI assistants
- Supporting regulatory and business documentation

---

# 4. Logical Entity Model

The Business Glossary module consists of the following logical entities.

| Entity | Description |
|----------|-------------|
| Business Glossary | Container for enterprise business terminology |
| Business Category | Logical grouping of business terms |
| Business Term | Approved business concept |
| Business Definition | Formal definition of a business term |
| Acronym | Approved abbreviation |
| Synonym | Alternate business name |
| Business Rule Association | Links business rules to business terms |
| Business Term Relationship | Defines relationships between business terms |

---

# 5. Entity Relationships

The Business Glossary follows the logical structure below.

```text
Business Glossary
        │
        ▼
Business Category
        │
        ▼
Business Term
   ├──────────────┐
   ▼              ▼
Definition     Acronym
   │              │
   └──────┬───────┘
          ▼
      Synonym
          │
          ▼
Business Rule Association
          │
          ▼
Business Term Relationship
          │
          ▼
Metadata Repository
```

---

# 6. Logical Relationship Matrix

| Parent Entity | Child Entity | Relationship |
|---------------|-------------|--------------|
| Business Glossary | Business Category | One-to-Many |
| Business Category | Business Term | One-to-Many |
| Business Term | Business Definition | One-to-One |
| Business Term | Acronym | One-to-Many |
| Business Term | Synonym | One-to-Many |
| Business Term | Business Rule Association | One-to-Many |
| Business Term | Business Term Relationship | One-to-Many |
| Business Term | Data Asset | Many-to-Many |

---

# 7. Logical Entity Definitions

## 7.1 Business Glossary

### Purpose

Represents the top-level repository containing approved enterprise business terminology.

A Business Glossary organizes business terms into logical business categories and provides a standardized vocabulary across the enterprise.

---

### Primary Key

Business Glossary Identifier

---

### Business Key

Glossary Name

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Business Glossary Identifier | Unique identifier | Yes |
| Glossary Name | Name of the glossary | Yes |
| Display Name | User-friendly name | Yes |
| Description | Business description | Yes |
| Version | Glossary version | Yes |
| Status | Lifecycle status | Yes |
| Owner | Business owner | Yes |
| Steward | Business steward | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Business Glossary | Business Category | 1 : N |

---

### Business Rules

- Every Business Glossary shall have a unique name.
- Every Business Glossary shall have one Owner.
- Every Business Glossary shall contain one or more Business Categories.
- Every Business Glossary shall maintain version history.

---

# 7.2 Business Category

### Purpose

Represents a logical grouping of Business Terms within a Business Glossary.

Business Categories organize business knowledge into meaningful business domains, making enterprise terminology easier to discover, manage, and govern.

Examples include:

- Customer
- Accounts
- Loans
- Payments
- Products
- Treasury
- Risk
- Compliance

---

### Primary Key

Business Category Identifier

---

### Business Key

Business Glossary + Category Name

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Business Category Identifier | Unique identifier | Yes |
| Business Glossary Identifier | Parent Business Glossary | Yes |
| Category Name | Business category name | Yes |
| Display Name | Friendly name | Yes |
| Description | Business description | Yes |
| Parent Category | Parent business category | No |
| Status | Lifecycle status | Yes |
| Owner | Business owner | Yes |
| Steward | Business steward | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Business Glossary | Business Category | 1 : N |
| Business Category | Business Term | 1 : N |

---

### Business Rules

- Every Business Category belongs to one Business Glossary.
- Category Names shall be unique within a Business Glossary.
- Categories may contain sub-categories.
- Every Business Category shall contain one or more Business Terms.

---

# 7.3 Business Term

### Purpose

Represents an approved business concept used consistently across the enterprise.

Business Terms provide the common language between business users, technical teams, governance teams, reporting solutions, and AI services.

---

### Primary Key

Business Term Identifier

---

### Business Key

Business Category + Business Term Name

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Business Term Identifier | Unique identifier | Yes |
| Business Category Identifier | Parent Category | Yes |
| Business Term Name | Approved business term | Yes |
| Display Name | Friendly display name | Yes |
| Preferred Definition | Primary business definition | Yes |
| Business Domain | Owning business domain | Yes |
| Business Capability | Associated capability | No |
| Status | Lifecycle status | Yes |
| Owner | Business owner | Yes |
| Steward | Business steward | Yes |
| Classification | Information classification | No |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Business Category | Business Term | 1 : N |
| Business Term | Business Definition | 1 : N |
| Business Term | Acronym | 1 : N |
| Business Term | Synonym | 1 : N |
| Business Term | Business Rule Association | 1 : N |
| Business Term | Business Term Relationship | 1 : N |
| Business Term | Data Asset | M : N |

---

### Business Rules

- Every Business Term belongs to one Business Category.
- Business Term Names shall be unique within a Business Glossary.
- Every Business Term shall have at least one approved definition.
- Every Business Term shall have one Owner.
- Every Business Term may be linked to multiple Data Assets.

---

# 7.4 Business Definition

### Purpose

Represents the formal business definition of a Business Term.

A Business Term may have multiple definitions over time through versioning, but only one active approved definition.

---

### Primary Key

Business Definition Identifier

---

### Business Key

Business Term + Version

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Business Definition Identifier | Unique identifier | Yes |
| Business Term Identifier | Parent Business Term | Yes |
| Definition Text | Business definition | Yes |
| Definition Source | Source of definition | No |
| Version | Definition version | Yes |
| Status | Lifecycle status | Yes |
| Effective Date | Effective date | Yes |
| Expiry Date | Expiration date | No |
| Approved By | Approver | Yes |
| Approved Date | Approval timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Business Term | Business Definition | 1 : N |

---

### Business Rules

- Every Business Definition belongs to one Business Term.
- Only one definition may be Active at any time.
- Historical definitions shall be retained.

---

# 7.5 Acronym

### Purpose

Represents an approved abbreviation for a Business Term.

Example:

| Business Term | Acronym |
|---------------|----------|
| Customer Information File | CIF |
| Know Your Customer | KYC |
| Anti Money Laundering | AML |

---

### Primary Key

Acronym Identifier

---

### Business Key

Business Term + Acronym

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Acronym Identifier | Unique identifier | Yes |
| Business Term Identifier | Parent Business Term | Yes |
| Acronym | Approved abbreviation | Yes |
| Description | Description | No |
| Status | Lifecycle status | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Business Term | Acronym | 1 : N |

---

### Business Rules

- Acronyms shall be unique within the Business Glossary.
- Every Acronym belongs to one Business Term.

---

# 7.6 Synonym

### Purpose

Represents an alternate business name for a Business Term.

Synonyms improve metadata discovery and enterprise search.

---

### Primary Key

Synonym Identifier

---

### Business Key

Business Term + Synonym

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Synonym Identifier | Unique identifier | Yes |
| Business Term Identifier | Parent Business Term | Yes |
| Synonym | Alternate business name | Yes |
| Status | Lifecycle status | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Business Term | Synonym | 1 : N |

---

### Business Rules

- Synonyms improve search but do not replace the approved Business Term.
- Duplicate Synonyms are not permitted within the same Business Glossary.

---

# 7.7 Business Rule Association

### Purpose

Represents the relationship between Business Terms and Business Rules.

A Business Rule may govern one or more Business Terms, and a Business Term may be governed by multiple Business Rules.

Examples:

- Customer Age ≥ 18
- Loan Amount > 0
- Account Number must be unique

---

### Primary Key

Business Rule Association Identifier

---

### Business Key

Business Term + Business Rule

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Business Rule Association Identifier | Unique identifier | Yes |
| Business Term Identifier | Parent Business Term | Yes |
| Business Rule Identifier | Associated Business Rule | Yes |
| Relationship Type | Governs, Validates, Calculates, Derives | Yes |
| Status | Lifecycle status | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Business Term | Business Rule Association | 1 : N |
| Business Rule | Business Rule Association | 1 : N |

---

### Business Rules

- Every association shall reference one Business Term.
- Every association shall reference one Business Rule.
- Duplicate associations are not permitted.
- Relationship Type shall be selected from the approved enumeration.

---

# 7.8 Business Term Relationship

### Purpose

Defines semantic relationships between Business Terms.

These relationships enable navigation, impact analysis, knowledge discovery, and AI-assisted reasoning.

Examples:

- Customer **owns** Account
- Account **contains** Transaction
- Loan **belongs to** Customer
- Product **is part of** Portfolio

---

### Primary Key

Business Term Relationship Identifier

---

### Business Key

Source Business Term + Relationship Type + Target Business Term

---

### Attributes

| Attribute | Description | Mandatory |
|-----------|-------------|-----------|
| Business Term Relationship Identifier | Unique identifier | Yes |
| Source Business Term Identifier | Parent Business Term | Yes |
| Target Business Term Identifier | Related Business Term | Yes |
| Relationship Type | Relationship classification | Yes |
| Description | Business explanation | No |
| Status | Lifecycle status | Yes |
| Created Date | Creation timestamp | Yes |
| Modified Date | Last modification timestamp | Yes |

---

### Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| Business Term | Business Term Relationship | 1 : N |

---

### Business Rules

- Source and Target Business Terms shall exist.
- A Business Term cannot reference itself.
- Duplicate relationships are not permitted.
- Relationship Type shall follow approved enterprise standards.

---

# 8. Logical Constraints

## 8.1 Uniqueness

The Business Glossary shall enforce the following uniqueness constraints.

- Business Glossary Name
- Category Name within a Business Glossary
- Business Term Name within a Business Glossary
- Acronym within a Business Glossary
- Synonym within a Business Glossary
- Business Definition Version for a Business Term

---

## 8.2 Ownership

Every Business Glossary entity shall have:

- Business Owner
- Business Steward
- Lifecycle Status

---

## 8.3 Versioning

The Business Glossary shall support version management.

Versioning applies to:

- Business Glossary
- Business Definition
- Business Terms

Historical versions shall remain available for audit and reference.

---

## 8.4 Metadata Integration

Every Business Term may be linked to one or more Data Assets from the Metadata Repository.

Supported asset types include:

- Database Tables
- Table Columns
- Database Views
- File Assets
- API Assets

These relationships provide traceability between business concepts and technical implementation.

---

# 9. Governance Rules

The Business Glossary module shall support enterprise governance through the following principles.

- Every Business Term shall have an assigned Business Owner.
- Every Business Term shall have an assigned Business Steward.
- Business Definitions shall be approved before becoming Active.
- Changes shall be fully auditable.
- Historical versions shall be retained.
- Every Business Term shall support workflow approval.
- AI-generated content shall require human approval before publication.

---

# 10. Summary

The Business Glossary Logical Data Model defines the logical structure for managing enterprise business terminology and business metadata.

The module provides:

- Enterprise Business Glossary
- Business Categories
- Business Terms
- Business Definitions
- Acronyms
- Synonyms
- Business Rule Associations
- Business Term Relationships

The Business Glossary establishes a common business vocabulary across the enterprise and creates traceability between business concepts and technical metadata managed within the Metadata Repository.

This logical model serves as the foundation for the Business Glossary Physical Data Model, REST APIs, User Interface, AI Services, and implementation.