from __future__ import annotations

import uuid
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.data_quality.data_quality_assessment import DataQualityAssessment
from app.models.data_quality.data_quality_result import DataQualityResult
from app.models.data_quality.data_quality_rule import DataQualityRule
from app.repositories.data_quality_repository import (
    DataQualityResultRepository,
    DataQualityRuleRepository,
)
from app.schemas.data_quality import (
    DataQualityResultCreate,
    DataQualityResultResponse,
    DataQualityRuleCreate,
)


class DataQualityRuleService:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = DataQualityRuleRepository(session)

    def get(
        self,
        rule_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataQualityRule:
        rule = self.repository.get_by_id(
            rule_id,
            include_inactive=include_inactive,
        )
        if not rule:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"DataQualityRule with id {rule_id} not found",
            )
        return rule

    def list(
        self,
        *,
        target_data_asset_id: uuid.UUID | None = None,
        rule_status: str | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[DataQualityRule]:
        return self.repository.list_all(
            target_data_asset_id=target_data_asset_id,
            status=rule_status,
            skip=skip,
            limit=limit,
            include_inactive=include_inactive,
        )

    def create(self, rule_create: DataQualityRuleCreate) -> DataQualityRule:
        existing = self.repository.get_by_code(rule_create.rule_code)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"DataQualityRule with code '{rule_create.rule_code}' already exists",
            )

        asset_exists = self.repository.data_asset_exists(rule_create.target_data_asset_id)
        column_exists = self.repository.column_exists(rule_create.target_data_asset_id)
        if not asset_exists and not column_exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Referenced DataAsset or Column with id {rule_create.target_data_asset_id} not found",
            )

        if rule_create.data_quality_dimension_id is not None:
            if not self.repository.dimension_exists(rule_create.data_quality_dimension_id):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"DataQualityDimension with id {rule_create.data_quality_dimension_id} not found",
                )
            dimension_id = rule_create.data_quality_dimension_id
        else:
            dimension = self.repository.get_or_create_default_dimension()
            dimension_id = dimension.data_quality_dimension_id

        if rule_create.business_rule_id is not None:
            if not self.repository.business_rule_exists(rule_create.business_rule_id):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"BusinessRule with id {rule_create.business_rule_id} not found",
                )
            business_rule_id = rule_create.business_rule_id
        else:
            br = self.repository.get_or_create_default_business_rule()
            business_rule_id = br.business_rule_id

        rule = DataQualityRule(
            data_quality_rule_id=uuid.uuid4(),
            data_quality_dimension_id=dimension_id,
            business_rule_id=business_rule_id,
            rule_code=rule_create.rule_code,
            rule_name=rule_create.rule_name,
            target_data_asset_id=rule_create.target_data_asset_id,
            severity=rule_create.severity,
            threshold_percentage=rule_create.threshold_percentage,
            execution_frequency=rule_create.execution_frequency,
            owner=rule_create.owner,
            status=rule_create.status,
            created_by="system",
            created_date=datetime.now(timezone.utc),
            is_active=rule_create.is_active,
        )

        created = self.repository.create(rule)
        self.session.commit()
        self.session.refresh(created)
        return created


