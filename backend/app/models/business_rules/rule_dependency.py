import uuid

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


class RuleDependency(Base):
    __tablename__ = "rule_dependency"

    rule_dependency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    parent_business_rule_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("business_rule.business_rule_id"),
        nullable=False,
    )

    dependent_business_rule_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("business_rule.business_rule_id"),
        nullable=False,
    )

    dependency_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
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
            "parent_business_rule_id",
            "dependent_business_rule_id",
            name="uq_rule_dependency_parent_dependent",
        ),
        Index("idx_rule_dependency_parent", "parent_business_rule_id"),
        Index("idx_rule_dependency_child", "dependent_business_rule_id"),
        Index("idx_rule_dependency_status", "status"),
    )
