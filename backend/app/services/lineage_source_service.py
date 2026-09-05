from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.lineage_source import DataLineageSource
from app.repositories.lineage_source_repository import LineageSourceRepository


class LineageSourceService:
    """Business operations for Lineage Source."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = LineageSourceRepository(session)

    def get(
        self,
        lineage_source_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageSource | None:
        return self.repository.get_by_id(
            lineage_source_id,
            include_inactive=include_inactive,
        )

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
        return self.repository.list(
            status=status,
            source_type=source_type,
            system_name=system_name,
            business_domain=business_domain,
            owner=owner,
            include_inactive=include_inactive,
        )

    def create(
        self,
        *,
        source_name: str,
        source_type: str,
        system_name: str,
        business_domain: str,
        owner: str,
        status: str,
        created_by: str,
    ) -> DataLineageSource:
        existing = self.repository.get_by_name(
            source_name,
            system_name,
            include_inactive=True,
        )

        if existing is not None:
            raise ValueError(
                "A Lineage Source with the supplied Source Name and "
                "System Name already exists."
            )

        entity = DataLineageSource(
            lineage_source_id=uuid.uuid4(),
            source_name=source_name,
            source_type=source_type,
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
        entity: DataLineageSource,
        *,
        modified_by: str,
        source_name: str | None = None,
        source_type: str | None = None,
        system_name: str | None = None,
        business_domain: str | None = None,
        owner: str | None = None,
        status: str | None = None,
    ) -> DataLineageSource:
        new_source_name = source_name if source_name is not None else entity.source_name
        new_system_name = system_name if system_name is not None else entity.system_name

        duplicate = self.repository.get_by_name(
            new_source_name,
            new_system_name,
            include_inactive=True,
        )
        if duplicate is not None and duplicate.lineage_source_id != entity.lineage_source_id:
            raise ValueError(
                "A Lineage Source with the same source name and system name "
                "already exists."
            )

        if source_name is not None:
            entity.source_name = source_name

        if source_type is not None:
            entity.source_type = source_type

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
        entity: DataLineageSource,
        *,
        modified_by: str,
    ) -> DataLineageSource:
        return self.repository.soft_delete(
            entity,
            modified_by=modified_by,
        )
