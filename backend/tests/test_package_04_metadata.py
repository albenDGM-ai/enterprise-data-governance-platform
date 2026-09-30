import uuid
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models.metadata.source_system import SourceSystem
from app.models.metadata.database import Database
from app.models.metadata.database_schema import DatabaseSchema
from app.models.metadata.database_table import DatabaseTable
from app.models.metadata.table_column import TableColumn


# --- SOURCE SYSTEM TESTS ---

def test_source_system_creation_and_retrieval(client: TestClient, db: Session):
    system_code = f"SRC_{uuid.uuid4().hex[:8]}"
    payload = {
        "system_code": system_code,
        "system_name": "Salesforce Production",
        "description": "Primary CRM source system",
        "system_type": "CRM",
        "vendor": "Salesforce",
        "business_domain": "Sales",
        "environment": "PROD",
        "owner": "sales_engineering",
        "steward": "john_doe",
        "status": "active",
        "is_active": True,
    }

    response = client.post("/api/v1/metadata/source-systems", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["system_code"] == system_code
    assert "source_system_id" in data

    source_system_id = data["source_system_id"]

    # Retrieval by ID
    get_res = client.get(f"/api/v1/metadata/source-systems/{source_system_id}")
    assert get_res.status_code == 200
    assert get_res.json()["system_name"] == "Salesforce Production"

    # List
    list_res = client.get("/api/v1/metadata/source-systems")
    assert list_res.status_code == 200
    systems = list_res.json()
    assert any(s["source_system_id"] == source_system_id for s in systems)


def test_source_system_duplicate_handling(client: TestClient):
    system_code = f"SRC_DUP_{uuid.uuid4().hex[:8]}"
    payload = {
        "system_code": system_code,
        "system_name": "ERP System",
        "system_type": "ERP",
        "business_domain": "Finance",
        "environment": "PROD",
        "owner": "finance_team",
        "steward": "jane_doe",
        "status": "active",
        "is_active": True,
    }

    res1 = client.post("/api/v1/metadata/source-systems", json=payload)
    assert res1.status_code == 201

    res2 = client.post("/api/v1/metadata/source-systems", json=payload)
    assert res2.status_code == 409


def test_source_system_validation_failure(client: TestClient):
    payload = {
        "system_code": "",  # Empty system code should fail validation
        "system_name": "Test System",
        "system_type": "RDBMS",
        "business_domain": "IT",
        "environment": "DEV",
        "owner": "admin",
        "steward": "admin",
        "status": "active",
    }
    response = client.post("/api/v1/metadata/source-systems", json=payload)
    assert response.status_code == 422


# --- DATABASE TESTS ---

def test_database_creation_and_retrieval(client: TestClient):
    # 1. Create source system
    system_code = f"SRC_DB_{uuid.uuid4().hex[:8]}"
    src_res = client.post("/api/v1/metadata/source-systems", json={
        "system_code": system_code,
        "system_name": "DW Source",
        "system_type": "RDBMS",
        "business_domain": "Data Warehouse",
        "environment": "PROD",
        "owner": "dw_admin",
        "steward": "dw_steward",
        "status": "active",
    })
    assert src_res.status_code == 201
    src_id = src_res.json()["source_system_id"]

    # 2. Create database
    db_payload = {
        "source_system_id": src_id,
        "database_name": "dw_prod",
        "database_type": "PostgreSQL",
        "version": "15.2",
        "description": "Main warehouse database",
        "owner": "dw_admin",
        "status": "active",
    }
    db_res = client.post("/api/v1/metadata/databases", json=db_payload)
    assert db_res.status_code == 201
    db_data = db_res.json()
    assert db_data["database_name"] == "dw_prod"
    database_id = db_data["database_id"]

    # 3. Get database by ID
    get_res = client.get(f"/api/v1/metadata/databases/{database_id}")
    assert get_res.status_code == 200
    assert get_res.json()["database_type"] == "PostgreSQL"

    # 4. List databases with filter
    list_res = client.get(f"/api/v1/metadata/databases?source_system_id={src_id}")
    assert list_res.status_code == 200
    dbs = list_res.json()
    assert len(dbs) == 1
    assert dbs[0]["database_id"] == database_id


def test_database_invalid_parent_rejection(client: TestClient):
    fake_source_system_id = str(uuid.uuid4())
    payload = {
        "source_system_id": fake_source_system_id,
        "database_name": "ghost_db",
        "database_type": "PostgreSQL",
        "owner": "admin",
        "status": "active",
    }
    response = client.post("/api/v1/metadata/databases", json=payload)
    assert response.status_code == 400
    assert "SourceSystem with id" in response.json()["detail"]


# --- SCHEMA TESTS ---

def test_schema_creation_and_retrieval(client: TestClient):
    # Setup parent hierarchy
    src_code = f"SRC_SCH_{uuid.uuid4().hex[:8]}"
    src_id = client.post("/api/v1/metadata/source-systems", json={
        "system_code": src_code,
        "system_name": "ERP Source",
        "system_type": "RDBMS",
        "business_domain": "Operations",
        "environment": "PROD",
        "owner": "ops",
        "steward": "ops",
        "status": "active",
    }).json()["source_system_id"]

    db_id = client.post("/api/v1/metadata/databases", json={
        "source_system_id": src_id,
        "database_name": "erp_db",
        "database_type": "Oracle",
        "owner": "ops",
        "status": "active",
    }).json()["database_id"]

    # Create schema
    schema_payload = {
        "database_id": db_id,
        "schema_name": "sales",
        "description": "Sales schema",
        "owner": "sales_lead",
        "status": "active",
    }
    schema_res = client.post("/api/v1/metadata/schemas", json=schema_payload)
    assert schema_res.status_code == 201
    schema_data = schema_res.json()
    assert schema_data["schema_name"] == "sales"
    schema_id = schema_data["database_schema_id"]

    # Retrieve schema
    get_res = client.get(f"/api/v1/metadata/schemas/{schema_id}")
    assert get_res.status_code == 200
    assert get_res.json()["schema_name"] == "sales"

    # List schemas
    list_res = client.get(f"/api/v1/metadata/schemas?database_id={db_id}")
    assert list_res.status_code == 200
    assert len(list_res.json()) == 1


def test_schema_invalid_parent_rejection(client: TestClient):
    fake_db_id = str(uuid.uuid4())
    payload = {
        "database_id": fake_db_id,
        "schema_name": "orphan_schema",
        "owner": "admin",
        "status": "active",
    }
    response = client.post("/api/v1/metadata/schemas", json=payload)
    assert response.status_code == 400
    assert "Database with id" in response.json()["detail"]


# --- TABLE TESTS ---

def test_table_creation_and_retrieval(client: TestClient):
    # Setup parent hierarchy
    src_code = f"SRC_TBL_{uuid.uuid4().hex[:8]}"
    src_id = client.post("/api/v1/metadata/source-systems", json={
        "system_code": src_code,
        "system_name": "CRM System",
        "system_type": "RDBMS",
        "business_domain": "Sales",
        "environment": "PROD",
        "owner": "crm",
        "steward": "crm",
        "status": "active",
    }).json()["source_system_id"]

    db_id = client.post("/api/v1/metadata/databases", json={
        "source_system_id": src_id,
        "database_name": "crm_db",
        "database_type": "PostgreSQL",
        "owner": "crm",
        "status": "active",
    }).json()["database_id"]

    schema_id = client.post("/api/v1/metadata/schemas", json={
        "database_id": db_id,
        "schema_name": "public",
        "owner": "crm",
        "status": "active",
    }).json()["database_schema_id"]

    # Create table
    table_payload = {
        "database_schema_id": schema_id,
        "table_name": "customers",
        "display_name": "Customers Table",
        "description": "Customer accounts and details",
        "table_type": "BASE TABLE",
        "row_count": 100000,
        "owner": "crm_lead",
        "classification": "confidential",
        "status": "active",
    }
    table_res = client.post("/api/v1/metadata/tables", json=table_payload)
    assert table_res.status_code == 201
    table_data = table_res.json()
    assert table_data["table_name"] == "customers"
    table_id = table_data["database_table_id"]

    # Get table
    get_res = client.get(f"/api/v1/metadata/tables/{table_id}")
    assert get_res.status_code == 200
    assert get_res.json()["table_name"] == "customers"

    # List tables
    list_res = client.get(f"/api/v1/metadata/tables?database_schema_id={schema_id}")
    assert list_res.status_code == 200
    assert len(list_res.json()) == 1


def test_table_invalid_parent_rejection(client: TestClient):
    fake_schema_id = str(uuid.uuid4())
    payload = {
        "database_schema_id": fake_schema_id,
        "table_name": "orphan_table",
        "display_name": "Orphan Table",
        "table_type": "BASE TABLE",
        "owner": "admin",
        "classification": "public",
        "status": "active",
    }
    response = client.post("/api/v1/metadata/tables", json=payload)
    assert response.status_code == 400
    assert "DatabaseSchema with id" in response.json()["detail"]


# --- COLUMN TESTS ---

def test_column_creation_and_retrieval(client: TestClient):
    # Setup parent hierarchy
    src_code = f"SRC_COL_{uuid.uuid4().hex[:8]}"
    src_id = client.post("/api/v1/metadata/source-systems", json={
        "system_code": src_code,
        "system_name": "Analytics DB",
        "system_type": "RDBMS",
        "business_domain": "Analytics",
        "environment": "PROD",
        "owner": "analytics",
        "steward": "analytics",
        "status": "active",
    }).json()["source_system_id"]

    db_id = client.post("/api/v1/metadata/databases", json={
        "source_system_id": src_id,
        "database_name": "analytics_db",
        "database_type": "PostgreSQL",
        "owner": "analytics",
        "status": "active",
    }).json()["database_id"]

    schema_id = client.post("/api/v1/metadata/schemas", json={
        "database_id": db_id,
        "schema_name": "reporting",
        "owner": "analytics",
        "status": "active",
    }).json()["database_schema_id"]

    table_id = client.post("/api/v1/metadata/tables", json={
        "database_schema_id": schema_id,
        "table_name": "revenue_report",
        "display_name": "Revenue Report",
        "table_type": "VIEW",
        "owner": "analytics",
        "classification": "internal",
        "status": "active",
    }).json()["database_table_id"]

    # Create column
    col_payload = {
        "database_table_id": table_id,
        "column_name": "customer_id",
        "display_name": "Customer Identifier",
        "description": "Unique key for customer",
        "logical_data_type": "UUID",
        "nullable": False,
        "primary_key_flag": True,
        "foreign_key_flag": False,
        "classification": "confidential",
        "critical_data_element_flag": True,
        "ordinal_position": 1,
    }
    col_res = client.post("/api/v1/metadata/columns", json=col_payload)
    assert col_res.status_code == 201
    col_data = col_res.json()
    assert col_data["column_name"] == "customer_id"
    col_id = col_data["table_column_id"]

    # Get column
    get_res = client.get(f"/api/v1/metadata/columns/{col_id}")
    assert get_res.status_code == 200
    assert get_res.json()["logical_data_type"] == "UUID"

    # List columns
    list_res = client.get(f"/api/v1/metadata/columns?database_table_id={table_id}")
    assert list_res.status_code == 200
    assert len(list_res.json()) == 1


def test_column_invalid_parent_rejection(client: TestClient):
    fake_table_id = str(uuid.uuid4())
    payload = {
        "database_table_id": fake_table_id,
        "column_name": "orphan_column",
        "display_name": "Orphan Column",
        "logical_data_type": "VARCHAR",
        "nullable": True,
        "primary_key_flag": False,
        "foreign_key_flag": False,
        "classification": "public",
        "critical_data_element_flag": False,
        "ordinal_position": 1,
    }
    response = client.post("/api/v1/metadata/columns", json=payload)
    assert response.status_code == 400
    assert "DatabaseTable with id" in response.json()["detail"]


# --- FULL METADATA HIERARCHY INTEGRATION TEST ---

def test_full_technical_metadata_hierarchy_with_data_asset(client: TestClient):
    # 1. Source System
    src_code = f"SRC_FULL_{uuid.uuid4().hex[:8]}"
    src_res = client.post("/api/v1/metadata/source-systems", json={
        "system_code": src_code,
        "system_name": "Enterprise Data Hub",
        "system_type": "RDBMS",
        "business_domain": "Core",
        "environment": "PROD",
        "owner": "data_gov",
        "steward": "data_steward",
        "status": "active",
    })
    assert src_res.status_code == 201
    src_id = src_res.json()["source_system_id"]

    # 2. Database
    db_res = client.post("/api/v1/metadata/databases", json={
        "source_system_id": src_id,
        "database_name": "edh_prod",
        "database_type": "PostgreSQL",
        "owner": "data_gov",
        "status": "active",
    })
    assert db_res.status_code == 201
    db_id = db_res.json()["database_id"]

    # 3. Schema
    schema_res = client.post("/api/v1/metadata/schemas", json={
        "database_id": db_id,
        "schema_name": "finance",
        "owner": "finance_gov",
        "status": "active",
    })
    assert schema_res.status_code == 201
    schema_id = schema_res.json()["database_schema_id"]

    # 4. Table
    table_res = client.post("/api/v1/metadata/tables", json={
        "database_schema_id": schema_id,
        "table_name": "general_ledger",
        "display_name": "General Ledger",
        "table_type": "BASE TABLE",
        "owner": "finance_gov",
        "classification": "restricted",
        "status": "active",
    })
    assert table_res.status_code == 201
    table_id = table_res.json()["database_table_id"]

    # 5. Column
    col_res = client.post("/api/v1/metadata/columns", json={
        "database_table_id": table_id,
        "column_name": "account_balance",
        "display_name": "Account Balance",
        "logical_data_type": "DECIMAL(18,2)",
        "nullable": False,
        "primary_key_flag": False,
        "foreign_key_flag": False,
        "classification": "restricted",
        "critical_data_element_flag": True,
        "ordinal_position": 2,
    })
    assert col_res.status_code == 201
    col_id = col_res.json()["table_column_id"]

    # 6. Data Asset pointing to Table and Source System
    asset_payload = {
        "asset_type": "table",
        "asset_identifier": table_id,
        "asset_name": "general_ledger_asset",
        "display_name": "General Ledger Asset",
        "description": "Data Asset representing general ledger table",
        "business_domain": "Finance",
        "source_system_id": src_id,
        "owner": "finance_gov",
        "steward": "data_steward",
        "classification": "restricted",
        "critical_data_element_flag": True,
        "status": "active",
        "is_active": True,
    }
    asset_res = client.post("/api/v1/metadata/data-assets", json=asset_payload)
    assert asset_res.status_code == 201
    asset_data = asset_res.json()
    assert asset_data["asset_identifier"] == table_id
    assert asset_data["source_system_id"] == src_id
