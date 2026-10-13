from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.metadata.data_asset import DataAsset
from app.repositories.metadata_asset_repository import DataAssetRepository
from app.schemas.metadata.data_asset import DataAssetCreate


class DataAssetService:
    """Business operations for Data Asset."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = DataAssetRepository(session)

    def get(
        self,
        data_asset_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataAsset:
        asset = self.repository.get_by_id(
            data_asset_id,
            include_inactive=include_inactive,
        )
        if not asset:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"DataAsset with id {data_asset_id} not found",
            )
        return asset

    def list(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[DataAsset]:
        return self.repository.list_all(
            skip=skip,
            limit=limit,
            include_inactive=include_inactive,
        )

    def create(self, asset_create: DataAssetCreate) -> DataAsset:
        existing_asset = self.repository.get_by_type_and_identifier(
            asset_create.asset_type,
            asset_create.asset_identifier,
        )
        if existing_asset:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"DataAsset with type {asset_create.asset_type} and identifier {asset_create.asset_identifier} already exists",
            )

        data_asset = DataAsset(
            data_asset_id=uuid.uuid4(),
            asset_type=asset_create.asset_type,
            asset_identifier=asset_create.asset_identifier,
            asset_name=asset_create.asset_name,
            display_name=asset_create.display_name,
            description=asset_create.description,
            business_domain=asset_create.business_domain,
            source_system_id=asset_create.source_system_id,
            owner=asset_create.owner,
            steward=asset_create.steward,
            classification=asset_create.classification,
            critical_data_element_flag=asset_create.critical_data_element_flag,
            status=asset_create.status,
            created_by="system",  # Assuming system or context-provided in future
            created_date=datetime.now(timezone.utc),
            is_active=asset_create.is_active,
        )

        created_asset = self.repository.create(data_asset)
        self.session.commit()
        self.session.refresh(created_asset)
        return created_asset
