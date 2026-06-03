from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import time
import uuid
from datetime import datetime

from core.config import settings
from core.models import QueryRequest, QueryResponse, QueryMetadata, QueryType, ModelProvider
from core.router import QueryRouter
from monitoring.logger import SystemLogger

# Initialize monitoring
logger = SystemLogger()

# Lifespan context manager for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("🚀 AI System Hub starting...")
    logger.info(f"Environment: {settings.LOG_LEVEL}")
    
    # Initialize router
    app.state.router = QueryRouter()
    
    yield
    
    # Shutdown
    logger.info("👋 AI System Hub shutting down...")

# Create FastAPI app
app = FastAPI(
    title="AI System Hub",
    description="Production-grade AI platform with RAG, agents, and intelligent routing",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    request.state.start_time = time.time()
    
    logger.info(f"📥 Request {request_id}: {request.method} {request.url.path}")
    
    response = await call_next(request)
    
    latency = (time.time() - request.state.start_time) * 1000
    logger.info(f"📤 Response {request_id}: {response.status_code} ({latency:.2f}ms)")
    
    return response

# Health check
@app.get("/health")
async def health_check():
    """System health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }

# Main query endpoint
@app.post("/api/v1/query", response_model=QueryResponse)
async def process_query(query_request: QueryRequest, request: Request):
    """
    Process a user query through the AI system hub.
    
    The system will:
    1. Route the query (RAG / Agent / Direct)
    2. Select the appropriate model
    3. Generate a response
    4. Log everything for monitoring
    """
    try:
        request_id = request.state.request_id
        start_time = time.time()
        
        logger.info(f"Processing query for user {query_request.user_id}: '{query_request.query[:50]}...'")
        
        # Route and process query
        router = request.state.router
        result = await router.route_and_execute(query_request)
        
        # Calculate metrics
        latency_ms = (time.time() - start_time) * 1000
        
        # Build metadata
        metadata = QueryMetadata(
            request_id=request_id,
            timestamp=datetime.utcnow(),
            query_type=result["query_type"],
            model_used=result["model_used"],
            provider=result["provider"],
            tokens_used=result.get("tokens_used", 0),
            cost_usd=result.get("cost_usd", 0.0),
            latency_ms=latency_ms,
            rag_chunks_retrieved=result.get("chunks_retrieved")
        )
        
        # Log the interaction
        logger.log_query(
            request_id=request_id,
            user_id=query_request.user_id,
            query=query_request.query,
            response=result["response"],
            metadata=metadata.model_dump()
        )
        
        return QueryResponse(
            response=result["response"],
            metadata=metadata,
            sources=result.get("sources")
        )
        
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Query processing failed: {str(e)}")

# Metrics endpoint
if settings.ENABLE_METRICS:
    @app.get("/metrics")
    async def get_metrics():
        """Get system metrics (Prometheus format)"""
        return logger.get_metrics()

# Include additional routes
from api.routes import health
from monitoring import dashboard as dash

app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(dash.router, tags=["monitoring"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api.gateway:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True,
        log_level=settings.LOG_LEVEL.lower()
    )
