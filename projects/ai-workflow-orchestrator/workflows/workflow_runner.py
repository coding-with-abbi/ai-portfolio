from memory.state import WorkflowState, Plan, Task
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent

class WorkflowRunner:
    def __init__(self):
        self.state = WorkflowState(original_request="")
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
    
    def run(self, request: str):
        self.state.original_request = request
        print("🧠 Planning tasks...")
        plan_data = self.planner.create_plan(request)
        tasks = [Task(**t) for t in plan_data]
        self.state.plan = Plan(tasks=tasks)
        print(f"📋 Plan created with {len(tasks)} tasks:")
        for t in tasks:
            print(f"  - [{t.id}] {t.description} (Tool: {t.tool_name})")
        
        print("\n⚙️ Executing Plan...\n")
        for task in self.state.plan.tasks:
            print(f"▶️ Executing Task {task.id}: {task.description}")
            result = self.executor.execute_task(task, self.state.context_results)
            task.result = result
            task.status = "completed"
            self.state.context_results.append(result)
            preview = result[:100] + "..." if len(result) > 100 else result
            print(f"✅ Completed. Result: {preview}\n")
