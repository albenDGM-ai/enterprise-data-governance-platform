import uuid
from datetime import datetime

from sqlalchemy import Boolean, Index, String, TIMESTAMP, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DataLineageProcess(Base):
    __tablename__ = "lineage_process"

    lineage_process_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    process_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    process_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    technology: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    schedule: Mapped[str | None] = mapped_column(
        String(100),
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
            "process_name",
            name="uq_lineage_process_name",
        ),
        Index(
            "idx_lineage_process_name",
            "process_name",
        ),
        Index(
            "idx_lineage_process_type",
            "process_type",
        ),
        Index(
            "idx_lineage_process_status",
            "status",
        ),
    )
