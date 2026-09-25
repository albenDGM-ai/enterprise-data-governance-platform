from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.metadata.data_asset import DataAssetCreate, DataAssetResponse
from app.services.metadata_asset_service import DataAssetService

router = APIRouter(prefix="/metadata", tags=["metadata"])


@router.post(
    "/data-assets",
    response_model=DataAssetResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a data asset",
)
def create_data_asset(
    asset_in: DataAssetCreate,
    db: Session = Depends(get_db),
):
    """Register a new data asset."""
    service = DataAssetService(db)
    return service.create(asset_in)


@router.get(
    "/data-assets/{data_asset_id}",
    response_model=DataAssetResponse,
    summary="Get a data asset by ID",
)
def get_data_asset(
    data_asset_id: UUID,
    include_inactive: bool = Query(False, description="Include inactive assets"),
    db: Session = Depends(get_db),
):
    """Retrieve a data asset by its ID."""
    service = DataAssetService(db)
    return service.get(data_asset_id, include_inactive=include_inactive)


@router.get(
    "/data-assets",
    response_model=list[DataAssetResponse],
    summary="List data assets",
)
def list_data_assets(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    include_inactive: bool = Query(False, description="Include inactive assets"),
    db: Session = Depends(get_db),
):
    """List data assets."""
    service = DataAssetService(db)
    return service.list(
        skip=skip,
        limit=limit,
        include_inactive=include_inactive,
    )
