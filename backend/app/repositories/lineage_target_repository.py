from __future__ import annotations

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lineage_target import DataLineageTarget


class LineageTargetRepository:
    """Persistence operations for Lineage Target."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        lineage_target_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageTarget | None:
        statement = select(DataLineageTarget).where(
            DataLineageTarget.lineage_target_id == lineage_target_id
        )

        if not include_inactive:
            statement = statement.where(DataLineageTarget.is_active.is_(True))

        return self.session.scalar(statement)

    def get_by_name(
        self,
        target_name: str,
        system_name: str,
        *,
        include_inactive: bool = False,
    ) -> DataLineageTarget | None:
        statement = select(DataLineageTarget).where(
            DataLineageTarget.target_name == target_name,
            DataLineageTarget.system_name == system_name,
        )

        if not include_inactive:
            statement = statement.where(DataLineageTarget.is_active.is_(True))

        return self.session.scalar(statement)

    def list(
        self,
        *,
        status: str | None = None,
        target_type: str | None = None,
        system_name: str | None = None,
        business_domain: str | None = None,
        owner: str | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageTarget]:
        statement = select(DataLineageTarget)

        if not include_inactive:
            statement = statement.where(DataLineageTarget.is_active.is_(True))
        if status is not None:
            statement = statement.where(DataLineageTarget.status == status)
        if target_type is not None:
            statement = statement.where(
                DataLineageTarget.target_type == target_type
            )
        if system_name is not None:
            statement = statement.where(
                DataLineageTarget.system_name == system_name
            )
        if business_domain is not None:
            statement = statement.where(
                DataLineageTarget.business_domain == business_domain
            )
        if owner is not None:
            statement = statement.where(DataLineageTarget.owner == owner)

        statement = statement.order_by(DataLineageTarget.target_name)

        return list(self.session.scalars(statement).all())

    def create(self, entity: DataLineageTarget) -> DataLineageTarget:
        self.session.add(entity)
        self.session.flush()
        return entity

    def update(self, entity: DataLineageTarget) -> DataLineageTarget:
        self.session.add(entity)
        self.session.flush()
        return entity

    def soft_delete(
        self,
        entity: DataLineageTarget,
        *,
        modified_by: str,
    ) -> DataLineageTarget:
        entity.is_active = False
        entity.modified_by = modified_by
        self.session.add(entity)
        self.session.flush()
        return entity
