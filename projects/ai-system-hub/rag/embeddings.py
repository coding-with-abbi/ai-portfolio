from langchain_openai import AzureOpenAIEmbeddings
from core.config import settings
from monitoring.logger import system_logger as logger
from typing import List
import numpy as np

class EmbeddingService:
    """Service for generating embeddings using Azure OpenAI"""
    
    def __init__(self):
        self.embeddings = AzureOpenAIEmbeddings(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
            azure_deployment=settings.EMBEDDING_MODEL,
            api_version=settings.AZURE_OPENAI_API_VERSION
        )
        logger.info(f"🔤 Embedding service initialized with model: {settings.EMBEDDING_MODEL}")
    
    async def embed_query(self, text: str) -> List[float]:
        """Generate embedding for a single query"""
        try:
            embedding = await self.embeddings.aembed_query(text)
            logger.debug(f"Generated embedding for query (dim={len(embedding)})")
            return embedding
        except Exception as e:
            logger.error(f"Failed to generate query embedding: {e}")
            raise
    
    async def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple documents"""
        try:
            embeddings = await self.embeddings.aembed_documents(texts)
            logger.debug(f"Generated {len(embeddings)} document embeddings")
            return embeddings
        except Exception as e:
            logger.error(f"Failed to generate document embeddings: {e}")
            raise
    
    def compute_similarity(self, embedding1: List[float], embedding2: List[float]) -> float:
        """Compute cosine similarity between two embeddings"""
        vec1 = np.array(embedding1)
        vec2 = np.array(embedding2)
        
        similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
        return float(similarity)

# Global instance
embedding_service = EmbeddingService()
