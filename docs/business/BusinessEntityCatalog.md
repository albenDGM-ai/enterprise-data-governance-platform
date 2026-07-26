# Business Entity Catalog

## Enterprise Data Governance Platform

---

# 1. Purpose

## 1.1 Objective

The purpose of this document is to define the canonical Business Entities used within the Enterprise Business Model.

Business Entities represent the core business objects managed by a universal banking organization.

These entities provide the foundation for:

- Business Glossary
- Metadata Repository
- Data Dictionary
- Logical Data Model
- Physical Data Model
- REST APIs
- User Interface
- AI Knowledge Base

This catalog serves as the authoritative source for all enterprise business entities.

---

# 2. Scope

## 2.1 In Scope

This document defines:

- Business Entities
- Entity Descriptions
- Parent Business Domain
- Parent Business Capability
- Entity Purpose
- Business Relationships

## 2.2 Out of Scope

This document does not define:

- Business Attributes
- Database Tables
- APIs
- UI Screens
- Data Quality Rules

These will be documented separately.

---

# 3. Business Entity Classification

Business Entities are organized according to their parent Business Domain.

Each Business Entity belongs to one primary Business Domain.

---

# 4. Customer Management Entities

---

## 4.1 BE-001 Customer

### Description

Represents an individual or organization that maintains a business relationship with the bank.

### Parent Business Domain

BD-001 Customer Management

### Parent Business Capability

BC-001 Customer Onboarding

### Business Purpose

Maintain the master customer record used throughout the enterprise.

---

## 4.2 BE-002 Customer Address

### Description

Represents one or more physical or mailing addresses associated with a Customer.

### Parent Business Domain

BD-001 Customer Management

### Parent Business Capability

BC-002 Customer Maintenance

---

## 4.3 BE-003 Customer Contact

### Description

Represents customer communication information including phone numbers, email addresses and preferred communication channels.

### Parent Business Domain

BD-001 Customer Management

### Parent Business Capability

BC-002 Customer Maintenance

---

## 4.4 BE-004 Customer Identification

### Description

Represents official identification documents used to uniquely identify a customer.

Examples include:

- Passport
- National ID
- Driver License
- Tax Identification Number

---

## 4.5 BE-005 Customer Consent

### Description

Represents customer consent for data processing, marketing preferences and regulatory permissions.

---

## 4.6 BE-006 Customer Relationship

### Description

Represents relationships between customers including family, business, legal and financial relationships.

---

## 4.7 BE-007 Customer Segment

### Description

Represents business segmentation of customers.

Examples include:

- Retail
- SME
- Corporate
- Private Banking
- High Net Worth

---

## 4.8 BE-008 Customer Risk Profile

### Description

Represents customer risk assessment used for compliance and risk management.

---

## 4.9 BE-009 Customer Employment

### Description

Represents employment information associated with individual customers.

---

## 4.10 BE-010 Customer Tax Profile

### Description

Represents taxation information required for regulatory reporting.

---

# 5. Product Management Entities

---

## 5.1 BE-011 Product

Represents a banking product offered by the organization.

---

## 5.2 BE-012 Product Category

Represents logical grouping of banking products.

---

## 5.3 BE-013 Product Offering

Represents a marketable product configuration.

---

## 5.4 BE-014 Product Feature

Represents individual product functionality.

---

## 5.5 BE-015 Pricing Plan

Represents pricing associated with a banking product.

---

## 5.6 BE-016 Interest Rate

Represents interest rates applicable to financial products.

---

## 5.7 BE-017 Fee

Represents fees charged for banking services.

---

## 5.8 BE-018 Product Bundle

Represents grouped banking products sold together.

---

# 6. Account Management Entities

---

## 6.1 BE-019 Account

Represents a financial account maintained by the bank.

---

## 6.2 BE-020 Account Holder

Represents ownership of an account.

---

## 6.3 BE-021 Account Balance

Represents the financial balance associated with an account.

---

## 6.4 BE-022 Account Statement

Represents periodic financial statements.

---

## 6.5 BE-023 Account Limit

Represents account transaction limits.

---

