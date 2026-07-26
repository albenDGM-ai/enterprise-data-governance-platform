# Enterprise Identifier Standards

## Enterprise Data Governance Platform

**Version:** 1.0

**Status:** Approved

---

# 1. Purpose

## 1.1 Objective

The purpose of this document is to define the enterprise-wide identifier standards used throughout the Enterprise Data Governance Platform.

Every business, governance, technical, and architectural artifact shall have a unique identifier following the standards defined in this document.

These identifiers provide:

- Enterprise-wide uniqueness
- End-to-end traceability
- Consistent documentation
- Improved navigation
- AI-friendly referencing
- Simplified governance

This document is the authoritative standard for all identifiers used across the project.

---

# 2. Scope

These standards apply to:

- Business Architecture
- Information Architecture
- Governance Architecture
- Technical Architecture
- Source Code
- APIs
- User Interfaces
- Database Design
- Documentation
- Test Cases

---

# 3. Identifier Design Principles

Enterprise identifiers shall comply with the following principles.

## 3.1 Uniqueness

Every identifier shall be globally unique within its artifact type.

---

## 3.2 Stability

Identifiers shall never change after assignment.

Business names may evolve.

Identifiers shall remain constant.

---

## 3.3 Readability

Identifiers shall use meaningful prefixes that immediately identify the artifact type.

Example:

```
BE-001
```

immediately identifies a Business Entity.

---

## 3.4 Traceability

Identifiers shall support complete traceability across all architectural layers.

Example

```
Business Domain

↓

Business Capability

↓

Business Entity

↓

Business Rule

↓

Business Term

↓

Logical Model

↓

Physical Model

↓

Database

↓

API

↓

UI
```

---

## 3.5 Scalability

All identifiers shall use a minimum three-digit numeric sequence.

Examples

```
BD-001

BD-145

BD-982
```

This allows future expansion without renumbering.

---

# 4. Identifier Standards

## 4.1 Business Architecture

| Artifact | Prefix | Example |
|----------|---------|----------|
| Business Domain | BD | BD-001 |
| Business Capability | BC | BC-001 |
| Business Process | BP | BP-001 |
| Business Entity | BE | BE-001 |
| Business Rule | BR | BR-001 |
| Business Event | EVT | EVT-001 |
| Business Service | BS | BS-001 |

---

## 4.2 Information Architecture

| Artifact | Prefix | Example |
|----------|---------|----------|
| Business Glossary | BG | BG-001 |
| Business Term | BT | BT-001 |
| Reference Data | RD | RD-001 |
| Reference Data Set | RDS | RDS-001 |
| Critical Data Element | CDE | CDE-001 |
| Data Standard | DS | DS-001 |
| Data Policy | DP | DP-001 |

---

## 4.3 Governance Architecture

| Artifact | Prefix | Example |
|----------|---------|----------|
| Data Quality Rule | DQR | DQR-001 |
| Data Quality Result | DQRES | DQRES-001 |
| Data Quality Scorecard | DQS | DQS-001 |
| Classification | CLS | CLS-001 |
| Tag | TAG | TAG-001 |
| Lineage | LIN | LIN-001 |
| Data Owner | DO | DO-001 |
| Data Steward | DST | DST-001 |
| Workflow | WF | WF-001 |
| Workflow Task | WT | WT-001 |
| Approval | APR | APR-001 |
| Issue | ISS | ISS-001 |
| Audit Log | AUD | AUD-001 |

---

## 4.4 Technical Architecture

| Artifact | Prefix | Example |
|----------|---------|----------|
| Source System | SS | SS-001 |
| Database | DB | DB-001 |
| Schema | SCH | SCH-001 |
| Table | TBL | TBL-001 |
| Column | COL | COL-001 |
| Data Asset | DA | DA-001 |
| API | API | API-001 |
| UI Screen | UI | UI-001 |
| Integration | INT | INT-001 |
| Batch Job | JOB | JOB-001 |

---

## 4.5 Security

| Artifact | Prefix | Example |
|----------|---------|----------|
| User | USR | USR-001 |
| Role | ROL | ROL-001 |
| Permission | PER | PER-001 |
| Security Policy | SEC | SEC-001 |

---

# 5. Naming Convention

Identifiers shall follow the format below.

```
<PREFIX>-<NUMBER>
```

Examples

```
BD-001

BC-015

BE-127

API-023

TBL-084
```

---

# 6. Cross-Reference Standards

Every architectural artifact should reference related identifiers wherever applicable.

Example

```
Business Domain

BD-001

Customer Management

↓

Business Capability

BC-001

Customer Onboarding

↓

Business Entity

BE-001

Customer

↓

Business Rule

BR-001

Customer must have one primary identifier.

↓

Business Term

BT-001

Customer Identifier

↓

Table

TBL-001

CUSTOMER_MASTER

↓

Column

COL-001

customer_id

↓

API

API-001

Create Customer

↓

UI

UI-001

Customer Dashboard
```

---

# 7. Reserved Prefixes

The following prefixes are reserved for future use.

| Prefix | Reserved For |
|---------|--------------|
| AI | Artificial Intelligence |
| ML | Machine Learning |
| KG | Knowledge Graph |
| DPD | Data Product |
| DC | Data Contract |
| SEM | Semantic Layer |
| EVT | Event Catalog |
| MSG | Messaging |

---

# 8. Future Scope

Future versions of this standard may include:

- UUID Standards
- Versioning Standards
- Multi-tenant Identifier Standards
- Event Identifiers
- Knowledge Graph Node Identifiers
- AI Prompt Identifiers

---

# 9. Summary

This document establishes the enterprise identifier standard for the Enterprise Data Governance Platform.

All business, governance, information, technical, and application artifacts shall follow these conventions.

Adoption of these standards ensures consistency, traceability, maintainability, and interoperability across the entire architecture and implementation lifecycle.