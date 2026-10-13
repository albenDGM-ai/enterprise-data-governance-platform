from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.business_glossary.business_term import BusinessTerm
from app.repositories.business_glossary_repository import BusinessTermRepository
from app.schemas.business_glossary import BusinessTermCreate


class BusinessTermService:
    """Business operations for Business Term."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = BusinessTermRepository(session)

    def get(
        self,
        business_term_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> BusinessTerm:
        term = self.repository.get_by_id(
            business_term_id,
            include_inactive=include_inactive,
        )
        if not term:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"BusinessTerm with id {business_term_id} not found",
            )
        return term

    def list(
        self,
        *,
        business_category_id: uuid.UUID | None = None,
        data_asset_id: uuid.UUID | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[BusinessTerm]:
        return self.repository.list_all(
            business_category_id=business_category_id,
            data_asset_id=data_asset_id,
            skip=skip,
            limit=limit,
            include_inactive=include_inactive,
        )

    def create(self, term_create: BusinessTermCreate) -> BusinessTerm:
        if not self.repository.category_exists(term_create.business_category_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"BusinessCategory with id {term_create.business_category_id} not found",
            )

        if term_create.data_asset_id is not None:
            if not self.repository.data_asset_exists(term_create.data_asset_id):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"DataAsset with id {term_create.data_asset_id} not found",
                )

        existing = self.repository.get_by_category_and_name(
            term_create.business_category_id,
            term_create.business_term_name,
        )
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"BusinessTerm with name '{term_create.business_term_name}' already exists in category {term_create.business_category_id}",
            )

        term = BusinessTerm(
            business_term_id=uuid.uuid4(),
            business_category_id=term_create.business_category_id,
            data_asset_id=term_create.data_asset_id,
            business_term_name=term_create.business_term_name,
            display_name=term_create.display_name,
            preferred_definition=term_create.preferred_definition,
            business_domain=term_create.business_domain,
            business_capability=term_create.business_capability,
            owner=term_create.owner,
            steward=term_create.steward,
            classification=term_create.classification,
            status=term_create.status,
            created_by="system",
            created_date=datetime.now(timezone.utc),
            is_active=term_create.is_active,
        )

        created = self.repository.create(term)
        self.session.commit()
        self.session.refresh(created)
        return created
