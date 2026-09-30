from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.metadata.data_asset import DataAssetCreate, DataAssetResponse
from app.schemas.metadata.database import DatabaseCreate, DatabaseResponse
from app.schemas.metadata.database_schema import DatabaseSchemaCreate, DatabaseSchemaResponse
from app.schemas.metadata.database_table import DatabaseTableCreate, DatabaseTableResponse
from app.schemas.metadata.source_system import SourceSystemCreate, SourceSystemResponse
from app.schemas.metadata.table_column import TableColumnCreate, TableColumnResponse
from app.services.database_schema_service import DatabaseSchemaService
from app.services.database_service import DatabaseService
from app.services.database_table_service import DatabaseTableService
from app.services.metadata_asset_service import DataAssetService
from app.services.source_system_service import SourceSystemService
from app.services.table_column_service import TableColumnService

router = APIRouter(prefix="/metadata", tags=["metadata"])


# --- SOURCE SYSTEM ENDPOINTS ---

@router.post(
    "/source-systems",
    response_model=SourceSystemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a source system",
)
def create_source_system(
    system_in: SourceSystemCreate,
    db: Session = Depends(get_db),
):
    """Register a new source system."""
    service = SourceSystemService(db)
    return service.create(system_in)


@router.get(
    "/source-systems/{source_system_id}",
    response_model=SourceSystemResponse,
    summary="Get a source system by ID",
)
def get_source_system(
    source_system_id: UUID,
    include_inactive: bool = Query(False, description="Include inactive systems"),
    db: Session = Depends(get_db),
):
    """Retrieve a source system by its ID."""
    service = SourceSystemService(db)
    return service.get(source_system_id, include_inactive=include_inactive)


@router.get(
    "/source-systems",
    response_model=list[SourceSystemResponse],
    summary="List source systems",
)
def list_source_systems(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    include_inactive: bool = Query(False, description="Include inactive systems"),
    db: Session = Depends(get_db),
):
    """List source systems."""
    service = SourceSystemService(db)
    return service.list(
        skip=skip,
        limit=limit,
        include_inactive=include_inactive,
    )


# --- DATABASE ENDPOINTS ---

@router.post(
    "/databases",
    response_model=DatabaseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a database catalog entry",
)
def create_database(
    db_in: DatabaseCreate,
    db: Session = Depends(get_db),
):
    """Register a new database under a source system."""
    service = DatabaseService(db)
    return service.create(db_in)


@router.get(
    "/databases/{database_id}",
    response_model=DatabaseResponse,
    summary="Get a database by ID",
)
def get_database(
    database_id: UUID,
    include_inactive: bool = Query(False, description="Include inactive databases"),
    db: Session = Depends(get_db),
):
    """Retrieve a database by its ID."""
    service = DatabaseService(db)
    return service.get(database_id, include_inactive=include_inactive)


