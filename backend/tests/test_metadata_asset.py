import uuid
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.models.metadata.data_asset import DataAsset
from app.models.metadata.source_system import SourceSystem
from app.main import app

def test_create_data_asset(client: TestClient, db: Session):
    asset_identifier = str(uuid.uuid4())
    payload = {
        "asset_type": "table",
        "asset_identifier": asset_identifier,
        "asset_name": "users_table",
        "display_name": "Users Table",
        "description": "Stores user information",
        "business_domain": "HR",
        "owner": "data_engineering",
        "steward": "jane_doe",
        "classification": "confidential",
        "critical_data_element_flag": True,
        "status": "active",
        "is_active": True
    }

    response = client.post("/api/v1/metadata/data-assets", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["asset_name"] == "users_table"
    assert data["business_domain"] == "HR"
    assert "data_asset_id" in data

    # check db
    asset_id = uuid.UUID(data["data_asset_id"])
    db_asset = db.query(DataAsset).filter(DataAsset.data_asset_id == asset_id).first()
    assert db_asset is not None
    assert db_asset.asset_name == "users_table"
    assert db_asset.business_domain == "HR"

def test_create_data_asset_with_source_system(client: TestClient, db: Session):
    # Create a source system first
    source_system_id = uuid.uuid4()
    source_system = SourceSystem(
        source_system_id=source_system_id,
        system_code="HR_SYS",
        system_name="HR System",
        system_type="RDBMS",
        business_domain="HR",
        environment="PROD",
        owner="admin",
        steward="admin",
        status="active",
        created_by="test",
        created_date=__import__('datetime').datetime.now()
    )
    db.add(source_system)
    db.commit()

    asset_identifier = str(uuid.uuid4())
    payload = {
        "asset_type": "table",
        "asset_identifier": asset_identifier,
        "asset_name": "employees_table",
        "display_name": "Employees Table",
        "description": "Stores employee information",
        "business_domain": "HR",
        "source_system_id": str(source_system_id),
        "owner": "data_engineering",
        "steward": "jane_doe",
        "classification": "confidential",
        "critical_data_element_flag": True,
        "status": "active",
        "is_active": True
    }

    response = client.post("/api/v1/metadata/data-assets", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["source_system_id"] == str(source_system_id)

    # check db
    asset_id = uuid.UUID(data["data_asset_id"])
    db_asset = db.query(DataAsset).filter(DataAsset.data_asset_id == asset_id).first()
    assert db_asset is not None
    assert str(db_asset.source_system_id) == str(source_system_id)

    # Check retrieval returns it
    get_response = client.get(f"/api/v1/metadata/data-assets/{asset_id}")
    assert get_response.status_code == 200
    assert get_response.json()["source_system_id"] == str(source_system_id)

def test_create_data_asset_duplicate(client: TestClient, db: Session):
    asset_identifier = str(uuid.uuid4())
    payload = {
        "asset_type": "table",
        "asset_identifier": asset_identifier,
        "asset_name": "users_table",
        "display_name": "Users Table",
        "description": "Stores user information",
        "business_domain": "HR",
        "owner": "data_engineering",
        "steward": "jane_doe",
        "classification": "confidential",
        "critical_data_element_flag": True,
        "status": "active",
        "is_active": True
    }

    # First creation should succeed
    response = client.post("/api/v1/metadata/data-assets", json=payload)
    assert response.status_code == 201

    # Second creation should fail with conflict
    response2 = client.post("/api/v1/metadata/data-assets", json=payload)
    assert response2.status_code == 409

def test_create_data_asset_invalid(client: TestClient):
    asset_identifier = str(uuid.uuid4())
    payload = {
        "asset_type": "table",
        "asset_identifier": asset_identifier,
        "asset_name": "", # empty asset_name should fail validation
        "display_name": "Users Table",
        "description": "Stores user information",
        "business_domain": "HR",
        "owner": "data_engineering",
        "steward": "jane_doe",
        "classification": "confidential",
        "critical_data_element_flag": True,
        "status": "active",
        "is_active": True
    }

    response = client.post("/api/v1/metadata/data-assets", json=payload)
    assert response.status_code == 422 # Unprocessable Entity

def test_get_data_asset(client: TestClient, db: Session):
    asset_identifier = str(uuid.uuid4())
    payload = {
        "asset_type": "view",
        "asset_identifier": asset_identifier,
        "asset_name": "active_users_view",
        "display_name": "Active Users View",
        "description": "View of active users",
        "business_domain": "HR",
        "owner": "analytics",
        "steward": "john_doe",
        "classification": "public",
        "critical_data_element_flag": False,
        "status": "active",
        "is_active": True
    }

    create_response = client.post("/api/v1/metadata/data-assets", json=payload)
    assert create_response.status_code == 201
    created_data = create_response.json()
    asset_id = created_data["data_asset_id"]

    get_response = client.get(f"/api/v1/metadata/data-assets/{asset_id}")
    assert get_response.status_code == 200

    data = get_response.json()
    assert data["data_asset_id"] == asset_id
    assert data["asset_name"] == "active_users_view"
    assert data["business_domain"] == "HR"

def test_get_data_asset_not_found(client: TestClient):
    random_id = str(uuid.uuid4())
    response = client.get(f"/api/v1/metadata/data-assets/{random_id}")
    assert response.status_code == 404

def test_list_data_assets(client: TestClient, db: Session):
    asset_identifier = str(uuid.uuid4())
    payload = {
        "asset_type": "file",
        "asset_identifier": asset_identifier,
        "asset_name": "data_dump.csv",
        "display_name": "Data Dump CSV",
        "description": "Monthly data dump",
        "business_domain": "Finance",
        "owner": "admin",
        "steward": "admin",
        "classification": "internal",
        "critical_data_element_flag": False,
        "status": "archived",
        "is_active": True
    }

    client.post("/api/v1/metadata/data-assets", json=payload)

    response = client.get("/api/v1/metadata/data-assets")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

    # Ensure our created asset is in the list
    found = any(asset["asset_identifier"] == asset_identifier for asset in data)
    assert found