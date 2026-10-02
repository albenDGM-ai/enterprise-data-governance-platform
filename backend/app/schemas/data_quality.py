from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DataQualityRuleCreate(BaseModel):
    rule_code: str = Field(..., min_length=1, max_length=50)
    rule_name: str = Field(..., min_length=1, max_length=255)
    target_data_asset_id: UUID
    data_quality_dimension_id: UUID | None = None
    business_rule_id: UUID | None = None
    severity: str = Field("HIGH", max_length=30)
    threshold_percentage: Decimal = Field(Decimal("95.00"), ge=Decimal("0.00"), le=Decimal("100.00"))
    execution_frequency: str = Field("DAILY", max_length=50)
    owner: str = Field("data_governance_team", max_length=100)
    status: str = Field("ACTIVE", max_length=30)
    is_active: bool = True


class DataQualityRuleResponse(BaseModel):
    data_quality_rule_id: UUID
    rule_code: str
    rule_name: str
    target_data_asset_id: UUID
    data_quality_dimension_id: UUID
    business_rule_id: UUID
    severity: str
    threshold_percentage: Decimal
    execution_frequency: str
    owner: str
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class DataQualityResultCreate(BaseModel):
    data_quality_rule_id: UUID
    target_data_asset_id: UUID | None = None
    total_records: int = Field(..., ge=0)
    passed_records: int = Field(..., ge=0)
    failed_records: int = Field(..., ge=0)
    warning_records: int | None = Field(0, ge=0)
    quality_percentage: Decimal | None = Field(None, ge=Decimal("0.00"), le=Decimal("100.00"))
    result_status: str = Field("PASSED", max_length=30)
    execution_duration_ms: int | None = Field(None, ge=0)


class DataQualityResultResponse(BaseModel):
    data_quality_result_id: UUID
    data_quality_assessment_id: UUID
    data_quality_rule_id: UUID | None = None
    target_data_asset_id: UUID
    total_records: int
    passed_records: int
    failed_records: int
    warning_records: int | None = 0
    quality_percentage: Decimal
    result_status: str
    execution_duration_ms: int | None = None
    created_by: str
    created_date: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
