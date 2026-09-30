from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict, Field

from app.schemas.common import APIBaseSchema


class DatabaseCreate(APIBaseSchema):
    source_system_id: UUID
    database_name: str = Field(..., min_length=1, max_length=150)
    database_type: str = Field(..., max_length=50)
    version: str | None = Field(None, max_length=30)
    description: str | None = None
    owner: str = Field(..., max_length=100)
    status: str = Field(..., max_length=30)
    is_active: bool = True


class DatabaseUpdate(APIBaseSchema):
    database_name: str | None = Field(None, min_length=1, max_length=150)
    database_type: str | None = Field(None, max_length=50)
    version: str | None = Field(None, max_length=30)
    description: str | None = None
    owner: str | None = Field(None, max_length=100)
    status: str | None = Field(None, max_length=30)
    is_active: bool | None = None


class DatabaseResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    database_id: UUID
    source_system_id: UUID
    database_name: str
    database_type: str
    version: str | None = None
    description: str | None = None
    owner: str
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
