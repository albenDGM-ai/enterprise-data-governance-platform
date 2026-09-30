from __future__ import annotations

import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.metadata.database import Database


class DatabaseRepository:
    """Persistence operations for Database."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        database_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> Database | None:
        statement = select(Database).where(
            Database.database_id == database_id
        )
        if not include_inactive:
            statement = statement.where(Database.is_active.is_(True))
        return self.session.scalar(statement)

    def get_by_source_and_name(
        self,
        source_system_id: uuid.UUID,
        database_name: str,
    ) -> Database | None:
        statement = select(Database).where(
            Database.source_system_id == source_system_id,
            Database.database_name == database_name,
        )
        return self.session.scalar(statement)

    def list_all(
        self,
        *,
        source_system_id: uuid.UUID | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[Database]:
        statement = select(Database)
        if source_system_id is not None:
            statement = statement.where(Database.source_system_id == source_system_id)
        if not include_inactive:
            statement = statement.where(Database.is_active.is_(True))
        statement = statement.offset(skip).limit(limit)
        return self.session.scalars(statement).all()

    def create(self, database: Database) -> Database:
        self.session.add(database)
        self.session.flush()
        self.session.refresh(database)
        return database

    def update(self, database: Database) -> Database:
        self.session.flush()
        self.session.refresh(database)
        return database

    def delete(self, database: Database) -> None:
        self.session.delete(database)
        self.session.flush()
