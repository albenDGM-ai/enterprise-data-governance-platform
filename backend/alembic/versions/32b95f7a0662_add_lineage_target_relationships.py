"""add lineage target relationships

Revision ID: 32b95f7a0662
Revises: afddcea9037e
Create Date: 2026-09-06 14:45:26.612094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32b95f7a0662'
down_revision: Union[str, Sequence[str], None] = 'afddcea9037e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'lineage_target',
        sa.Column('lineage_transformation_id', sa.UUID(), nullable=True),
    )
    op.create_index('idx_lineage_target_transformation', 'lineage_target', ['lineage_transformation_id'], unique=False)
    op.create_foreign_key(
        'fk_lineage_target_lineage_transformation_id',
        'lineage_target',
        'lineage_transformation',
        ['lineage_transformation_id'],
        ['lineage_transformation_id'],
    )
    op.add_column(
        'lineage_mapping',
        sa.Column('lineage_target_id', sa.UUID(), nullable=True),
    )
    op.create_index('idx_lineage_mapping_target_id', 'lineage_mapping', ['lineage_target_id'], unique=False)
    op.create_foreign_key(
        'fk_lineage_mapping_lineage_target_id',
        'lineage_mapping',
        'lineage_target',
        ['lineage_target_id'],
        ['lineage_target_id'],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        'fk_lineage_mapping_lineage_target_id',
        'lineage_mapping',
        type_='foreignkey',
    )
    op.drop_index('idx_lineage_mapping_target_id', table_name='lineage_mapping')
    op.drop_column('lineage_mapping', 'lineage_target_id')
    op.drop_constraint(
        'fk_lineage_target_lineage_transformation_id',
        'lineage_target',
        type_='foreignkey',
    )
    op.drop_index('idx_lineage_target_transformation', table_name='lineage_target')
    op.drop_column('lineage_target', 'lineage_transformation_id')
