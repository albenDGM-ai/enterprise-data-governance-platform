from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.impact_analysis import ImpactAnalysis


class ImpactAnalysisRepository:
    """Persistence operations for Impact Analysis."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        impact_analysis_id: uuid.UUID,
    ) -> ImpactAnalysis | None:
        statement = select(ImpactAnalysis).where(
            ImpactAnalysis.impact_analysis_id == impact_analysis_id
        )
        return self.session.scalar(statement)

    def get_by_number(
        self,
        analysis_number: str,
    ) -> ImpactAnalysis | None:
        statement = select(ImpactAnalysis).where(
            ImpactAnalysis.analysis_number == analysis_number
        )
        return self.session.scalar(statement)

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
        statement = select(ImpactAnalysis)

        if lineage_mapping_id is not None:
            statement = statement.where(
                ImpactAnalysis.lineage_mapping_id == lineage_mapping_id
            )
        if impact_scope is not None:
            statement = statement.where(
                ImpactAnalysis.impact_scope == impact_scope
            )
        if status is not None:
            statement = statement.where(ImpactAnalysis.status == status)
        if requested_by is not None:
            statement = statement.where(
                ImpactAnalysis.requested_by == requested_by
            )
        if analysis_date_from is not None:
            statement = statement.where(
                ImpactAnalysis.analysis_date >= analysis_date_from
            )
        if analysis_date_to is not None:
            statement = statement.where(
                ImpactAnalysis.analysis_date <= analysis_date_to
            )

        statement = statement.order_by(ImpactAnalysis.analysis_date.desc())

        return list(self.session.scalars(statement).all())

    def create(self, entity: ImpactAnalysis) -> ImpactAnalysis:
        self.session.add(entity)
        self.session.flush()
        return entity

    def update(self, entity: ImpactAnalysis) -> ImpactAnalysis:
        self.session.add(entity)
        self.session.flush()
        return entity

    def delete(self, entity: ImpactAnalysis) -> None:
        self.session.delete(entity)
        self.session.flush()