class DataQualityResultService:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.rule_repository = DataQualityRuleRepository(session)
        self.result_repository = DataQualityResultRepository(session)

    def get(
        self,
        result_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataQualityResultResponse:
        item = self.result_repository.get_result_by_id(
            result_id,
            include_inactive=include_inactive,
        )
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"DataQualityResult with id {result_id} not found",
            )
        result, rule_id = item
        return DataQualityResultResponse(
            data_quality_result_id=result.data_quality_result_id,
            data_quality_assessment_id=result.data_quality_assessment_id,
            data_quality_rule_id=rule_id,
            target_data_asset_id=result.target_data_asset_id,
            total_records=result.total_records,
            passed_records=result.passed_records,
            failed_records=result.failed_records,
            warning_records=result.warning_records,
            quality_percentage=result.quality_percentage,
            result_status=result.result_status,
            execution_duration_ms=result.execution_duration_ms,
            created_by=result.created_by,
            created_date=result.created_date,
            is_active=result.is_active,
        )

    def list(
        self,
        *,
        data_quality_rule_id: uuid.UUID | None = None,
        target_data_asset_id: uuid.UUID | None = None,
        result_status: str | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> list[DataQualityResultResponse]:
        items = self.result_repository.list_results(
            data_quality_rule_id=data_quality_rule_id,
            target_data_asset_id=target_data_asset_id,
            result_status=result_status,
            skip=skip,
            limit=limit,
            include_inactive=include_inactive,
        )
        return [
            DataQualityResultResponse(
                data_quality_result_id=result.data_quality_result_id,
                data_quality_assessment_id=result.data_quality_assessment_id,
                data_quality_rule_id=rule_id,
                target_data_asset_id=result.target_data_asset_id,
                total_records=result.total_records,
                passed_records=result.passed_records,
                failed_records=result.failed_records,
                warning_records=result.warning_records,
                quality_percentage=result.quality_percentage,
                result_status=result.result_status,
                execution_duration_ms=result.execution_duration_ms,
                created_by=result.created_by,
                created_date=result.created_date,
                is_active=result.is_active,
            )
            for result, rule_id in items
        ]

    def create(self, result_create: DataQualityResultCreate) -> DataQualityResultResponse:
        rule = self.rule_repository.get_by_id(result_create.data_quality_rule_id)
        if not rule:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"DataQualityRule with id {result_create.data_quality_rule_id} not found",
            )

        if result_create.target_data_asset_id is not None:
            if result_create.target_data_asset_id != rule.target_data_asset_id:
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail=f"Result target_data_asset_id '{result_create.target_data_asset_id}' does not match rule target_data_asset_id '{rule.target_data_asset_id}'",
                )
            asset_exists = self.rule_repository.data_asset_exists(result_create.target_data_asset_id)
            column_exists = self.rule_repository.column_exists(result_create.target_data_asset_id)
            if not asset_exists and not column_exists:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Referenced DataAsset or Column with id {result_create.target_data_asset_id} not found",
                )
            target_asset_id = result_create.target_data_asset_id
        else:
            target_asset_id = rule.target_data_asset_id

        if result_create.total_records > 0:
            calc = (Decimal(result_create.passed_records) / Decimal(result_create.total_records)) * Decimal("100.00")
            quality_pct = calc.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        else:
            quality_pct = Decimal("0.00")

        now = datetime.now(timezone.utc)
        assessment_id = uuid.uuid4()
        assessment = DataQualityAssessment(
            data_quality_assessment_id=assessment_id,
            data_quality_rule_id=rule.data_quality_rule_id,
            assessment_number=f"ASM-{uuid.uuid4().hex[:12].upper()}",
            assessment_name=f"Assessment for {rule.rule_code}",
            assessment_type="AUTOMATED",
            execution_start_time=now,
            execution_end_time=now,
            executed_by="system",
            status="COMPLETED",
            created_by="system",
            created_date=now,
            is_active=True,
        )

        result_id = uuid.uuid4()
        result = DataQualityResult(
            data_quality_result_id=result_id,
            data_quality_assessment_id=assessment_id,
            target_data_asset_id=target_asset_id,
            total_records=result_create.total_records,
            passed_records=result_create.passed_records,
            failed_records=result_create.failed_records,
            warning_records=result_create.warning_records,
            quality_percentage=quality_pct,
            result_status=result_create.result_status,
            execution_duration_ms=result_create.execution_duration_ms,
            created_by="system",
            created_date=now,
            is_active=True,
        )

        created_result = self.result_repository.create_assessment_and_result(assessment, result)
        self.session.commit()

        return DataQualityResultResponse(
            data_quality_result_id=created_result.data_quality_result_id,
            data_quality_assessment_id=created_result.data_quality_assessment_id,
            data_quality_rule_id=rule.data_quality_rule_id,
            target_data_asset_id=created_result.target_data_asset_id,
            total_records=created_result.total_records,
            passed_records=created_result.passed_records,
            failed_records=created_result.failed_records,
            warning_records=created_result.warning_records,
            quality_percentage=created_result.quality_percentage,
            result_status=created_result.result_status,
            execution_duration_ms=created_result.execution_duration_ms,
            created_by=created_result.created_by,
            created_date=created_result.created_date,
            is_active=created_result.is_active,
        )
