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


class ApiAsset(Base):
    __tablename__ = "api_asset"

    api_asset_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    source_system_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("source_system.source_system_id"),
        nullable=False,
    )

    api_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    display_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    api_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    api_version: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    base_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    owner: Mapped[str] = mapped_column(
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
    )

    __table_args__ = (
        UniqueConstraint(
            "source_system_id",
            "api_name",
            "api_version",
            name="uq_api_source_system_name_version",
        ),
        Index("idx_api_name", "api_name"),
        Index("idx_api_type", "api_type"),
        Index("idx_api_status", "status"),
    )
