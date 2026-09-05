import uuid
from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, Index, String, TIMESTAMP, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DataLineageFlow(Base):
    __tablename__ = "lineage_flow"

    lineage_flow_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    lineage_source_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("lineage_source.lineage_source_id"),
        nullable=False,
    )
    lineage_process_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("lineage_process.lineage_process_id"),
        nullable=False,
    )
    flow_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    flow_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    direction: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    frequency: Mapped[str] = mapped_column(
        String(50),
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
            "flow_name",
            name="uq_lineage_flow_name",
        ),
        Index(
            "idx_lineage_flow_name",
            "flow_name",
        ),
        Index(
            "idx_lineage_flow_source",
            "lineage_source_id",
        ),
        Index(
            "idx_lineage_flow_process",
            "lineage_process_id",
        ),
        Index(
            "idx_lineage_flow_status",
            "status",
        ),
    )
