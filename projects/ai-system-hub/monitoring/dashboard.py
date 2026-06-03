"""
Simple web-based monitoring dashboard using FastAPI's templating.
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from monitoring.logger import system_logger
import json

router = APIRouter()

# Set up templates
templates_dir = Path(__file__).parent / "templates"
templates_dir.mkdir(exist_ok=True)
templates = Jinja2Templates(directory=str(templates_dir))

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Monitoring dashboard page"""
    
    # Get metrics
    metrics = system_logger.get_metrics()
    
    # Calculate summary stats
    total_requests = sum(m["total_requests"] for m in metrics.values())
    total_cost = sum(m["total_cost_usd"] for m in metrics.values())
    avg_latency = sum(m["avg_latency_ms"] * m["total_requests"] for m in metrics.values()) / total_requests if total_requests > 0 else 0
    
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "metrics": metrics,
        "total_requests": total_requests,
        "total_cost": total_cost,
        "avg_latency": avg_latency
    })

@router.get("/metrics/json")
async def metrics_json():
    """Get metrics as JSON"""
    return system_logger.get_metrics()
