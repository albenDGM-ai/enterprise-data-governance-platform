import uuid
from decimal import Decimal
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def test_data_asset(client: TestClient):
    """Fixture to create a test DataAsset."""
    asset_payload = {
        "asset_type": "table",
        "asset_identifier": str(uuid.uuid4()),
        "asset_name": f"customer_orders_{uuid.uuid4().hex[:8]}",
        "display_name": "Customer Orders",
        "business_domain": "Sales",
        "owner": "sales_lead",
        "steward": "sales_steward",
        "classification": "confidential",
        "critical_data_element_flag": True,
        "status": "active",
        "is_active": True,
    }
    response = client.post("/api/v1/metadata/data-assets", json=asset_payload)
    assert response.status_code == 201
    return response.json()


@pytest.fixture
def test_column(client: TestClient):
    """Fixture to create a full technical metadata hierarchy including a Column."""
    # 1. Source System
    ss_payload = {
        "system_code": f"SYS_{uuid.uuid4().hex[:6].upper()}",
        "system_name": "Core CRM",
        "system_type": "OLTP",
        "business_domain": "Sales",
        "environment": "PROD",
        "owner": "it_admin",
        "steward": "it_steward",
        "status": "ACTIVE",
    }
    ss_res = client.post("/api/v1/metadata/source-systems", json=ss_payload)
    assert ss_res.status_code == 201
    ss_id = ss_res.json()["source_system_id"]

    # 2. Database
    db_payload = {
        "source_system_id": ss_id,
        "database_name": f"crm_db_{uuid.uuid4().hex[:6]}",
        "display_name": "CRM Database",
        "database_type": "PostgreSQL",
        "owner": "db_admin",
        "status": "ACTIVE",
    }
    db_res = client.post("/api/v1/metadata/databases", json=db_payload)
    assert db_res.status_code == 201
    db_id = db_res.json()["database_id"]

    # 3. Schema
    schema_payload = {
        "database_id": db_id,
        "schema_name": f"public_{uuid.uuid4().hex[:6]}",
        "display_name": "Public Schema",
        "owner": "db_admin",
        "status": "ACTIVE",
    }
    schema_res = client.post("/api/v1/metadata/schemas", json=schema_payload)
    assert schema_res.status_code == 201
    schema_id = schema_res.json()["database_schema_id"]

    # 4. Table
    table_payload = {
        "database_schema_id": schema_id,
        "table_name": f"customers_{uuid.uuid4().hex[:6]}",
        "display_name": "Customers Table",
        "table_type": "BASE TABLE",
        "owner": "db_admin",
        "classification": "public",
        "status": "ACTIVE",
    }
    table_res = client.post("/api/v1/metadata/tables", json=table_payload)
    assert table_res.status_code == 201
    table_id = table_res.json()["database_table_id"]

    # 5. Column
    column_payload = {
        "database_table_id": table_id,
        "column_name": "email",
        "display_name": "Customer Email Address",
        "logical_data_type": "VARCHAR",
        "nullable": False,
        "primary_key_flag": False,
        "foreign_key_flag": False,
        "classification": "CONFIDENTIAL",
        "critical_data_element_flag": True,
        "ordinal_position": 1,
    }
    col_res = client.post("/api/v1/metadata/columns", json=column_payload)
    assert col_res.status_code == 201
    return col_res.json()


def test_data_quality_rule_creation(client: TestClient, test_data_asset: dict):
    rule_code = f"DQ_RULE_{uuid.uuid4().hex[:8].upper()}"
    asset_id = test_data_asset["data_asset_id"]

    payload = {
        "rule_code": rule_code,
        "rule_name": "Check Non-Null Customer IDs",
        "target_data_asset_id": asset_id,
        "severity": "CRITICAL",
        "threshold_percentage": "99.50",
        "execution_frequency": "DAILY",
        "owner": "data_quality_team",
        "status": "ACTIVE",
    }

    response = client.post("/api/v1/quality/rules", json=payload)
    assert response.status_code == 201
    data = response.json()

    assert data["rule_code"] == rule_code
    assert data["target_data_asset_id"] == asset_id
    assert data["severity"] == "CRITICAL"
    assert data["threshold_percentage"] == "99.50"
    assert data["status"] == "ACTIVE"
    assert "data_quality_rule_id" in data
    assert "data_quality_dimension_id" in data
    assert "business_rule_id" in data


