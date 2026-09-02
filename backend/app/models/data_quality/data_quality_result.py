import uuid
from decimal import Decimal
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    ForeignKey,
    Index,
    Numeric,
    String,
    TIMESTAMP,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DataQualityResult(Base):
    __tablename__ = "data_quality_result"

    data_quality_result_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    data_quality_assessment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("data_quality_assessment.data_quality_assessment_id"),
        nullable=False,
    )

    target_data_asset_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
    )

    total_records: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    passed_records: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    failed_records: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    warning_records: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True,
    )

    quality_percentage: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    result_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    execution_duration_ms: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True,
    )

    created_by: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    created_date: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
    )

    modified_by: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    modified_date: Mapped[datetime | None] = mapped_column(
        TIMESTAMP,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="TRUE",
    )

    __table_args__ = (
        Index(
            "idx_dq_result_assessment",
            "data_quality_assessment_id",
        ),
        Index(
            "idx_dq_result_asset",
            "target_data_asset_id",
        ),
        Index(
            "idx_dq_result_status",
            "result_status",
        ),
        Index(
            "idx_dq_result_quality",
            "quality_percentage",
        ),
    )
