from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict

from app.schemas.common import APIBaseSchema


class LineageSnapshotCreate(APIBaseSchema):
    lineage_flow_id: UUID
    snapshot_name: str
    snapshot_date: datetime
    status: str


class LineageSnapshotUpdate(APIBaseSchema):
    lineage_flow_id: UUID | None = None
    snapshot_name: str | None = None
    snapshot_date: datetime | None = None
    status: str | None = None


class LineageSnapshotReplace(APIBaseSchema):
    lineage_flow_id: UUID
    snapshot_name: str
    snapshot_date: datetime
    status: str


class LineageSnapshotResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    lineage_snapshot_id: UUID
    lineage_flow_id: UUID
    snapshot_name: str
    snapshot_date: datetime
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
