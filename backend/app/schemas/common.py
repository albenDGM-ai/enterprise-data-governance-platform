from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class APIBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class AuditResponseSchema(APIBaseSchema):
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None


class UUIDResponseSchema(APIBaseSchema):
    id: UUID
