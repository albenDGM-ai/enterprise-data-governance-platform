# Metadata Repository API Design

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
- 06_PhysicalModel.md
- 09_DataDictionary.md
- 10_NamingStandards.md

---

# 1. Purpose

## 1.1 Objective

This document defines the REST API specification for the Metadata Repository module of the Enterprise Data Governance Platform.

The Metadata Repository provides centralized management of enterprise technical metadata and serves as the foundational module upon which all other platform capabilities depend.

This document specifies:

- REST resources
- Endpoint definitions
- Request models
- Response models
- Validation rules
- Authentication requirements
- Authorization rules
- Search capabilities
- Bulk operations
- Error handling conventions

The APIs defined in this document will be implemented using FastAPI and documented using the OpenAPI Specification.

---

## 1.2 Scope

This document defines APIs for the following metadata resources:

- Source Systems
- Databases
- Database Schemas
- Database Tables
- Table Columns
- Database Views
- File Assets
- API Assets
- Data Assets

The document also defines common platform APIs including:

- Search
- Import
- Export
- Bulk Operations
- Metadata Validation

---

# 2. API Design Principles

The Metadata Repository APIs shall adhere to the following design principles.

## 2.1 RESTful Architecture

APIs shall follow REST architectural principles.

Resources shall be represented using nouns.

Examples:

```
/source-systems
/tables
/data-assets
```

HTTP verbs shall define the operation.

| Method | Purpose |
|----------|----------|
| GET | Retrieve |
| POST | Create |
| PUT | Replace |
| PATCH | Partial Update |
| DELETE | Soft Delete |

---

## 2.2 Versioning

All APIs shall be versioned.

Current Version

```
/api/v1
```

Future versions shall be introduced without breaking backward compatibility.

Examples

```
/api/v2
/api/v3
```

---

## 2.3 JSON

All requests and responses shall use JSON.

Content-Type

```
application/json
```

---

## 2.4 Stateless

The Metadata Repository APIs shall remain stateless.

Each request shall contain all information required for processing.

---

## 2.5 Consistency

All APIs shall follow consistent naming conventions.

Examples

```
GET     /tables

GET     /tables/{id}

POST    /tables

PUT     /tables/{id}

PATCH   /tables/{id}

DELETE  /tables/{id}
```

---

## 2.6 Pagination

Collection APIs shall support pagination.

Example

```
GET /tables?page=1&pageSize=25
```

---

## 2.7 Sorting

Collection APIs shall support sorting.

Example

```
GET /tables?sort=tableName&direction=asc
```

---

## 2.8 Filtering

Collection APIs shall support filtering.

Example

```
GET /tables?status=Active
```

---

## 2.9 Searching

Collection APIs shall support keyword searching.

Example

```
GET /tables?search=customer
```

---

# 3. Authentication and Authorization

## 3.1 Authentication

All Metadata Repository APIs shall require authentication except platform health endpoints.

Authentication shall use:

- OAuth2
- JWT Bearer Tokens

Authorization header

```
Authorization: Bearer <JWT Token>
```

---

## 3.2 Authorization

Authorization shall use Role-Based Access Control (RBAC).

Supported roles include:

- Platform Administrator
- Data Governance Administrator
- Data Owner
- Data Steward
- Data Architect
- Business Analyst
- Read Only User
- AI Service Account

Each API shall validate user permissions before executing business logic.

---

# 4. Standard Request Headers

| Header | Required | Description |
|----------|----------|-------------|
| Authorization | Yes | JWT Bearer Token |
| Content-Type | Yes | application/json |
| Accept | Yes | application/json |
| X-Correlation-ID | No | Request trace identifier |
| X-Request-ID | No | Client request identifier |

---

# 5. Standard Query Parameters

All collection APIs shall support the following query parameters.

| Parameter | Description |
|-----------|-------------|
| page | Page number |
| pageSize | Records per page |
| sort | Sort column |
| direction | asc or desc |
| search | Keyword search |
| status | Lifecycle status |
| owner | Data Owner |
| steward | Data Steward |
| classification | Information Classification |

