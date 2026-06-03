from langchain_openai import AzureChatOpenAI
from core.config import settings
from monitoring.logger import system_logger as logger
from typing import Optional, Dict, Any

class AzureOpenAIProvider:
    """Azure OpenAI provider for LLM calls"""
    
    def __init__(self, deployment: Optional[str] = None, temperature: float = 0.7):
        """
        Initialize Azure OpenAI provider.
        
        Args:
            deployment: Azure deployment name (defaults to settings.DEFAULT_MODEL)
            temperature: Sampling temperature (0.0 = deterministic, 1.0 = creative)
        """
        self.deployment = deployment or settings.DEFAULT_MODEL
        self.temperature = temperature
        
        self.llm = AzureChatOpenAI(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
            azure_deployment=self.deployment,
            api_version=settings.AZURE_OPENAI_API_VERSION,
            temperature=self.temperature
        )
        
        logger.info(f"🤖 Azure OpenAI provider initialized (deployment: {self.deployment})")
    
    async def generate(
        self, 
        prompt: str,
        max_tokens: Optional[int] = None,
        stop_sequences: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Generate a response from the LLM.
        
        Args:
            prompt: The input prompt
            max_tokens: Maximum tokens to generate
            stop_sequences: Sequences that stop generation
            
        Returns:
            Dict with 'response', 'tokens_used', 'model'
        """
        try:
            # Make the call
            response = await self.llm.ainvoke(prompt)
            
            # Extract usage info
            usage = response.response_metadata.get("token_usage", {})
            
            result = {
                "response": response.content,
                "tokens_used": usage.get("total_tokens", 0),
                "prompt_tokens": usage.get("prompt_tokens", 0),
                "completion_tokens": usage.get("completion_tokens", 0),
                "model": self.deployment
            }
            
            logger.debug(f"Generated response ({result['tokens_used']} tokens)")
            return result
            
        except Exception as e:
            logger.error(f"Azure OpenAI generation failed: {e}")
            raise
    
    def calculate_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        """
        Calculate cost based on token usage.
        
        Prices (as of 2024):
        - GPT-4: $0.03/1K prompt, $0.06/1K completion
        - GPT-3.5-Turbo: $0.0015/1K prompt, $0.002/1K completion
        """
        if "gpt-4" in self.deployment.lower():
            cost = (prompt_tokens / 1000 * 0.03) + (completion_tokens / 1000 * 0.06)
        else:  # GPT-3.5
            cost = (prompt_tokens / 1000 * 0.0015) + (completion_tokens / 1000 * 0.002)
        
        return cost
