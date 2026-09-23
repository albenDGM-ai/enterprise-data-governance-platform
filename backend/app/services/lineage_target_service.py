from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.lineage_target import DataLineageTarget
from app.repositories.lineage_flow_repository import LineageFlowRepository
from app.repositories.lineage_target_repository import LineageTargetRepository
from app.repositories.lineage_transformation_repository import (
    LineageTransformationRepository,
)
from app.services.lineage_validation import LineageRelationshipValidationError


class LineageTargetService:
    """Business operations for Lineage Target."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = LineageTargetRepository(session)
        self.flow_repository = LineageFlowRepository(session)
        self.transformation_repository = LineageTransformationRepository(session)

    def _validate_transformation(
        self,
        lineage_transformation_id: uuid.UUID,
    ) -> None:
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
        flow = self.flow_repository.get_by_id(
            transformation.lineage_flow_id,
            include_inactive=True,
        )
        if flow is None:
            raise LineageRelationshipValidationError(
                "The supplied Lineage Transformation references a missing Lineage Flow."
            )
        if not flow.is_active:
            raise LineageRelationshipValidationError(
                "The supplied Lineage Transformation belongs to an inactive Lineage Flow."
            )

    def get(
        self,
        lineage_target_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageTarget | None:
        return self.repository.get_by_id(
            lineage_target_id,
            include_inactive=include_inactive,
        )

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
        return self.repository.list(
            status=status,
            target_type=target_type,
            system_name=system_name,
            business_domain=business_domain,
            owner=owner,
            include_inactive=include_inactive,
        )

    def create(
        self,
        *,
        lineage_transformation_id: uuid.UUID,
        target_name: str,
        target_type: str,
        system_name: str,
        business_domain: str,
        owner: str,
        status: str,
        created_by: str,
    ) -> DataLineageTarget:
        self._validate_transformation(lineage_transformation_id)

        existing = self.repository.get_by_name(
            target_name,
            system_name,
            include_inactive=True,
        )

        if existing is not None:
            raise ValueError(
                "A Lineage Target with the supplied Target Name and "
                "System Name already exists."
            )

        entity = DataLineageTarget(
            lineage_target_id=uuid.uuid4(),
            lineage_transformation_id=lineage_transformation_id,
            target_name=target_name,
            target_type=target_type,
            system_name=system_name,
            business_domain=business_domain,
            owner=owner,
            status=status,
            created_by=created_by,
            created_date=datetime.now(timezone.utc).replace(tzinfo=None),
            is_active=True,
        )

        self.repository.create(entity)
        return entity

    def update(
        self,
        entity: DataLineageTarget,
        *,
        modified_by: str,
        lineage_transformation_id: uuid.UUID | None = None,
        target_name: str | None = None,
        target_type: str | None = None,
        system_name: str | None = None,
        business_domain: str | None = None,
        owner: str | None = None,
        status: str | None = None,
    ) -> DataLineageTarget:
        new_target_name = target_name if target_name is not None else entity.target_name
        new_system_name = system_name if system_name is not None else entity.system_name

        duplicate = self.repository.get_by_name(
            new_target_name,
            new_system_name,
            include_inactive=True,
        )
        if duplicate is not None and duplicate.lineage_target_id != entity.lineage_target_id:
            raise ValueError(
                "A Lineage Target with the same target name and system name "
                "already exists."
            )

        if lineage_transformation_id is not None:
            self._validate_transformation(lineage_transformation_id)
            entity.lineage_transformation_id = lineage_transformation_id
        if target_name is not None:
            entity.target_name = target_name
        if target_type is not None:
            entity.target_type = target_type
        if system_name is not None:
            entity.system_name = system_name
        if business_domain is not None:
            entity.business_domain = business_domain
        if owner is not None:
            entity.owner = owner
        if status is not None:
            entity.status = status

        entity.modified_by = modified_by
        entity.modified_date = datetime.now(timezone.utc).replace(tzinfo=None)

        self.repository.update(entity)
        return entity

    def delete(
        self,
        entity: DataLineageTarget,
        *,
        modified_by: str,
    ) -> DataLineageTarget:
        return self.repository.soft_delete(
            entity,
            modified_by=modified_by,
        )