## 6.6 BE-024 Account Status

Represents lifecycle status of an account.

---

## 6.7 BE-025 Account Relationship

Represents relationships between multiple accounts.

---

# 7. Summary

This section establishes the first twenty-five canonical Business Entities used throughout the Enterprise Data Governance Platform.

Subsequent sections of this catalog will define entities for:

- Deposits
- Lending
- Cards
- Payments
- Treasury
- Finance
- Risk
- Compliance
- AML
- KYC
- Fraud
- Human Resources
- Vendor Management
- Enterprise Reporting

# 8. Deposit Business Entities

Deposit Management governs all customer deposit products and their lifecycle.

**Parent Business Domain:**

BD-005 Deposits

---

## 8.1 BE-026 Deposit

### Description

Represents a deposit relationship established between a customer and the bank.

### Business Purpose

Acts as the primary business object for deposit products.

### Parent Business Capability

BC-020 Deposit Management

---

## 8.2 BE-027 Deposit Account

### Description

Represents the account in which deposits are maintained.

---

## 8.3 BE-028 Deposit Product

### Description

Represents the type of deposit product.

### Examples

- Savings Deposit
- Current Deposit
- Fixed Deposit
- Recurring Deposit

---

## 8.4 BE-029 Deposit Interest

### Description

Represents interest earned on customer deposits.

---

## 8.5 BE-030 Deposit Maturity

### Description

Represents maturity information for term deposits.

---

## 8.6 BE-031 Deposit Renewal

### Description

Represents renewal instructions for maturing deposits.

---

## 8.7 BE-032 Deposit Nominee

### Description

Represents nominee information associated with a deposit.

---

## 8.8 BE-033 Deposit Beneficiary

### Description

Represents beneficiary information associated with deposits.

---

# 9. Lending Business Entities

Lending governs all credit facilities provided by the bank.

**Parent Business Domain:**

BD-006 Lending

---

## 9.1 BE-034 Loan

### Description

Represents a financial loan provided to a customer.

### Parent Business Capability

BC-022 Loan Origination

---

## 9.2 BE-035 Loan Application

### Description

Represents an application submitted for a loan.

---

## 9.3 BE-036 Loan Applicant

### Description

Represents an applicant requesting a loan.

---

## 9.4 BE-037 Loan Product

### Description

Represents the lending product selected by the applicant.

---

## 9.5 BE-038 Loan Agreement

### Description

Represents the contractual agreement governing a loan.

---

## 9.6 BE-039 Loan Repayment

### Description

Represents scheduled and completed loan repayments.

---

## 9.7 BE-040 Loan Installment

### Description

Represents an individual repayment installment.

---

## 9.8 BE-041 Loan Interest

### Description

Represents interest charged on a loan.

---

## 9.9 BE-042 Loan Collateral

### Description

Represents assets pledged as loan security.

### Examples

- Property
- Vehicle
- Fixed Deposit
- Securities

---

## 9.10 BE-043 Loan Guarantor

### Description

Represents an individual or organization guaranteeing loan repayment.

---

## 9.11 BE-044 Credit Assessment

### Description

Represents credit evaluation performed before loan approval.

---

## 9.12 BE-045 Credit Score

### Description

Represents a numerical creditworthiness assessment.

---

## 9.13 BE-046 Loan Disbursement

### Description

Represents release of approved loan funds.

---

## 9.14 BE-047 Loan Closure

### Description

Represents successful completion or settlement of a loan.

---

# 10. Card Management Business Entities

Card Management governs debit, credit and prepaid card services.

**Parent Business Domain:**

BD-007 Cards

---

## 10.1 BE-048 Card

### Description

Represents a payment card issued by the bank.

### Examples

- Debit Card
- Credit Card
- Prepaid Card
- Virtual Card

---

## 10.2 BE-049 Card Holder

### Description

Represents the customer authorized to use a card.

---

## 10.3 BE-050 Card Account

### Description

Represents the account linked to a payment card.

---

## 10.4 BE-051 Card Transaction

### Description

Represents financial transactions performed using a card.

---

## 10.5 BE-052 Card Limit

### Description