def test_data_quality_rule_retrieval(client: TestClient, test_data_asset: dict):
    rule_code = f"DQ_RULE_{uuid.uuid4().hex[:8].upper()}"
    asset_id = test_data_asset["data_asset_id"]

    payload = {
        "rule_code": rule_code,
        "rule_name": "Check Valid Emails",
        "target_data_asset_id": asset_id,
        "severity": "HIGH",
        "threshold_percentage": "95.00",
        "execution_frequency": "HOURLY",
        "owner": "qa_team",
        "status": "ACTIVE",
    }
    create_res = client.post("/api/v1/quality/rules", json=payload)
    assert create_res.status_code == 201
    rule_id = create_res.json()["data_quality_rule_id"]

    get_res = client.get(f"/api/v1/quality/rules/{rule_id}")
    assert get_res.status_code == 200
    data = get_res.json()
    assert data["data_quality_rule_id"] == rule_id
    assert data["rule_code"] == rule_code
    assert data["rule_name"] == "Check Valid Emails"


def test_data_quality_rule_listing(client: TestClient, test_data_asset: dict):
    asset_id = test_data_asset["data_asset_id"]
    rule_code = f"DQ_RULE_LIST_{uuid.uuid4().hex[:8].upper()}"

    payload = {
        "rule_code": rule_code,
        "rule_name": "List Test Rule",
        "target_data_asset_id": asset_id,
        "severity": "MEDIUM",
        "threshold_percentage": "90.00",
        "execution_frequency": "WEEKLY",
        "owner": "steward",
        "status": "ACTIVE",
    }
    create_res = client.post("/api/v1/quality/rules", json=payload)
    assert create_res.status_code == 201
    rule_id = create_res.json()["data_quality_rule_id"]

    list_res = client.get(f"/api/v1/quality/rules?target_data_asset_id={asset_id}&status=ACTIVE")
    assert list_res.status_code == 200
    rules = list_res.json()
    assert len(rules) >= 1
    assert any(r["data_quality_rule_id"] == rule_id for r in rules)


def test_data_quality_rule_validation_failure(client: TestClient, test_data_asset: dict):
    # Invalid threshold_percentage (> 100)
    payload = {
        "rule_code": f"DQ_RULE_BAD_{uuid.uuid4().hex[:6]}",
        "rule_name": "Bad Threshold Rule",
        "target_data_asset_id": test_data_asset["data_asset_id"],
        "threshold_percentage": "150.00",
    }
    response = client.post("/api/v1/quality/rules", json=payload)
    assert response.status_code == 422


def test_data_quality_rule_duplicate_handling(client: TestClient, test_data_asset: dict):
    rule_code = f"DQ_DUP_{uuid.uuid4().hex[:8].upper()}"
    payload = {
        "rule_code": rule_code,
        "rule_name": "Duplicate Check Rule",
        "target_data_asset_id": test_data_asset["data_asset_id"],
        "severity": "HIGH",
        "threshold_percentage": "95.00",
        "execution_frequency": "DAILY",
        "owner": "owner",
        "status": "ACTIVE",
    }

    res1 = client.post("/api/v1/quality/rules", json=payload)
    assert res1.status_code == 201

    res2 = client.post("/api/v1/quality/rules", json=payload)
    assert res2.status_code == 409
    assert "already exists" in res2.json()["detail"]


def test_data_quality_rule_not_found(client: TestClient):
    fake_id = str(uuid.uuid4())
    get_res = client.get(f"/api/v1/quality/rules/{fake_id}")
    assert get_res.status_code == 404
    assert f"DataQualityRule with id {fake_id} not found" in get_res.json()["detail"]


def test_data_quality_rule_asset_and_column_relationship(client: TestClient, test_data_asset: dict, test_column: dict):
    # 1. Rule linked to DataAsset
    asset_id = test_data_asset["data_asset_id"]
    payload_asset = {
        "rule_code": f"DQ_ASSET_{uuid.uuid4().hex[:8].upper()}",
        "rule_name": "Asset Level Rule",
        "target_data_asset_id": asset_id,
        "severity": "HIGH",
        "threshold_percentage": "95.00",
        "execution_frequency": "DAILY",
        "owner": "owner",
        "status": "ACTIVE",
    }
    res_asset = client.post("/api/v1/quality/rules", json=payload_asset)
    assert res_asset.status_code == 201
    assert res_asset.json()["target_data_asset_id"] == asset_id

    # 2. Rule linked to TableColumn
    col_id = test_column["table_column_id"]
    payload_col = {
        "rule_code": f"DQ_COL_{uuid.uuid4().hex[:8].upper()}",
        "rule_name": "Column Level Rule",
        "target_data_asset_id": col_id,
        "severity": "CRITICAL",
        "threshold_percentage": "100.00",
        "execution_frequency": "HOURLY",
        "owner": "owner",
        "status": "ACTIVE",
    }
    res_col = client.post("/api/v1/quality/rules", json=payload_col)
    assert res_col.status_code == 201
    assert res_col.json()["target_data_asset_id"] == col_id

    # 3. Rule linked to invalid target ID -> 404
    fake_id = str(uuid.uuid4())
    payload_fake = {
        "rule_code": f"DQ_FAKE_{uuid.uuid4().hex[:8].upper()}",
        "rule_name": "Fake Asset Rule",
        "target_data_asset_id": fake_id,
        "severity": "LOW",
        "threshold_percentage": "50.00",
        "execution_frequency": "MONTHLY",
        "owner": "owner",
        "status": "ACTIVE",
    }
    res_fake = client.post("/api/v1/quality/rules", json=payload_fake)
    assert res_fake.status_code == 404
    assert f"Referenced DataAsset or Column with id {fake_id} not found" in res_fake.json()["detail"]


