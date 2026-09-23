from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict

from app.schemas.common import APIBaseSchema


class LineageProcessCreate(APIBaseSchema):
    process_name: str
    process_type: str
    technology: str
    schedule: str | None = None
    owner: str
    status: str


class LineageProcessUpdate(APIBaseSchema):
    process_name: str | None = None
    process_type: str | None = None
    technology: str | None = None
    schedule: str | None = None
    owner: str | None = None
    status: str | None = None


class LineageProcessReplace(APIBaseSchema):
    process_name: str
    process_type: str
    technology: str
    schedule: str | None = None
    owner: str
    status: str


class LineageProcessResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    lineage_process_id: UUID
    process_name: str
    process_type: str
    technology: str
    schedule: str | None = None
    owner: str
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