Represents spending and withdrawal limits assigned to a card.

---

## 10.6 BE-053 Card Reward

### Description

Represents loyalty rewards associated with card usage.

---

## 10.7 BE-054 Card Statement

### Description

Represents periodic statements generated for card accounts.

---

## 10.8 BE-055 Card Dispute

### Description

Represents disputes raised against card transactions.

---

## 10.9 BE-056 Card Fraud Case

### Description

Represents fraud investigations associated with cards.

---

# 11. Payment Business Entities

Payment Management governs movement of funds between parties.

**Parent Business Domain:**

BD-008 Payments

---

## 11.1 BE-057 Payment

### Description

Represents a financial payment transaction.

### Parent Business Capability

BC-032 Payment Initiation

---

## 11.2 BE-058 Payment Instruction

### Description

Represents instructions used to execute a payment.

---

## 11.3 BE-059 Payment Channel

### Description

Represents the channel through which a payment is initiated.

### Examples

- Branch
- ATM
- Mobile Banking
- Internet Banking
- API

---

## 11.4 BE-060 Payment Method

### Description

Represents the payment mechanism selected by a customer.

### Examples

- NEFT
- RTGS
- IMPS
- UPI
- SWIFT
- Card Payment

---

## 11.5 BE-061 Payment Beneficiary

### Description

Represents the receiving party of a payment.

---

## 11.6 BE-062 Payment Settlement

### Description

Represents settlement of payment obligations.

---

## 11.7 BE-063 Payment Batch

### Description

Represents a logical group of payments processed together.

---

## 11.8 BE-064 Payment Schedule

### Description

Represents recurring or scheduled payments.

---

## 11.9 BE-065 Payment Status

### Description

Represents the lifecycle state of a payment.

### Examples

- Pending
- Authorized
- Processing
- Settled
- Failed
- Reversed

---

## 11.10 BE-066 Payment Exception

### Description

Represents exceptions encountered during payment processing.

---

## 11.11 BE-067 Payment Reconciliation

### Description

Represents reconciliation of processed payments.

---

## 11.12 BE-068 Payment Charge

### Description

Represents charges applied to payment transactions.

---

# 12. Summary

This section expands the Canonical Banking Information Model to include Deposit, Lending, Card, and Payment business entities.

The Enterprise Business Model now contains sixty-eight canonical business entities across the following domains:

- Customer Management
- Product Management
- Account Management
- Deposits
- Lending
- Cards
- Payments

The next section of this catalog will introduce business entities for:

- Treasury
- Finance & General Ledger
- Investment Services
- Wealth Management
- Foreign Exchange

# 13. Treasury Business Entities

Treasury Management governs enterprise liquidity, funding, investments, and treasury operations.

**Parent Business Domain:**

BD-009 Treasury

---

## 13.1 BE-069 Treasury Position

### Description

Represents the financial position of the bank across various treasury portfolios.

### Parent Business Capability

BC-038 Treasury Position Management

---

## 13.2 BE-070 Liquidity Position

### Description

Represents available liquidity used to support business operations and regulatory requirements.

---

## 13.3 BE-071 Cash Position

### Description

Represents cash available across currencies and banking locations.

---

## 13.4 BE-072 Funding Source

### Description

Represents sources of funding available to the bank.

### Examples

- Customer Deposits
- Interbank Borrowing
- Bond Issuance
- Capital

---

## 13.5 BE-073 Investment Portfolio

### Description

Represents treasury investment portfolios managed by the bank.

---

## 13.6 BE-074 Financial Instrument

### Description

Represents financial instruments held or traded by the bank.

### Examples

- Bonds
- Government Securities
- Treasury Bills
- Commercial Paper

---

## 13.7 BE-075 Treasury Transaction

### Description

Represents treasury-related financial transactions.

---

## 13.8 BE-076 Treasury Limit

### Description

Represents operational and regulatory limits applied to treasury activities.

---

# 14. Finance & General Ledger Business Entities

Finance manages accounting and statutory reporting.

**Parent Business Domain:**

BD-011 Finance & General Ledger

---

## 14.1 BE-077 General Ledger