Example

```
GET /tables?page=1&pageSize=20&sort=tableName&direction=asc&status=Active
```

---

# 6. Metadata Repository Resources

The Metadata Repository exposes the following REST resources.

| Resource | Endpoint |
|----------|----------|
| Source Systems | /source-systems |
| Databases | /databases |
| Database Schemas | /schemas |
| Database Tables | /tables |
| Table Columns | /columns |
| Database Views | /views |
| File Assets | /files |
| API Assets | /apis |
| Data Assets | /data-assets |

These resources collectively provide complete management of enterprise technical metadata.

---

# 7. Source System API

## 7.1 Overview

The Source System API manages enterprise applications and systems that produce or consume enterprise data.

Examples include:

- Core Banking
- CRM
- ERP
- Data Warehouse
- SAP
- Salesforce
- External Vendor Systems

---

## 7.2 Resource URI

```
/api/v1/source-systems
```

---

## 7.3 Supported Operations

| Operation | Method | Endpoint |
|-----------|--------|----------|
| List Source Systems | GET | /source-systems |
| Get Source System | GET | /source-systems/{id} |
| Create Source System | POST | /source-systems |
| Replace Source System | PUT | /source-systems/{id} |
| Update Source System | PATCH | /source-systems/{id} |
| Delete Source System | DELETE | /source-systems/{id} |
| Search Source Systems | GET | /source-systems/search |

---

## 7.4 Create Source System

### Endpoint

```
POST /api/v1/source-systems
```

### Description

Registers a new Source System within the Metadata Repository.

### Request Body

```json
{
  "systemCode": "CBS",
  "systemName": "Core Banking System",
  "description": "Primary banking platform",
  "systemType": "Core Banking",
  "vendor": "Temenos",
  "businessDomain": "Retail Banking",
  "environment": "Production",
  "owner": "Head of Retail Banking",
  "steward": "Retail Data Steward",
  "status": "Active"
}
```

### Success Response

```
201 Created
```

Returns the newly created Source System resource.

### Validation Rules

- System Code is mandatory.
- System Code shall be unique.
- System Name is mandatory.
- Business Domain is mandatory.
- Owner is mandatory.
- Steward is mandatory.

---

## 7.5 Retrieve Source Systems

### Endpoint

```
GET /api/v1/source-systems
```

### Description

Returns a paginated list of Source Systems.

### Query Parameters

| Parameter | Description |
|-----------|-------------|
| page | Page number |
| pageSize | Number of records |
| search | Keyword search |
| sort | Sort field |
| direction | asc or desc |
| status | Lifecycle status |
| owner | Data Owner |
| businessDomain | Business Domain |

### Success Response

```
200 OK
```

---

## 7.6 Retrieve Source System

### Endpoint

```
GET /api/v1/source-systems/{id}
```

### Description

Returns detailed information about a specific Source System.

### Success Response

```
200 OK
```

### Error Responses

```
404 Not Found

401 Unauthorized

403 Forbidden
```

---

## 7.7 Update Source System

### Endpoint

```
PUT /api/v1/source-systems/{id}
```

### Description

Replaces an existing Source System.

### Success Response

```
200 OK
```

---

## 7.8 Partial Update

### Endpoint

```
PATCH /api/v1/source-systems/{id}
```

### Description

Updates one or more Source System attributes.

---

## 7.9 Delete Source System

### Endpoint

```
DELETE /api/v1/source-systems/{id}
```

### Description

Performs a soft delete by marking the Source System as inactive.

Physical deletion is not permitted.

---

# 8. Database API

## Resource URI

```
/api/v1/databases
```

## Supported Operations

| Operation | Method |
|-----------|--------|
| List Databases | GET |
| Retrieve Database | GET |
| Create Database | POST |
| Replace Database | PUT |
| Update Database | PATCH |
| Delete Database | DELETE |
| Search Databases | GET |

### Create Database

```
POST /api/v1/databases
```

Mandatory fields:

