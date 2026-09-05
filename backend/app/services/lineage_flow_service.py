from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.lineage_flow import DataLineageFlow
from app.repositories.lineage_flow_repository import LineageFlowRepository
from app.repositories.lineage_process_repository import LineageProcessRepository
from app.repositories.lineage_source_repository import LineageSourceRepository


class LineageFlowService:
    """Business operations for Lineage Flow."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = LineageFlowRepository(session)
        self.source_repository = LineageSourceRepository(session)
        self.process_repository = LineageProcessRepository(session)

    def get(
        self,
        lineage_flow_id: uuid.UUID,
        *,
        include_inactive: bool = False,
    ) -> DataLineageFlow | None:
        return self.repository.get_by_id(
            lineage_flow_id,
            include_inactive=include_inactive,
        )

    def list(
        self,
        *,
        status: str | None = None,
        flow_type: str | None = None,
        direction: str | None = None,
        owner: str | None = None,
        lineage_source_id: uuid.UUID | None = None,
        lineage_process_id: uuid.UUID | None = None,
        include_inactive: bool = False,
    ) -> list[DataLineageFlow]:
        return self.repository.list(
            status=status,
            flow_type=flow_type,
            direction=direction,
            owner=owner,
            lineage_source_id=lineage_source_id,
            lineage_process_id=lineage_process_id,
            include_inactive=include_inactive,
        )

    def create(
        self,
        *,
        flow_name: str,
        lineage_source_id: uuid.UUID,
        lineage_process_id: uuid.UUID,
        flow_type: str,
        direction: str,
        frequency: str,
        owner: str,
        status: str,
        created_by: str,
    ) -> DataLineageFlow:
        source = self.source_repository.get_by_id(
            lineage_source_id,
        )

        if source is None:
            raise ValueError(
                "The supplied Lineage Source does not exist or is inactive."
            )

        process = self.process_repository.get_by_id(
            lineage_process_id,
        )

        if process is None:
            raise ValueError(
                "The supplied Lineage Process does not exist or is inactive."
            )

        existing = self.repository.get_by_name(
            flow_name,
            include_inactive=True,
        )

        if existing is not None:
            raise ValueError(
                "A Lineage Flow with the supplied Flow Name already exists."
            )

        entity = DataLineageFlow(
            lineage_flow_id=uuid.uuid4(),
            lineage_source_id=lineage_source_id,
            lineage_process_id=lineage_process_id,
            flow_name=flow_name,
            flow_type=flow_type,
            direction=direction,
            frequency=frequency,
            owner=owner,
            status=status,
            created_by=created_by,
            created_date=datetime.now(timezone.utc).replace(tzinfo=None),
            is_active=True,
        )

        self.repository.create(entity)
        return entity

    def update(
        self,
        entity: DataLineageFlow,
        *,
        modified_by: str,
        flow_name: str | None = None,
        lineage_source_id: uuid.UUID | None = None,
        lineage_process_id: uuid.UUID | None = None,
        flow_type: str | None = None,
        direction: str | None = None,
        frequency: str | None = None,
        owner: str | None = None,
        status: str | None = None,
    ) -> DataLineageFlow:
        new_flow_name = flow_name if flow_name is not None else entity.flow_name

        duplicate = self.repository.get_by_name(
            new_flow_name,
            include_inactive=True,
        )
        if duplicate is not None and duplicate.lineage_flow_id != entity.lineage_flow_id:
            raise ValueError(
                "A Lineage Flow with the same flow name already exists."
            )

        if lineage_source_id is not None:
            source = self.source_repository.get_by_id(
                lineage_source_id,
            )

            if source is None:
                raise ValueError(
                    "The supplied Lineage Source does not exist "
                    "or is inactive."
                )

            entity.lineage_source_id = lineage_source_id

        if lineage_process_id is not None:
            process = self.process_repository.get_by_id(
                lineage_process_id,
            )

            if process is None:
                raise ValueError(
                    "The supplied Lineage Process does not exist "
                    "or is inactive."
                )

            entity.lineage_process_id = lineage_process_id

        if flow_name is not None:
            entity.flow_name = flow_name

        if flow_type is not None:
            entity.flow_type = flow_type

        if direction is not None:
            entity.direction = direction

        if frequency is not None:
            entity.frequency = frequency

        if owner is not None:
            entity.owner = owner

        if status is not None:
            entity.status = status

        entity.modified_by = modified_by
        entity.modified_date = datetime.now(timezone.utc).replace(tzinfo=None)

        self.repository.update(entity)
        return entity

    def delete(
        self,
        entity: DataLineageFlow,
        *,
        modified_by: str,
    ) -> DataLineageFlow:
        return self.repository.soft_delete(
            entity,
            modified_by=modified_by,
        )
