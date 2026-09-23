from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict

from app.schemas.common import APIBaseSchema


class LineageFlowCreate(APIBaseSchema):
    lineage_source_id: UUID
    lineage_process_id: UUID
    flow_name: str
    flow_type: str
    direction: str
    frequency: str
    owner: str
    status: str


class LineageFlowUpdate(APIBaseSchema):
    lineage_source_id: UUID | None = None
    lineage_process_id: UUID | None = None
    flow_name: str | None = None
    flow_type: str | None = None
    direction: str | None = None
    frequency: str | None = None
    owner: str | None = None
    status: str | None = None


class LineageFlowReplace(APIBaseSchema):
    lineage_source_id: UUID
    lineage_process_id: UUID
    flow_name: str
    flow_type: str
    direction: str
    frequency: str
    owner: str
    status: str


class LineageFlowResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    lineage_flow_id: UUID
    lineage_source_id: UUID
    lineage_process_id: UUID
    flow_name: str
    flow_type: str
    direction: str
    frequency: str
    owner: str
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
