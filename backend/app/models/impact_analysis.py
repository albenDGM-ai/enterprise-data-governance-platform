import uuid
from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, Index, Integer, String, TIMESTAMP, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ImpactAnalysis(Base):
    __tablename__ = "impact_analysis"

    impact_analysis_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    lineage_mapping_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("lineage_mapping.lineage_mapping_id"),
        nullable=False,
    )
    analysis_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    source_asset: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    impact_scope: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    affected_objects: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    analysis_date: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
    )
    requested_by: Mapped[str] = mapped_column(
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
            "analysis_number",
            name="uq_impact_analysis_number",
        ),
        Index(
            "idx_impact_analysis_number",
            "analysis_number",
        ),
        Index(
            "idx_impact_analysis_scope",
            "impact_scope",
        ),
        Index(
            "idx_impact_analysis_date",
            "analysis_date",
        ),
        Index(
            "idx_impact_analysis_status",
            "status",
        ),
    )
