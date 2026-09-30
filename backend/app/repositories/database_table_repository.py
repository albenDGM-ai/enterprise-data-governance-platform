from __future__ import annotations

import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.metadata.database_table import DatabaseTable


class DatabaseTableRepository:
    """Persistence operations for DatabaseTable."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        database_table_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DatabaseTable | None:
        statement = select(DatabaseTable).where(
            DatabaseTable.database_table_id == database_table_id
        )
        if not include_inactive:
            statement = statement.where(DatabaseTable.is_active.is_(True))
        return self.session.scalar(statement)

    def get_by_schema_and_name(
        self,
        database_schema_id: uuid.UUID,
        table_name: str,
    ) -> DatabaseTable | None:
        statement = select(DatabaseTable).where(
            DatabaseTable.database_schema_id == database_schema_id,
            DatabaseTable.table_name == table_name,
        )
        return self.session.scalar(statement)

    def list_all(
        self,
        *,
        database_schema_id: uuid.UUID | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[DatabaseTable]:
        statement = select(DatabaseTable)
        if database_schema_id is not None:
            statement = statement.where(DatabaseTable.database_schema_id == database_schema_id)
        if not include_inactive:
            statement = statement.where(DatabaseTable.is_active.is_(True))
        statement = statement.offset(skip).limit(limit)
        return self.session.scalars(statement).all()

    def create(self, table: DatabaseTable) -> DatabaseTable:
        self.session.add(table)
        self.session.flush()
        self.session.refresh(table)
        return table

    def update(self, table: DatabaseTable) -> DatabaseTable:
        self.session.flush()
        self.session.refresh(table)
        return table

    def delete(self, table: DatabaseTable) -> None:
        self.session.delete(table)
        self.session.flush()
