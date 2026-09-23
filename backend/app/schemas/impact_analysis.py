from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict

from app.schemas.common import APIBaseSchema


class ImpactAnalysisCreate(APIBaseSchema):
    lineage_mapping_id: UUID
    analysis_number: str
    source_asset: str
    impact_scope: str
    affected_objects: int
    analysis_date: datetime
    requested_by: str
    status: str


class ImpactAnalysisUpdate(APIBaseSchema):
    source_asset: str | None = None
    impact_scope: str | None = None
    affected_objects: int | None = None
    analysis_date: datetime | None = None
    requested_by: str | None = None
    status: str | None = None


class ImpactAnalysisResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    impact_analysis_id: UUID
    lineage_mapping_id: UUID
    analysis_number: str
    source_asset: str
    impact_scope: str
    affected_objects: int
    analysis_date: datetime
    requested_by: str
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
