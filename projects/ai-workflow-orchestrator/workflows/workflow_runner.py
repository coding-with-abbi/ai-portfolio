from memory.state import WorkflowState, Plan, Task
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from monitoring.monitor import Monitor

class WorkflowRunner:
    def __init__(self):
        self.state = WorkflowState(original_request="")
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.monitor = Monitor()
    
    def run(self, request: str):
        self.state.original_request = request
        print("🧠 Planning tasks...")
        plan_data = self.planner.create_plan(request, monitor=self.monitor)
        tasks = [Task(**t) for t in plan_data]
        self.state.plan = Plan(tasks=tasks)
        print(f"📋 Plan created with {len(tasks)} tasks:")
        for t in tasks:
            print(f"  - [{t.id}] {t.description} (Tool: {t.tool_name})")
        
        print("\n⚙️ Executing Plan...\n")
        for task in self.state.plan.tasks:
            print(f"▶️ Executing Task {task.id}: {task.description}")
            self.monitor.track_task(task.id, task.description, task.tool_name, "in_progress")
            
            result = self.executor.execute_task(task, self.state.context_results, monitor=self.monitor)
            
            task.result = result
            task.status = "completed"
            self.monitor.track_task(task.id, task.description, task.tool_name, "completed", result[:100])
            
            self.state.context_results.append(result)
            preview = result[:100] + "..." if len(result) > 100 else result
            print(f"✅ Completed. Result: {preview}\n")
        
        report_path = self.monitor.finalize()
        print(self.monitor.get_summary_text())
        print(f"\n📂 Full monitoring report saved to: {report_path}")
