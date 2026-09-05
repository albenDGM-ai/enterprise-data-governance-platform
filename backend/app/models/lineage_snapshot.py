import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Index, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class LineageSnapshot(Base):
    __tablename__ = "lineage_snapshot"

    lineage_snapshot_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    lineage_flow_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("lineage_flow.lineage_flow_id"),
        nullable=False,
    )

    snapshot_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    snapshot_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    created_by: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    created_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    modified_by: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    modified_date: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="TRUE",
    )

    __table_args__ = (
        UniqueConstraint(
            "lineage_flow_id",
            "snapshot_name",
            name="uq_lineage_snapshot_flow_name",
        ),
        Index(
            "idx_lineage_snapshot_flow",
            "lineage_flow_id",
        ),
        Index(
            "idx_lineage_snapshot_name",
            "snapshot_name",
        ),
        Index(
            "idx_lineage_snapshot_date",
            "snapshot_date",
        ),
        Index(
            "idx_lineage_snapshot_status",
            "status",
        ),
    )
