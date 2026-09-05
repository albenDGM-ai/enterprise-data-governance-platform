from __future__ import annotations

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lineage_source import DataLineageSource


class LineageSourceRepository:
    """Persistence operations for Lineage Source."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        lineage_source_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageSource | None:
        statement = select(DataLineageSource).where(
            DataLineageSource.lineage_source_id == lineage_source_id
        )

        if not include_inactive:
            statement = statement.where(DataLineageSource.is_active.is_(True))

        return self.session.scalar(statement)

    def get_by_name(
        self,
        source_name: str,
        system_name: str,
        *,
        include_inactive: bool = False,
    ) -> DataLineageSource | None:
        statement = select(DataLineageSource).where(
            DataLineageSource.source_name == source_name,
            DataLineageSource.system_name == system_name,
        )

        if not include_inactive:
            statement = statement.where(DataLineageSource.is_active.is_(True))

        return self.session.scalar(statement)

    def list(
        self,
        *,
        status: str | None = None,
        source_type: str | None = None,
        system_name: str | None = None,
        business_domain: str | None = None,
        owner: str | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageSource]:
        statement = select(DataLineageSource)

        if not include_inactive:
            statement = statement.where(DataLineageSource.is_active.is_(True))

        if status is not None:
            statement = statement.where(DataLineageSource.status == status)

        if source_type is not None:
            statement = statement.where(
                DataLineageSource.source_type == source_type
            )

        if system_name is not None:
            statement = statement.where(
                DataLineageSource.system_name == system_name
            )

        if business_domain is not None:
            statement = statement.where(
                DataLineageSource.business_domain == business_domain
            )

        if owner is not None:
            statement = statement.where(DataLineageSource.owner == owner)

        statement = statement.order_by(DataLineageSource.source_name)

        return list(self.session.scalars(statement).all())

    def create(self, entity: DataLineageSource) -> DataLineageSource:
        self.session.add(entity)
        self.session.flush()
        return entity

    def update(self, entity: DataLineageSource) -> DataLineageSource:
        self.session.add(entity)
        self.session.flush()
        return entity

    def soft_delete(
        self,
        entity: DataLineageSource,
        *,
        modified_by: str,
    ) -> DataLineageSource:
        entity.is_active = False
        entity.modified_by = modified_by
        self.session.add(entity)
        self.session.flush()
        return entity
