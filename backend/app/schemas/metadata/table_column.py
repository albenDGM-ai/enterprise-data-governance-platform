from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict, Field

from app.schemas.common import APIBaseSchema


class TableColumnCreate(APIBaseSchema):
    database_table_id: UUID
    column_name: str = Field(..., min_length=1, max_length=200)
    display_name: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    logical_data_type: str = Field(..., max_length=50)
    nullable: bool = True
    primary_key_flag: bool = False
    foreign_key_flag: bool = False
    classification: str = Field(..., max_length=50)
    critical_data_element_flag: bool = False
    ordinal_position: int = Field(..., ge=1)
    is_active: bool = True


class TableColumnUpdate(APIBaseSchema):
    column_name: str | None = Field(None, min_length=1, max_length=200)
    display_name: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = None
    logical_data_type: str | None = Field(None, max_length=50)
    nullable: bool | None = None
    primary_key_flag: bool | None = None
    foreign_key_flag: bool | None = None
    classification: str | None = Field(None, max_length=50)
    critical_data_element_flag: bool | None = None
    ordinal_position: int | None = Field(None, ge=1)
    is_active: bool | None = None


class TableColumnResponse(APIBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    table_column_id: UUID
    database_table_id: UUID
    column_name: str
    display_name: str
    description: str | None = None
    logical_data_type: str
    nullable: bool
    primary_key_flag: bool
    foreign_key_flag: bool
    classification: str
    critical_data_element_flag: bool
    ordinal_position: int
    created_by: str
    created_date: datetime
    modified_by: str | None = None
    modified_date: datetime | None = None
    is_active: bool
