from typing import Optional, Dict, Any
from datetime import datetime

class PromptTemplate:
    """Base class for prompt templates"""
    
    def __init__(self, name: str, template: str, version: str = "1.0"):
        self.name = name
        self.template = template
        self.version = version
    
    def format(self, **kwargs) -> str:
        """Format the template with provided variables"""
        return self.template.format(**kwargs)

class PromptEngine:
    """Prompt engineering engine for consistent LLM interactions"""
    
    def __init__(self):
        self.templates = self._init_templates()
    
    def _init_templates(self) -> Dict[str, PromptTemplate]:
        """Initialize predefined templates"""
        
        return {
            "rag_qa": PromptTemplate(
                name="RAG Q&A",
                template="""You are a helpful AI assistant. Answer the user's question based on the provided context.

**Context:**
{context}

**User Question:**
{query}

**Instructions:**
- Answer based solely on the provided context
- If the context doesn't contain enough information, say so
- Be concise but comprehensive
- Cite sources when possible

**Answer:**"""
            ),
            
            "direct_qa": PromptTemplate(
                name="Direct Q&A",
                template="""You are a helpful AI assistant. Answer the following question concisely and accurately.

**Question:** {query}

**Answer:**"""
            ),
            
            "summarization": PromptTemplate(
                name="Summarization",
                template="""Summarize the following text concisely while preserving key information.

**Text:**
{text}

**Summary:**"""
            ),
            
            "conversation": PromptTemplate(
                name="Conversation",
                template="""You are a helpful AI assistant having a conversation with a user.

**Conversation History:**
{history}

**User:** {query}

**Assistant:**"""
            )
        }
    
    def build_rag_prompt(
        self, 
        query: str, 
        context: str,
        custom_instructions: Optional[str] = None
    ) -> str:
        """Build a prompt for RAG-based Q&A"""
        
        template = self.templates["rag_qa"]
        
        # Add custom instructions if provided
        if custom_instructions:
            modified_template = template.template.replace(
                "**Answer:**",
                f"**Additional Instructions:**\n{custom_instructions}\n\n**Answer:**"
            )
            return modified_template.format(query=query, context=context)
        
        return template.format(query=query, context=context)
    
    def build_direct_prompt(self, query: str) -> str:
        """Build a prompt for direct Q&A (no RAG)"""
        return self.templates["direct_qa"].format(query=query)
    
    def build_conversation_prompt(
        self, 
        query: str, 
        history: list[Dict[str, str]]
    ) -> str:
        """Build a prompt for conversational interaction"""
        
        # Format history
        history_str = "\n".join([
            f"**User:** {msg['query']}\n**Assistant:** {msg['response']}"
            for msg in history
        ])
        
        return self.templates["conversation"].format(
            query=query,
            history=history_str if history else "(No previous conversation)"
        )
    
    def add_template(self, template: PromptTemplate):
        """Add a custom template"""
        self.templates[template.name] = template
    
    def get_template(self, name: str) -> Optional[PromptTemplate]:
        """Get a template by name"""
        return self.templates.get(name)
    
    def list_templates(self) -> list[str]:
        """List all available template names"""
        return list(self.templates.keys())

# Global instance
prompt_engine = PromptEngine()
