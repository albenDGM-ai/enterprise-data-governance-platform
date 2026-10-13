from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.metadata.database_table import DatabaseTable
from app.repositories.database_schema_repository import DatabaseSchemaRepository
from app.repositories.database_table_repository import DatabaseTableRepository
from app.schemas.metadata.database_table import DatabaseTableCreate, DatabaseTableUpdate


class DatabaseTableService:
    """Business operations for DatabaseTable."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = DatabaseTableRepository(session)
        self.schema_repository = DatabaseSchemaRepository(session)

    def get(
        self,
        database_table_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DatabaseTable:
        table = self.repository.get_by_id(
            database_table_id,
            include_inactive=include_inactive,
        )
        if not table:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"DatabaseTable with id {database_table_id} not found",
            )
        return table

    def list(
        self,
        *,
        database_schema_id: uuid.UUID | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[DatabaseTable]:
        return self.repository.list_all(
            database_schema_id=database_schema_id,
            skip=skip,
            limit=limit,
            include_inactive=include_inactive,
        )

    def create(self, table_create: DatabaseTableCreate) -> DatabaseTable:
        # Validate parent DatabaseSchema exists
        schema_obj = self.schema_repository.get_by_id(
            table_create.database_schema_id,
            include_inactive=True,
        )
        if not schema_obj:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"DatabaseSchema with id {table_create.database_schema_id} does not exist",
            )

        # Check duplicate
        existing = self.repository.get_by_schema_and_name(
            table_create.database_schema_id,
            table_create.table_name,
        )
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"DatabaseTable with name '{table_create.table_name}' already exists in Schema {table_create.database_schema_id}",
            )

        table_obj = DatabaseTable(
            database_table_id=uuid.uuid4(),
            database_schema_id=table_create.database_schema_id,
            table_name=table_create.table_name,
            display_name=table_create.display_name,
            description=table_create.description,
            table_type=table_create.table_type,
            row_count=table_create.row_count,
            owner=table_create.owner,
            classification=table_create.classification,
            status=table_create.status,
            created_by="system",
            created_date=datetime.now(timezone.utc),
            is_active=table_create.is_active,
        )

        created = self.repository.create(table_obj)
        self.session.commit()
        self.session.refresh(created)
        return created
