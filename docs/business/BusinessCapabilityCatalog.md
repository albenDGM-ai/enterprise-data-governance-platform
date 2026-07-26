# Business Capability Catalog

## Enterprise Data Governance Platform

---

# 1. Purpose

## 1.1 Objective

The purpose of this document is to define the Enterprise Business Capabilities of a universal banking organization.

Business Capabilities describe what the business is able to perform, independent of organizational structure, technology platforms, or implementation approaches.

This catalog serves as the authoritative inventory of business capabilities and forms the bridge between Business Domains and Business Entities.

---

# 2. Scope

## 2.1 In Scope

This catalog defines:

- Enterprise Business Capabilities
- Capability Objectives
- Parent Business Domains
- Capability Classification
- Capability Relationships

## 2.2 Out of Scope

This document does not define:

- Business Processes
- Business Entities
- Business Rules
- Information Models
- Technical Systems
- Database Structures
- APIs

These subjects are documented separately.

---

# 3. Capability Classification

Enterprise Business Capabilities are organized according to their parent Business Domain.

Each capability belongs to one primary Business Domain.

---

# 4. Business Capability Catalog

| Capability ID | Business Capability | Parent Domain | Priority |
|---------------|---------------------|---------------|----------|
| BC-001 | Customer Onboarding | BD-001 | Core |
| BC-002 | Customer Maintenance | BD-001 | Core |
| BC-003 | Customer Search | BD-001 | Core |
| BC-004 | Customer Segmentation | BD-001 | Core |
| BC-005 | Customer Relationship Management | BD-001 | Core |
| BC-006 | Customer Consent Management | BD-001 | Core |
| BC-007 | Customer Risk Profiling | BD-001 | Core |
| BC-008 | Customer Offboarding | BD-001 | Supporting |
| BC-009 | Party Management | BD-002 | Core |
| BC-010 | Legal Entity Management | BD-002 | Core |
| BC-011 | Product Lifecycle Management | BD-003 | Core |
| BC-012 | Product Pricing | BD-003 | Core |
| BC-013 | Product Configuration | BD-003 | Core |
| BC-014 | Product Retirement | BD-003 | Supporting |
| BC-015 | Account Opening | BD-004 | Core |
| BC-016 | Account Maintenance | BD-004 | Core |
| BC-017 | Balance Management | BD-004 | Core |
| BC-018 | Statement Generation | BD-004 | Core |
| BC-019 | Account Closure | BD-004 | Supporting |
| BC-020 | Deposit Management | BD-005 | Core |
| BC-021 | Interest Calculation | BD-005 | Core |
| BC-022 | Loan Origination | BD-006 | Core |
| BC-023 | Credit Assessment | BD-006 | Core |
| BC-024 | Loan Approval | BD-006 | Core |
| BC-025 | Loan Disbursement | BD-006 | Core |
| BC-026 | Loan Servicing | BD-006 | Core |
| BC-027 | Loan Closure | BD-006 | Supporting |
| BC-028 | Card Issuance | BD-007 | Core |
| BC-029 | Card Activation | BD-007 | Core |
| BC-030 | Card Replacement | BD-007 | Supporting |
| BC-031 | Card Blocking | BD-007 | Core |
| BC-032 | Payment Initiation | BD-008 | Core |
| BC-033 | Payment Validation | BD-008 | Core |
| BC-034 | Payment Authorization | BD-008 | Core |
| BC-035 | Payment Processing | BD-008 | Core |
| BC-036 | Payment Settlement | BD-008 | Core |
| BC-037 | Payment Reconciliation | BD-008 | Supporting |
| BC-038 | Treasury Position Management | BD-009 | Core |
| BC-039 | Liquidity Management | BD-009 | Core |
| BC-040 | Trade Finance Processing | BD-010 | Core |
| BC-041 | General Ledger Management | BD-011 | Core |
| BC-042 | Financial Reporting | BD-011 | Core |
| BC-043 | Investment Portfolio Management | BD-012 | Core |
| BC-044 | Wealth Advisory | BD-013 | Supporting |
| BC-045 | Foreign Exchange Trading | BD-014 | Core |
| BC-046 | Credit Risk Management | BD-015 | Core |
| BC-047 | Market Risk Management | BD-015 | Core |
| BC-048 | Operational Risk Management | BD-015 | Core |
| BC-049 | Regulatory Compliance | BD-016 | Core |
| BC-050 | Policy Management | BD-016 | Core |
| BC-051 | AML Monitoring | BD-017 | Core |
| BC-052 | Sanctions Screening | BD-017 | Core |
| BC-053 | Customer Due Diligence | BD-018 | Core |
| BC-054 | Periodic KYC Review | BD-018 | Core |
| BC-055 | Fraud Detection | BD-019 | Core |
| BC-056 | Fraud Investigation | BD-019 | Supporting |
| BC-057 | Employee Management | BD-020 | Supporting |
| BC-058 | Recruitment Management | BD-020 | Supporting |
| BC-059 | Procurement Management | BD-021 | Supporting |
| BC-060 | Vendor Lifecycle Management | BD-022 | Supporting |
| BC-061 | Asset Lifecycle Management | BD-023 | Supporting |
| BC-062 | Branch Operations | BD-024 | Core |
| BC-063 | Mobile Banking | BD-025 | Core |
| BC-064 | Internet Banking | BD-025 | Core |
| BC-065 | ATM Services | BD-025 | Core |
| BC-066 | Enterprise Reporting | BD-026 | Core |
| BC-067 | Regulatory Reporting | BD-026 | Core |

---

# 5. Capability Definitions

## 5.1 Capability Identifier

Each Business Capability shall have a unique identifier.

Example:

BC-001

---

## 5.2 Capability Name

Each capability shall have a descriptive business-friendly name.

Example:

Customer Onboarding

---

## 5.3 Parent Business Domain

Every capability shall belong to one Business Domain.

Example:

BD-001 Customer Management

---

## 5.4 Business Objective

Each capability shall define its primary business objective.

---

## 5.5 Business Description

Each capability shall include a description of the business function it performs.

---

## 5.6 Future Business Entities

Business Entities managed by the capability will be documented within the Business Entity Catalog.

Example:

Customer Onboarding

↓

Customer

↓

Customer Address

↓

Customer Contact

↓

Customer Identification

---

## 5.7 Priority

Business Capabilities shall be classified as:

- Core
- Supporting
- Future

---

## 5.8 Status

Business Capabilities may be classified as:

- Planned
- Active
- Deprecated

---

# 6. Capability Relationships

Business Capabilities collaborate to deliver enterprise business services.

Examples include:

Customer Onboarding

↓

Account Opening

↓

Payment Initiation

↓

Payment Settlement

Another example:

Loan Origination

↓

Credit Assessment

↓

Loan Approval

↓

Loan Disbursement

↓

Loan Servicing

---

# 7. Design Principles

Business Capabilities shall be:

- Business Driven
- Technology Independent
- Stable
- Reusable
- Modular
- Governable
- Traceable
- Extensible

---

# 8. Future Scope

Future versions of this catalog may include:

- Capability Owners
- Capability KPIs
- Capability Heat Maps
- Capability Maturity Assessment
- Business Services
- Process Mapping
- AI Agents by Capability

---

# 9. Summary

The Business Capability Catalog defines the complete inventory of enterprise business capabilities.

Business Capabilities bridge Business Domains and Business Entities and provide the foundation for Business Processes, Information Models, Governance Models, APIs, and AI-assisted automation.

Every Business Entity shall be managed by one or more Business Capabilities.