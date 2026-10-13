from __future__ import annotations

import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.metadata.table_column import TableColumn


class TableColumnRepository:
    """Persistence operations for TableColumn."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        table_column_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> TableColumn | None:
        statement = select(TableColumn).where(
            TableColumn.table_column_id == table_column_id
        )
        if not include_inactive:
            statement = statement.where(TableColumn.is_active.is_(True))
        return self.session.scalar(statement)

    def get_by_table_and_name(
        self,
        database_table_id: uuid.UUID,
        column_name: str,
    ) -> TableColumn | None:
        statement = select(TableColumn).where(
            TableColumn.database_table_id == database_table_id,
            TableColumn.column_name == column_name,
        )
        return self.session.scalar(statement)

    def list_all(
        self,
        *,
        database_table_id: uuid.UUID | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[TableColumn]:
        statement = select(TableColumn)
        if database_table_id is not None:
            statement = statement.where(TableColumn.database_table_id == database_table_id)
        if not include_inactive:
            statement = statement.where(TableColumn.is_active.is_(True))
        statement = statement.offset(skip).limit(limit)
        return self.session.scalars(statement).all()

    def create(self, column: TableColumn) -> TableColumn:
        self.session.add(column)
        self.session.flush()
        self.session.refresh(column)
        return column

    def update(self, column: TableColumn) -> TableColumn:
        self.session.flush()
        self.session.refresh(column)
        return column

    def delete(self, column: TableColumn) -> None:
        self.session.delete(column)
        self.session.flush()
