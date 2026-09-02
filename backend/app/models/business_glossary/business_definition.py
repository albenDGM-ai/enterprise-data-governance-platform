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
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class BusinessDefinition(Base):
    __tablename__ = "business_definition"

    business_definition_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    business_term_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("business_term.business_term_id"),
        nullable=False,
    )

    definition_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    definition_source: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    version: Mapped[str] = mapped_column(
        String(20),
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
        Index("idx_definition_term", "business_term_id"),
        Index("idx_definition_status", "status"),
        Index("idx_definition_version", "version"),
    )
