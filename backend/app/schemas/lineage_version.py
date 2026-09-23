from datetime import date, datetime
from uuid import UUID

from pydantic import ConfigDict

from app.schemas.common import APIBaseSchema


class LineageVersionCreate(APIBaseSchema):
    lineage_flow_id: UUID
    version_number: str
    change_summary: str
    effective_date: date
    approved_by: str
    status: str


class LineageVersionUpdate(APIBaseSchema):
    lineage_flow_id: UUID | None = None
    version_number: str | None = None
    change_summary: str | None = None
    effective_date: date | None = None
    approved_by: str | None = None
    status: str | None = None


class LineageVersionReplace(APIBaseSchema):
    lineage_flow_id: UUID
    version_number: str
    change_summary: str
    effective_date: date
    approved_by: str
    status: str


class LineageVersionResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    lineage_version_id: UUID
    lineage_flow_id: UUID
    version_number: str
    change_summary: str
    effective_date: date
    approved_by: str
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