### Description

Represents the enterprise chart of accounts.

### Parent Business Capability

BC-041 General Ledger Management

---

## 14.2 BE-078 Ledger Account

### Description

Represents an individual accounting account.

---

## 14.3 BE-079 Journal Entry

### Description

Represents accounting journal entries posted to the General Ledger.

---

## 14.4 BE-080 Accounting Period

### Description

Represents accounting periods used for financial reporting.

---

## 14.5 BE-081 Financial Statement

### Description

Represents statutory financial statements.

### Examples

- Balance Sheet
- Income Statement
- Cash Flow Statement

---

## 14.6 BE-082 Cost Centre

### Description

Represents organizational units used for financial allocation.

---

## 14.7 BE-083 Profit Centre

### Description

Represents business units responsible for revenue generation.

---

## 14.8 BE-084 Accounting Transaction

### Description

Represents financial transactions posted to accounting records.

---

## 14.9 BE-085 Tax Record

### Description

Represents taxation records maintained by the finance function.

---

# 15. Investment Services Business Entities

Investment Services manages customer investment products.

**Parent Business Domain:**

BD-012 Investment Services

---

## 15.1 BE-086 Investment Account

### Description

Represents investment accounts maintained by customers.

---

## 15.2 BE-087 Investment Portfolio

### Description

Represents collections of investment assets.

---

## 15.3 BE-088 Security

### Description

Represents financial securities available for investment.

### Examples

- Equity
- Bond
- Mutual Fund
- ETF

---

## 15.4 BE-089 Investment Transaction

### Description

Represents purchase, sale, or transfer of investments.

---

## 15.5 BE-090 Dividend

### Description

Represents dividend payments received from investments.

---

## 15.6 BE-091 Corporate Action

### Description

Represents events initiated by security issuers.

### Examples

- Stock Split
- Bonus Issue
- Rights Issue
- Merger

---

# 16. Wealth Management Business Entities

Wealth Management provides advisory and portfolio management services.

**Parent Business Domain:**

BD-013 Wealth Management

---

## 16.1 BE-092 Wealth Portfolio

### Description

Represents customer wealth portfolios managed by advisors.

---

## 16.2 BE-093 Wealth Plan

### Description

Represents long-term financial planning strategies.

---

## 16.3 BE-094 Investment Goal

### Description

Represents customer investment objectives.

### Examples

- Retirement
- Education
- Wealth Growth
- Income Generation

---

## 16.4 BE-095 Advisor

### Description

Represents financial advisors managing customer portfolios.

---

## 16.5 BE-096 Advisory Recommendation

### Description

Represents investment recommendations made by advisors.

---

# 17. Foreign Exchange Business Entities

Foreign Exchange manages currency trading and settlement.

**Parent Business Domain:**

BD-014 Foreign Exchange

---

## 17.1 BE-097 Currency

### Description

Represents currencies supported by the bank.

---

## 17.2 BE-098 Exchange Rate

### Description

Represents currency conversion rates.

---

## 17.3 BE-099 FX Transaction

### Description

Represents foreign exchange transactions.

---

## 17.4 BE-100 FX Contract

### Description

Represents contractual foreign exchange agreements.

---

## 17.5 BE-101 FX Settlement

### Description

Represents settlement of foreign exchange transactions.

---

## 17.6 BE-102 FX Position

### Description

Represents the bank's exposure to foreign currencies.

---

# 18. Summary

The Canonical Banking Information Model now includes business entities covering:

- Treasury
- Finance & General Ledger
- Investment Services
- Wealth Management
- Foreign Exchange

The Enterprise Business Model currently contains **102 canonical business entities**.

The next section of this catalog introduces entities for:

- Risk Management
- Compliance
- Anti-Money Laundering (AML)
- Know Your Customer (KYC)
- Fraud Management

# 19. Risk Management Business Entities

Risk Management governs the identification, assessment, monitoring, reporting, and mitigation of enterprise risks.

**Parent Business Domain:**

BD-015 Risk Management

---

## 19.1 BE-103 Risk

### Description

Represents a potential event that may impact the achievement of business objectives.

