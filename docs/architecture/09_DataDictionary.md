
# Enterprise Data Dictionary & Metadata Standards

## Enterprise Data Governance Platform

Version: 1.0

Status: Draft

---

## Foundation Reference

This document shall be read in conjunction with the following architecture documents:

- 00_EnterpriseArchitectureOverview.md
- 01_ProjectVision.md
- 02_BusinessRequirements.md
- 03_EnterpriseBusinessModel.md
- 04_ConceptualModel.md

# 1. Purpose

## 1.1 Objective

The Enterprise Data Dictionary defines the enterprise metadata standards used throughout the Enterprise Data Governance Platform.

This document establishes standardized attribute definitions, metadata conventions, validation rules, naming standards, audit attributes, and reusable metadata structures that ensure consistency across all platform modules.

The Data Dictionary serves as the authoritative reference for all logical entities, physical database objects, APIs, user interfaces, and AI services.

---

## 1.2 Goals

The objectives of this document are to:

- Standardize metadata definitions.
- Promote consistency across modules.
- Reduce duplication.
- Support governance.
- Improve interoperability.
- Enable AI understanding of enterprise metadata.
- Provide reusable metadata standards.
- Support future scalability.

---

# 2. Scope

This document applies to every platform module including:

- Metadata Repository
- Business Glossary
- Business Rules
- Data Quality
- Data Lineage
- Governance
- Workflow
- Security
- Reporting
- AI Services
- Administration

Every logical entity defined within the platform shall comply with the standards contained in this document.

---

# 3. Enterprise Metadata Standards

The platform shall maintain metadata according to the following principles.

- Every entity shall have a unique identifier.
- Every entity shall have a business name.
- Every entity shall have a business description.
- Every entity shall have an owner.
- Every entity shall have lifecycle information.
- Every entity shall support auditing.
- Every entity shall support versioning where applicable.
- Every entity shall support future extensibility.

---

# 4. Common Metadata Attributes

## 4.1 Overview

Every entity managed by the Enterprise Data Governance Platform shall include a standard set of metadata attributes.

These attributes provide consistency across all platform modules and simplify implementation, governance, reporting, auditing, and AI-assisted capabilities.

---

## 4.2 Mandatory Metadata Attributes

| Attribute | Description | Required |
|-----------|-------------|----------|
| Identifier | Unique identifier for the entity | Yes |
| Name | Business-friendly name | Yes |
| Display Name | User-friendly display name | Yes |
| Description | Business description | Yes |
| Entity Type | Type of metadata object | Yes |
| Status | Current lifecycle status | Yes |
| Owner | Business owner | Yes |
| Steward | Operational steward | Yes |
| Classification | Information classification | Yes |
| Version | Current version | Yes |
| Active Flag | Indicates whether the entity is active | Yes |

---

## 4.3 Optional Metadata Attributes

| Attribute | Description |
|-----------|-------------|
| Business Domain | Associated business domain |
| Business Capability | Associated business capability |
| Parent Entity | Parent metadata object |
| Tags | User-defined labels |
| Keywords | Search keywords |
| External Identifier | Identifier from external systems |
| Source Reference | Original source identifier |
| Notes | Additional comments |
| Documentation Link | Reference to supporting documentation |

---

## 4.4 Lifecycle Metadata

Every entity shall maintain lifecycle information.

| Attribute | Description |
|-----------|-------------|
| Lifecycle Stage | Current lifecycle phase |
| Effective Date | Date the entity becomes effective |
| Expiry Date | Date the entity expires |
| Review Date | Next scheduled review |
| Approval Status | Governance approval status |

---

# 5. Standard Data Types

## 5.1 Purpose

Logical data types provide a technology-independent representation of data.

These logical data types will later be mapped to PostgreSQL data types within the Physical Data Model.

---

## 5.2 Standard Logical Data Types

