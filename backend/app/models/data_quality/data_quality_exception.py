import uuid
from datetime import date, datetime

from sqlalchemy import (
    Boolean,
    Date,
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


class DataQualityException(Base):
    __tablename__ = "data_quality_exception"

    data_quality_exception_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    data_quality_issue_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("data_quality_issue.data_quality_issue_id"),
        nullable=False,
    )
    exception_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    exception_reason: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    approved_by: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    approval_date: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
    )
    expiry_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
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
            "exception_number",
            name="uq_dq_exception_number",
        ),
        Index(
            "idx_dq_exception_number",
            "exception_number",
        ),
        Index(
            "idx_dq_exception_status",
            "status",
        ),
        Index(
            "idx_dq_exception_expiry",
            "expiry_date",
        ),
    )