### Parent Business Capability

BC-046 Credit Risk Management

---

## 19.2 BE-104 Risk Category

### Description

Represents the classification of enterprise risks.

### Examples

- Credit Risk
- Market Risk
- Operational Risk
- Liquidity Risk
- Strategic Risk

---

## 19.3 BE-105 Risk Assessment

### Description

Represents an evaluation performed to determine the likelihood and impact of a risk.

---

## 19.4 BE-106 Risk Rating

### Description

Represents the overall rating assigned to a risk.

### Examples

- Low
- Medium
- High
- Critical

---

## 19.5 BE-107 Risk Exposure

### Description

Represents the financial or operational exposure associated with a risk.

---

## 19.6 BE-108 Risk Control

### Description

Represents controls implemented to mitigate enterprise risks.

---

## 19.7 BE-109 Risk Event

### Description

Represents an event that has resulted in or may result in a loss.

---

## 19.8 BE-110 Risk Appetite

### Description

Represents the level of risk the organization is willing to accept.

---

# 20. Compliance Business Entities

Compliance Management governs adherence to regulatory requirements and internal policies.

**Parent Business Domain:**

BD-016 Compliance

---

## 20.1 BE-111 Regulation

### Description

Represents an external regulatory requirement.

### Examples

- BCBS 239
- GDPR
- UAE PDPL
- RBI Guidelines
- FATCA

---

## 20.2 BE-112 Compliance Policy

### Description

Represents an internal policy established to comply with regulations.

---

## 20.3 BE-113 Compliance Control

### Description

Represents a control implemented to satisfy compliance requirements.

---

## 20.4 BE-114 Compliance Assessment

### Description

Represents an evaluation of compliance against regulatory requirements.

---

## 20.5 BE-115 Compliance Finding

### Description

Represents observations identified during compliance reviews.

---

## 20.6 BE-116 Compliance Exception

### Description

Represents deviations from approved compliance standards.

---

## 20.7 BE-117 Regulatory Report

### Description

Represents reports submitted to regulatory authorities.

---

# 21. Anti-Money Laundering (AML) Business Entities

AML governs the detection and investigation of suspicious financial activities.

**Parent Business Domain:**

BD-017 Anti-Money Laundering (AML)

---

## 21.1 BE-118 AML Alert

### Description

Represents a suspicious activity alert generated by monitoring systems.

---

## 21.2 BE-119 AML Case

### Description

Represents an investigation initiated from an AML alert.

---

## 21.3 BE-120 Sanction List

### Description

Represents external sanction lists used for customer screening.

### Examples

- OFAC
- UN
- EU
- UK HMT

---

## 21.4 BE-121 Sanction Match

### Description

Represents a potential match identified during sanctions screening.

---

## 21.5 BE-122 Suspicious Transaction

### Description

Represents a transaction identified as potentially suspicious.

---

## 21.6 BE-123 Suspicious Activity Report (SAR)

### Description

Represents a formal report submitted to regulators regarding suspicious activity.

---

# 22. Know Your Customer (KYC) Business Entities

KYC governs customer due diligence and identity verification.

**Parent Business Domain:**

BD-018 Know Your Customer (KYC)

---

## 22.1 BE-124 KYC Profile

### Description

Represents the complete KYC profile maintained for a customer.

---

## 22.2 BE-125 KYC Document

### Description

Represents documents collected during customer onboarding.

### Examples

- Passport
- Driver License
- Utility Bill
- Tax Certificate

---

## 22.3 BE-126 KYC Verification

### Description

Represents verification activities performed on customer documents.

---

## 22.4 BE-127 KYC Review

### Description

Represents periodic customer due diligence reviews.

---

## 22.5 BE-128 Enhanced Due Diligence (EDD)

### Description

Represents additional due diligence performed for high-risk customers.

---

## 22.6 BE-129 Beneficial Owner

### Description

Represents the ultimate beneficial owner of a legal entity.

---

# 23. Fraud Management Business Entities

Fraud Management governs prevention, detection, investigation, and resolution of fraud.

**Parent Business Domain:**

BD-019 Fraud Management

