from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.lineage_snapshot import LineageSnapshot
from app.repositories.lineage_flow_repository import LineageFlowRepository
from app.repositories.lineage_snapshot_repository import LineageSnapshotRepository


class LineageSnapshotService:
    """Business operations for Lineage Snapshot."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = LineageSnapshotRepository(session)
        self.flow_repository = LineageFlowRepository(session)

    def get(
        self,
        lineage_snapshot_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> LineageSnapshot | None:
        return self.repository.get_by_id(
            lineage_snapshot_id,
            include_inactive=include_inactive,
        )

    def list(
        self,
        *,
        lineage_flow_id: uuid.UUID | None = None,
        status: str | None = None,
        snapshot_date_from: datetime | None = None,
        snapshot_date_to: datetime | None = None,
        include_inactive: bool = False,
    ) -> list[LineageSnapshot]:
        return self.repository.list(
            lineage_flow_id=lineage_flow_id,
            status=status,
            snapshot_date_from=snapshot_date_from,
            snapshot_date_to=snapshot_date_to,
            include_inactive=include_inactive,
        )

    def create(
        self,
        *,
        lineage_flow_id: uuid.UUID,
        snapshot_name: str,
        snapshot_date: datetime,
        created_by: str,
        status: str,
    ) -> LineageSnapshot:
        flow = self.flow_repository.get_by_id(lineage_flow_id)

        if flow is None:
            raise ValueError(
                "The supplied Lineage Flow does not exist or is inactive."
            )

        existing = self.repository.get_by_flow_and_name(
            lineage_flow_id,
            snapshot_name,
            include_inactive=True,
        )

        if existing is not None:
            raise ValueError(
                "A Lineage Snapshot with the supplied Lineage Flow "
                "and Snapshot Name already exists."
            )

        entity = LineageSnapshot(
            lineage_snapshot_id=uuid.uuid4(),
            lineage_flow_id=lineage_flow_id,
            snapshot_name=snapshot_name,
            snapshot_date=snapshot_date,
            created_by=created_by,
            status=status,
            created_date=datetime.now(timezone.utc).replace(tzinfo=None),
            is_active=True,
        )

        self.repository.create(entity)
        return entity

    def update(
        self,
        entity: LineageSnapshot,
        *,
        modified_by: str,
        snapshot_name: str | None = None,
        snapshot_date: datetime | None = None,
        status: str | None = None,
    ) -> LineageSnapshot:
        new_snapshot_name = (
            snapshot_name
            if snapshot_name is not None
            else entity.snapshot_name
        )

        duplicate = self.repository.get_by_flow_and_name(
            entity.lineage_flow_id,
            new_snapshot_name,
            include_inactive=True,
        )
        if duplicate is not None and duplicate.lineage_snapshot_id != entity.lineage_snapshot_id:
            raise ValueError(
                "A Lineage Snapshot with the same flow and snapshot name "
                "already exists."
            )

        if snapshot_name is not None:
            entity.snapshot_name = snapshot_name
        if snapshot_date is not None:
            entity.snapshot_date = snapshot_date
        if status is not None:
            entity.status = status

        entity.modified_by = modified_by
        entity.modified_date = datetime.now(timezone.utc).replace(tzinfo=None)

        self.repository.update(entity)
        return entity

    def archive(
        self,
        entity: LineageSnapshot,
        *,
        modified_by: str,
    ) -> LineageSnapshot:
        return self.repository.archive(
            entity,
            modified_by=modified_by,
        )
