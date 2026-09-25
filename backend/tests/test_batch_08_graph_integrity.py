"""Focused service-level checks for Batch 08 lineage graph invariants."""

from types import SimpleNamespace
from uuid import uuid4

import pytest

from app.models.lineage_mapping import DataLineageMapping
from app.models.lineage_target import DataLineageTarget
from app.schemas.lineage_mapping import LineageMappingResponse
from app.schemas.lineage_target import LineageTargetResponse
from app.services.lineage_mapping_service import LineageMappingService
from app.services.lineage_target_service import LineageTargetService
from app.services.lineage_validation import LineageRelationshipValidationError


class StubRepository:
    def __init__(self, records=None):
        self.records = records or {}
        self.created = []
        self.updated = []

    def get_by_id(self, record_id, *, include_inactive=False):
        return self.records.get(record_id)

    def get_by_attributes(self, *args, **kwargs):
        return None

    def get_by_name(self, *args, **kwargs):
        return None

    def create(self, entity):
        self.created.append(entity)
        return entity

    def update(self, entity):
        self.updated.append(entity)
        return entity


def record(record_id, *, is_active=True, lineage_flow_id=None, lineage_transformation_id=None):
    return SimpleNamespace(
        lineage_flow_id=lineage_flow_id,
        lineage_target_id=record_id,
        lineage_transformation_id=lineage_transformation_id or record_id,
        is_active=is_active,
    )


def mapping_service(*, flow, target=None, transformations=()):
    service = LineageMappingService(session=object())
    service.repository = StubRepository()
    service.flow_repository = StubRepository({flow.lineage_flow_id: flow})
    service.target_repository = StubRepository(
        {} if target is None else {target.lineage_target_id: target}
    )
    service.transformation_repository = StubRepository(
        {item.lineage_transformation_id: item for item in transformations}
    )
    return service


def create_mapping(service, *, flow_id, target_id, transformation_id=None):
    return service.create(
        lineage_flow_id=flow_id,
        lineage_target_id=target_id,
        lineage_transformation_id=transformation_id,
        source_attribute="source.customer_id",
        target_attribute="target.customer_id",
        mapping_type="DIRECT",
        status="ACTIVE",
        created_by="batch-08-test",
    )


def test_valid_mapping_uses_the_target_transformation_flow() -> None:
    flow_id = uuid4()
    transformation_id = uuid4()
    target_id = uuid4()
    flow = SimpleNamespace(lineage_flow_id=flow_id, is_active=True)
    transformation = record(transformation_id, lineage_flow_id=flow_id)
    target = record(target_id, lineage_transformation_id=transformation_id)
    service = mapping_service(
        flow=flow,
        target=target,
        transformations=(transformation,),
    )

    mapping = create_mapping(
        service,
        flow_id=flow_id,
        target_id=target_id,
        transformation_id=transformation_id,
    )

    assert mapping.lineage_flow_id == flow_id
    assert service.repository.created == [mapping]


def test_cross_flow_target_mapping_is_rejected_before_persistence() -> None:
    flow_a_id, flow_b_id, transformation_id, target_id = (uuid4() for _ in range(4))
    service = mapping_service(
        flow=SimpleNamespace(lineage_flow_id=flow_a_id, is_active=True),
        target=record(target_id, lineage_transformation_id=transformation_id),
        transformations=(record(transformation_id, lineage_flow_id=flow_b_id),),
    )

    with pytest.raises(LineageRelationshipValidationError, match="different Lineage Flow"):
        create_mapping(service, flow_id=flow_a_id, target_id=target_id)

    assert service.repository.created == []


def test_cross_flow_mapping_transformation_is_rejected() -> None:
    flow_a_id, flow_b_id, transformation_id, target_id = (uuid4() for _ in range(4))
    target_transformation = uuid4()
    service = mapping_service(
        flow=SimpleNamespace(lineage_flow_id=flow_a_id, is_active=True),
        target=record(target_id, lineage_transformation_id=target_transformation),
        transformations=(
            record(target_transformation, lineage_flow_id=flow_a_id),
            record(transformation_id, lineage_flow_id=flow_b_id),
        ),
    )

    with pytest.raises(LineageRelationshipValidationError, match="different Lineage Flow"):
        create_mapping(
            service,
            flow_id=flow_a_id,
            target_id=target_id,
            transformation_id=transformation_id,
        )