- Source System
- Database Name
- Database Type
- Owner
- Status

---

# 9. Database Schema API

## Resource URI

```
/api/v1/schemas
```

Supported Operations

- List
- Retrieve
- Create
- Replace
- Update
- Delete
- Search

Mandatory fields

- Database
- Schema Name
- Owner
- Status

---

# 10. Database Table API

## Resource URI

```
/api/v1/tables
```

Supported Operations

- List
- Retrieve
- Create
- Replace
- Update
- Delete
- Search

Additional Operations

```
GET /tables/{id}/columns

GET /tables/{id}/views

GET /tables/{id}/statistics

GET /tables/{id}/relationships

GET /tables/{id}/lineage

GET /tables/{id}/quality
```

Mandatory Fields

- Schema
- Table Name
- Classification
- Owner
- Status

---

# 11. Table Column API

## Resource URI

```
/api/v1/columns
```

Supported Operations

- List
- Retrieve
- Create
- Replace
- Update
- Delete
- Search

Additional Operations

```
GET /columns/{id}/lineage

GET /columns/{id}/quality

GET /columns/{id}/business-terms
```

Mandatory Fields

- Table
- Column Name
- Logical Data Type
- Nullable
- Classification

---

# 12. Database View API

## Resource URI

```
/api/v1/views
```

Supported Operations

- List
- Retrieve
- Create
- Replace
- Update
- Delete
- Search

Mandatory Fields

- Schema
- View Name
- View Type

---

# 13. File Asset API

## Resource URI

```
/api/v1/files
```

Supported Operations

- List
- Retrieve
- Create
- Replace
- Update
- Delete
- Search

Mandatory Fields

- Source System
- File Name
- File Type
- Owner

---

# 14. API Asset API

## Resource URI

```
/api/v1/apis
```

Supported Operations

- List
- Retrieve
- Create
- Replace
- Update
- Delete
- Search

Mandatory Fields

- Source System
- API Name
- API Type
- API Version

---

# 15. Data Asset API

## Resource URI

```
/api/v1/data-assets
```

Supported Operations

- List
- Retrieve
- Create
- Replace
- Update
- Delete
- Search

Additional Operations

```
GET /data-assets/{id}/quality

GET /data-assets/{id}/lineage

GET /data-assets/{id}/classifications

GET /data-assets/{id}/business-terms

GET /data-assets/{id}/policies
```

Mandatory Fields

- Asset Type
- Asset Name
- Owner
- Steward
- Classification
- Status

---

# 16. Global Search API

## 16.1 Purpose

The Global Search API provides a unified search capability across all metadata resources within the Metadata Repository.

It enables users, applications, and AI services to locate metadata objects using a single endpoint.

---

## 16.2 Resource URI

```
/api/v1/search
```

---

## 16.3 Supported Operations

| Operation | Method | Endpoint |
|-----------|--------|----------|
| Global Search | GET | /search |
| Advanced Search | POST | /search/advanced |
| Search Suggestions | GET | /search/suggestions |

---

## 16.4 Query Parameters

| Parameter | Description |
|-----------|-------------|
| search | Search keyword |
| resourceType | SourceSystem, Database, Schema, Table, Column, View, File, API, DataAsset |
| classification | Information Classification |
| owner | Data Owner |
| steward | Data Steward |
| status | Lifecycle Status |
| page | Page Number |
| pageSize | Records Per Page |

---

# 17. Import and Export APIs

## 17.1 Purpose

Import and Export APIs support bulk metadata loading and extraction.

---

## 17.2 Import APIs

| Operation | Method | Endpoint |
|-----------|--------|----------|
| Import Metadata | POST | /metadata/import |
| Validate Import | POST | /metadata/import/validate |
| Import Status | GET | /metadata/import/{jobId} |

Supported file formats:

- CSV
- Excel
- JSON

---

## 17.3 Export APIs

| Operation | Method | Endpoint |
|-----------|--------|----------|
| Export Metadata | GET | /metadata/export |
| Export Tables | GET | /tables/export |
| Export Columns | GET | /columns/export |
| Export Data Assets | GET | /data-assets/export |

