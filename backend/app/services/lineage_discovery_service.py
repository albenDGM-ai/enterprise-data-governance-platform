from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lineage_flow import DataLineageFlow
from app.models.lineage_mapping import DataLineageMapping
from app.models.lineage_process import DataLineageProcess
from app.models.lineage_source import DataLineageSource
from app.models.lineage_target import DataLineageTarget
from app.models.lineage_transformation import DataLineageTransformation


class LineageDiscoveryService:
    """
    Read-only service for assembling the persisted
    lineage chain into a single discovery response.

    Physical lineage structure:

        Source
          |
        Process
          |
        Flow
          |
    Transformation
          |
        Target
          |
        Mapping
    """

    def __init__(self, db: Session):
        self.session = db

    def discover(
        self,
        *,
        lineage_source_id: UUID | None = None,
        lineage_process_id: UUID | None = None,
        lineage_flow_id: UUID | None = None,
        include_inactive: bool = False,
    ) -> list[dict]:
        flow_stmt = select(DataLineageFlow)

        if not include_inactive:
            flow_stmt = flow_stmt.where(
                DataLineageFlow.is_active.is_(True)
            )

        if lineage_source_id is not None:
            flow_stmt = flow_stmt.where(
                DataLineageFlow.lineage_source_id == lineage_source_id
            )

        if lineage_process_id is not None:
            flow_stmt = flow_stmt.where(
                DataLineageFlow.lineage_process_id == lineage_process_id
            )

        if lineage_flow_id is not None:
            flow_stmt = flow_stmt.where(
                DataLineageFlow.lineage_flow_id == lineage_flow_id
            )

        flows = self.session.scalars(
            flow_stmt.order_by(DataLineageFlow.flow_name)
        ).all()

        results: list[dict] = []

        for flow in flows:
            source = self.session.get(
                DataLineageSource,
                flow.lineage_source_id,
            )
            process = self.session.get(
                DataLineageProcess,
                flow.lineage_process_id,
            )

            if source is None or process is None:
                continue

            transformation_stmt = select(
                DataLineageTransformation
            ).where(
                DataLineageTransformation.lineage_flow_id
                == flow.lineage_flow_id
            )

            if not include_inactive:
                transformation_stmt = transformation_stmt.where(
                    DataLineageTransformation.is_active.is_(True)
                )

            transformations = self.session.scalars(
                transformation_stmt.order_by(
                    DataLineageTransformation.sequence_number
                )
            ).all()

            transformation_results = []

            for transformation in transformations:
                target_stmt = select(DataLineageTarget).where(
                    DataLineageTarget.lineage_transformation_id
                    == transformation.lineage_transformation_id
                )

                if not include_inactive:
                    target_stmt = target_stmt.where(
                        DataLineageTarget.is_active.is_(True)
                    )

                targets = self.session.scalars(
                    target_stmt.order_by(DataLineageTarget.target_name)
                ).all()

                target_results = []

                for target in targets:
                    mapping_stmt = select(DataLineageMapping).where(
                        DataLineageMapping.lineage_target_id
                        == target.lineage_target_id
                    )

                    if not include_inactive:
                        mapping_stmt = mapping_stmt.where(
                            DataLineageMapping.is_active.is_(True)
                        )

                    mappings = self.session.scalars(
                        mapping_stmt.order_by(
                            DataLineageMapping.source_attribute,
                            DataLineageMapping.target_attribute,
                        )
                    ).all()

                    target_results.append(
                        {
                            "lineage_target_id": target.lineage_target_id,
                            "lineage_transformation_id": (
                                target.lineage_transformation_id
                            ),
                            "target_name": target.target_name,
                            "target_type": target.target_type,
                            "system_name": target.system_name,
                            "business_domain": target.business_domain,
                            "owner": target.owner,
                            "status": target.status,
                            "is_active": target.is_active,
                            "mappings": mappings,
                        }
                    )

                transformation_results.append(
                    {
                        "lineage_transformation_id": (
                            transformation.lineage_transformation_id
                        ),
                        "sequence_number": transformation.sequence_number,
                        "transformation_name": transformation.transformation_name,
                        "transformation_type": transformation.transformation_type,
                        "description": transformation.description,
                        "expression": transformation.expression,
                        "status": transformation.status,
                        "is_active": transformation.is_active,
                        "targets": target_results,
                    }
                )

            results.append(
                {
                    "source": source,
                    "process": process,
                    "flow": flow,
                    "transformations": transformation_results,
                }
            )

        return results
