from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict

from app.schemas.common import APIBaseSchema


class LineageTransformationCreate(APIBaseSchema):
    lineage_flow_id: UUID
    sequence_number: int
    transformation_name: str
    transformation_type: str
    description: str | None = None
    expression: str | None = None
    status: str


class LineageTransformationUpdate(APIBaseSchema):
    sequence_number: int | None = None
    transformation_name: str | None = None
    transformation_type: str | None = None
    description: str | None = None
    expression: str | None = None
    status: str | None = None


class LineageTransformationReplace(APIBaseSchema):
    lineage_flow_id: UUID
    sequence_number: int
    transformation_name: str
    transformation_type: str
    description: str | None = None
    expression: str | None = None
    status: str


class LineageTransformationResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    lineage_transformation_id: UUID
    lineage_flow_id: UUID
    sequence_number: int
    transformation_name: str
    transformation_type: str
    description: str | None = None
    expression: str | None = None
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