def test_data_quality_result_creation(client: TestClient, test_data_asset: dict):
    # Create rule first
    rule_payload = {
        "rule_code": f"DQ_RESULT_{uuid.uuid4().hex[:8].upper()}",
        "rule_name": "Result Test Rule",
        "target_data_asset_id": test_data_asset["data_asset_id"],
        "severity": "HIGH",
        "threshold_percentage": "95.00",
        "execution_frequency": "DAILY",
        "owner": "qa_team",
        "status": "ACTIVE",
    }
    rule_res = client.post("/api/v1/quality/rules", json=rule_payload)
    assert rule_res.status_code == 201
    rule_id = rule_res.json()["data_quality_rule_id"]

    # Create result
    result_payload = {
        "data_quality_rule_id": rule_id,
        "total_records": 1000,
        "passed_records": 980,
        "failed_records": 20,
        "warning_records": 0,
        "result_status": "PASSED",
        "execution_duration_ms": 150,
    }
    response = client.post("/api/v1/quality/results", json=result_payload)
    assert response.status_code == 201
    data = response.json()

    assert data["data_quality_rule_id"] == rule_id
    assert data["target_data_asset_id"] == test_data_asset["data_asset_id"]
    assert data["total_records"] == 1000
    assert data["passed_records"] == 980
    assert data["failed_records"] == 20
    assert data["quality_percentage"] == "98.00"
    assert data["result_status"] == "PASSED"
    assert "data_quality_result_id" in data
    assert "data_quality_assessment_id" in data


def test_data_quality_result_invalid_rule_reference(client: TestClient):
    fake_rule_id = str(uuid.uuid4())
    payload = {
        "data_quality_rule_id": fake_rule_id,
        "total_records": 100,
        "passed_records": 100,
        "failed_records": 0,
        "result_status": "PASSED",
    }
    response = client.post("/api/v1/quality/results", json=payload)
    assert response.status_code == 404
    assert f"DataQualityRule with id {fake_rule_id} not found" in response.json()["detail"]


def test_data_quality_result_retrieval_and_listing(client: TestClient, test_data_asset: dict):
    rule_payload = {
        "rule_code": f"DQ_RES_LIST_{uuid.uuid4().hex[:8].upper()}",
        "rule_name": "Result List Test Rule",
        "target_data_asset_id": test_data_asset["data_asset_id"],
        "severity": "CRITICAL",
        "threshold_percentage": "99.00",
        "execution_frequency": "HOURLY",
        "owner": "steward",
        "status": "ACTIVE",
    }
    rule_res = client.post("/api/v1/quality/rules", json=rule_payload)
    assert rule_res.status_code == 201
    rule_id = rule_res.json()["data_quality_rule_id"]

    res_payload = {
        "data_quality_rule_id": rule_id,
        "total_records": 500,
        "passed_records": 495,
        "failed_records": 5,
        "result_status": "PASSED",
    }
    create_res = client.post("/api/v1/quality/results", json=res_payload)
    assert create_res.status_code == 201
    result_id = create_res.json()["data_quality_result_id"]

    # 1. Retrieve by ID
    get_res = client.get(f"/api/v1/quality/results/{result_id}")
    assert get_res.status_code == 200
    assert get_res.json()["data_quality_result_id"] == result_id
    assert get_res.json()["data_quality_rule_id"] == rule_id

    # 2. List results filtered by rule_id
    list_res = client.get(f"/api/v1/quality/results?data_quality_rule_id={rule_id}")
    assert list_res.status_code == 200
    results = list_res.json()
    assert len(results) == 1
    assert results[0]["data_quality_result_id"] == result_id

    # 3. Non-existent result ID -> 404
    fake_res_id = str(uuid.uuid4())
    get_fake = client.get(f"/api/v1/quality/results/{fake_res_id}")
    assert get_fake.status_code == 404


