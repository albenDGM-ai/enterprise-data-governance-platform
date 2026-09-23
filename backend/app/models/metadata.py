import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Text, BigInt, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base

class SourceSystem(Base):
    __tablename__ = 'source_system'
    source_system_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    system_code = Column(String(50), nullable=False, unique=True)
    system_name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    system_type = Column(String(50), nullable=False)
    vendor = Column(String(100), nullable=True)
    business_domain = Column(String(100), nullable=False)
    environment = Column(String(30), nullable=False)
    owner = Column(String(100), nullable=False)
    steward = Column(String(100), nullable=False)
    status = Column(String(30), nullable=False)
    created_by = Column(String(100), nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    modified_by = Column(String(100), nullable=True)
    modified_date = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
    is_active = Column(Boolean, nullable=False, default=True)

class DatabaseCatalog(Base):
    __tablename__ = 'database'
    database_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_system_id = Column(UUID(as_uuid=True), ForeignKey('source_system.source_system_id'), nullable=False)
    database_name = Column(String(150), nullable=False)
    database_type = Column(String(50), nullable=False)
    version = Column(String(30), nullable=True)
    description = Column(Text, nullable=True)
    owner = Column(String(100), nullable=False)
    status = Column(String(30), nullable=False)
    created_by = Column(String(100), nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    modified_by = Column(String(100), nullable=True)
    modified_date = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
    is_active = Column(Boolean, nullable=False, default=True)

class DatabaseSchema(Base):
    __tablename__ = 'schema'
    database_schema_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    database_id = Column(UUID(as_uuid=True), ForeignKey('database.database_id'), nullable=False)
    schema_name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    owner = Column(String(100), nullable=False)
    status = Column(String(30), nullable=False)
    created_by = Column(String(100), nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    modified_by = Column(String(100), nullable=True)
    modified_date = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
    is_active = Column(Boolean, nullable=False, default=True)

class DatabaseTable(Base):
    __tablename__ = 'table'
    database_table_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    database_schema_id = Column(UUID(as_uuid=True), ForeignKey('schema.database_schema_id'), nullable=False)
    table_name = Column(String(200), nullable=False)
    display_name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    table_type = Column(String(50), nullable=False)
    row_count = Column(BigInt, nullable=True)
    owner = Column(String(100), nullable=False)
    classification = Column(String(50), nullable=False)
    status = Column(String(30), nullable=False)
    created_by = Column(String(100), nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    modified_by = Column(String(100), nullable=True)
    modified_date = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
    is_active = Column(Boolean, nullable=False, default=True)
