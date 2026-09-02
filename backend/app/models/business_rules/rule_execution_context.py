import uuid

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


class RuleExecutionContext(Base):
    __tablename__ = "rule_execution_context"

    rule_execution_context_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    business_rule_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("business_rule.business_rule_id"),
        nullable=False,
    )

    context_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    trigger_event: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    execution_frequency: Mapped[str] = mapped_column(
        String(50),
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
            "context_name",
            name="uq_execution_context_rule_name",
        ),
        Index("idx_execution_context_rule", "business_rule_id"),
        Index("idx_execution_context_name", "context_name"),
        Index("idx_execution_context_status", "status"),
    )
