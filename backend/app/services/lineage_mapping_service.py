from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.lineage_mapping import DataLineageMapping
from app.repositories.lineage_flow_repository import LineageFlowRepository
from app.repositories.lineage_mapping_repository import LineageMappingRepository
from app.repositories.lineage_target_repository import LineageTargetRepository
from app.repositories.lineage_transformation_repository import (
    LineageTransformationRepository,
)
from app.services.lineage_validation import LineageRelationshipValidationError


class LineageMappingService:
    """Business operations for Lineage Mapping."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = LineageMappingRepository(session)
        self.flow_repository = LineageFlowRepository(session)
        self.target_repository = LineageTargetRepository(session)
        self.transformation_repository = LineageTransformationRepository(session)

    def _validate_relationships(
        self,
        *,
        lineage_flow_id: uuid.UUID,
        lineage_target_id: uuid.UUID | None,
        lineage_transformation_id: uuid.UUID | None,
    ) -> None:
        flow = self.flow_repository.get_by_id(
            lineage_flow_id,
            include_inactive=True,
        )
        if flow is None:
            raise LineageRelationshipValidationError(
                "The supplied Lineage Flow does not exist."
            )
        if not flow.is_active:
            raise LineageRelationshipValidationError(
                "The supplied Lineage Flow is inactive."
            )

        target_transformation = None
        if lineage_target_id is not None:
            target = self.target_repository.get_by_id(
                lineage_target_id,
                include_inactive=True,
            )
            if target is None:
                raise LineageRelationshipValidationError(
                    "The supplied Lineage Target does not exist."
                )
            if not target.is_active:
                raise LineageRelationshipValidationError(
                    "The supplied Lineage Target is inactive."
                )
            if target.lineage_transformation_id is None:
                raise LineageRelationshipValidationError(
                    "The supplied Lineage Target has no Lineage Transformation."
                )

            target_transformation = self.transformation_repository.get_by_id(
                target.lineage_transformation_id,
                include_inactive=True,
            )
            if target_transformation is None:
                raise LineageRelationshipValidationError(
                    "The supplied Lineage Target references a missing Lineage Transformation."
                )
            if not target_transformation.is_active:
                raise LineageRelationshipValidationError(
                    "The supplied Lineage Target references an inactive Lineage Transformation."
                )
            if target_transformation.lineage_flow_id != lineage_flow_id:
                raise LineageRelationshipValidationError(
                    "The supplied Lineage Target belongs to a different Lineage Flow."
                )

        if lineage_transformation_id is not None:
            transformation = self.transformation_repository.get_by_id(
                lineage_transformation_id,
                include_inactive=True,
            )
            if transformation is None:
                raise LineageRelationshipValidationError(
                    "The supplied Lineage Transformation does not exist."
                )
            if not transformation.is_active:
                raise LineageRelationshipValidationError(
                    "The supplied Lineage Transformation is inactive."
                )
            if transformation.lineage_flow_id != lineage_flow_id:
                raise LineageRelationshipValidationError(
                    "The supplied Lineage Transformation belongs to a different Lineage Flow."
                )
            if (
                target_transformation is not None
                and transformation.lineage_transformation_id
                != target_transformation.lineage_transformation_id
            ):
                raise LineageRelationshipValidationError(
                    "The supplied Lineage Transformation does not own the supplied Lineage Target."
                )

    def get(
        self,
        lineage_mapping_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageMapping | None:
        return self.repository.get_by_id(
            lineage_mapping_id,
            include_inactive=include_inactive,
        )

    def get_by_attributes(
        self,
        lineage_flow_id: uuid.UUID,
        source_attribute: str,
        target_attribute: str,
        *,
        include_inactive: bool = False,
    ) -> DataLineageMapping | None:
        return self.repository.get_by_attributes(
            lineage_flow_id,
            source_attribute,
            target_attribute,
            include_inactive=include_inactive,
        )

    def list(
        self,
        *,
        lineage_flow_id: uuid.UUID | None = None,
        lineage_transformation_id: uuid.UUID | None = None,
        mapping_type: str | None = None,
        status: str | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageMapping]:
        return self.repository.list(
            lineage_flow_id=lineage_flow_id,
            lineage_transformation_id=lineage_transformation_id,
            mapping_type=mapping_type,
            status=status,
            include_inactive=include_inactive,
        )

    def create(
        self,
        *,
        lineage_flow_id: uuid.UUID,
        lineage_target_id: uuid.UUID,
        lineage_transformation_id: uuid.UUID | None,
        source_attribute: str,
        target_attribute: str,
        mapping_type: str,
        status: str,
        created_by: str,
    ) -> DataLineageMapping:
        self._validate_relationships(
            lineage_flow_id=lineage_flow_id,
            lineage_target_id=lineage_target_id,
            lineage_transformation_id=lineage_transformation_id,
        )

        existing = self.repository.get_by_attributes(
            lineage_flow_id,
            source_attribute,
            target_attribute,
            include_inactive=True,
        )

        if existing is not None:
            raise ValueError(
                "A Lineage Mapping with the supplied Lineage Flow, "
                "Source Attribute, and Target Attribute already exists."
            )

        entity = DataLineageMapping(
            lineage_mapping_id=uuid.uuid4(),
            lineage_flow_id=lineage_flow_id,
            lineage_target_id=lineage_target_id,
            lineage_transformation_id=lineage_transformation_id,
            source_attribute=source_attribute,
            target_attribute=target_attribute,
            mapping_type=mapping_type,
            status=status,
            created_by=created_by,
            created_date=datetime.now(timezone.utc).replace(tzinfo=None),
            is_active=True,
        )

        self.repository.create(entity)
        return entity

    def update(
        self,
        entity: DataLineageMapping,
        *,
        modified_by: str,
        lineage_flow_id: uuid.UUID | None = None,
        lineage_target_id: uuid.UUID | None = None,
        lineage_transformation_id: uuid.UUID | None = None,
        source_attribute: str | None = None,
        target_attribute: str | None = None,
        mapping_type: str | None = None,
        status: str | None = None,
    ) -> DataLineageMapping:
        new_lineage_flow_id = (
            lineage_flow_id
            if lineage_flow_id is not None
            else entity.lineage_flow_id
        )
        new_lineage_target_id = (
            lineage_target_id
            if lineage_target_id is not None
            else entity.lineage_target_id
        )
        new_lineage_transformation_id = (
            lineage_transformation_id
            if lineage_transformation_id is not None
            else entity.lineage_transformation_id
        )
        self._validate_relationships(
            lineage_flow_id=new_lineage_flow_id,
            lineage_target_id=new_lineage_target_id,
            lineage_transformation_id=new_lineage_transformation_id,
        )

        new_source_attribute = (
            source_attribute
            if source_attribute is not None
            else entity.source_attribute
        )
        new_target_attribute = (
            target_attribute
            if target_attribute is not None
            else entity.target_attribute
        )

        duplicate = self.repository.get_by_attributes(
            new_lineage_flow_id,
            new_source_attribute,
            new_target_attribute,
            include_inactive=True,
        )
        if duplicate is not None and duplicate.lineage_mapping_id != entity.lineage_mapping_id:
            raise ValueError(
                "A Lineage Mapping with the same flow, source attribute, "
                "and target attribute already exists."
            )

        if lineage_flow_id is not None:
            entity.lineage_flow_id = lineage_flow_id
        if lineage_target_id is not None:
            entity.lineage_target_id = lineage_target_id
        if lineage_transformation_id is not None:
            entity.lineage_transformation_id = lineage_transformation_id
        if source_attribute is not None:
            entity.source_attribute = source_attribute
        if target_attribute is not None:
            entity.target_attribute = target_attribute
        if mapping_type is not None:
            entity.mapping_type = mapping_type
        if status is not None:
            entity.status = status

        entity.modified_by = modified_by
        entity.modified_date = datetime.now(timezone.utc).replace(tzinfo=None)

        self.repository.update(entity)
        return entity

    def delete(
        self,
        entity: DataLineageMapping,
        *,
        modified_by: str,
    ) -> DataLineageMapping:
        return self.repository.soft_delete(
            entity,
            modified_by=modified_by,
        )
