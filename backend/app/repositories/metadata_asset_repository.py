from __future__ import annotations

import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.metadata.data_asset import DataAsset


class DataAssetRepository:
    """Persistence operations for Data Asset."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        data_asset_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataAsset | None:
        statement = select(DataAsset).where(
            DataAsset.data_asset_id == data_asset_id
        )

        if not include_inactive:
            statement = statement.where(DataAsset.is_active.is_(True))

        return self.session.scalar(statement)

    def get_by_type_and_identifier(
        self,
        asset_type: str,
        asset_identifier: uuid.UUID,
    ) -> DataAsset | None:
        statement = select(DataAsset).where(
            DataAsset.asset_type == asset_type,
            DataAsset.asset_identifier == asset_identifier,
        )
        return self.session.scalar(statement)

    def list_all(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[DataAsset]:
        statement = select(DataAsset)

        if not include_inactive:
            statement = statement.where(DataAsset.is_active.is_(True))

        statement = statement.offset(skip).limit(limit)

        return self.session.scalars(statement).all()

    def create(self, data_asset: DataAsset) -> DataAsset:
        self.session.add(data_asset)
        self.session.flush()
        self.session.refresh(data_asset)
        return data_asset

    def update(self, data_asset: DataAsset) -> DataAsset:
        self.session.flush()
        self.session.refresh(data_asset)
        return data_asset

    def delete(self, data_asset: DataAsset) -> None:
        self.session.delete(data_asset)
        self.session.flush()
