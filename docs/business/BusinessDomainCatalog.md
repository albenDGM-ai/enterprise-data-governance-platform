# Business Domain Catalog

## Enterprise Data Governance Platform

---

# 1. Purpose

## 1.1 Objective

The purpose of this document is to define the Enterprise Business Domains that collectively represent the operating model of a universal banking organization.

Business Domains organize enterprise capabilities, business processes, business entities, and governance responsibilities into logical functional areas.

This catalog serves as the authoritative reference for all Business Domains used throughout the Enterprise Data Governance Platform.

---

# 2. Scope

## 2.1 In Scope

This catalog defines:

- Enterprise Business Domains
- Business Domain Descriptions
- Business Objectives
- Business Responsibilities
- Domain Classification
- Domain Relationships

## 2.2 Out of Scope

This document does not define:

- Business Capabilities
- Business Processes
- Business Entities
- Business Rules
- Information Models
- Technical Systems
- Database Structures
- APIs

These subjects are documented separately.

---

# 3. Business Domain Classification

Enterprise Business Domains are organized into four logical categories.

## 3.1 Core Banking

Business domains responsible for delivering products and services directly to customers.

## 3.2 Financial Operations

Business domains responsible for financial accounting, treasury, and investment operations.

## 3.3 Risk & Compliance

Business domains responsible for governance, regulatory compliance, and enterprise risk management.

## 3.4 Enterprise Support

Business domains responsible for supporting internal business operations.

---

# 4. Business Domain Catalog

| Domain ID | Business Domain | Category |
|------------|----------------|----------------------|
| BD-001 | Customer Management | Core Banking |
| BD-002 | Party Management | Core Banking |
| BD-003 | Product Management | Core Banking |
| BD-004 | Account Management | Core Banking |
| BD-005 | Deposits | Core Banking |
| BD-006 | Lending | Core Banking |
| BD-007 | Cards | Core Banking |
| BD-008 | Payments | Core Banking |
| BD-009 | Treasury | Financial Operations |
| BD-010 | Trade Finance | Financial Operations |
| BD-011 | Finance & General Ledger | Financial Operations |
| BD-012 | Investment Services | Financial Operations |
| BD-013 | Wealth Management | Financial Operations |
| BD-014 | Foreign Exchange | Financial Operations |
| BD-015 | Risk Management | Risk & Compliance |
| BD-016 | Compliance | Risk & Compliance |
| BD-017 | Anti-Money Laundering (AML) | Risk & Compliance |
| BD-018 | Know Your Customer (KYC) | Risk & Compliance |
| BD-019 | Fraud Management | Risk & Compliance |
| BD-020 | Human Resources | Enterprise Support |
| BD-021 | Procurement | Enterprise Support |
| BD-022 | Vendor Management | Enterprise Support |
| BD-023 | Enterprise Asset Management | Enterprise Support |
| BD-024 | Branch Operations | Enterprise Support |
| BD-025 | Digital Channels | Enterprise Support |
| BD-026 | Enterprise Reporting | Enterprise Support |

---

# 5. Business Domain Definitions

## 5.1 BD-001 Customer Management

### Objective

Manage the complete customer lifecycle across the enterprise.

### Responsibilities

- Customer onboarding
- Customer maintenance
- Customer profiling
- Customer segmentation
- Customer relationship management
- Customer lifecycle management

---

## 5.2 BD-002 Party Management

### Objective

Manage all individuals, organizations, legal entities, and their relationships.

### Responsibilities

- Party registration
- Party hierarchy
- Legal entity management
- Relationship management

---

## 5.3 BD-003 Product Management

### Objective

Manage the lifecycle of banking products and services.

### Responsibilities

- Product creation
- Product maintenance
- Pricing
- Product retirement

---

## 5.4 BD-004 Account Management

### Objective

Manage customer accounts throughout their lifecycle.

### Responsibilities

- Account opening
- Account maintenance
- Balance management
- Statement generation
- Account closure

