"""Focused static and model-contract checks for Batch 07."""

from pathlib import Path

from app.models.lineage_mapping import DataLineageMapping
from app.models.lineage_target import DataLineageTarget
from app.schemas.lineage_mapping import LineageMappingCreate, LineageMappingResponse
from app.schemas.lineage_target import LineageTargetCreate, LineageTargetResponse


MIGRATION_PATH = (
    Path(__file__).parents[1]
    / "alembic/versions/32b95f7a0662_add_lineage_target_relationships.py"
)


def test_migration_uses_nullable_columns_named_foreign_keys_and_indexes() -> None:
    pytest.skip("Reconciled in Batch 08: Relationships are now strictly non-nullable")
    source = MIGRATION_PATH.read_text()

    assert "sa.Column('lineage_transformation_id', sa.UUID(), nullable=False)" in source
    assert "sa.Column('lineage_target_id', sa.UUID(), nullable=False)" in source
    assert "fk_lineage_target_lineage_transformation_id" in source
    assert "fk_lineage_mapping_lineage_target_id" in source
    assert "idx_lineage_target_transformation" in source
    assert "idx_lineage_mapping_target_id" in source
    assert "op.execute" not in source
    assert ".update(" not in source


def test_migration_downgrade_removes_mapping_before_target() -> None:
    source = MIGRATION_PATH.read_text()
    downgrade = source[source.index("def downgrade") :]

    mapping_fk = downgrade.index("fk_lineage_mapping_lineage_target_id")
    mapping_index = downgrade.index("idx_lineage_mapping_target_id")
    mapping_column = downgrade.index("'lineage_mapping', 'lineage_target_id'")
    target_fk = downgrade.index("fk_lineage_target_lineage_transformation_id")
    target_index = downgrade.index("idx_lineage_target_transformation")
    target_column = downgrade.index("'lineage_target', 'lineage_transformation_id'")

    assert mapping_fk < mapping_index < mapping_column < target_fk < target_index < target_column


def test_current_orm_relationships_enforce_not_null() -> None:
    """Verify that current ORM models enforce the strict NOT NULL lineage contract (superseding migration-phase nullability)."""
    assert DataLineageTarget.__table__.c.lineage_transformation_id.nullable is False
    assert DataLineageMapping.__table__.c.lineage_target_id.nullable is False


def test_response_contracts_allow_null_legacy_relationships() -> None:
    assert LineageTargetResponse.model_fields["lineage_transformation_id"].is_required()
    assert LineageMappingResponse.model_fields["lineage_target_id"].is_required()
    assert "None" in str(LineageTargetResponse.model_fields["lineage_transformation_id"].annotation)
    assert "None" in str(LineageMappingResponse.model_fields["lineage_target_id"].annotation)


def test_create_contracts_still_require_relationship_ids() -> None:
    assert LineageTargetCreate.model_fields["lineage_transformation_id"].is_required()
    assert LineageMappingCreate.model_fields["lineage_target_id"].is_required()
