from __future__ import annotations

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lineage_mapping import DataLineageMapping


class LineageMappingRepository:
    """Persistence operations for Lineage Mapping."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        lineage_mapping_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageMapping | None:
        statement = select(DataLineageMapping).where(
            DataLineageMapping.lineage_mapping_id == lineage_mapping_id
        )

        if not include_inactive:
            statement = statement.where(
                DataLineageMapping.is_active.is_(True)
            )

        return self.session.scalar(statement)

    def get_by_attributes(
        self,
        lineage_flow_id: uuid.UUID,
        source_attribute: str,
        target_attribute: str,
        *,
        include_inactive: bool = False,
    ) -> DataLineageMapping | None:
        statement = select(DataLineageMapping).where(
            DataLineageMapping.lineage_flow_id == lineage_flow_id,
            DataLineageMapping.source_attribute == source_attribute,
            DataLineageMapping.target_attribute == target_attribute,
        )

        if not include_inactive:
            statement = statement.where(
                DataLineageMapping.is_active.is_(True)
            )

        return self.session.scalar(statement)

    def list(
        self,
        *,
        lineage_flow_id: uuid.UUID | None = None,
        lineage_transformation_id: uuid.UUID | None = None,
        mapping_type: str | None = None,
        status: str | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageMapping]:
        statement = select(DataLineageMapping)

        if not include_inactive:
            statement = statement.where(
                DataLineageMapping.is_active.is_(True)
            )
        if lineage_flow_id is not None:
            statement = statement.where(
                DataLineageMapping.lineage_flow_id == lineage_flow_id
            )
        if lineage_transformation_id is not None:
            statement = statement.where(
                DataLineageMapping.lineage_transformation_id
                == lineage_transformation_id
            )
        if mapping_type is not None:
            statement = statement.where(
                DataLineageMapping.mapping_type == mapping_type
            )
        if status is not None:
            statement = statement.where(DataLineageMapping.status == status)

        statement = statement.order_by(
            DataLineageMapping.source_attribute,
            DataLineageMapping.target_attribute,
        )

        return list(self.session.scalars(statement).all())

    def create(self, entity: DataLineageMapping) -> DataLineageMapping:
        self.session.add(entity)
        self.session.flush()
        return entity

    def update(self, entity: DataLineageMapping) -> DataLineageMapping:
        self.session.add(entity)
        self.session.flush()
        return entity

    def soft_delete(
        self,
        entity: DataLineageMapping,
        *,
        modified_by: str,
    ) -> DataLineageMapping:
        entity.is_active = False
        entity.modified_by = modified_by
        self.session.add(entity)
        self.session.flush()
        return entity
