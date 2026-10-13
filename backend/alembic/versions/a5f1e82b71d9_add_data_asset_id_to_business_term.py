"""Add data_asset_id to BusinessTerm

Revision ID: a5f1e82b71d9
Revises: 97d2b1dccf12
Create Date: 2026-10-02 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5f1e82b71d9'
down_revision: Union[str, Sequence[str], None] = '97d2b1dccf12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'business_term',
        sa.Column('data_asset_id', sa.UUID(as_uuid=True), nullable=True)
    )
    op.create_foreign_key(
        'fk_business_term_data_asset_id',
        'business_term',
        'data_asset',
        ['data_asset_id'],
        ['data_asset_id'],
    )
    op.create_index(
        'idx_business_term_data_asset',
        'business_term',
        ['data_asset_id'],
        unique=False
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('idx_business_term_data_asset', table_name='business_term')
    op.drop_constraint('fk_business_term_data_asset_id', 'business_term', type_='foreignkey')
    op.drop_column('business_term', 'data_asset_id')
