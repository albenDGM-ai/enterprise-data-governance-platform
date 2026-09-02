import uuid
from datetime import date

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


class RuleVersion(Base):
    __tablename__ = "rule_version"

    rule_version_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    business_rule_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("business_rule.business_rule_id"),
        nullable=False,
    )

    version_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    change_summary: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    effective_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    expiry_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    approved_by: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    approved_date: Mapped[object] = mapped_column(
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
            "business_rule_id",
            "version_number",
            name="uq_rule_version_rule_version",
        ),
        Index("idx_rule_version_rule", "business_rule_id"),
        Index("idx_rule_version_number", "version_number"),
        Index("idx_rule_version_status", "status"),
    )