---

## 23.1 BE-130 Fraud Alert

### Description

Represents an alert generated when fraudulent activity is suspected.

---

## 23.2 BE-131 Fraud Case

### Description

Represents an investigation into suspected fraud.

---

## 23.3 BE-132 Fraud Pattern

### Description

Represents known patterns of fraudulent activity.

---

## 23.4 BE-133 Fraud Investigation

### Description

Represents activities performed to investigate fraud.

---

## 23.5 BE-134 Fraud Loss

### Description

Represents financial losses resulting from fraud.

---

## 23.6 BE-135 Fraud Recovery

### Description

Represents recovery of funds lost through fraudulent activity.

---

## 23.7 BE-136 Fraud Rule

### Description

Represents business rules used to detect fraud.

---

# 24. Summary

The Enterprise Business Model now includes canonical entities covering:

- Risk Management
- Compliance
- Anti-Money Laundering (AML)
- Know Your Customer (KYC)
- Fraud Management

The Canonical Banking Information Model currently contains **136 Business Entities**.

The final section of this catalog introduces enterprise support entities for:

- Human Resources
- Procurement
- Vendor Management
- Enterprise Asset Management
- Branch Operations
- Digital Channels
- Enterprise Reporting

It also concludes the Business Entity Catalog with governance principles and implementation guidance.

# 25. Human Resources Business Entities

Human Resources manages the employee lifecycle and organizational structure.

**Parent Business Domain:**

BD-020 Human Resources

---

## 25.1 BE-137 Employee

### Description

Represents an individual employed by the organization.

### Parent Business Capability

BC-057 Employee Management

---

## 25.2 BE-138 Department

### Description

Represents an organizational department within the enterprise.

---

## 25.3 BE-139 Position

### Description

Represents a job position within the organization.

---

## 25.4 BE-140 Organization Unit

### Description

Represents the organizational hierarchy of the enterprise.

---

## 25.5 BE-141 Employment Contract

### Description

Represents contractual agreements between employees and the organization.

---

# 26. Procurement Business Entities

Procurement manages sourcing and purchasing of goods and services.

**Parent Business Domain:**

BD-021 Procurement

---

## 26.1 BE-142 Purchase Request

### Description

Represents a request for procurement.

---

## 26.2 BE-143 Purchase Order

### Description

Represents an approved order issued to a supplier.

---

## 26.3 BE-144 Invoice

### Description

Represents supplier invoices received by the organization.

---

## 26.4 BE-145 Payment Voucher

### Description

Represents authorization for supplier payments.

---

# 27. Vendor Management Business Entities

Vendor Management governs relationships with third-party suppliers.

**Parent Business Domain:**

BD-022 Vendor Management

---

## 27.1 BE-146 Vendor

### Description

Represents a third-party supplier providing products or services.

---

## 27.2 BE-147 Vendor Contract

### Description

Represents contractual agreements between the bank and vendors.

---

## 27.3 BE-148 Vendor Assessment

### Description

Represents performance and risk evaluations of vendors.

---

## 27.4 BE-149 Service Level Agreement (SLA)

### Description

Represents agreed service levels between the organization and vendors.

---

# 28. Enterprise Asset Management Business Entities

Enterprise Asset Management governs physical and digital assets owned by the organization.

**Parent Business Domain:**

BD-023 Enterprise Asset Management

---

## 28.1 BE-150 Asset

### Description

Represents an enterprise asset.

### Examples

- Laptop
- Server
- Software License
- Office Equipment

---

## 28.2 BE-151 Asset Category

### Description

Represents logical classifications of enterprise assets.

---

## 28.3 BE-152 Asset Assignment

### Description

Represents assignment of assets to employees or departments.

---

## 28.4 BE-153 Asset Maintenance

### Description

Represents maintenance history associated with enterprise assets.

---

# 29. Branch Operations Business Entities

Branch Operations governs physical branch locations and branch services.

**Parent Business Domain:**

BD-024 Branch Operations

---

## 29.1 BE-154 Branch

### Description

Represents a physical banking branch.

---

## 29.2 BE-155 Branch Employee

