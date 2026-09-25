"""Add business domain and source system to DataAsset

Revision ID: 97d2b1dccf12
Revises: e2d453a0ad03
Create Date: 2026-09-25 08:37:42.425809

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97d2b1dccf12'
down_revision: Union[str, Sequence[str], None] = 'e2d453a0ad03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema.

    Assumption: For this initial rollout of the Data Asset Metadata capability,
    there are no existing production records in the `data_asset` table.
    We are safely adding `business_domain` as a non-null column without
    resorting to a synthetic default like 'default_domain'.
    """
    op.add_column('data_asset', sa.Column('business_domain', sa.String(length=100), nullable=True))

    # Since we documented the assumption that there are NO existing production records,
    # we can safely alter the column to non-nullable without any backfilling or
    # synthetic updates.
    op.alter_column('data_asset', 'business_domain', nullable=False)

    op.add_column('data_asset', sa.Column('source_system_id', sa.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key('fk_data_asset_source_system_id', 'data_asset', 'source_system', ['source_system_id'], ['source_system_id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_data_asset_source_system_id', 'data_asset', type_='foreignkey')
    op.drop_column('data_asset', 'source_system_id')
    op.drop_column('data_asset', 'business_domain')
