from __future__ import annotations

import uuid
from datetime import date, datetime, timezone

from sqlalchemy.orm import Session

from app.models.lineage_version import DataLineageVersion
from app.repositories.lineage_flow_repository import LineageFlowRepository
from app.repositories.lineage_version_repository import LineageVersionRepository


class LineageVersionService:
    """Business operations for Lineage Version."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = LineageVersionRepository(session)
        self.flow_repository = LineageFlowRepository(session)

    def get(
        self,
        lineage_version_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageVersion | None:
        return self.repository.get_by_id(
            lineage_version_id,
            include_inactive=include_inactive,
        )

    def list(
        self,
        *,
        lineage_flow_id: uuid.UUID | None = None,
        status: str | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageVersion]:
        return self.repository.list(
            lineage_flow_id=lineage_flow_id,
            status=status,
            include_inactive=include_inactive,
        )

    def create(
        self,
        *,
        lineage_flow_id: uuid.UUID,
        version_number: str,
        change_summary: str,
        effective_date: date,
        approved_by: str,
        status: str,
        created_by: str,
    ) -> DataLineageVersion:
        flow = self.flow_repository.get_by_id(lineage_flow_id)

        if flow is None:
            raise ValueError(
                "The supplied Lineage Flow does not exist or is inactive."
            )

        existing = self.repository.get_by_flow_and_version(
            lineage_flow_id,
            version_number,
            include_inactive=True,
        )

        if existing is not None:
            raise ValueError(
                "A Lineage Version with the supplied Lineage Flow "
                "and Version Number already exists."
            )

        entity = DataLineageVersion(
            lineage_version_id=uuid.uuid4(),
            lineage_flow_id=lineage_flow_id,
            version_number=version_number,
            change_summary=change_summary,
            effective_date=effective_date,
            approved_by=approved_by,
            status=status,
            created_by=created_by,
            created_date=datetime.now(timezone.utc).replace(tzinfo=None),
            is_active=True,
        )

        self.repository.create(entity)
        return entity

    def update(
        self,
        entity: DataLineageVersion,
        *,
        modified_by: str,
        version_number: str | None = None,
        change_summary: str | None = None,
        effective_date: date | None = None,
        approved_by: str | None = None,
        status: str | None = None,
    ) -> DataLineageVersion:
        new_version_number = (
            version_number
            if version_number is not None
            else entity.version_number
        )

        duplicate = self.repository.get_by_flow_and_version(
            entity.lineage_flow_id,
            new_version_number,
            include_inactive=True,
        )
        if duplicate is not None and duplicate.lineage_version_id != entity.lineage_version_id:
            raise ValueError(
                "A Lineage Version with the same flow and version number "
                "already exists."
            )

        if version_number is not None:
            entity.version_number = version_number
        if change_summary is not None:
            entity.change_summary = change_summary
        if effective_date is not None:
            entity.effective_date = effective_date
        if approved_by is not None:
            entity.approved_by = approved_by
        if status is not None:
            entity.status = status

        entity.modified_by = modified_by
        entity.modified_date = datetime.now(timezone.utc).replace(tzinfo=None)

        self.repository.update(entity)
        return entity

    def archive(
        self,
        entity: DataLineageVersion,
        *,
        modified_by: str,
    ) -> DataLineageVersion:
        return self.repository.archive(
            entity,
            modified_by=modified_by,
        )
