import uuid
from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, Index, Integer, String, Text, TIMESTAMP, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DataLineageTransformation(Base):
    __tablename__ = "lineage_transformation"

    lineage_transformation_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    lineage_flow_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("lineage_flow.lineage_flow_id"),
        nullable=False,
    )
    sequence_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    transformation_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    transformation_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
    expression: Mapped[str | None] = mapped_column(
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
            "sequence_number",
            name="uq_lineage_transformation_flow_sequence",
        ),
        Index(
            "idx_lineage_transformation_flow",
            "lineage_flow_id",
        ),
        Index(
            "idx_lineage_transformation_sequence",
            "sequence_number",
        ),
        Index(
            "idx_lineage_transformation_type",
            "transformation_type",
        ),
        Index(
            "idx_lineage_transformation_status",
            "status",
        ),
    )