def test_mapping_transformation_must_own_its_target() -> None:
    flow_id, target_transformation_id, supplied_transformation_id, target_id = (
        uuid4() for _ in range(4)
    )
    service = mapping_service(
        flow=SimpleNamespace(lineage_flow_id=flow_id, is_active=True),
        target=record(target_id, lineage_transformation_id=target_transformation_id),
        transformations=(
            record(target_transformation_id, lineage_flow_id=flow_id),
            record(supplied_transformation_id, lineage_flow_id=flow_id),
        ),
    )

    with pytest.raises(LineageRelationshipValidationError, match="does not own"):
        create_mapping(
            service,
            flow_id=flow_id,
            target_id=target_id,
            transformation_id=supplied_transformation_id,
        )


def test_inactive_parent_relationships_are_rejected() -> None:
    flow_id, transformation_id, target_id = (uuid4() for _ in range(3))
    service = mapping_service(
        flow=SimpleNamespace(lineage_flow_id=flow_id, is_active=False),
        target=record(target_id, lineage_transformation_id=transformation_id),
        transformations=(record(transformation_id, lineage_flow_id=flow_id),),
    )

    with pytest.raises(LineageRelationshipValidationError, match="Flow is inactive"):
        create_mapping(service, flow_id=flow_id, target_id=target_id)

    target_service = LineageTargetService(session=object())
    target_service.repository = StubRepository()
    target_service.flow_repository = StubRepository({flow_id: SimpleNamespace(is_active=True)})
    target_service.transformation_repository = StubRepository(
        {transformation_id: record(transformation_id, is_active=False, lineage_flow_id=flow_id)}
    )
    with pytest.raises(LineageRelationshipValidationError, match="Transformation is inactive"):
        target_service.create(
            lineage_transformation_id=transformation_id,
            target_name="customer",
            target_type="TABLE",
            system_name="warehouse",
            business_domain="sales",
            owner="steward",
            status="ACTIVE",
            created_by="batch-08-test",
        )


def test_target_update_rejects_a_cross_flow_replacement() -> None:
    flow_a_id, flow_b_id, trans_a_id, trans_b_id, target_id = (uuid4() for _ in range(5))
    service = LineageTargetService(session=object())
    service.repository = StubRepository()
    service.flow_repository = StubRepository({
        flow_a_id: SimpleNamespace(lineage_flow_id=flow_a_id, is_active=True),
        flow_b_id: SimpleNamespace(lineage_flow_id=flow_b_id, is_active=True),
    })
    service.transformation_repository = StubRepository({
        trans_a_id: record(trans_a_id, lineage_flow_id=flow_a_id),
        trans_b_id: record(trans_b_id, lineage_flow_id=flow_b_id),
    })

    entity = SimpleNamespace(
        lineage_target_id=target_id,
        lineage_transformation_id=trans_a_id,
        target_name="t1",
        system_name="s1",
    )

    with pytest.raises(LineageRelationshipValidationError, match="different Lineage Flow"):
        service.update(
            entity,
            modified_by="batch-08-test",
            lineage_transformation_id=trans_b_id,
        )

    assert service.repository.updated == []

def test_update_rejects_a_cross_flow_replacement() -> None:
    flow_a_id, flow_b_id, transformation_a_id, transformation_b_id, target_a_id, target_b_id = (
        uuid4() for _ in range(6)
    )
    service = mapping_service(
        flow=SimpleNamespace(lineage_flow_id=flow_a_id, is_active=True),
        target=record(target_b_id, lineage_transformation_id=transformation_b_id),
        transformations=(record(transformation_b_id, lineage_flow_id=flow_b_id),),
    )
    entity = SimpleNamespace(
        lineage_mapping_id=uuid4(),
        lineage_flow_id=flow_a_id,
        lineage_target_id=target_a_id,
        lineage_transformation_id=transformation_a_id,
        source_attribute="source.customer_id",
        target_attribute="target.customer_id",
    )

    with pytest.raises(LineageRelationshipValidationError, match="different Lineage Flow"):
        service.update(
            entity,
            modified_by="batch-08-test",
            lineage_target_id=target_b_id,
        )

    assert service.repository.updated == []


def test_legacy_null_relationships_remain_readable() -> None:
    assert DataLineageTarget.__table__.c.lineage_transformation_id.nullable is False
    assert DataLineageMapping.__table__.c.lineage_target_id.nullable is False
    assert "None" in str(LineageTargetResponse.model_fields["lineage_transformation_id"].annotation)
    assert "None" in str(LineageMappingResponse.model_fields["lineage_target_id"].annotation)


def test_transformation_update_contract_does_not_expose_flow_reassignment() -> None:
    from app.schemas.lineage_transformation import LineageTransformationUpdate

    fields = LineageTransformationUpdate.model_fields

    assert "lineage_flow_id" not in fields
    assert "sequence_number" in fields
    assert "transformation_name" in fields
    assert "transformation_type" in fields
    assert "description" in fields
    assert "expression" in fields
    assert "status" in fields
