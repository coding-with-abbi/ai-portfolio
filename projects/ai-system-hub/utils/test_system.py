"""
Quick test script to verify the system is working end-to-end.

Usage:
    python utils/test_system.py
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.models import QueryRequest
from core.router import QueryRouter
from monitoring.logger import system_logger as logger

async def test_query(query: str, query_type_expected: str):
    """Test a single query"""
    logger.info(f"\n{'='*60}\nTesting: {query}\nExpected type: {query_type_expected}\n{'='*60}")
    
    router = QueryRouter()
    request = QueryRequest(
        query=query,
        user_id="test_user",
        session_id="test_session"
    )
    
    try:
        result = await router.route_and_execute(request)
        
        logger.info(f"✅ Response generated successfully")
        logger.info(f"   Query Type: {result['query_type']}")
        logger.info(f"   Model Used: {result['model_used']}")
        logger.info(f"   Tokens: {result['tokens_used']}")
        logger.info(f"   Cost: ${result['cost_usd']:.4f}")
        logger.info(f"   Response Preview: {result['response'][:150]}...")
        
        if result.get('sources'):
            logger.info(f"   Sources: {len(result['sources'])} chunks retrieved")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Run all tests"""
    logger.info("🧪 Starting system tests...\n")
    
    tests = [
        ("What is BERT?", "RAG"),  # Should retrieve from KB
        ("What is the capital of France?", "DIRECT"),  # Simple knowledge question
        ("Explain the theory of relativity", "DIRECT"),  # No KB match, direct
    ]
    
    results = []
    for query, expected_type in tests:
        result = await test_query(query, expected_type)
        results.append(result)
        await asyncio.sleep(1)  # Rate limiting
    
    # Summary
    logger.info(f"\n{'='*60}")
    logger.info(f"TEST SUMMARY: {sum(results)}/{len(results)} passed")
    logger.info(f"{'='*60}\n")

if __name__ == "__main__":
    asyncio.run(main())
