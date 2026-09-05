import uuid

from sqlalchemy import Boolean, Index, String, TIMESTAMP, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DataLineageTarget(Base):
    __tablename__ = "lineage_target"

    lineage_target_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    target_name: Mapped[str] = mapped_column(String(255), nullable=False)
    target_type: Mapped[str] = mapped_column(String(100), nullable=False)
    system_name: Mapped[str] = mapped_column(String(150), nullable=False)
    business_domain: Mapped[str] = mapped_column(String(150), nullable=False)
    owner: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False)
    created_by: Mapped[str] = mapped_column(String(100), nullable=False)
    created_date: Mapped[object] = mapped_column(TIMESTAMP, nullable=False)
    modified_by: Mapped[str | None] = mapped_column(String(100), nullable=True)
    modified_date: Mapped[object | None] = mapped_column(TIMESTAMP, nullable=True)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="TRUE",
    )

    __table_args__ = (
        UniqueConstraint(
            "target_name",
            "system_name",
            name="uq_lineage_target_name_system",
        ),
        Index("idx_lineage_target_name", "target_name"),
        Index("idx_lineage_target_type", "target_type"),
        Index("idx_lineage_target_system", "system_name"),
        Index("idx_lineage_target_status", "status"),
    )
