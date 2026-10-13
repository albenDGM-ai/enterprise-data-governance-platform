from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.business_glossary import BusinessTermCreate, BusinessTermResponse
from app.services.business_glossary_service import BusinessTermService

router = APIRouter(prefix="/glossary", tags=["business-glossary"])


@router.post(
    "/terms",
    response_model=BusinessTermResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a business term",
)
def create_business_term(
    term_in: BusinessTermCreate,
    db: Session = Depends(get_db),
):
    """Register a new business term."""
    service = BusinessTermService(db)
    return service.create(term_in)


@router.get(
    "/terms/{business_term_id}",
    response_model=BusinessTermResponse,
    summary="Get a business term by ID",
)
def get_business_term(
    business_term_id: UUID,
    include_inactive: bool = Query(False, description="Include inactive terms"),
    db: Session = Depends(get_db),
):
    """Retrieve a business term by its ID."""
    service = BusinessTermService(db)
    return service.get(business_term_id, include_inactive=include_inactive)


@router.get(
    "/terms",
    response_model=list[BusinessTermResponse],
    summary="List business terms",
)
def list_business_terms(
    business_category_id: UUID | None = Query(None, description="Filter by business category ID"),
    data_asset_id: UUID | None = Query(None, description="Filter by data asset ID"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    include_inactive: bool = Query(False, description="Include inactive terms"),
    db: Session = Depends(get_db),
):
    """List business terms."""
    service = BusinessTermService(db)
    return service.list(
        business_category_id=business_category_id,
        data_asset_id=data_asset_id,
        skip=skip,
        limit=limit,
        include_inactive=include_inactive,
    )