def test_data_quality_result_reject_inconsistent_record_counts(client: TestClient, test_data_asset: dict):
    rule_payload = {
        "rule_code": f"DQ_RES_COUNT_{uuid.uuid4().hex[:8].upper()}",
        "rule_name": "Count Invariant Test Rule",
        "target_data_asset_id": test_data_asset["data_asset_id"],
        "severity": "HIGH",
        "threshold_percentage": "90.00",
        "execution_frequency": "DAILY",
        "owner": "qa_team",
        "status": "ACTIVE",
    }
    rule_res = client.post("/api/v1/quality/rules", json=rule_payload)
    assert rule_res.status_code == 201
    rule_id = rule_res.json()["data_quality_rule_id"]

    # total_records = 10, passed_records = 8, failed_records = 5 (passed + failed = 13 > 10)
    inconsistent_payload = {
        "data_quality_rule_id": rule_id,
        "total_records": 10,
        "passed_records": 8,
        "failed_records": 5,
        "result_status": "FAILED",
    }
    response = client.post("/api/v1/quality/results", json=inconsistent_payload)
    assert response.status_code == 422

    # Verify no result is created for this rule
    list_res = client.get(f"/api/v1/quality/results?data_quality_rule_id={rule_id}")
    assert list_res.status_code == 200
    assert len(list_res.json()) == 0


def test_data_quality_result_deterministic_quality_percentage(client: TestClient, test_data_asset: dict):
    rule_payload = {
        "rule_code": f"DQ_RES_PCT_{uuid.uuid4().hex[:8].upper()}",
        "rule_name": "Percentage Test Rule",
        "target_data_asset_id": test_data_asset["data_asset_id"],
        "severity": "HIGH",
        "threshold_percentage": "90.00",
        "execution_frequency": "DAILY",
        "owner": "qa_team",
        "status": "ACTIVE",
    }
    rule_res = client.post("/api/v1/quality/rules", json=rule_payload)
    assert rule_res.status_code == 201
    rule_id = rule_res.json()["data_quality_rule_id"]

    # 1. Provide a conflicting client value 12.34; expect calculated value 80.00
    conflicting_payload = {
        "data_quality_rule_id": rule_id,
        "total_records": 100,
        "passed_records": 80,
        "failed_records": 20,
        "quality_percentage": 12.34,
        "result_status": "PASSED",
    }
    res1 = client.post("/api/v1/quality/results", json=conflicting_payload)
    assert res1.status_code == 201
    assert res1.json()["quality_percentage"] == "80.00"

    # 2. Test total_records = 0
    zero_records_payload = {
        "data_quality_rule_id": rule_id,
        "total_records": 0,
        "passed_records": 0,
        "failed_records": 0,
        "result_status": "PASSED",
    }
    res2 = client.post("/api/v1/quality/results", json=zero_records_payload)
    assert res2.status_code == 201
    assert res2.json()["quality_percentage"] == "0.00"


def test_data_quality_result_target_mismatch_rejection_and_omission(
    client: TestClient, test_data_asset: dict, test_column: dict
):
    target_a_id = test_data_asset["data_asset_id"]
    target_b_id = test_column["table_column_id"]

    rule_payload = {
        "rule_code": f"DQ_RES_TGT_{uuid.uuid4().hex[:8].upper()}",
        "rule_name": "Target Mismatch Test Rule",
        "target_data_asset_id": target_a_id,
        "severity": "CRITICAL",
        "threshold_percentage": "95.00",
        "execution_frequency": "DAILY",
        "owner": "qa_team",
        "status": "ACTIVE",
    }
    rule_res = client.post("/api/v1/quality/rules", json=rule_payload)
    assert rule_res.status_code == 201
    rule_id = rule_res.json()["data_quality_rule_id"]

    # 1. Target mismatch (rule target A, result target B) -> 422
    mismatch_payload = {
        "data_quality_rule_id": rule_id,
        "target_data_asset_id": target_b_id,
        "total_records": 100,
        "passed_records": 95,
        "failed_records": 5,
        "result_status": "PASSED",
    }
    mismatch_res = client.post("/api/v1/quality/results", json=mismatch_payload)
    assert mismatch_res.status_code == 422

    # Verify no result was created
    list_res = client.get(f"/api/v1/quality/results?data_quality_rule_id={rule_id}")
    assert list_res.status_code == 200
    assert len(list_res.json()) == 0

    # 2. Target omitted -> uses rule target A
    omitted_payload = {
        "data_quality_rule_id": rule_id,
        "total_records": 100,
        "passed_records": 95,
        "failed_records": 5,
        "result_status": "PASSED",
    }
    omitted_res = client.post("/api/v1/quality/results", json=omitted_payload)
    assert omitted_res.status_code == 201
    assert omitted_res.json()["target_data_asset_id"] == target_a_id

    # 3. Matching target supplied -> succeeds
    matching_payload = {
        "data_quality_rule_id": rule_id,
        "target_data_asset_id": target_a_id,
        "total_records": 50,
        "passed_records": 50,
        "failed_records": 0,
        "result_status": "PASSED",
    }
    matching_res = client.post("/api/v1/quality/results", json=matching_payload)
    assert matching_res.status_code == 201
    assert matching_res.json()["target_data_asset_id"] == target_a_id