@router.get(
    "/databases",
    response_model=list[DatabaseResponse],
    summary="List databases",
)
def list_databases(
    source_system_id: UUID | None = Query(None, description="Filter by source system ID"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    include_inactive: bool = Query(False, description="Include inactive databases"),
    db: Session = Depends(get_db),
):
    """List databases."""
    service = DatabaseService(db)
    return service.list(
        source_system_id=source_system_id,
        skip=skip,
        limit=limit,
        include_inactive=include_inactive,
    )


# --- SCHEMA ENDPOINTS ---

@router.post(
    "/schemas",
    response_model=DatabaseSchemaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a database schema entry",
)
def create_schema(
    schema_in: DatabaseSchemaCreate,
    db: Session = Depends(get_db),
):
    """Register a new schema under a database."""
    service = DatabaseSchemaService(db)
    return service.create(schema_in)


@router.get(
    "/schemas/{database_schema_id}",
    response_model=DatabaseSchemaResponse,
    summary="Get a schema by ID",
)
def get_schema(
    database_schema_id: UUID,
    include_inactive: bool = Query(False, description="Include inactive schemas"),
    db: Session = Depends(get_db),
):
    """Retrieve a database schema by its ID."""
    service = DatabaseSchemaService(db)
    return service.get(database_schema_id, include_inactive=include_inactive)


@router.get(
    "/schemas",
    response_model=list[DatabaseSchemaResponse],
    summary="List database schemas",
)
def list_schemas(
    database_id: UUID | None = Query(None, description="Filter by database ID"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    include_inactive: bool = Query(False, description="Include inactive schemas"),
    db: Session = Depends(get_db),
):
    """List database schemas."""
    service = DatabaseSchemaService(db)
    return service.list(
        database_id=database_id,
        skip=skip,
        limit=limit,
        include_inactive=include_inactive,
    )


# --- TABLE ENDPOINTS ---

@router.post(
    "/tables",
    response_model=DatabaseTableResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a database table entry",
)
def create_table(
    table_in: DatabaseTableCreate,
    db: Session = Depends(get_db),
):
    """Register a new table under a database schema."""
    service = DatabaseTableService(db)
    return service.create(table_in)


@router.get(
    "/tables/{database_table_id}",
    response_model=DatabaseTableResponse,
    summary="Get a table by ID",
)
def get_table(
    database_table_id: UUID,
    include_inactive: bool = Query(False, description="Include inactive tables"),
    db: Session = Depends(get_db),
):
    """Retrieve a table by its ID."""
    service = DatabaseTableService(db)
    return service.get(database_table_id, include_inactive=include_inactive)


@router.get(
    "/tables",
    response_model=list[DatabaseTableResponse],
    summary="List database tables",
)
def list_tables(
    database_schema_id: UUID | None = Query(None, description="Filter by database schema ID"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    include_inactive: bool = Query(False, description="Include inactive tables"),
    db: Session = Depends(get_db),
):
    """List database tables."""
    service = DatabaseTableService(db)
    return service.list(
        database_schema_id=database_schema_id,
        skip=skip,
        limit=limit,
        include_inactive=include_inactive,
    )


# --- COLUMN ENDPOINTS ---

@router.post(
    "/columns",
    response_model=TableColumnResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a table column entry",
)
def create_column(
    column_in: TableColumnCreate,
    db: Session = Depends(get_db),
):
    """Register a new column under a table."""
    service = TableColumnService(db)
    return service.create(column_in)


@router.get(
    "/columns/{table_column_id}",
    response_model=TableColumnResponse,
    summary="Get a column by ID",
)
def get_column(
    table_column_id: UUID,
    include_inactive: bool = Query(False, description="Include inactive columns"),
    db: Session = Depends(get_db),
):
    """Retrieve a column by its ID."""
    service = TableColumnService(db)
    return service.get(table_column_id, include_inactive=include_inactive)


@router.get(
    "/columns",
    response_model=list[TableColumnResponse],
    summary="List table columns",
)
def list_columns(
    database_table_id: UUID | None = Query(None, description="Filter by database table ID"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    include_inactive: bool = Query(False, description="Include inactive columns"),
    db: Session = Depends(get_db),
):
    """List table columns."""
    service = TableColumnService(db)
    return service.list(
        database_table_id=database_table_id,
        skip=skip,
        limit=limit,
        include_inactive=include_inactive,
    )


# --- DATA ASSET ENDPOINTS ---

@router.post(
    "/data-assets",
    response_model=DataAssetResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a data asset",
)
def create_data_asset(
    asset_in: DataAssetCreate,
    db: Session = Depends(get_db),
):
    """Register a new data asset."""
    service = DataAssetService(db)
    return service.create(asset_in)


@router.get(
    "/data-assets/{data_asset_id}",
    response_model=DataAssetResponse,
    summary="Get a data asset by ID",
)
def get_data_asset(
    data_asset_id: UUID,
    include_inactive: bool = Query(False, description="Include inactive assets"),
    db: Session = Depends(get_db),
):
    """Retrieve a data asset by its ID."""
    service = DataAssetService(db)
    return service.get(data_asset_id, include_inactive=include_inactive)


@router.get(
    "/data-assets",
    response_model=list[DataAssetResponse],
    summary="List data assets",
)
def list_data_assets(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    include_inactive: bool = Query(False, description="Include inactive assets"),
    db: Session = Depends(get_db),
):
    """List data assets."""
    service = DataAssetService(db)
    return service.list(
        skip=skip,
        limit=limit,
        include_inactive=include_inactive,
    )
