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


class RuleMapping(Base):
    __tablename__ = "rule_mapping"

    rule_mapping_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    business_rule_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("business_rule.business_rule_id"),
        nullable=False,
    )

    target_object_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    target_object_identifier: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
    )

    mapping_type: Mapped[str] = mapped_column(
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
            "target_object_type",
            "target_object_identifier",
            name="uq_rule_mapping_rule_target",
        ),
        Index("idx_rule_mapping_rule", "business_rule_id"),
        Index("idx_rule_mapping_target", "target_object_identifier"),
        Index("idx_rule_mapping_type", "target_object_type"),
        Index("idx_rule_mapping_status", "status"),
    )
