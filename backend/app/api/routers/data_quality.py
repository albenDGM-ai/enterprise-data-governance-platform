from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.data_quality import (
    DataQualityResultCreate,
    DataQualityResultResponse,
    DataQualityRuleCreate,
    DataQualityRuleResponse,
)
from app.services.data_quality_service import (
    DataQualityResultService,
    DataQualityRuleService,
)

router = APIRouter(prefix="/quality", tags=["data-quality"])


@router.post(
    "/rules",
    response_model=DataQualityRuleResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a data quality rule",
)
def create_rule(
    rule_in: DataQualityRuleCreate,
    db: Session = Depends(get_db),
):
    """Register a new data quality rule."""
    service = DataQualityRuleService(db)
    return service.create(rule_in)


@router.get(
    "/rules/{data_quality_rule_id}",
    response_model=DataQualityRuleResponse,
    summary="Get a data quality rule by ID",
)
def get_rule(
    data_quality_rule_id: UUID,
    include_inactive: bool = Query(False, description="Include inactive rules"),
    db: Session = Depends(get_db),
):
    """Retrieve a data quality rule by ID."""
    service = DataQualityRuleService(db)
    return service.get(data_quality_rule_id, include_inactive=include_inactive)


@router.get(
    "/rules",
    response_model=list[DataQualityRuleResponse],
    summary="List data quality rules",
)
def list_rules(
    target_data_asset_id: UUID | None = Query(None, description="Filter by target data asset ID"),
    rule_status: str | None = Query(None, alias="status", description="Filter by status"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    include_inactive: bool = Query(False, description="Include inactive rules"),
    db: Session = Depends(get_db),
):
    """List data quality rules."""
    service = DataQualityRuleService(db)
    return service.list(
        target_data_asset_id=target_data_asset_id,
        rule_status=rule_status,
        skip=skip,
        limit=limit,
        include_inactive=include_inactive,
    )


@router.post(
    "/results",
    response_model=DataQualityResultResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a data quality result",
)
def create_result(
    result_in: DataQualityResultCreate,
    db: Session = Depends(get_db),
):
    """Record an execution result for a data quality rule."""
    service = DataQualityResultService(db)
    return service.create(result_in)


@router.get(
    "/results/{data_quality_result_id}",
    response_model=DataQualityResultResponse,
    summary="Get a data quality result by ID",
)
def get_result(
    data_quality_result_id: UUID,
    include_inactive: bool = Query(False, description="Include inactive results"),
    db: Session = Depends(get_db),
):
    """Retrieve a data quality result by ID."""
    service = DataQualityResultService(db)
    return service.get(data_quality_result_id, include_inactive=include_inactive)


@router.get(
    "/results",
    response_model=list[DataQualityResultResponse],
    summary="List data quality results",
)
def list_results(
    data_quality_rule_id: UUID | None = Query(None, description="Filter by data quality rule ID"),
    target_data_asset_id: UUID | None = Query(None, description="Filter by target data asset ID"),
    result_status: str | None = Query(None, description="Filter by result status"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    include_inactive: bool = Query(False, description="Include inactive results"),
    db: Session = Depends(get_db),
):
    """List data quality results."""
    service = DataQualityResultService(db)
    return service.list(
        data_quality_rule_id=data_quality_rule_id,
        target_data_asset_id=target_data_asset_id,
        result_status=result_status,
        skip=skip,
        limit=limit,
        include_inactive=include_inactive,
    )