### Description

Represents employees assigned to a branch.

---

## 29.3 BE-156 Branch Service

### Description

Represents services provided at a branch.

---

## 29.4 BE-157 Cash Vault

### Description

Represents secure storage of physical cash within a branch.

---

# 30. Digital Channels Business Entities

Digital Channels governs customer-facing digital platforms.

**Parent Business Domain:**

BD-025 Digital Channels

---

## 30.1 BE-158 Mobile Banking

### Description

Represents the mobile banking channel.

---

## 30.2 BE-159 Internet Banking

### Description

Represents the online banking channel.

---

## 30.3 BE-160 ATM

### Description

Represents Automated Teller Machines operated by the bank.

---

## 30.4 BE-161 API Channel

### Description

Represents external APIs exposed to customers and partners.

---

## 30.5 BE-162 Notification

### Description

Represents customer notifications generated by digital services.

### Examples

- SMS
- Email
- Push Notification

---

# 31. Enterprise Reporting Business Entities

Enterprise Reporting governs business intelligence and regulatory reporting.

**Parent Business Domain:**

BD-026 Enterprise Reporting

---

## 31.1 BE-163 Dashboard

### Description

Represents visual dashboards used by business users.

---

## 31.2 BE-164 Report

### Description

Represents operational, analytical, or regulatory reports.

---

## 31.3 BE-165 KPI

### Description

Represents Key Performance Indicators used for business monitoring.

---

## 31.4 BE-166 Metric

### Description

Represents measurable business values.

---

## 31.5 BE-167 Regulatory Submission

### Description

Represents reports submitted to regulatory authorities.

---

## 31.6 BE-168 Data Extract

### Description

Represents structured data prepared for reporting or regulatory submission.

---

# 32. Cross-Domain Business Entities

The following entities are shared across multiple Business Domains.

---

## 32.1 BE-169 Document

### Description

Represents documents used across enterprise business processes.

### Examples

- Identity Document
- Loan Agreement
- Contract
- Statement

---

## 32.2 BE-170 Attachment

### Description

Represents files associated with business records.

---

## 32.3 BE-171 Case

### Description

Represents business cases requiring investigation or workflow.

### Examples

- AML Case
- Fraud Case
- Customer Complaint
- Compliance Review

---

## 32.4 BE-172 Task

### Description

Represents business tasks assigned to users.

---

## 32.5 BE-173 Comment

### Description

Represents notes and collaboration related to business entities.

---

## 32.6 BE-174 Event

### Description

Represents significant business events occurring within the enterprise.

---

## 32.7 BE-175 Reference Data

### Description

Represents standardized reference values shared across the enterprise.

### Examples

- Country
- Currency
- Language
- Gender
- Branch Code

---

# 33. Business Entity Design Principles

Business Entities shall adhere to the following principles.

## 33.1 Business Focus

Business Entities shall represent business concepts rather than technical implementations.

---

## 33.2 Technology Independence

Business Entities shall remain independent of databases, applications, and programming languages.

---

## 33.3 Reusability

Business Entities shall be reusable across multiple business domains where appropriate.

---

## 33.4 Governance

Every Business Entity shall eventually be linked to:

- Business Terms
- Business Rules
- Critical Data Elements
- Data Owners
- Data Stewards
- Data Quality Rules

---

## 33.5 Traceability

Every Business Entity shall be traceable to:

- Business Domain
- Business Capability
- Information Model
- Logical Data Model
- Physical Data Model
- API
- User Interface

---

# 34. Summary

The Business Entity Catalog establishes the Canonical Banking Information Model for the Enterprise Data Governance Platform.

The model currently defines approximately **175 canonical Business Entities** organized across **26 Business Domains**.

These Business Entities form the foundation for:

- Enterprise Business Model
- Business Glossary
- Metadata Repository
- Data Dictionary
- Information Architecture
- Logical Data Model
- Physical Data Model
- REST APIs
- User Interface
- AI Knowledge Base

This catalog serves as the authoritative business vocabulary for the Enterprise Data Governance Platform and shall be referenced by all future architecture, governance, and implementation artifacts.