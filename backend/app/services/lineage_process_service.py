from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.lineage_process import DataLineageProcess
from app.repositories.lineage_process_repository import LineageProcessRepository


class LineageProcessService:
    """Business operations for Lineage Process."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = LineageProcessRepository(session)

    def get(
        self,
        lineage_process_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageProcess | None:
        return self.repository.get_by_id(
            lineage_process_id,
            include_inactive=include_inactive,
        )

    def list(
        self,
        *,
        status: str | None = None,
        process_type: str | None = None,
        technology: str | None = None,
        owner: str | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageProcess]:
        return self.repository.list(
            status=status,
            process_type=process_type,
            technology=technology,
            owner=owner,
            include_inactive=include_inactive,
        )

    def create(
        self,
        *,
        process_name: str,
        process_type: str,
        technology: str,
        schedule: str | None,
        owner: str,
        status: str,
        created_by: str,
    ) -> DataLineageProcess:
        existing = self.repository.get_by_name(
            process_name,
            include_inactive=True,
        )

        if existing is not None:
            raise ValueError(
                "A Lineage Process with the supplied Process Name "
                "already exists."
            )

        entity = DataLineageProcess(
            lineage_process_id=uuid.uuid4(),
            process_name=process_name,
            process_type=process_type,
            technology=technology,
            schedule=schedule,
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
        entity: DataLineageProcess,
        *,
        modified_by: str,
        process_name: str | None = None,
        process_type: str | None = None,
        technology: str | None = None,
        schedule: str | None = None,
        owner: str | None = None,
        status: str | None = None,
    ) -> DataLineageProcess:
        new_process_name = (
            process_name if process_name is not None else entity.process_name
        )

        duplicate = self.repository.get_by_name(
            new_process_name,
            include_inactive=True,
        )
        if duplicate is not None and duplicate.lineage_process_id != entity.lineage_process_id:
            raise ValueError(
                "A Lineage Process with the same process name already exists."
            )

        if process_name is not None:
            entity.process_name = process_name
        if process_type is not None:
            entity.process_type = process_type
        if technology is not None:
            entity.technology = technology
        if schedule is not None:
            entity.schedule = schedule
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
        entity: DataLineageProcess,
        *,
        modified_by: str,
    ) -> DataLineageProcess:
        return self.repository.soft_delete(
            entity,
            modified_by=modified_by,
        )
