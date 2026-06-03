from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """System-wide configuration"""
    
    # API Keys
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_DEPLOYMENT: str = "gpt-4"
    AZURE_OPENAI_API_VERSION: str = "2023-12-01-preview"
    
    ANTHROPIC_API_KEY: Optional[str] = None
    
    # Database
    POSTGRES_URL: Optional[str] = None
    
    # Vector Store
    CHROMA_PERSIST_DIRECTORY: str = "./data/vector_store"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    
    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_WORKERS: int = 4
    
    # Model Routing
    DEFAULT_MODEL: str = "gpt-4"
    FAST_MODEL: str = "gpt-3.5-turbo"
    LONG_CONTEXT_MODEL: str = "claude-3-5-sonnet"
    
    # RAG
    RAG_TOP_K: int = 5
    RAG_SIMILARITY_THRESHOLD: float = 0.7
    RERANK_TOP_N: int = 3
    
    # Monitoring
    LOG_LEVEL: str = "INFO"
    ENABLE_METRICS: bool = True
    METRICS_PORT: int = 9090
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Global settings instance
settings = Settings()
