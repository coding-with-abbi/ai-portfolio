from core.models import QueryRequest, QueryType, RoutingDecision, ModelProvider
from core.config import settings
from monitoring.logger import system_logger as logger
from typing import Dict, Any

class QueryRouter:
    """
    Intelligent router that decides how to handle incoming queries.
    
    Decision flow:
    1. Analyze query characteristics
    2. Decide: RAG / Agent / Direct
    3. Select appropriate model
    4. Execute and return result
    """
    
    def __init__(self):
        logger.info("🧠 Query Router initialized")
        
        # Keywords for routing logic (simplified for MVP)
        self.rag_keywords = ["what is", "explain", "tell me about", "definition of", "how does"]
        self.agent_keywords = ["calculate", "find", "search for", "write", "create", "compare"]
    
    async def route_and_execute(self, query_request: QueryRequest) -> Dict[str, Any]:
        """Main routing and execution logic"""
        
        # Step 1: Decide query type
        decision = self._make_routing_decision(query_request.query)
        logger.info(f"Routing decision: {decision.query_type} (confidence: {decision.confidence:.2f})")
        
        # Step 2: Execute based on decision
        if decision.query_type == QueryType.RAG:
            return await self._execute_rag(query_request, decision)
        elif decision.query_type == QueryType.AGENT:
            return await self._execute_agent(query_request, decision)
        else:
            return await self._execute_direct(query_request, decision)
    
    def _make_routing_decision(self, query: str) -> RoutingDecision:
        """Analyze query and decide routing"""
        query_lower = query.lower()
        
        # Simple keyword-based routing (will be replaced with embedding-based classification)
        rag_score = sum(1 for kw in self.rag_keywords if kw in query_lower)
        agent_score = sum(1 for kw in self.agent_keywords if kw in query_lower)
        
        if rag_score > agent_score:
            return RoutingDecision(
                query_type=QueryType.RAG,
                confidence=0.8,
                reasoning="Query contains knowledge-seeking keywords",
                recommended_model=settings.DEFAULT_MODEL
            )
        elif agent_score > 0:
            return RoutingDecision(
                query_type=QueryType.AGENT,
                confidence=0.7,
                reasoning="Query requires tools/actions",
                recommended_model=settings.DEFAULT_MODEL
            )
        else:
            return RoutingDecision(
                query_type=QueryType.DIRECT,
                confidence=0.6,
                reasoning="Simple query, direct LLM call sufficient",
                recommended_model=settings.FAST_MODEL
            )
    
    async def _execute_rag(self, query_request: QueryRequest, decision: RoutingDecision) -> Dict[str, Any]:
        """Execute RAG pipeline"""
        logger.info("📚 Executing RAG pipeline...")
        
        # Import here to avoid circular dependency
        from rag.retriever import retriever
        from llm.prompt_engine import prompt_engine
        from llm.model_router import model_router
        
        try:
            # Retrieve relevant chunks
            chunks = await retriever.retrieve(
                query=query_request.query,
                rerank=True,
                use_mmr=False
            )
            
            if not chunks:
                logger.warning("No relevant chunks found, falling back to direct LLM")
                return await self._execute_direct(query_request, decision)
            
            # Build context from chunks
            context = retriever.build_context(chunks)
            
            # Build prompt with context
            prompt = prompt_engine.build_rag_prompt(
                query=query_request.query,
                context=context
            )
            
            # Select model
            model = model_router.select_model(
                query=query_request.query,
                context=context,
                requires_reasoning=False
            )
            
            # Generate response
            llm_result = await model_router.generate(prompt, model=model)
            
            # Build sources list
            sources = [
                {
                    "source": chunk.source,
                    "metadata": chunk.metadata,
                    "score": chunk.score
                }
                for chunk in chunks
            ]
            
            return {
                "response": llm_result["response"],
                "query_type": QueryType.RAG,
                "model_used": llm_result["model"],
                "provider": llm_result["provider"],
                "tokens_used": llm_result["tokens_used"],
                "cost_usd": llm_result["cost_usd"],
                "chunks_retrieved": len(chunks),
                "sources": sources
            }
            
        except Exception as e:
            logger.error(f"RAG pipeline failed: {e}")
            logger.info("Falling back to direct LLM")
            return await self._execute_direct(query_request, decision)
    
    async def _execute_agent(self, query_request: QueryRequest, decision: RoutingDecision) -> Dict[str, Any]:
        """Execute agent workflow"""
        logger.info("🤖 Executing agent workflow...")
        
        try:
            from agents.workflow_adapter import workflow_adapter
            
            if workflow_adapter is None or not workflow_adapter.is_available():
                logger.warning("Workflow orchestrator not available, falling back to direct LLM")
                return await self._execute_direct(query_request, decision)
            
            # Execute the workflow
            result = await workflow_adapter.execute(query_request.query)
            
            if not result["success"]:
                logger.error(f"Workflow failed: {result['response']}")
                return await self._execute_direct(query_request, decision)
            
            # Estimate token usage (workflow doesn't track this yet)
            estimated_tokens = len(result["response"].split()) * 2  # Rough estimate
            
            return {
                "response": result["response"],
                "query_type": QueryType.AGENT,
                "model_used": decision.recommended_model,
                "provider": ModelProvider.AZURE_OPENAI,
                "tokens_used": estimated_tokens,
                "cost_usd": estimated_tokens / 1000 * 0.06,  # Rough estimate
                "tasks_completed": result["tasks_completed"]
            }
            
        except Exception as e:
            logger.error(f"Agent execution failed: {e}")
            logger.info("Falling back to direct LLM")
            return await self._execute_direct(query_request, decision)
    
    async def _execute_direct(self, query_request: QueryRequest, decision: RoutingDecision) -> Dict[str, Any]:
        """Execute direct LLM call"""
        logger.info("⚡ Executing direct LLM call...")
        
        from llm.prompt_engine import prompt_engine
        from llm.model_router import model_router
        
        try:
            # Build simple prompt
            prompt = prompt_engine.build_direct_prompt(query=query_request.query)
            
            # Select model (direct calls can use faster model)
            model = model_router.select_model(
                query=query_request.query,
                requires_reasoning=False
            )
            
            # Generate response
            llm_result = await model_router.generate(prompt, model=model)
            
            return {
                "response": llm_result["response"],
                "query_type": QueryType.DIRECT,
                "model_used": llm_result["model"],
                "provider": llm_result["provider"],
                "tokens_used": llm_result["tokens_used"],
                "cost_usd": llm_result["cost_usd"],
            }
            
        except Exception as e:
            logger.error(f"Direct LLM call failed: {e}")
            return {
                "response": f"I apologize, but I encountered an error: {str(e)}",
                "query_type": QueryType.DIRECT,
                "model_used": "error",
                "provider": ModelProvider.AZURE_OPENAI,
                "tokens_used": 0,
                "cost_usd": 0.0,
            }