Supported export formats:

- CSV
- Excel
- JSON

---

# 18. Bulk Operations APIs

## 18.1 Purpose

Bulk APIs allow multiple metadata records to be processed within a single request.

---

## 18.2 Supported Operations

| Operation | Method | Endpoint |
|-----------|--------|----------|
| Bulk Create | POST | /bulk/create |
| Bulk Update | PUT | /bulk/update |
| Bulk Delete | DELETE | /bulk/delete |
| Bulk Validate | POST | /bulk/validate |

---

## 18.3 Business Rules

- Every request shall be validated before execution.
- Invalid records shall be reported individually.
- Successful records shall not be rolled back unless transactional execution is requested.
- All bulk operations shall be recorded in the Audit Log.

---

# 19. AI Metadata APIs

## 19.1 Purpose

The AI Metadata APIs provide AI-assisted capabilities for metadata management.

These APIs are intended for use by the platform's AI Services Module and future AI agents.

---

## 19.2 Supported Operations

| Operation | Method | Endpoint |
|-----------|--------|----------|
| Generate Metadata | POST | /ai/generate-metadata |
| Suggest Business Name | POST | /ai/suggest-name |
| Generate Description | POST | /ai/generate-description |
| Classify Metadata | POST | /ai/classify |
| Detect Duplicates | POST | /ai/detect-duplicates |
| Recommend Owner | POST | /ai/recommend-owner |
| Recommend Steward | POST | /ai/recommend-steward |
| Explain Metadata | POST | /ai/explain |

---

## 19.3 AI Business Rules

- AI shall not persist changes directly.
- AI-generated content shall require user approval.
- AI recommendations shall be auditable.
- AI responses shall reference the underlying metadata where applicable.

---

# 20. Standard Response Model

All successful API responses shall follow a consistent structure.

Example

```json
{
  "success": true,
  "message": "Operation completed successfully.",
  "data": {},
  "timestamp": "2026-08-01T10:30:00Z",
  "requestId": "REQ-123456"
}
```

---

# 21. Standard Error Model

All error responses shall follow a consistent structure.

Example

```json
{
  "success": false,
  "errorCode": "METADATA-001",
  "message": "Source System already exists.",
  "details": [],
  "timestamp": "2026-08-01T10:30:00Z",
  "requestId": "REQ-123456"
}
```

---

# 22. HTTP Status Codes

| Status Code | Description |
|--------------|-------------|
| 200 | Success |
| 201 | Resource Created |
| 204 | Resource Deleted |
| 400 | Bad Request |
| 401 | Authentication Required |
| 403 | Access Denied |
| 404 | Resource Not Found |
| 409 | Duplicate Resource |
| 422 | Validation Failed |
| 429 | Too Many Requests |
| 500 | Internal Server Error |

---

# 23. API Versioning Strategy

The Metadata Repository APIs shall support versioning to maintain backward compatibility.

Current Version

```
/api/v1
```

Future versions

```
/api/v2
/api/v3
```

Deprecation of API versions shall follow the platform's release management policy.

---

# 24. Security Considerations

The Metadata Repository APIs shall implement the following security controls.

- OAuth2 Authentication
- JWT Authorization
- Role-Based Access Control (RBAC)
- HTTPS Only
- Input Validation
- Output Encoding
- Request Logging
- Audit Logging
- Rate Limiting
- API Version Validation

---

# 25. Summary

The Metadata Repository API provides a comprehensive REST interface for managing enterprise technical metadata.

The API specification includes:

- Resource APIs
- Search APIs
- Import APIs
- Export APIs
- Bulk Operations APIs
- AI-assisted Metadata APIs
- Standard Request and Response Models
- Error Handling Standards
- Authentication and Authorization
- API Versioning
- Security Controls

The APIs defined in this document will be implemented using FastAPI and exposed through OpenAPI documentation.

These APIs provide the integration layer between the PostgreSQL database, React frontend, AI Services Module, external systems, and future enterprise integrations.