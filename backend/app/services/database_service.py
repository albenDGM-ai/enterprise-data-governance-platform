from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.metadata.database import Database
from app.repositories.database_repository import DatabaseRepository
from app.repositories.source_system_repository import SourceSystemRepository
from app.schemas.metadata.database import DatabaseCreate, DatabaseUpdate


class DatabaseService:
    """Business operations for Database."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = DatabaseRepository(session)
        self.source_system_repository = SourceSystemRepository(session)

    def get(
        self,
        database_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> Database:
        db_obj = self.repository.get_by_id(
            database_id,
            include_inactive=include_inactive,
        )
        if not db_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Database with id {database_id} not found",
            )
        return db_obj

    def list(
        self,
        *,
        source_system_id: uuid.UUID | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[Database]:
        return self.repository.list_all(
            source_system_id=source_system_id,
            skip=skip,
            limit=limit,
            include_inactive=include_inactive,
        )

    def create(self, db_create: DatabaseCreate) -> Database:
        # Validate parent SourceSystem exists
        source_system = self.source_system_repository.get_by_id(
            db_create.source_system_id,
            include_inactive=True,
        )
        if not source_system:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"SourceSystem with id {db_create.source_system_id} does not exist",
            )

        # Check duplicate
        existing = self.repository.get_by_source_and_name(
            db_create.source_system_id,
            db_create.database_name,
        )
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Database with name '{db_create.database_name}' already exists in SourceSystem {db_create.source_system_id}",
            )

        database_obj = Database(
            database_id=uuid.uuid4(),
            source_system_id=db_create.source_system_id,
            database_name=db_create.database_name,
            database_type=db_create.database_type,
            version=db_create.version,
            description=db_create.description,
            owner=db_create.owner,
            status=db_create.status,
            created_by="system",
            created_date=datetime.now(timezone.utc),
            is_active=db_create.is_active,
        )

        created = self.repository.create(database_obj)
        self.session.commit()
        self.session.refresh(created)
        return created
