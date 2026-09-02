import uuid
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Index,
    Numeric,
    String,
    TIMESTAMP,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DataQualityRule(Base):
    __tablename__ = "data_quality_rule"

    data_quality_rule_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    data_quality_dimension_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("data_quality_dimension.data_quality_dimension_id"),
        nullable=False,
    )

    business_rule_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("business_rule.business_rule_id"),
        nullable=False,
    )

    rule_code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    rule_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    target_data_asset_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
    )

    severity: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    threshold_percentage: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    execution_frequency: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    owner: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    created_by: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    created_date: Mapped[object] = mapped_column(
        TIMESTAMP,
        nullable=False,
    )

    modified_by: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    modified_date: Mapped[object | None] = mapped_column(
        TIMESTAMP,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="TRUE",
    )

    __table_args__ = (
        UniqueConstraint(
            "rule_code",
            name="uq_dq_rule_code",
        ),
        Index(
            "idx_dq_rule_code",
            "rule_code",
        ),
        Index(
            "idx_dq_rule_dimension",
            "data_quality_dimension_id",
        ),
        Index(
            "idx_dq_rule_owner",
            "owner",
        ),
        Index(
            "idx_dq_rule_status",
            "status",
        ),
    )
