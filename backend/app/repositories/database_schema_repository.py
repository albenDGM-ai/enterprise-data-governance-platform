from __future__ import annotations

import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.metadata.database_schema import DatabaseSchema


class DatabaseSchemaRepository:
    """Persistence operations for DatabaseSchema."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        database_schema_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DatabaseSchema | None:
        statement = select(DatabaseSchema).where(
            DatabaseSchema.database_schema_id == database_schema_id
        )
        if not include_inactive:
            statement = statement.where(DatabaseSchema.is_active.is_(True))
        return self.session.scalar(statement)

    def get_by_database_and_name(
        self,
        database_id: uuid.UUID,
        schema_name: str,
    ) -> DatabaseSchema | None:
        statement = select(DatabaseSchema).where(
            DatabaseSchema.database_id == database_id,
            DatabaseSchema.schema_name == schema_name,
        )
        return self.session.scalar(statement)

    def list_all(
        self,
        *,
        database_id: uuid.UUID | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[DatabaseSchema]:
        statement = select(DatabaseSchema)
        if database_id is not None:
            statement = statement.where(DatabaseSchema.database_id == database_id)
        if not include_inactive:
            statement = statement.where(DatabaseSchema.is_active.is_(True))
        statement = statement.offset(skip).limit(limit)
        return self.session.scalars(statement).all()

    def create(self, schema: DatabaseSchema) -> DatabaseSchema:
        self.session.add(schema)
        self.session.flush()
        self.session.refresh(schema)
        return schema

    def update(self, schema: DatabaseSchema) -> DatabaseSchema:
        self.session.flush()
        self.session.refresh(schema)
        return schema

    def delete(self, schema: DatabaseSchema) -> None:
        self.session.delete(schema)
        self.session.flush()
