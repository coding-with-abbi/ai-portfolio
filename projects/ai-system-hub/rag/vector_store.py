import chromadb
from chromadb.config import Settings as ChromaSettings
from core.config import settings
from core.models import RetrievedChunk
from monitoring.logger import system_logger as logger
from typing import List, Dict, Any, Optional
import uuid

class VectorStore:
    """Vector store using ChromaDB for similarity search"""
    
    def __init__(self):
        # Initialize ChromaDB with persistent storage
        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PERSIST_DIRECTORY,
            settings=ChromaSettings(anonymized_telemetry=False)
        )
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name="knowledge_base",
            metadata={"description": "Main knowledge base for RAG"}
        )
        
        logger.info(f"📚 Vector store initialized at {settings.CHROMA_PERSIST_DIRECTORY}")
        logger.info(f"Collection 'knowledge_base' has {self.collection.count()} documents")
    
    def add_documents(
        self, 
        texts: List[str], 
        embeddings: List[List[float]], 
        metadatas: Optional[List[Dict[str, Any]]] = None,
        ids: Optional[List[str]] = None
    ):
        """Add documents to the vector store"""
        
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in texts]
        
        if metadatas is None:
            metadatas = [{} for _ in texts]
        
        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        
        logger.info(f"Added {len(texts)} documents to vector store")
    
    def search(
        self, 
        query_embedding: List[float], 
        top_k: int = None,
        filter_metadata: Optional[Dict[str, Any]] = None
    ) -> List[RetrievedChunk]:
        """Search for similar documents"""
        
        if top_k is None:
            top_k = settings.RAG_TOP_K
        
        # Query ChromaDB
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=filter_metadata
        )
        
        # Convert to RetrievedChunk objects
        chunks = []
        if results["documents"][0]:  # Check if we got results
            for i, doc in enumerate(results["documents"][0]):
                chunk = RetrievedChunk(
                    content=doc,
                    source=results["metadatas"][0][i].get("source", "unknown"),
                    metadata=results["metadatas"][0][i],
                    score=1.0 - results["distances"][0][i]  # Convert distance to similarity
                )
                chunks.append(chunk)
        
        logger.debug(f"Retrieved {len(chunks)} chunks from vector store")
        return chunks
    
    def delete_collection(self):
        """Delete the entire collection (use with caution!)"""
        self.client.delete_collection(name="knowledge_base")
        logger.warning("⚠️ Deleted knowledge_base collection")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the vector store"""
        return {
            "total_documents": self.collection.count(),
            "collection_name": self.collection.name,
            "persist_directory": settings.CHROMA_PERSIST_DIRECTORY
        }

# Global instance
vector_store = VectorStore()
