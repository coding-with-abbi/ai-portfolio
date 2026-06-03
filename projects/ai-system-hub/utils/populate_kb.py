"""
Utility script to populate the knowledge base with sample documents.

Usage:
    python utils/populate_kb.py
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from rag.retriever import retriever
from monitoring.logger import system_logger as logger

# Sample documents about AI/ML topics
SAMPLE_DOCUMENTS = [
    {
        "text": """
        BERT (Bidirectional Encoder Representations from Transformers) is a language representation model 
        developed by Google in 2018. It uses a transformer architecture and is trained on a large corpus 
        of unlabeled text through masked language modeling and next sentence prediction tasks.
        
        BERT's bidirectional nature allows it to understand context from both left and right sides of a token,
        making it highly effective for tasks like question answering, named entity recognition, and text classification.
        """,
        "metadata": {"source": "bert_overview.md", "category": "nlp", "year": 2018}
    },
    {
        "text": """
        GPT (Generative Pre-trained Transformer) is an autoregressive language model that uses transformer 
        architecture. Unlike BERT, GPT is unidirectional and generates text by predicting the next token 
        based on previous context.
        
        GPT-4, released in 2023, is a multimodal model capable of processing both text and images. It demonstrates
        significant improvements in reasoning, creativity, and factual accuracy compared to previous versions.
        """,
        "metadata": {"source": "gpt_overview.md", "category": "nlp", "year": 2023}
    },
    {
        "text": """
        RAG (Retrieval-Augmented Generation) combines information retrieval with text generation. It retrieves
        relevant documents from a knowledge base and uses them as context for generating responses.
        
        The RAG pipeline typically consists of: 1) Embedding the query, 2) Retrieving similar documents from
        a vector database, 3) Re-ranking results, 4) Generating a response conditioned on retrieved context.
        This approach reduces hallucinations and allows LLMs to access up-to-date information.
        """,
        "metadata": {"source": "rag_explained.md", "category": "architecture", "year": 2020}
    },
    {
        "text": """
        ChromaDB is an open-source embedding database designed for AI applications. It provides a simple
        Python API for storing and querying embeddings with metadata filtering capabilities.
        
        ChromaDB supports both in-memory and persistent storage, making it suitable for development and
        production environments. It integrates well with popular frameworks like LangChain and LlamaIndex.
        """,
        "metadata": {"source": "chromadb_guide.md", "category": "tools", "year": 2023}
    },
    {
        "text": """
        LangChain is a framework for developing applications powered by language models. It provides
        abstractions for chains, agents, and tools that simplify building complex LLM workflows.
        
        Key components include: Prompts (templates for LLM inputs), Chains (sequences of calls),
        Agents (autonomous decision-makers), and Memory (conversation history management).
        """,
        "metadata": {"source": "langchain_intro.md", "category": "frameworks", "year": 2023}
    },
    {
        "text": """
        Vector databases store high-dimensional embeddings and enable efficient similarity search.
        Common distance metrics include cosine similarity, Euclidean distance, and dot product.
        
        Popular vector databases include Pinecone, Weaviate, Qdrant, and Milvus. Each offers different
        trade-offs in terms of scalability, speed, and features like filtering and multi-tenancy.
        """,
        "metadata": {"source": "vector_db_comparison.md", "category": "databases", "year": 2023}
    }
]

async def populate():
    """Populate the knowledge base with sample documents"""
    
    logger.info("🚀 Starting knowledge base population...")
    
    texts = [doc["text"].strip() for doc in SAMPLE_DOCUMENTS]
    metadatas = [doc["metadata"] for doc in SAMPLE_DOCUMENTS]
    
    try:
        await retriever.add_knowledge(texts=texts, metadatas=metadatas)
        logger.info(f"✅ Successfully added {len(texts)} documents to knowledge base")
        
        # Print stats
        stats = retriever.vector_store.get_stats()
        logger.info(f"📊 Vector store stats: {stats}")
        
    except Exception as e:
        logger.error(f"❌ Failed to populate knowledge base: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(populate())
