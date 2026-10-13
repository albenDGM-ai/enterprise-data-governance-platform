from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict, Field

from app.schemas.common import APIBaseSchema


class DatabaseSchemaCreate(APIBaseSchema):
    database_id: UUID
    schema_name: str = Field(..., min_length=1, max_length=150)
    description: str | None = None
    owner: str = Field(..., max_length=100)
    status: str = Field(..., max_length=30)
    is_active: bool = True


class DatabaseSchemaUpdate(APIBaseSchema):
    schema_name: str | None = Field(None, min_length=1, max_length=150)
    description: str | None = None
    owner: str | None = Field(None, max_length=100)
    status: str | None = Field(None, max_length=30)
    is_active: bool | None = None


class DatabaseSchemaResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    database_schema_id: UUID
    database_id: UUID
    schema_name: str
    description: str | None = None
    owner: str
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
