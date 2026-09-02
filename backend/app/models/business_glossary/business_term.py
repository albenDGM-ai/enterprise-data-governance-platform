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


class BusinessTerm(Base):
    __tablename__ = "business_term"

    business_term_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    business_category_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("business_category.business_category_id"),
        nullable=False,
    )

    business_term_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    display_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    preferred_definition: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    business_domain: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    business_capability: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    owner: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    steward: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    classification: Mapped[str | None] = mapped_column(
        String(50),
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
            "business_category_id",
            "business_term_name",
            name="uq_business_term_category_name",
        ),
        Index("idx_business_term_name", "business_term_name"),
        Index("idx_business_domain", "business_domain"),
        Index("idx_business_term_owner", "owner"),
        Index("idx_business_term_status", "status"),
    )
