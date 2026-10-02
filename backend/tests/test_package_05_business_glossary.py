import uuid
from datetime import datetime, timezone
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models.business_glossary.business_glossary import BusinessGlossary
from app.models.business_glossary.business_category import BusinessCategory


@pytest.fixture
def test_category(db: Session):
    """Fixture to create a parent BusinessGlossary and BusinessCategory for testing."""
    glossary = BusinessGlossary(
        business_glossary_id=uuid.uuid4(),
        glossary_name=f"Enterprise Glossary {uuid.uuid4().hex[:8]}",
        display_name="Enterprise Glossary",
        description="Test Glossary",
        version="1.0",
        status="Active",
        owner="enterprise_owner",
        steward="enterprise_steward",
        created_by="system",
        created_date=datetime.now(timezone.utc),
        is_active=True,
    )
    db.add(glossary)
    db.flush()

    category = BusinessCategory(
        business_category_id=uuid.uuid4(),
        business_glossary_id=glossary.business_glossary_id,
        category_name=f"Finance Category {uuid.uuid4().hex[:8]}",
        display_name="Finance Category",
        description="Finance terms category",
        owner="finance_owner",
        steward="finance_steward",
        status="Active",
        created_by="system",
        created_date=datetime.now(timezone.utc),
        is_active=True,
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def test_business_term_creation_and_retrieval(client: TestClient, test_category: BusinessCategory):
    term_name = f"Term_{uuid.uuid4().hex[:8]}"
    payload = {
        "business_category_id": str(test_category.business_category_id),
        "business_term_name": term_name,
        "display_name": "Net Revenue",
        "preferred_definition": "Total sales revenue minus discounts, returns, and allowances.",
        "business_domain": "Finance",
        "business_capability": "Financial Reporting",
        "owner": "finance_lead",
        "steward": "revenue_steward",
        "classification": "Internal",
        "status": "Active",
        "is_active": True,
    }

    response = client.post("/api/v1/glossary/terms", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["business_term_name"] == term_name
    assert data["business_category_id"] == str(test_category.business_category_id)
    assert data["data_asset_id"] is None
    assert "business_term_id" in data

    term_id = data["business_term_id"]

    # Retrieval by ID
    get_res = client.get(f"/api/v1/glossary/terms/{term_id}")
    assert get_res.status_code == 200
    assert get_res.json()["display_name"] == "Net Revenue"

    # List
    list_res = client.get("/api/v1/glossary/terms")
    assert list_res.status_code == 200
    terms = list_res.json()
    assert any(t["business_term_id"] == term_id for t in terms)


def test_business_term_creation_with_data_asset(client: TestClient, test_category: BusinessCategory):
    # Create Data Asset first
    asset_payload = {
        "asset_type": "table",
        "asset_identifier": str(uuid.uuid4()),
        "asset_name": f"ledger_{uuid.uuid4().hex[:8]}",
        "display_name": "Ledger Table Asset",
        "business_domain": "Finance",
        "owner": "finance_lead",
        "steward": "finance_steward",
        "classification": "restricted",
        "critical_data_element_flag": True,
        "status": "active",
        "is_active": True,
    }
    asset_res = client.post("/api/v1/metadata/data-assets", json=asset_payload)
    assert asset_res.status_code == 201
    asset_id = asset_res.json()["data_asset_id"]

    # Create Business Term linked to Data Asset
    term_name = f"Term_Asset_{uuid.uuid4().hex[:8]}"
    term_payload = {
        "business_category_id": str(test_category.business_category_id),
        "data_asset_id": asset_id,
        "business_term_name": term_name,
        "display_name": "Gross Margin",
        "preferred_definition": "Gross profit divided by net sales.",
        "business_domain": "Finance",
        "owner": "finance_lead",
        "steward": "margin_steward",
        "status": "Active",
    }
    term_res = client.post("/api/v1/glossary/terms", json=term_payload)
    assert term_res.status_code == 201
    term_data = term_res.json()
    assert term_data["data_asset_id"] == asset_id

    # List terms filtered by data_asset_id
    list_res = client.get(f"/api/v1/glossary/terms?data_asset_id={asset_id}")
    assert list_res.status_code == 200
    filtered_terms = list_res.json()
    assert len(filtered_terms) == 1
    assert filtered_terms[0]["business_term_id"] == term_data["business_term_id"]


def test_business_term_duplicate_handling(client: TestClient, test_category: BusinessCategory):
    term_name = f"Term_Dup_{uuid.uuid4().hex[:8]}"
    payload = {
        "business_category_id": str(test_category.business_category_id),
        "business_term_name": term_name,
        "display_name": "Operating Income",
        "preferred_definition": "Earnings before interest and taxes.",
        "business_domain": "Finance",
        "owner": "finance_lead",
        "steward": "steward",
        "status": "Active",
    }

    res1 = client.post("/api/v1/glossary/terms", json=payload)
    assert res1.status_code == 201

    res2 = client.post("/api/v1/glossary/terms", json=payload)
    assert res2.status_code == 409
    assert "already exists" in res2.json()["detail"]


def test_business_term_validation_failure(client: TestClient, test_category: BusinessCategory):
    # Empty term name
    payload = {
        "business_category_id": str(test_category.business_category_id),
        "business_term_name": "",
        "display_name": "Test Term",
        "preferred_definition": "Definition",
        "business_domain": "Finance",
        "owner": "owner",
        "steward": "steward",
        "status": "Active",
    }
    response = client.post("/api/v1/glossary/terms", json=payload)
    assert response.status_code == 422


def test_business_term_not_found(client: TestClient):
    fake_id = str(uuid.uuid4())
    get_res = client.get(f"/api/v1/glossary/terms/{fake_id}")
    assert get_res.status_code == 404
    assert f"BusinessTerm with id {fake_id} not found" in get_res.json()["detail"]


def test_business_term_invalid_category_rejection(client: TestClient):
    fake_category_id = str(uuid.uuid4())
    payload = {
        "business_category_id": fake_category_id,
        "business_term_name": "Orphan Term",
        "display_name": "Orphan Term",
        "preferred_definition": "A term without a valid category",
        "business_domain": "General",
        "owner": "owner",
        "steward": "steward",
        "status": "Active",
    }
    response = client.post("/api/v1/glossary/terms", json=payload)
    assert response.status_code == 404
    assert f"BusinessCategory with id {fake_category_id} not found" in response.json()["detail"]


def test_business_term_invalid_data_asset_rejection(client: TestClient, test_category: BusinessCategory):
    fake_asset_id = str(uuid.uuid4())
    payload = {
        "business_category_id": str(test_category.business_category_id),
        "data_asset_id": fake_asset_id,
        "business_term_name": f"Invalid_Asset_Term_{uuid.uuid4().hex[:8]}",
        "display_name": "Invalid Asset Term",
        "preferred_definition": "A term referencing a fake data asset",
        "business_domain": "General",
        "owner": "owner",
        "steward": "steward",
        "status": "Active",
    }
    response = client.post("/api/v1/glossary/terms", json=payload)
    assert response.status_code == 404
    assert f"DataAsset with id {fake_asset_id} not found" in response.json()["detail"]
