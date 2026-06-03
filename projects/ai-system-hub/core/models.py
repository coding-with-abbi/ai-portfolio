from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import Enum

class QueryType(str, Enum):
    """Types of queries the system can handle"""
    RAG = "rag"              # Needs context retrieval
    AGENT = "agent"          # Needs tools/actions
    DIRECT = "direct"        # Simple LLM call

class ModelProvider(str, Enum):
    """Supported model providers"""
    AZURE_OPENAI = "azure_openai"
    ANTHROPIC = "anthropic"
    LOCAL = "local"

# Request Models
class QueryRequest(BaseModel):
    """Incoming query from user"""
    query: str = Field(..., min_length=1, description="User's input query")
    user_id: str = Field(..., description="Unique user identifier")
    session_id: Optional[str] = Field(None, description="Session ID for context")
    context: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional context")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "What is BERT and how does it work?",
                "user_id": "user_123",
                "session_id": "session_456",
                "context": {"domain": "nlp"}
            }
        }

# Response Models
class QueryMetadata(BaseModel):
    """Metadata about query processing"""
    request_id: str
    timestamp: datetime
    query_type: QueryType
    model_used: str
    provider: ModelProvider
    tokens_used: int
    cost_usd: float
    latency_ms: float
    rag_chunks_retrieved: Optional[int] = None
    

class QueryResponse(BaseModel):
    """Response to user query"""
    response: str
    metadata: QueryMetadata
    sources: Optional[List[Dict[str, Any]]] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "response": "BERT (Bidirectional Encoder Representations from Transformers) is...",
                "metadata": {
                    "request_id": "req_abc123",
                    "timestamp": "2026-01-06T12:00:00Z",
                    "query_type": "rag",
                    "model_used": "gpt-4",
                    "provider": "azure_openai",
                    "tokens_used": 450,
                    "cost_usd": 0.0135,
                    "latency_ms": 1250,
                    "rag_chunks_retrieved": 3
                },
                "sources": [
                    {"document": "bert_paper.pdf", "page": 1, "score": 0.92}
                ]
            }
        }

# Internal Models
class RetrievedChunk(BaseModel):
    """A chunk retrieved from vector store"""
    content: str
    source: str
    metadata: Dict[str, Any]
    score: float

class RoutingDecision(BaseModel):
    """Router's decision on how to handle query"""
    query_type: QueryType
    confidence: float
    reasoning: str
    recommended_model: str
