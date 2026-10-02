from app.api.routers.business_glossary import router as business_glossary_router
from app.api.routers.lineage import router as lineage_router
from app.api.routers.metadata_asset import router as metadata_asset_router

__all__ = ["business_glossary_router", "lineage_router", "metadata_asset_router"]
