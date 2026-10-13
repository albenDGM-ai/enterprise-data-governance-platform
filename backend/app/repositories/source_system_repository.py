from __future__ import annotations

import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.metadata.source_system import SourceSystem


class SourceSystemRepository:
    """Persistence operations for SourceSystem."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        source_system_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> SourceSystem | None:
        statement = select(SourceSystem).where(
            SourceSystem.source_system_id == source_system_id
        )
        if not include_inactive:
            statement = statement.where(SourceSystem.is_active.is_(True))
        return self.session.scalar(statement)

    def get_by_code(
        self,
        system_code: str,
    ) -> SourceSystem | None:
        statement = select(SourceSystem).where(
            SourceSystem.system_code == system_code
        )
        return self.session.scalar(statement)

    def list_all(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[SourceSystem]:
        statement = select(SourceSystem)
        if not include_inactive:
            statement = statement.where(SourceSystem.is_active.is_(True))
        statement = statement.offset(skip).limit(limit)
        return self.session.scalars(statement).all()

    def create(self, source_system: SourceSystem) -> SourceSystem:
        self.session.add(source_system)
        self.session.flush()
        self.session.refresh(source_system)
        return source_system

    def update(self, source_system: SourceSystem) -> SourceSystem:
        self.session.flush()
        self.session.refresh(source_system)
        return source_system

    def delete(self, source_system: SourceSystem) -> None:
        self.session.delete(source_system)
        self.session.flush()
