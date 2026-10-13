from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.metadata.source_system import SourceSystem
from app.repositories.source_system_repository import SourceSystemRepository
from app.schemas.metadata.source_system import SourceSystemCreate, SourceSystemUpdate


class SourceSystemService:
    """Business operations for SourceSystem."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = SourceSystemRepository(session)

    def get(
        self,
        source_system_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> SourceSystem:
        system = self.repository.get_by_id(
            source_system_id,
            include_inactive=include_inactive,
        )
        if not system:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"SourceSystem with id {source_system_id} not found",
            )
        return system

    def list(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[SourceSystem]:
        return self.repository.list_all(
            skip=skip,
            limit=limit,
            include_inactive=include_inactive,
        )

    def create(self, system_create: SourceSystemCreate) -> SourceSystem:
        existing = self.repository.get_by_code(system_create.system_code)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"SourceSystem with code {system_create.system_code} already exists",
            )

        source_system = SourceSystem(
            source_system_id=uuid.uuid4(),
            system_code=system_create.system_code,
            system_name=system_create.system_name,
            description=system_create.description,
            system_type=system_create.system_type,
            vendor=system_create.vendor,
            business_domain=system_create.business_domain,
            environment=system_create.environment,
            owner=system_create.owner,
            steward=system_create.steward,
            status=system_create.status,
            created_by="system",
            created_date=datetime.now(timezone.utc),
            is_active=system_create.is_active,
        )

        created = self.repository.create(source_system)
        self.session.commit()
        self.session.refresh(created)
        return created
