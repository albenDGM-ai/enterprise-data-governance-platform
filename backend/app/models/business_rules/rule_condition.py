import uuid

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    TIMESTAMP,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class RuleCondition(Base):
    __tablename__ = "rule_condition"

    rule_condition_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    business_rule_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("business_rule.business_rule_id"),
        nullable=False,
    )

    sequence_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    left_operand: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    operator: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    right_operand: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    logical_operator: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
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
            "sequence_number",
            name="uq_rule_condition_rule_sequence",
        ),
        Index("idx_rule_condition_rule", "business_rule_id"),
        Index("idx_rule_condition_sequence", "sequence_number"),
        Index("idx_rule_condition_status", "status"),
    )
