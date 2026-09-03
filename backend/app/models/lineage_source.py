import uuid
from datetime import datetime

from sqlalchemy import Boolean, Index, String, TIMESTAMP, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DataLineageSource(Base):
    __tablename__ = "lineage_source"

    lineage_source_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    source_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    source_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    system_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )
    business_domain: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
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
            "source_name",
            "system_name",
            name="uq_lineage_source_name_system",
        ),
        Index(
            "idx_lineage_source_name",
            "source_name",
        ),
        Index(
            "idx_lineage_source_type",
            "source_type",
        ),
        Index(
            "idx_lineage_source_system",
            "system_name",
        ),
        Index(
            "idx_lineage_source_status",
            "status",
        ),
    )
