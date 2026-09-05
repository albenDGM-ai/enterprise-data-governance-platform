from __future__ import annotations

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lineage_transformation import DataLineageTransformation


class LineageTransformationRepository:
    """Persistence operations for Lineage Transformation."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        lineage_transformation_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageTransformation | None:
        statement = select(DataLineageTransformation).where(
            DataLineageTransformation.lineage_transformation_id
            == lineage_transformation_id
        )

        if not include_inactive:
            statement = statement.where(
                DataLineageTransformation.is_active.is_(True)
            )

        return self.session.scalar(statement)

    def get_by_flow_and_sequence(
        self,
        lineage_flow_id: uuid.UUID,
        sequence_number: int,
        *,
        include_inactive: bool = False,
    ) -> DataLineageTransformation | None:
        statement = select(DataLineageTransformation).where(
            DataLineageTransformation.lineage_flow_id == lineage_flow_id,
            DataLineageTransformation.sequence_number == sequence_number,
        )

        if not include_inactive:
            statement = statement.where(
                DataLineageTransformation.is_active.is_(True)
            )

        return self.session.scalar(statement)

    def list(
        self,
        *,
        lineage_flow_id: uuid.UUID | None = None,
        transformation_type: str | None = None,
        status: str | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageTransformation]:
        statement = select(DataLineageTransformation)

        if not include_inactive:
            statement = statement.where(
                DataLineageTransformation.is_active.is_(True)
            )
        if lineage_flow_id is not None:
            statement = statement.where(
                DataLineageTransformation.lineage_flow_id == lineage_flow_id
            )
        if transformation_type is not None:
            statement = statement.where(
                DataLineageTransformation.transformation_type
                == transformation_type
            )
        if status is not None:
            statement = statement.where(
                DataLineageTransformation.status == status
            )

        statement = statement.order_by(
            DataLineageTransformation.sequence_number
        )

        return list(self.session.scalars(statement).all())

    def create(
        self,
        entity: DataLineageTransformation,
    ) -> DataLineageTransformation:
        self.session.add(entity)
        self.session.flush()
        return entity

    def update(
        self,
        entity: DataLineageTransformation,
    ) -> DataLineageTransformation:
        self.session.add(entity)
        self.session.flush()
        return entity

    def soft_delete(
        self,
        entity: DataLineageTransformation,
        *,
        modified_by: str,
    ) -> DataLineageTransformation:
        entity.is_active = False
        entity.modified_by = modified_by
        self.session.add(entity)
        self.session.flush()
        return entity
