"""
Adapter to integrate the ai-workflow-orchestrator as an agent tool.

This allows the AI System Hub to delegate complex, multi-step tasks
to the existing workflow orchestrator.
"""

import sys
from pathlib import Path
from typing import Dict, Any
from monitoring.logger import system_logger as logger

# Add workflow orchestrator to path
workflow_path = Path(__file__).parent.parent.parent / "ai-workflow-orchestrator"
sys.path.insert(0, str(workflow_path))

try:
    from workflows.workflow_runner import WorkflowRunner
    from memory.state import WorkflowState, Plan, Task
    WORKFLOW_AVAILABLE = True
    logger.info("✅ Workflow orchestrator successfully imported")
except Exception as e:
    WORKFLOW_AVAILABLE = False
    logger.warning(f"⚠️ Workflow orchestrator not available: {e}")
    WorkflowRunner = None

class WorkflowAdapter:
    """Adapter for the ai-workflow-orchestrator"""
    
    def __init__(self):
        if not WORKFLOW_AVAILABLE:
            raise RuntimeError("Workflow orchestrator is not available")
        
        self.runner = None
        logger.info("🔧 Workflow adapter initialized")
    
    async def execute(self, task_description: str) -> Dict[str, Any]:
        """
        Execute a complex task using the workflow orchestrator.
        
        Args:
            task_description: Description of the task to perform
            
        Returns:
            Dict with response and metadata
        """
        
        logger.info(f"Executing workflow for: '{task_description[:50]}...'")
        
        try:
            # Create new runner for this task
            self.runner = WorkflowRunner()
            
            # Run the workflow
            self.runner.run(task_description)
            
            # Extract results
            plan = self.runner.state.plan
            results = self.runner.state.context_results
            
            # Build response from results
            response = self._build_response(plan, results)
            
            # Get monitoring metrics
            metrics = self.runner.monitor.metrics if hasattr(self.runner, 'monitor') else {}
            
            return {
                "success": True,
                "response": response,
                "tasks_completed": len(plan.tasks) if plan else 0,
                "metrics": metrics
            }
            
        except Exception as e:
            logger.error(f"Workflow execution failed: {e}")
            return {
                "success": False,
                "response": f"Workflow failed: {str(e)}",
                "tasks_completed": 0,
                "metrics": {}
            }
    
    def _build_response(self, plan, results: list) -> str:
        """Build a user-friendly response from workflow results"""
        
        if not results:
            return "The workflow completed but produced no results."
        
        # Combine results into a coherent response
        response_parts = [
            f"I've completed a {len(results)}-step workflow to address your request:\n"
        ]
        
        # Summarize results
        for i, result in enumerate(results, 1):
            preview = result[:150] + "..." if len(result) > 150 else result
            response_parts.append(f"{i}. {preview}")
        
        return "\n".join(response_parts)
    
    def is_available(self) -> bool:
        """Check if the workflow orchestrator is available"""
        return WORKFLOW_AVAILABLE

# Global instance
try:
    workflow_adapter = WorkflowAdapter()
except Exception as e:
    logger.warning(f"Could not initialize workflow adapter: {e}")
    workflow_adapter = None
