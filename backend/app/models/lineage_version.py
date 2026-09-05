import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, ForeignKey, Index, String, TIMESTAMP, Text, UniqueConstraint, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DataLineageVersion(Base):
    __tablename__ = "lineage_version"

    lineage_version_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    lineage_flow_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("lineage_flow.lineage_flow_id"),
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
    approved_by: Mapped[str] = mapped_column(
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
            "lineage_flow_id",
            "version_number",
            name="uq_lineage_version_flow_version",
        ),
        Index(
            "idx_lineage_version_flow",
            "lineage_flow_id",
        ),
        Index(
            "idx_lineage_version_number",
            "version_number",
        ),
        Index(
            "idx_lineage_version_status",
            "status",
        ),
    )
