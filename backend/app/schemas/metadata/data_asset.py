from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict, Field

from app.schemas.common import APIBaseSchema


class DataAssetCreate(APIBaseSchema):
    asset_type: str = Field(..., max_length=30)
    asset_identifier: UUID
    asset_name: str = Field(..., min_length=1, max_length=255)
    display_name: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    business_domain: str = Field(..., max_length=100)
    source_system_id: UUID | None = None
    owner: str = Field(..., max_length=100)
    steward: str = Field(..., max_length=100)
    classification: str = Field(..., max_length=50)
    critical_data_element_flag: bool
    status: str = Field(..., max_length=30)
    is_active: bool = True


class DataAssetResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    data_asset_id: UUID
    asset_type: str
    asset_identifier: UUID
    asset_name: str
    display_name: str
    description: str | None = None
    business_domain: str
    source_system_id: UUID | None = None
    owner: str
    steward: str
    classification: str
    critical_data_element_flag: bool
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