---

## 5.5 BD-005 Deposits

### Objective

Manage all deposit-based products.

### Responsibilities

- Savings accounts
- Current accounts
- Fixed deposits
- Recurring deposits

---

## 5.6 BD-006 Lending

### Objective

Manage lending products throughout their lifecycle.

### Responsibilities

- Loan origination
- Loan approval
- Loan servicing
- Loan closure

---

## 5.7 BD-007 Cards

### Objective

Manage debit, credit, prepaid, and virtual cards.

### Responsibilities

- Card issuance
- Card activation
- Card servicing
- Card replacement
- Card blocking

---

## 5.8 BD-008 Payments

### Objective

Manage domestic and international payment processing.

### Responsibilities

- Payment initiation
- Payment authorization
- Settlement
- Reconciliation

---

## 5.9 BD-009 Treasury

### Objective

Manage enterprise liquidity and treasury operations.

---

## 5.10 BD-010 Trade Finance

### Objective

Manage international trade finance products and services.

---

## 5.11 BD-011 Finance & General Ledger

### Objective

Manage financial accounting and statutory reporting.

---

## 5.12 BD-012 Investment Services

### Objective

Manage investment products and customer portfolios.

---

## 5.13 BD-013 Wealth Management

### Objective

Provide wealth advisory and portfolio management services.

---

## 5.14 BD-014 Foreign Exchange

### Objective

Manage foreign exchange transactions and settlements.

---

## 5.15 BD-015 Risk Management

### Objective

Identify, assess, monitor, and mitigate enterprise risk.

---

## 5.16 BD-016 Compliance

### Objective

Ensure compliance with regulatory and internal policy requirements.

---

## 5.17 BD-017 Anti-Money Laundering (AML)

### Objective

Monitor and investigate suspicious financial activities.

---

## 5.18 BD-018 Know Your Customer (KYC)

### Objective

Manage customer due diligence and identity verification.

---

## 5.19 BD-019 Fraud Management

### Objective

Prevent, detect, investigate, and manage fraud.

---

## 5.20 BD-020 Human Resources

### Objective

Manage the employee lifecycle.

---

## 5.21 BD-021 Procurement

### Objective

Manage procurement of enterprise goods and services.

---

## 5.22 BD-022 Vendor Management

### Objective

Manage third-party vendors and supplier relationships.

---

## 5.23 BD-023 Enterprise Asset Management

### Objective

Manage enterprise physical and digital assets.

---

## 5.24 BD-024 Branch Operations

### Objective

Manage branch network operations and customer servicing.

---

## 5.25 BD-025 Digital Channels

### Objective

Manage customer-facing digital channels.

---

## 5.26 BD-026 Enterprise Reporting

### Objective

Provide enterprise reporting, dashboards, regulatory reporting, and analytics.

---

# 6. Domain Relationships

Enterprise Business Domains collaborate to deliver banking products and services.

Examples include:

- Customer Management supports Account Management.
- Account Management supports Payments.
- Lending collaborates with Risk Management.
- Compliance collaborates with AML and KYC.
- Enterprise Reporting consumes information from all Business Domains.
- Digital Channels interact with nearly every Core Banking domain.

---

# 7. Design Principles

Business Domains shall be:

- Business Driven
- Technology Independent
- Stable
- Enterprise Wide
- Modular
- Scalable
- Extensible
- Governable

---

# 8. Future Scope

Future versions of this catalog may include:

- Domain Owners
- Capability Mapping
- Domain KPIs
- Domain Services
- Domain Events
- Domain APIs
- AI Agents by Domain

---

# 9. Summary

The Business Domain Catalog establishes the highest level of Business Architecture within the Enterprise Data Governance Platform.

Every Business Capability, Business Process, Business Entity, Business Rule, and Governance Artifact shall belong to one or more Business Domains.

This document serves as the authoritative reference for organizing the Enterprise Business Architecture.