| Logical Data Type | Description |
|-------------------|-------------|
| Identifier | Unique identifier |
| Short Text | Small text values |
| Long Text | Extended text values |
| Integer | Whole numbers |
| Decimal | Decimal numbers |
| Boolean | True or False |
| Date | Calendar date |
| Date Time | Date and time |
| Time | Time only |
| Duration | Time interval |
| Enumeration | Predefined list of values |
| JSON Object | Structured JSON data |
| Binary | Binary content |
| URL | Web address |
| Email | Email address |
| Phone Number | Telephone number |

---

## 5.3 Naming Recommendations

The following logical types should be used consistently.

| Attribute Type | Recommended Data Type |
|---------------|-----------------------|
| Identifier | Identifier |
| Name | Short Text |
| Description | Long Text |
| Status | Enumeration |
| Version | Short Text |
| Created Date | Date Time |
| Updated Date | Date Time |
| Active Flag | Boolean |

---

# 6. Standard Enumerations

## 6.1 Purpose

Enumerations standardize commonly used values across the platform.

This improves consistency, reporting, filtering, and API behavior.

---

## 6.2 Status Enumeration

| Value | Description |
|-------|-------------|
| Draft | Initial state |
| Pending Approval | Awaiting approval |
| Approved | Approved for use |
| Active | Currently in use |
| Deprecated | Scheduled for retirement |
| Archived | No longer active |

---

## 6.3 Information Classification

| Value | Description |
|-------|-------------|
| Public | Publicly available |
| Internal | Internal business use |
| Confidential | Restricted internal access |
| Restricted | Highly sensitive information |

---

## 6.4 Lifecycle Stage

| Value | Description |
|-------|-------------|
| Proposed | Newly created |
| Under Review | Being reviewed |
| Approved | Approved for implementation |
| Implemented | In production |
| Retired | No longer used |

---

## 6.5 Approval Status

| Value | Description |
|-------|-------------|
| Pending | Awaiting approval |
| Approved | Approved |
| Rejected | Rejected |
| Cancelled | Cancelled |

---

## 6.6 Data Quality Severity

| Value | Description |
|-------|-------------|
| Critical | Immediate action required |
| High | Significant issue |
| Medium | Moderate impact |
| Low | Minor issue |
| Informational | No immediate action required |

---

## 6.7 Issue Priority

| Value | Description |
|-------|-------------|
| Critical | Highest priority |
| High | High priority |
| Medium | Medium priority |
| Low | Low priority |

---

## 6.8 Workflow Status

| Value | Description |
|-------|-------------|
| Not Started | Workflow has not begun |
| In Progress | Work is in progress |
| Awaiting Approval | Pending approval |
| Completed | Successfully completed |
| Cancelled | Workflow cancelled |

---

# 7. Standard Audit Attributes

## 7.1 Overview

All platform entities shall maintain a standard set of audit attributes to ensure traceability, accountability, and regulatory compliance.

Audit information enables organizations to identify who created, modified, approved, or deleted metadata throughout its lifecycle.

---

## 7.2 Mandatory Audit Attributes

| Attribute | Description |
|-----------|-------------|
| Created By | User who created the entity |
| Created Date | Date and time the entity was created |
| Modified By | User who last modified the entity |
| Modified Date | Date and time of the last modification |
| Approved By | User who approved the entity |
| Approved Date | Date and time of approval |
| Deleted By | User who deleted the entity (if applicable) |
| Deleted Date | Date and time of deletion |
| Version Number | Current version of the entity |
| Change Reason | Reason for the latest modification |

---

## 7.3 Audit Requirements

The platform shall:

- Record every metadata change.
- Preserve historical versions where applicable.
- Maintain immutable audit records.
- Support audit reporting.
- Support regulatory compliance requirements.

---

# 8. Entity Attribute Standards

## 8.1 Overview

Every logical entity within the Enterprise Data Governance Platform shall conform to a consistent attribute structure.

---

## 8.2 Mandatory Entity Attributes

Every entity shall include the following attributes.

