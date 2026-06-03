from rag.embeddings import embedding_service
from rag.vector_store import vector_store
from rag.reranker import reranker
from core.models import RetrievedChunk
from core.config import settings
from monitoring.logger import system_logger as logger
from typing import List, Dict, Any

class Retriever:
    """Main retrieval orchestrator for RAG pipeline"""
    
    def __init__(self):
        self.embedding_service = embedding_service
        self.vector_store = vector_store
        self.reranker = reranker
        logger.info("🔍 Retriever initialized")
    
    async def retrieve(
        self, 
        query: str,
        top_k: int = None,
        rerank: bool = True,
        use_mmr: bool = False
    ) -> List[RetrievedChunk]:
        """
        Retrieve relevant chunks for a query.
        
        Pipeline:
        1. Generate query embedding
        2. Search vector store
        3. Filter by similarity threshold
        4. Re-rank (optional)
        5. Return top chunks
        
        Args:
            query: User's query
            top_k: Number of chunks to retrieve (before reranking)
            rerank: Whether to rerank results
            use_mmr: Use MMR for diversity
            
        Returns:
            List of relevant chunks
        """
        
        if top_k is None:
            top_k = settings.RAG_TOP_K
        
        logger.info(f"Retrieving chunks for query: '{query[:50]}...'")
        
        # Step 1: Generate query embedding
        query_embedding = await self.embedding_service.embed_query(query)
        
        # Step 2: Search vector store
        chunks = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k * 2  # Get more for reranking
        )
        
        if not chunks:
            logger.warning("No chunks retrieved from vector store")
            return []
        
        logger.debug(f"Retrieved {len(chunks)} initial chunks")
        
        # Step 3: Filter by threshold
        filtered_chunks = [
            chunk for chunk in chunks 
            if chunk.score >= settings.RAG_SIMILARITY_THRESHOLD
        ]
        
        if not filtered_chunks:
            logger.warning(f"No chunks passed similarity threshold ({settings.RAG_SIMILARITY_THRESHOLD})")
            return []
        
        logger.debug(f"{len(filtered_chunks)} chunks passed threshold filter")
        
        # Step 4: Re-rank
        if rerank and len(filtered_chunks) > 1:
            if use_mmr:
                final_chunks = self.reranker.mmr_rerank(
                    query_embedding=query_embedding,
                    chunks=filtered_chunks,
                    top_n=settings.RERANK_TOP_N
                )
            else:
                final_chunks = self.reranker.rerank(
                    query=query,
                    chunks=filtered_chunks,
                    top_n=settings.RERANK_TOP_N
                )
        else:
            final_chunks = filtered_chunks[:settings.RERANK_TOP_N]
        
        logger.info(f"✅ Final retrieval: {len(final_chunks)} chunks (avg score: {sum(c.score for c in final_chunks) / len(final_chunks):.3f})")
        
        return final_chunks
    
    def build_context(self, chunks: List[RetrievedChunk]) -> str:
        """Build context string from retrieved chunks"""
        
        if not chunks:
            return ""
        
        context_parts = []
        for i, chunk in enumerate(chunks, 1):
            source = chunk.metadata.get("source", "unknown")
            context_parts.append(
                f"[Context {i} - Source: {source}, Relevance: {chunk.score:.2f}]\n{chunk.content}\n"
            )
        
        return "\n".join(context_parts)
    
    async def add_knowledge(
        self,
        texts: List[str],
        metadatas: List[Dict[str, Any]] = None
    ):
        """Add new documents to the knowledge base"""
        
        logger.info(f"Adding {len(texts)} documents to knowledge base...")
        
        # Generate embeddings
        embeddings = await self.embedding_service.embed_documents(texts)
        
        # Add to vector store
        self.vector_store.add_documents(
            texts=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )
        
        logger.info("✅ Documents added successfully")

# Global instance
retriever = Retriever()
