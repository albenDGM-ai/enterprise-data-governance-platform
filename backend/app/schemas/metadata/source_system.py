from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict, Field

from app.schemas.common import APIBaseSchema


class SourceSystemCreate(APIBaseSchema):
    system_code: str = Field(..., min_length=1, max_length=50)
    system_name: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    system_type: str = Field(..., max_length=50)
    vendor: str | None = Field(None, max_length=100)
    business_domain: str = Field(..., max_length=100)
    environment: str = Field(..., max_length=30)
    owner: str = Field(..., max_length=100)
    steward: str = Field(..., max_length=100)
    status: str = Field(..., max_length=30)
    is_active: bool = True


class SourceSystemUpdate(APIBaseSchema):
    system_name: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = None
    system_type: str | None = Field(None, max_length=50)
    vendor: str | None = Field(None, max_length=100)
    business_domain: str | None = Field(None, max_length=100)
    environment: str | None = Field(None, max_length=30)
    owner: str | None = Field(None, max_length=100)
    steward: str | None = Field(None, max_length=100)
    status: str | None = Field(None, max_length=30)
    is_active: bool | None = None


class SourceSystemResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    source_system_id: UUID
    system_code: str
    system_name: str
    description: str | None = None
    system_type: str
    vendor: str | None = None
    business_domain: str
    environment: str
    owner: str
    steward: str
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
