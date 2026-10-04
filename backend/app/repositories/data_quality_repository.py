from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.business_rules.business_rule import BusinessRule
from app.models.business_rules.rule_category import RuleCategory
from app.models.business_rules.rule_type import RuleType
from app.models.data_quality.data_quality_assessment import DataQualityAssessment
from app.models.data_quality.data_quality_dimension import DataQualityDimension
from app.models.data_quality.data_quality_result import DataQualityResult
from app.models.data_quality.data_quality_rule import DataQualityRule
from app.models.metadata.data_asset import DataAsset
from app.models.metadata.table_column import TableColumn


class DataQualityRuleRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        rule_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataQualityRule | None:
        stmt = select(DataQualityRule).where(DataQualityRule.data_quality_rule_id == rule_id)
        if not include_inactive:
            stmt = stmt.where(DataQualityRule.is_active.is_(True))
        return self.session.execute(stmt).scalar_one_or_none()

    def get_by_code(self, rule_code: str) -> DataQualityRule | None:
        stmt = select(DataQualityRule).where(DataQualityRule.rule_code == rule_code)
        return self.session.execute(stmt).scalar_one_or_none()

    def list_all(
        self,
        *,
        target_data_asset_id: uuid.UUID | None = None,
        status: str | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> Sequence[DataQualityRule]:
        stmt = select(DataQualityRule)
        if not include_inactive:
            stmt = stmt.where(DataQualityRule.is_active.is_(True))
        if target_data_asset_id is not None:
            stmt = stmt.where(DataQualityRule.target_data_asset_id == target_data_asset_id)
        if status is not None:
            stmt = stmt.where(DataQualityRule.status == status)

        stmt = stmt.offset(skip).limit(limit)
        return self.session.execute(stmt).scalars().all()

    def data_asset_exists(self, asset_id: uuid.UUID) -> bool:
        stmt = select(DataAsset.data_asset_id).where(
            DataAsset.data_asset_id == asset_id,
            DataAsset.is_active.is_(True),
        )
        return self.session.execute(stmt).first() is not None

    def column_exists(self, column_id: uuid.UUID) -> bool:
        stmt = select(TableColumn.table_column_id).where(
            TableColumn.table_column_id == column_id,
            TableColumn.is_active.is_(True),
        )
        return self.session.execute(stmt).first() is not None

    def dimension_exists(self, dimension_id: uuid.UUID) -> bool:
        stmt = select(DataQualityDimension.data_quality_dimension_id).where(
            DataQualityDimension.data_quality_dimension_id == dimension_id,
        )
        return self.session.execute(stmt).first() is not None

    def business_rule_exists(self, business_rule_id: uuid.UUID) -> bool:
        stmt = select(BusinessRule.business_rule_id).where(
            BusinessRule.business_rule_id == business_rule_id,
        )
        return self.session.execute(stmt).first() is not None

    def get_or_create_default_dimension(self) -> DataQualityDimension:
        stmt = select(DataQualityDimension).where(DataQualityDimension.dimension_name == "General Quality")
        existing = self.session.execute(stmt).scalar_one_or_none()
        if existing:
            return existing

        dimension = DataQualityDimension(
            data_quality_dimension_id=uuid.uuid4(),
            dimension_name="General Quality",
            display_name="General Quality",
            description="Default dimension for general data quality rules",
            owner="data_governance_team",
            status="ACTIVE",
            created_by="system",
            created_date=datetime.now(timezone.utc),
            is_active=True,
        )
        self.session.add(dimension)
        self.session.flush()
        return dimension

    def get_or_create_default_business_rule(self) -> BusinessRule:
        stmt = select(BusinessRule).where(BusinessRule.rule_code == "BR_GENERAL_QUALITY")
        existing = self.session.execute(stmt).scalar_one_or_none()
        if existing:
            return existing

        cat_stmt = select(RuleCategory).where(RuleCategory.category_name == "General Quality")
        category = self.session.execute(cat_stmt).scalar_one_or_none()
        if not category:
            category = RuleCategory(
                rule_category_id=uuid.uuid4(),
                category_name="General Quality",
                display_name="General Quality",
                description="Default category for general quality rules",
                owner="data_governance_team",
                steward="data_governance_team",
                status="ACTIVE",
                created_by="system",
                created_date=datetime.now(timezone.utc),
                is_active=True,
            )
            self.session.add(category)
            self.session.flush()

        type_stmt = select(RuleType).where(RuleType.rule_type_name == "Validation Rule")
        rule_type = self.session.execute(type_stmt).scalar_one_or_none()
        if not rule_type:
            rule_type = RuleType(
                rule_type_id=uuid.uuid4(),
                rule_type_name="Validation Rule",
                display_name="Validation Rule",
                description="Default validation rule type",
                status="ACTIVE",
                created_by="system",
                created_date=datetime.now(timezone.utc),
                is_active=True,
            )
            self.session.add(rule_type)
            self.session.flush()

        now = datetime.now(timezone.utc)
        rule = BusinessRule(
            business_rule_id=uuid.uuid4(),
            rule_category_id=category.rule_category_id,
            rule_type_id=rule_type.rule_type_id,
            rule_code="BR_GENERAL_QUALITY",
            rule_name="General Data Quality Business Rule",
            description="Default business rule reference for data quality rules",
            severity="HIGH",
            priority=1,
            execution_order=1,
            owner="data_governance_team",
            steward="data_governance_team",
            effective_date=now.date(),
            status="ACTIVE",
            created_by="system",
            created_date=now,
            is_active=True,
        )
        self.session.add(rule)
        self.session.flush()
        return rule

    def create(self, rule: DataQualityRule) -> DataQualityRule:
        self.session.add(rule)
        self.session.flush()
        return rule


class DataQualityResultRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_assessment_and_result(
        self,
        assessment: DataQualityAssessment,
        result: DataQualityResult,
    ) -> DataQualityResult:
        self.session.add(assessment)
        self.session.flush()
        self.session.add(result)
        self.session.flush()
        return result

    def get_result_by_id(
        self,
        result_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> tuple[DataQualityResult, uuid.UUID] | None:
        stmt = (
            select(DataQualityResult, DataQualityAssessment.data_quality_rule_id)
            .join(
                DataQualityAssessment,
                DataQualityResult.data_quality_assessment_id == DataQualityAssessment.data_quality_assessment_id,
            )
            .where(DataQualityResult.data_quality_result_id == result_id)
        )
        if not include_inactive:
            stmt = stmt.where(DataQualityResult.is_active.is_(True))

        row = self.session.execute(stmt).first()
        if not row:
            return None
        return row[0], row[1]

    def list_results(
        self,
        *,
        data_quality_rule_id: uuid.UUID | None = None,
        target_data_asset_id: uuid.UUID | None = None,
        result_status: str | None = None,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False,
    ) -> list[tuple[DataQualityResult, uuid.UUID]]:
        stmt = (
            select(DataQualityResult, DataQualityAssessment.data_quality_rule_id)
            .join(
                DataQualityAssessment,
                DataQualityResult.data_quality_assessment_id == DataQualityAssessment.data_quality_assessment_id,
            )
        )
        if not include_inactive:
            stmt = stmt.where(DataQualityResult.is_active.is_(True))
        if data_quality_rule_id is not None:
            stmt = stmt.where(DataQualityAssessment.data_quality_rule_id == data_quality_rule_id)
        if target_data_asset_id is not None:
            stmt = stmt.where(DataQualityResult.target_data_asset_id == target_data_asset_id)
        if result_status is not None:
            stmt = stmt.where(DataQualityResult.result_status == result_status)

        stmt = stmt.offset(skip).limit(limit)
        rows = self.session.execute(stmt).all()
        return [(row[0], row[1]) for row in rows]
