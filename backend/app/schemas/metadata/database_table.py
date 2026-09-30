from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict, Field

from app.schemas.common import APIBaseSchema


class DatabaseTableCreate(APIBaseSchema):
    database_schema_id: UUID
    table_name: str = Field(..., min_length=1, max_length=200)
    display_name: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    table_type: str = Field(..., max_length=50)
    row_count: int | None = None
    owner: str = Field(..., max_length=100)
    classification: str = Field(..., max_length=50)
    status: str = Field(..., max_length=30)
    is_active: bool = True


class DatabaseTableUpdate(APIBaseSchema):
    table_name: str | None = Field(None, min_length=1, max_length=200)
    display_name: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = None
    table_type: str | None = Field(None, max_length=50)
    row_count: int | None = None
    owner: str | None = Field(None, max_length=100)
    classification: str | None = Field(None, max_length=50)
    status: str | None = Field(None, max_length=30)
    is_active: bool | None = None


class DatabaseTableResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    database_table_id: UUID
    database_schema_id: UUID
    table_name: str
    display_name: str
    description: str | None = None
    table_type: str
    row_count: int | None = None
    owner: str
    classification: str
    status: str
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
