from __future__ import annotations

import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.business_glossary.business_category import BusinessCategory
from app.models.business_glossary.business_term import BusinessTerm
from app.models.metadata.data_asset import DataAsset


class BusinessTermRepository:
    """Persistence operations for Business Term."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        business_term_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> BusinessTerm | None:
        statement = select(BusinessTerm).where(
            BusinessTerm.business_term_id == business_term_id
        )

        if not include_inactive:
            statement = statement.where(BusinessTerm.is_active.is_(True))

        return self.session.scalar(statement)

    def get_by_category_and_name(
        self,
        business_category_id: uuid.UUID,
        business_term_name: str,
    ) -> BusinessTerm | None:
        statement = select(BusinessTerm).where(
            BusinessTerm.business_category_id == business_category_id,
            BusinessTerm.business_term_name == business_term_name,
        )
        return self.session.scalar(statement)

    def list_all(
        self,
        *,
        business_category_id: uuid.UUID | None = None,
        data_asset_id: uuid.UUID | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[BusinessTerm]:
        statement = select(BusinessTerm)

        if not include_inactive:
            statement = statement.where(BusinessTerm.is_active.is_(True))

        if business_category_id is not None:
            statement = statement.where(BusinessTerm.business_category_id == business_category_id)

        if data_asset_id is not None:
            statement = statement.where(BusinessTerm.data_asset_id == data_asset_id)

        statement = statement.offset(skip).limit(limit)

        return self.session.scalars(statement).all()

    def create(self, business_term: BusinessTerm) -> BusinessTerm:
        self.session.add(business_term)
        self.session.flush()
        self.session.refresh(business_term)
        return business_term

    def category_exists(self, business_category_id: uuid.UUID) -> bool:
        statement = select(BusinessCategory).where(
            BusinessCategory.business_category_id == business_category_id,
            BusinessCategory.is_active.is_(True),
        )
        return self.session.scalar(statement) is not None

    def data_asset_exists(self, data_asset_id: uuid.UUID) -> bool:
        statement = select(DataAsset).where(
            DataAsset.data_asset_id == data_asset_id,
            DataAsset.is_active.is_(True),
        )
        return self.session.scalar(statement) is not None
