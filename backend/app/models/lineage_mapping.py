import uuid
from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, Index, String, TIMESTAMP, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DataLineageMapping(Base):
    __tablename__ = "lineage_mapping"

    lineage_mapping_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    lineage_flow_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("lineage_flow.lineage_flow_id"),
        nullable=False,
    )
    lineage_transformation_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("lineage_transformation.lineage_transformation_id"),
        nullable=True,
    )
    source_attribute: Mapped[str] = mapped_column(String(255), nullable=False)
    target_attribute: Mapped[str] = mapped_column(String(255), nullable=False)
    mapping_type: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False)
    created_by: Mapped[str] = mapped_column(String(100), nullable=False)
    created_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    modified_by: Mapped[str | None] = mapped_column(String(100), nullable=True)
    modified_date: Mapped[datetime | None] = mapped_column(TIMESTAMP, nullable=True)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="TRUE",
    )

    __table_args__ = (
        UniqueConstraint(
            "lineage_flow_id",
            "source_attribute",
            "target_attribute",
            name="uq_lineage_mapping_flow_source_target",
        ),
        Index("idx_lineage_mapping_flow", "lineage_flow_id"),
        Index("idx_lineage_mapping_source", "source_attribute"),
        Index("idx_lineage_mapping_target", "target_attribute"),
        Index("idx_lineage_mapping_status", "status"),
    )
