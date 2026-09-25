from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api import lineage_router, metadata_asset_router
from app.db.session import get_db


app = FastAPI(
    title="Enterprise Data Governance Platform",
    version="0.1.0",
)

app.include_router(
    lineage_router,
    prefix="/api/v1",
)

app.include_router(
    metadata_asset_router,
    prefix="/api/v1",
)


@app.get("/health")
def health_check():
    return {
        "status": "UP",
        "service": "enterprise-data-governance-platform",
    }


@app.get("/health/db")
def database_health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "status": "UP",
        "database": "connected",
    }
