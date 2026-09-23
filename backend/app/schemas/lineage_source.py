from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict

from app.schemas.common import APIBaseSchema


class LineageSourceCreate(APIBaseSchema):
    source_name: str
    source_type: str
    system_name: str
    business_domain: str
    owner: str
    status: str


class LineageSourceUpdate(APIBaseSchema):
    source_name: str | None = None
    source_type: str | None = None
    system_name: str | None = None
    business_domain: str | None = None
    owner: str | None = None
    status: str | None = None


class LineageSourceReplace(APIBaseSchema):
    source_name: str
    source_type: str
    system_name: str
    business_domain: str
    owner: str
    status: str


class LineageSourceResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    lineage_source_id: UUID
    source_name: str
    source_type: str
    system_name: str
    business_domain: str
    owner: str
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
