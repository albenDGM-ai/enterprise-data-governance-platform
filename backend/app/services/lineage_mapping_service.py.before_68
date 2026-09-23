from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.lineage_mapping import DataLineageMapping
from app.repositories.lineage_mapping_repository import LineageMappingRepository


class LineageMappingService:
    """Business operations for Lineage Mapping."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = LineageMappingRepository(session)

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
        lineage_transformation_id: uuid.UUID | None,
        source_attribute: str,
        target_attribute: str,
        mapping_type: str,
        status: str,
        created_by: str,
    ) -> DataLineageMapping:
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
        lineage_transformation_id: uuid.UUID | None = None,
        source_attribute: str | None = None,
        target_attribute: str | None = None,
        mapping_type: str | None = None,
        status: str | None = None,
    ) -> DataLineageMapping:
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
            entity.lineage_flow_id,
            new_source_attribute,
            new_target_attribute,
            include_inactive=True,
        )
        if duplicate is not None and duplicate.lineage_mapping_id != entity.lineage_mapping_id:
            raise ValueError(
                "A Lineage Mapping with the same flow, source attribute, "
                "and target attribute already exists."
            )

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
