from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Task(BaseModel):
    id: int
    description: str
    tool_name: str
    tool_input: Optional[Dict[str, Any]] = None
    result: Optional[str] = None
    status: str = "pending"

class Plan(BaseModel):
    tasks: List[Task] = []

class WorkflowState(BaseModel):
    original_request: str
    plan: Optional[Plan] = None
    context_results: List[str] = []
