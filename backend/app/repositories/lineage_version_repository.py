from __future__ import annotations

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lineage_version import DataLineageVersion


class LineageVersionRepository:
    """Persistence operations for Lineage Version."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        lineage_version_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageVersion | None:
        statement = select(DataLineageVersion).where(
            DataLineageVersion.lineage_version_id == lineage_version_id
        )

        if not include_inactive:
            statement = statement.where(
                DataLineageVersion.is_active.is_(True)
            )

        return self.session.scalar(statement)

    def get_by_flow_and_version(
        self,
        lineage_flow_id: uuid.UUID,
        version_number: str,
        *,
        include_inactive: bool = False,
    ) -> DataLineageVersion | None:
        statement = select(DataLineageVersion).where(
            DataLineageVersion.lineage_flow_id == lineage_flow_id,
            DataLineageVersion.version_number == version_number,
        )

        if not include_inactive:
            statement = statement.where(
                DataLineageVersion.is_active.is_(True)
            )

        return self.session.scalar(statement)

    def list(
        self,
        *,
        lineage_flow_id: uuid.UUID | None = None,
        status: str | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageVersion]:
        statement = select(DataLineageVersion)

        if not include_inactive:
            statement = statement.where(
                DataLineageVersion.is_active.is_(True)
            )
        if lineage_flow_id is not None:
            statement = statement.where(
                DataLineageVersion.lineage_flow_id == lineage_flow_id
            )
        if status is not None:
            statement = statement.where(DataLineageVersion.status == status)

        statement = statement.order_by(
            DataLineageVersion.effective_date.desc(),
            DataLineageVersion.version_number.desc(),
        )

        return list(self.session.scalars(statement).all())

    def create(
        self,
        entity: DataLineageVersion,
    ) -> DataLineageVersion:
        self.session.add(entity)
        self.session.flush()
        return entity

    def update(
        self,
        entity: DataLineageVersion,
    ) -> DataLineageVersion:
        self.session.add(entity)
        self.session.flush()
        return entity

    def archive(
        self,
        entity: DataLineageVersion,
        *,
        modified_by: str,
    ) -> DataLineageVersion:
        entity.is_active = False
        entity.modified_by = modified_by
        self.session.add(entity)
        self.session.flush()
        return entity
