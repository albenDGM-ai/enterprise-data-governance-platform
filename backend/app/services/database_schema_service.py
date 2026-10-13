from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.metadata.database_schema import DatabaseSchema
from app.repositories.database_repository import DatabaseRepository
from app.repositories.database_schema_repository import DatabaseSchemaRepository
from app.schemas.metadata.database_schema import DatabaseSchemaCreate, DatabaseSchemaUpdate


class DatabaseSchemaService:
    """Business operations for DatabaseSchema."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = DatabaseSchemaRepository(session)
        self.database_repository = DatabaseRepository(session)

    def get(
        self,
        database_schema_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DatabaseSchema:
        schema = self.repository.get_by_id(
            database_schema_id,
            include_inactive=include_inactive,
        )
        if not schema:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"DatabaseSchema with id {database_schema_id} not found",
            )
        return schema

    def list(
        self,
        *,
        database_id: uuid.UUID | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[DatabaseSchema]:
        return self.repository.list_all(
            database_id=database_id,
            skip=skip,
            limit=limit,
            include_inactive=include_inactive,
        )

    def create(self, schema_create: DatabaseSchemaCreate) -> DatabaseSchema:
        # Validate parent Database exists
        database_obj = self.database_repository.get_by_id(
            schema_create.database_id,
            include_inactive=True,
        )
        if not database_obj:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Database with id {schema_create.database_id} does not exist",
            )

        # Check duplicate
        existing = self.repository.get_by_database_and_name(
            schema_create.database_id,
            schema_create.schema_name,
        )
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"DatabaseSchema with name '{schema_create.schema_name}' already exists in Database {schema_create.database_id}",
            )

        schema_obj = DatabaseSchema(
            database_schema_id=uuid.uuid4(),
            database_id=schema_create.database_id,
            schema_name=schema_create.schema_name,
            description=schema_create.description,
            owner=schema_create.owner,
            status=schema_create.status,
            created_by="system",
            created_date=datetime.now(timezone.utc),
            is_active=schema_create.is_active,
        )

        created = self.repository.create(schema_obj)
        self.session.commit()
        self.session.refresh(created)
        return created
