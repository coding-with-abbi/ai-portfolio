from core.models import RetrievedChunk
from monitoring.logger import system_logger as logger
from typing import List
from sentence_transformers import CrossEncoder
import numpy as np

class Reranker:
    """Re-rank retrieved documents for better relevance"""
    
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        """
        Initialize cross-encoder for re-ranking.
        
        Args:
            model_name: HuggingFace model for cross-encoding
        """
        try:
            self.model = CrossEncoder(model_name)
            logger.info(f"🎯 Reranker initialized with model: {model_name}")
        except Exception as e:
            logger.warning(f"Failed to load reranker model, will use original scores: {e}")
            self.model = None
    
    def rerank(self, query: str, chunks: List[RetrievedChunk], top_n: int = 3) -> List[RetrievedChunk]:
        """
        Re-rank chunks using cross-encoder.
        
        Args:
            query: The user's query
            chunks: Retrieved chunks from vector store
            top_n: Number of top chunks to return
            
        Returns:
            Re-ranked and filtered chunks
        """
        
        if not chunks:
            return []
        
        if self.model is None:
            # Fallback: use original scores
            logger.debug("Using original similarity scores (no reranker)")
            sorted_chunks = sorted(chunks, key=lambda x: x.score, reverse=True)
            return sorted_chunks[:top_n]
        
        # Prepare query-document pairs
        pairs = [[query, chunk.content] for chunk in chunks]
        
        # Get cross-encoder scores
        scores = self.model.predict(pairs)
        
        # Update chunk scores and sort
        for chunk, score in zip(chunks, scores):
            chunk.score = float(score)
        
        # Sort by new scores and return top N
        reranked = sorted(chunks, key=lambda x: x.score, reverse=True)[:top_n]
        
        logger.debug(f"Reranked {len(chunks)} chunks, returning top {len(reranked)}")
        return reranked
    
    def mmr_rerank(
        self, 
        query_embedding: List[float], 
        chunks: List[RetrievedChunk], 
        lambda_param: float = 0.7,
        top_n: int = 3
    ) -> List[RetrievedChunk]:
        """
        Maximal Marginal Relevance (MMR) re-ranking for diversity.
        
        Args:
            query_embedding: Query embedding vector
            chunks: Retrieved chunks
            lambda_param: Balance between relevance (1.0) and diversity (0.0)
            top_n: Number of chunks to return
            
        Returns:
            Diversified set of chunks
        """
        
        if not chunks or len(chunks) <= top_n:
            return chunks
        
        selected = []
        remaining = chunks.copy()
        
        # Select first chunk (highest similarity)
        best_chunk = max(remaining, key=lambda x: x.score)
        selected.append(best_chunk)
        remaining.remove(best_chunk)
        
        # Iteratively select chunks using MMR
        while len(selected) < top_n and remaining:
            mmr_scores = []
            
            for candidate in remaining:
                # Relevance score
                relevance = candidate.score
                
                # Max similarity to already selected chunks
                similarities = [
                    self._cosine_similarity(candidate.content, sel.content)
                    for sel in selected
                ]
                max_sim = max(similarities) if similarities else 0
                
                # MMR formula
                mmr = lambda_param * relevance - (1 - lambda_param) * max_sim
                mmr_scores.append((candidate, mmr))
            
            # Select best MMR score
            best_candidate = max(mmr_scores, key=lambda x: x[1])[0]
            selected.append(best_candidate)
            remaining.remove(best_candidate)
        
        logger.debug(f"MMR reranking: selected {len(selected)} diverse chunks")
        return selected
    
    def _cosine_similarity(self, text1: str, text2: str) -> float:
        """Simple word-overlap based similarity (fallback)"""
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0.0

# Global instance
reranker = Reranker()
