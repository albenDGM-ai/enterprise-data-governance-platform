from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict

from app.schemas.common import APIBaseSchema


class LineageTargetCreate(APIBaseSchema):
    lineage_transformation_id: UUID
    target_name: str
    target_type: str
    system_name: str
    business_domain: str
    owner: str
    status: str


class LineageTargetUpdate(APIBaseSchema):
    lineage_transformation_id: UUID | None = None
    target_name: str | None = None
    target_type: str | None = None
    system_name: str | None = None
    business_domain: str | None = None
    owner: str | None = None
    status: str | None = None


class LineageTargetReplace(APIBaseSchema):
    lineage_transformation_id: UUID
    target_name: str
    target_type: str
    system_name: str
    business_domain: str
    owner: str
    status: str


class LineageTargetResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    lineage_target_id: UUID
    lineage_transformation_id: UUID | None
    target_name: str
    target_type: str
    system_name: str
    business_domain: str
    owner: str
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
