import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Index,
    String,
    Text,
    TIMESTAMP,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DataQualityIssue(Base):
    __tablename__ = "data_quality_issue"

    data_quality_issue_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    data_quality_result_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("data_quality_result.data_quality_result_id"),
        nullable=False,
    )
    issue_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    issue_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    severity: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    business_impact: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
    owner: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    detected_date: Mapped[datetime] = mapped_column(
        TIMESTAMP,
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
            "issue_number",
            name="uq_dq_issue_number",
        ),
        Index(
            "idx_dq_issue_number",
            "issue_number",
        ),
        Index(
            "idx_dq_issue_owner",
            "owner",
        ),
        Index(
            "idx_dq_issue_severity",
            "severity",
        ),
        Index(
            "idx_dq_issue_status",
            "status",
        ),
    )
