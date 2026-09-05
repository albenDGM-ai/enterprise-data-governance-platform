from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lineage_snapshot import LineageSnapshot


class LineageSnapshotRepository:
    """Persistence operations for Lineage Snapshot."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        lineage_snapshot_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> LineageSnapshot | None:
        statement = select(LineageSnapshot).where(
            LineageSnapshot.lineage_snapshot_id == lineage_snapshot_id
        )

        if not include_inactive:
            statement = statement.where(
                LineageSnapshot.is_active.is_(True)
            )

        return self.session.scalar(statement)

    def get_by_flow_and_name(
        self,
        lineage_flow_id: uuid.UUID,
        snapshot_name: str,
        *,
        include_inactive: bool = False,
    ) -> LineageSnapshot | None:
        statement = select(LineageSnapshot).where(
            LineageSnapshot.lineage_flow_id == lineage_flow_id,
            LineageSnapshot.snapshot_name == snapshot_name,
        )

        if not include_inactive:
            statement = statement.where(
                LineageSnapshot.is_active.is_(True)
            )

        return self.session.scalar(statement)

    def list(
        self,
        *,
        lineage_flow_id: uuid.UUID | None = None,
        status: str | None = None,
        snapshot_date_from: datetime | None = None,
        snapshot_date_to: datetime | None = None,
        include_inactive: bool = False,
    ) -> list[LineageSnapshot]:
        statement = select(LineageSnapshot)

        if not include_inactive:
            statement = statement.where(
                LineageSnapshot.is_active.is_(True)
            )
        if lineage_flow_id is not None:
            statement = statement.where(
                LineageSnapshot.lineage_flow_id == lineage_flow_id
            )
        if status is not None:
            statement = statement.where(LineageSnapshot.status == status)
        if snapshot_date_from is not None:
            statement = statement.where(
                LineageSnapshot.snapshot_date >= snapshot_date_from
            )
        if snapshot_date_to is not None:
            statement = statement.where(
                LineageSnapshot.snapshot_date <= snapshot_date_to
            )

        statement = statement.order_by(LineageSnapshot.snapshot_date.desc())

        return list(self.session.scalars(statement).all())

    def create(self, entity: LineageSnapshot) -> LineageSnapshot:
        self.session.add(entity)
        self.session.flush()
        return entity

    def update(self, entity: LineageSnapshot) -> LineageSnapshot:
        self.session.add(entity)
        self.session.flush()
        return entity

    def archive(
        self,
        entity: LineageSnapshot,
        *,
        modified_by: str,
    ) -> LineageSnapshot:
        entity.is_active = False
        entity.modified_by = modified_by
        self.session.add(entity)
        self.session.flush()
        return entity
