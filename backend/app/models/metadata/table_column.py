import uuid

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    TIMESTAMP,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class TableColumn(Base):
    __tablename__ = "column"

    table_column_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    database_table_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("table.database_table_id"),
        nullable=False,
    )

    column_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    display_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    logical_data_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    nullable: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    primary_key_flag: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    foreign_key_flag: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    classification: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    critical_data_element_flag: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    ordinal_position: Mapped[int] = mapped_column(
        Integer,
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
            "database_table_id",
            "column_name",
            name="uq_column_table_name",
        ),
        Index("idx_column_name", "column_name"),
        Index("idx_column_cde", "critical_data_element_flag"),
        Index("idx_column_datatype", "logical_data_type"),
    )
