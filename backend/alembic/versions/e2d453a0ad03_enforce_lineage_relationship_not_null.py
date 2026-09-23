"""enforce lineage relationship not null

Revision ID: e2d453a0ad03
Revises: 32b95f7a0662
Create Date: 2026-09-14 21:40:21
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e2d453a0ad03"
down_revision: Union[str, Sequence[str], None] = "32b95f7a0662"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Enforce required lineage relationships."""

    op.alter_column(
        "lineage_mapping",
        "lineage_target_id",
        existing_type=sa.UUID(),
        nullable=False,
    )

    op.alter_column(
        "lineage_target",
        "lineage_transformation_id",
        existing_type=sa.UUID(),
        nullable=False,
    )


def downgrade() -> None:
    """Restore historical nullable relationship definitions."""

    op.alter_column(
        "lineage_target",
        "lineage_transformation_id",
        existing_type=sa.UUID(),
        nullable=True,
    )

    op.alter_column(
        "lineage_mapping",
        "lineage_target_id",
        existing_type=sa.UUID(),
        nullable=True,
    )
