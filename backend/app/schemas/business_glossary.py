from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict, Field

from app.schemas.common import APIBaseSchema


class BusinessTermCreate(APIBaseSchema):
    business_category_id: UUID
    business_term_name: str = Field(..., min_length=1, max_length=255)
    display_name: str = Field(..., min_length=1, max_length=255)
    preferred_definition: str = Field(..., min_length=1)
    business_domain: str = Field(..., min_length=1, max_length=100)
    business_capability: str | None = Field(None, max_length=100)
    owner: str = Field(..., min_length=1, max_length=100)
    steward: str = Field(..., min_length=1, max_length=100)
    classification: str | None = Field(None, max_length=50)
    status: str = Field("Active", min_length=1, max_length=30)
    data_asset_id: UUID | None = None
    is_active: bool = True


class BusinessTermResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    business_term_id: UUID
    business_category_id: UUID
    data_asset_id: UUID | None = None
    business_term_name: str
    display_name: str
    preferred_definition: str
    business_domain: str
    business_capability: str | None = None
    owner: str
    steward: str
    classification: str | None = None
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
