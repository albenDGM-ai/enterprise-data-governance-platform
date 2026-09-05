from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.impact_analysis import ImpactAnalysis
from app.repositories.impact_analysis_repository import ImpactAnalysisRepository
from app.repositories.lineage_mapping_repository import LineageMappingRepository


class ImpactAnalysisService:
    """Business operations for Impact Analysis."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = ImpactAnalysisRepository(session)
        self.mapping_repository = LineageMappingRepository(session)

    def get(
        self,
        impact_analysis_id: uuid.UUID,
    ) -> ImpactAnalysis | None:
        return self.repository.get_by_id(impact_analysis_id)

    def list(
        self,
        *,
        lineage_mapping_id: uuid.UUID | None = None,
        impact_scope: str | None = None,
        status: str | None = None,
        requested_by: str | None = None,
        analysis_date_from: datetime | None = None,
        analysis_date_to: datetime | None = None,
    ) -> list[ImpactAnalysis]:
        return self.repository.list(
            lineage_mapping_id=lineage_mapping_id,
            impact_scope=impact_scope,
            status=status,
            requested_by=requested_by,
            analysis_date_from=analysis_date_from,
            analysis_date_to=analysis_date_to,
        )

    def create(
        self,
        *,
        lineage_mapping_id: uuid.UUID,
        analysis_number: str,
        source_asset: str,
        impact_scope: str,
        affected_objects: int | None,
        analysis_date: datetime,
        requested_by: str,
        status: str,
        created_by: str,
    ) -> ImpactAnalysis:
        mapping = self.mapping_repository.get_by_id(
            lineage_mapping_id,
        )

        if mapping is None:
            raise ValueError(
                "The supplied Lineage Mapping does not exist or is inactive."
            )

        existing = self.repository.get_by_number(
            analysis_number,
        )

        if existing is not None:
            raise ValueError(
                "An Impact Analysis with the supplied Analysis Number "
                "already exists."
            )

        entity = ImpactAnalysis(
            impact_analysis_id=uuid.uuid4(),
            lineage_mapping_id=lineage_mapping_id,
            analysis_number=analysis_number,
            source_asset=source_asset,
            impact_scope=impact_scope,
            affected_objects=affected_objects,
            analysis_date=analysis_date,
            requested_by=requested_by,
            status=status,
            created_by=created_by,
            created_date=datetime.now(timezone.utc).replace(tzinfo=None),
            is_active=True,
        )

        self.repository.create(entity)
        return entity

    def update(
        self,
        entity: ImpactAnalysis,
        *,
        modified_by: str,
        source_asset: str | None = None,
        impact_scope: str | None = None,
        affected_objects: int | None = None,
        analysis_date: datetime | None = None,
        requested_by: str | None = None,
        status: str | None = None,
    ) -> ImpactAnalysis:
        if source_asset is not None:
            entity.source_asset = source_asset
        if impact_scope is not None:
            entity.impact_scope = impact_scope
        if affected_objects is not None:
            entity.affected_objects = affected_objects
        if analysis_date is not None:
            entity.analysis_date = analysis_date
        if requested_by is not None:
            entity.requested_by = requested_by
        if status is not None:
            entity.status = status

        entity.modified_by = modified_by
        entity.modified_date = datetime.now(timezone.utc).replace(tzinfo=None)

        self.repository.update(entity)
        return entity

    def delete(
        self,
        entity: ImpactAnalysis,
    ) -> None:
        self.repository.delete(entity)
