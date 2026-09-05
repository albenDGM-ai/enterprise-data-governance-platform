from __future__ import annotations

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lineage_process import DataLineageProcess


class LineageProcessRepository:
    """Persistence operations for Lineage Process."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        lineage_process_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageProcess | None:
        statement = select(DataLineageProcess).where(
            DataLineageProcess.lineage_process_id == lineage_process_id
        )

        if not include_inactive:
            statement = statement.where(DataLineageProcess.is_active.is_(True))

        return self.session.scalar(statement)

    def get_by_name(
        self,
        process_name: str,
        *,
        include_inactive: bool = False,
    ) -> DataLineageProcess | None:
        statement = select(DataLineageProcess).where(
            DataLineageProcess.process_name == process_name
        )

        if not include_inactive:
            statement = statement.where(DataLineageProcess.is_active.is_(True))

        return self.session.scalar(statement)

    def list(
        self,
        *,
        status: str | None = None,
        process_type: str | None = None,
        technology: str | None = None,
        owner: str | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageProcess]:
        statement = select(DataLineageProcess)

        if not include_inactive:
            statement = statement.where(DataLineageProcess.is_active.is_(True))
        if status is not None:
            statement = statement.where(DataLineageProcess.status == status)
        if process_type is not None:
            statement = statement.where(
                DataLineageProcess.process_type == process_type
            )
        if technology is not None:
            statement = statement.where(
                DataLineageProcess.technology == technology
            )
        if owner is not None:
            statement = statement.where(DataLineageProcess.owner == owner)

        statement = statement.order_by(DataLineageProcess.process_name)

        return list(self.session.scalars(statement).all())

    def create(self, entity: DataLineageProcess) -> DataLineageProcess:
        self.session.add(entity)
        self.session.flush()
        return entity

    def update(self, entity: DataLineageProcess) -> DataLineageProcess:
        self.session.add(entity)
        self.session.flush()
        return entity

    def soft_delete(
        self,
        entity: DataLineageProcess,
        *,
        modified_by: str,
    ) -> DataLineageProcess:
        entity.is_active = False
        entity.modified_by = modified_by
        self.session.add(entity)
        self.session.flush()
        return entity