| Attribute | Purpose |
|-----------|---------|
| Identifier | Unique system identifier |
| Name | Business name |
| Display Name | Friendly display name |
| Description | Business description |
| Status | Current lifecycle status |
| Owner | Business owner |
| Steward | Data steward |
| Classification | Information sensitivity |
| Version | Entity version |
| Active Flag | Indicates whether the entity is active |

---

## 8.3 Optional Entity Attributes

Where applicable, entities may include:

- Business Domain
- Business Capability
- Parent Entity
- Tags
- Keywords
- External Reference
- Source System
- Documentation URL
- Notes

---

## 8.4 Entity Lifecycle

Each entity progresses through a controlled lifecycle.

```text
Draft
   │
   ▼
Under Review
   │
   ▼
Approved
   │
   ▼
Active
   │
   ▼
Deprecated
   │
   ▼
Archived
```

---

# 9. Relationship Standards

## 9.1 Overview

Relationships define how entities interact within the Enterprise Data Governance Platform.

Relationships shall be explicitly defined within the Logical Data Model.

---

## 9.2 Supported Relationship Types

| Relationship | Description |
|--------------|-------------|
| One-to-One | One entity relates to one entity |
| One-to-Many | One entity relates to many entities |
| Many-to-One | Many entities relate to one entity |
| Many-to-Many | Many entities relate to many entities |

---

## 9.3 Relationship Principles

Relationships shall:

- Have clearly defined ownership.
- Maintain referential integrity.
- Support traceability.
- Support impact analysis.
- Be documented within the Logical Model.

---

# 10. Validation Standards

## 10.1 Overview

Validation rules ensure metadata consistency, completeness, and quality.

Validation shall be applied during creation and modification of metadata.

---

## 10.2 Mandatory Validations

Every entity shall be validated for:

- Mandatory fields.
- Unique identifiers.
- Valid lifecycle status.
- Valid ownership.
- Valid relationships.
- Valid classifications.
- Duplicate names.
- Invalid references.

---

## 10.3 Business Rule Validation

Business rules shall ensure:

- Metadata complies with enterprise standards.
- Relationships remain valid.
- Lifecycle transitions are permitted.
- Required approvals are completed.

---

# 11. Metadata Quality Standards

## 11.1 Overview

Metadata quality shall be measured using standardized quality dimensions.

---

## 11.2 Quality Dimensions

| Dimension | Description |
|-----------|-------------|
| Completeness | Required metadata is populated |
| Accuracy | Metadata correctly represents the business object |
| Consistency | Metadata follows enterprise standards |
| Validity | Metadata complies with validation rules |
| Timeliness | Metadata is up to date |
| Uniqueness | Duplicate metadata does not exist |

---

## 11.3 Metadata Quality Objectives

The platform shall aim to:

- Improve metadata completeness.
- Reduce duplicate metadata.
- Standardize terminology.
- Improve metadata discoverability.
- Increase governance maturity.
- Support AI-ready metadata.

---

# 12. Naming Standards Reference

This document shall be used together with:

- 10_NamingStandards.md

Naming standards defined within that document apply to:

- Logical Entities
- Physical Tables
- REST APIs
- User Interface Components
- Source Code
- Database Objects
- AI Prompts
- Documentation

The Data Dictionary defines **what metadata exists**, while the Naming Standards define **how that metadata is named**.

---

# 13. Summary

The Enterprise Data Dictionary establishes the metadata standards used throughout the Enterprise Data Governance Platform.

It provides standardized definitions for:

- Common Metadata Attributes
- Standard Logical Data Types
- Standard Enumerations
- Audit Attributes
- Entity Attribute Standards
- Relationship Standards
- Validation Standards
- Metadata Quality Standards

These standards ensure consistency across all platform modules and provide the foundation for the Logical Data Models, Physical Data Models, APIs, User Interfaces, and AI Services.

All future platform modules shall comply with the standards defined in this document unless an approved architectural exception has been granted.