from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.metadata.table_column import TableColumn
from app.repositories.database_table_repository import DatabaseTableRepository
from app.repositories.table_column_repository import TableColumnRepository
from app.schemas.metadata.table_column import TableColumnCreate, TableColumnUpdate


class TableColumnService:
    """Business operations for TableColumn."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = TableColumnRepository(session)
        self.table_repository = DatabaseTableRepository(session)

    def get(
        self,
        table_column_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> TableColumn:
        column = self.repository.get_by_id(
            table_column_id,
            include_inactive=include_inactive,
        )
        if not column:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"TableColumn with id {table_column_id} not found",
            )
        return column

    def list(
        self,
        *,
        database_table_id: uuid.UUID | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[TableColumn]:
        return self.repository.list_all(
            database_table_id=database_table_id,
            skip=skip,
            limit=limit,
            include_inactive=include_inactive,
        )

    def create(self, column_create: TableColumnCreate) -> TableColumn:
        # Validate parent DatabaseTable exists
        table_obj = self.table_repository.get_by_id(
            column_create.database_table_id,
            include_inactive=True,
        )
        if not table_obj:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"DatabaseTable with id {column_create.database_table_id} does not exist",
            )

        # Check duplicate
        existing = self.repository.get_by_table_and_name(
            column_create.database_table_id,
            column_create.column_name,
        )
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"TableColumn with name '{column_create.column_name}' already exists in Table {column_create.database_table_id}",
            )

        column_obj = TableColumn(
            table_column_id=uuid.uuid4(),
            database_table_id=column_create.database_table_id,
            column_name=column_create.column_name,
            display_name=column_create.display_name,
            description=column_create.description,
            logical_data_type=column_create.logical_data_type,
            nullable=column_create.nullable,
            primary_key_flag=column_create.primary_key_flag,
            foreign_key_flag=column_create.foreign_key_flag,
            classification=column_create.classification,
            critical_data_element_flag=column_create.critical_data_element_flag,
            ordinal_position=column_create.ordinal_position,
            created_by="system",
            created_date=datetime.now(timezone.utc),
            is_active=column_create.is_active,
        )

        created = self.repository.create(column_obj)
        self.session.commit()
        self.session.refresh(created)
        return created
