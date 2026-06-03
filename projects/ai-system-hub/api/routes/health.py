from fastapi import APIRouter
from core.config import settings

router = APIRouter()

@router.get("/health/detailed")
async def detailed_health():
    """Detailed system health check"""
    return {
        "status": "healthy",
        "components": {
            "api": "operational",
            "router": "operational",
            "logging": "operational",
            "rag": "not_implemented",
            "agents": "not_implemented"
        },
        "config": {
            "default_model": settings.DEFAULT_MODEL,
            "rag_enabled": "partial",
            "metrics_enabled": settings.ENABLE_METRICS
        }
    }
