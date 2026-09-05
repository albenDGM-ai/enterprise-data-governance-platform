from __future__ import annotations

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lineage_flow import DataLineageFlow


class LineageFlowRepository:
    """Persistence operations for Lineage Flow."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        lineage_flow_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageFlow | None:
        statement = select(DataLineageFlow).where(
            DataLineageFlow.lineage_flow_id == lineage_flow_id
        )

        if not include_inactive:
            statement = statement.where(DataLineageFlow.is_active.is_(True))

        return self.session.scalar(statement)

    def get_by_name(
        self,
        flow_name: str,
        *,
        include_inactive: bool = False,
    ) -> DataLineageFlow | None:
        statement = select(DataLineageFlow).where(
            DataLineageFlow.flow_name == flow_name
        )

        if not include_inactive:
            statement = statement.where(DataLineageFlow.is_active.is_(True))

        return self.session.scalar(statement)

    def list(
        self,
        *,
        status: str | None = None,
        flow_type: str | None = None,
        direction: str | None = None,
        owner: str | None = None,
        lineage_source_id: uuid.UUID | None = None,
        lineage_process_id: uuid.UUID | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageFlow]:
        statement = select(DataLineageFlow)

        if not include_inactive:
            statement = statement.where(DataLineageFlow.is_active.is_(True))
        if status is not None:
            statement = statement.where(DataLineageFlow.status == status)
        if flow_type is not None:
            statement = statement.where(DataLineageFlow.flow_type == flow_type)
        if direction is not None:
            statement = statement.where(DataLineageFlow.direction == direction)
        if owner is not None:
            statement = statement.where(DataLineageFlow.owner == owner)
        if lineage_source_id is not None:
            statement = statement.where(
                DataLineageFlow.lineage_source_id == lineage_source_id
            )
        if lineage_process_id is not None:
            statement = statement.where(
                DataLineageFlow.lineage_process_id == lineage_process_id
            )

        statement = statement.order_by(DataLineageFlow.flow_name)

        return list(self.session.scalars(statement).all())

    def create(self, entity: DataLineageFlow) -> DataLineageFlow:
        self.session.add(entity)
        self.session.flush()
        return entity

    def update(self, entity: DataLineageFlow) -> DataLineageFlow:
        self.session.add(entity)
        self.session.flush()
        return entity

    def soft_delete(
        self,
        entity: DataLineageFlow,
        *,
        modified_by: str,
    ) -> DataLineageFlow:
        entity.is_active = False
        entity.modified_by = modified_by
        self.session.add(entity)
        self.session.flush()
        return entity
