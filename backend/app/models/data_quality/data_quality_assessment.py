import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Index,
    String,
    TIMESTAMP,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DataQualityAssessment(Base):
    __tablename__ = "data_quality_assessment"

    data_quality_assessment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    data_quality_rule_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("data_quality_rule.data_quality_rule_id"),
        nullable=False,
    )

    assessment_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    assessment_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    assessment_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    execution_start_time: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
    )

    execution_end_time: Mapped[datetime | None] = mapped_column(
        TIMESTAMP,
        nullable=True,
    )

    executed_by: Mapped[str] = mapped_column(
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
        UniqueConstraint(
            "assessment_number",
            name="uq_dq_assessment_number",
        ),
        Index(
            "idx_dq_assessment_number",
            "assessment_number",
        ),
        Index(
            "idx_dq_assessment_rule",
            "data_quality_rule_id",
        ),
        Index(
            "idx_dq_assessment_status",
            "status",
        ),
        Index(
            "idx_dq_assessment_start_time",
            "execution_start_time",
        ),
    )
