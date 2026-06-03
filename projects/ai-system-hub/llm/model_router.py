from core.config import settings
from core.models import ModelProvider
from llm.providers.azure_openai import AzureOpenAIProvider
from monitoring.logger import system_logger as logger
from typing import Dict, Any, Optional

class ModelRouter:
    """Intelligent model selection based on query characteristics"""
    
    def __init__(self):
        # Initialize providers
        self.providers = {
            "gpt-4": AzureOpenAIProvider(deployment=settings.DEFAULT_MODEL, temperature=0.7),
            "gpt-3.5": AzureOpenAIProvider(deployment=settings.FAST_MODEL, temperature=0.7),
        }
        logger.info("🎯 Model router initialized with providers: " + ", ".join(self.providers.keys()))
    
    def select_model(
        self, 
        query: str,
        context: Optional[str] = None,
        requires_reasoning: bool = False
    ) -> str:
        """
        Select the appropriate model based on query characteristics.
        
        Selection criteria:
        - Complex queries → GPT-4
        - Long context → GPT-4
        - Simple queries → GPT-3.5 (faster, cheaper)
        
        Args:
            query: The user's query
            context: Retrieved context (if RAG)
            requires_reasoning: Whether the query needs deep reasoning
            
        Returns:
            Model identifier
        """
        
        # Calculate complexity score
        query_length = len(query.split())
        context_length = len(context.split()) if context else 0
        
        # Decision logic
        if requires_reasoning:
            selected = "gpt-4"
            reason = "Requires complex reasoning"
        elif query_length > 50 or context_length > 1000:
            selected = "gpt-4"
            reason = "Long input (better comprehension needed)"
        elif any(keyword in query.lower() for keyword in ["compare", "analyze", "explain why", "reasoning"]):
            selected = "gpt-4"
            reason = "Complex analytical query"
        else:
            selected = "gpt-3.5"
            reason = "Simple query (optimize for speed/cost)"
        
        logger.debug(f"Model selection: {selected} ({reason})")
        return selected
    
    async def generate(
        self,
        prompt: str,
        model: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generate a response using the selected model.
        
        Args:
            prompt: The formatted prompt
            model: Model to use (if None, uses default)
            **kwargs: Additional parameters for generation
            
        Returns:
            Dict with response and metadata
        """
        
        if model is None:
            model = "gpt-4"
        
        provider = self.providers.get(model)
        if not provider:
            logger.warning(f"Model {model} not found, falling back to gpt-4")
            provider = self.providers["gpt-4"]
        
        # Generate response
        result = await provider.generate(prompt, **kwargs)
        
        # Calculate cost
        cost = provider.calculate_cost(
            result["prompt_tokens"],
            result["completion_tokens"]
        )
        
        return {
            **result,
            "cost_usd": cost,
            "provider": ModelProvider.AZURE_OPENAI
        }

# Global instance
model_router = ModelRouter()
