from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.lineage_transformation import DataLineageTransformation
from app.repositories.lineage_transformation_repository import (
    LineageTransformationRepository,
)


class LineageTransformationService:
    """Business operations for Lineage Transformation."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = LineageTransformationRepository(session)

    def get(
        self,
        lineage_transformation_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageTransformation | None:
        return self.repository.get_by_id(
            lineage_transformation_id,
            include_inactive=include_inactive,
        )

    def get_by_flow_and_sequence(
        self,
        lineage_flow_id: uuid.UUID,
        sequence_number: int,
        *,
        include_inactive: bool = False,
    ) -> DataLineageTransformation | None:
        return self.repository.get_by_flow_and_sequence(
            lineage_flow_id,
            sequence_number,
            include_inactive=include_inactive,
        )

    def list(
        self,
        *,
        lineage_flow_id: uuid.UUID | None = None,
        transformation_type: str | None = None,
        status: str | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageTransformation]:
        return self.repository.list(
            lineage_flow_id=lineage_flow_id,
            transformation_type=transformation_type,
            status=status,
            include_inactive=include_inactive,
        )

    def create(
        self,
        *,
        lineage_flow_id: uuid.UUID,
        sequence_number: int,
        transformation_name: str,
        transformation_type: str,
        description: str | None,
        expression: str | None,
        status: str,
        created_by: str,
    ) -> DataLineageTransformation:
        existing = self.repository.get_by_flow_and_sequence(
            lineage_flow_id,
            sequence_number,
            include_inactive=True,
        )

        if existing is not None:
            raise ValueError(
                "A Lineage Transformation with the supplied Lineage Flow "
                "and Sequence Number already exists."
            )

        entity = DataLineageTransformation(
            lineage_transformation_id=uuid.uuid4(),
            lineage_flow_id=lineage_flow_id,
            sequence_number=sequence_number,
            transformation_name=transformation_name,
            transformation_type=transformation_type,
            description=description,
            expression=expression,
            status=status,
            created_by=created_by,
            created_date=datetime.now(timezone.utc).replace(tzinfo=None),
            is_active=True,
        )

        self.repository.create(entity)
        return entity

    def update(
        self,
        entity: DataLineageTransformation,
        *,
        modified_by: str,
        sequence_number: int | None = None,
        transformation_name: str | None = None,
        transformation_type: str | None = None,
        description: str | None = None,
        expression: str | None = None,
        status: str | None = None,
    ) -> DataLineageTransformation:
        new_sequence_number = (
            sequence_number
            if sequence_number is not None
            else entity.sequence_number
        )

        duplicate = self.repository.get_by_flow_and_sequence(
            entity.lineage_flow_id,
            new_sequence_number,
            include_inactive=True,
        )
        if duplicate is not None and duplicate.lineage_transformation_id != entity.lineage_transformation_id:
            raise ValueError(
                "A Lineage Transformation with the same flow and sequence "
                "number already exists."
            )

        if sequence_number is not None:
            entity.sequence_number = sequence_number
        if transformation_name is not None:
            entity.transformation_name = transformation_name
        if transformation_type is not None:
            entity.transformation_type = transformation_type
        if description is not None:
            entity.description = description
        if expression is not None:
            entity.expression = expression
        if status is not None:
            entity.status = status

        entity.modified_by = modified_by
        entity.modified_date = datetime.now(timezone.utc).replace(tzinfo=None)

        self.repository.update(entity)
        return entity

    def delete(
        self,
        entity: DataLineageTransformation,
        *,
        modified_by: str,
    ) -> DataLineageTransformation:
        return self.repository.soft_delete(
            entity,
            modified_by=modified_by,
        )
