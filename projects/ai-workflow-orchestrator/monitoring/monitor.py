import json
import os
import time
from datetime import datetime

class Monitor:
    def __init__(self):
        self.start_time = time.time()
        self.metrics = {
            "workflow_info": {
                "start_time": datetime.now().isoformat(),
                "duration": 0,
                "total_cost": 0.0
            },
            "agents": {
                "planner": {"status": "pending", "tokens": 0, "errors": []},
                "executor": {"status": "pending", "tokens": 0, "errors": []}
            },
            "tasks": [],
            "tools": {},
            "token_usage": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0
            }
        }
        # Approximate costs for Azure OpenAI (GPT-4) - illustrative
        self.COST_PER_1K_PROMPT = 0.03 
        self.COST_PER_1K_COMPLETION = 0.06

    def track_llm_usage(self, agent_name, usage_metadata):
        if not usage_metadata:
            return
        
        p_tokens = usage_metadata.get("prompt_tokens", 0)
        c_tokens = usage_metadata.get("completion_tokens", 0)
        
        self.metrics["token_usage"]["prompt_tokens"] += p_tokens
        self.metrics["token_usage"]["completion_tokens"] += c_tokens
        self.metrics["token_usage"]["total_tokens"] += (p_tokens + c_tokens)
        
        cost = (p_tokens / 1000 * self.COST_PER_1K_PROMPT) + (c_tokens / 1000 * self.COST_PER_1K_COMPLETION)
        self.metrics["workflow_info"]["total_cost"] += cost
        
        if agent_name in self.metrics["agents"]:
            self.metrics["agents"][agent_name]["tokens"] += (p_tokens + c_tokens)

    def track_task(self, task_id, description, tool_name, status, result_preview=None):
        # Update existing task or add new one
        for task in self.metrics["tasks"]:
            if task["id"] == task_id:
                task["status"] = status
                task["timestamp"] = datetime.now().isoformat()
                return

        self.metrics["tasks"].append({
            "id": task_id,
            "description": description,
            "tool_name": tool_name,
            "status": status,
            "timestamp": datetime.now().isoformat()
        })

    def track_tool(self, tool_name, success, error_message=None, latency=0.0):
        if tool_name not in self.metrics["tools"]:
            self.metrics["tools"][tool_name] = {"calls": 0, "success": 0, "failures": 0, "errors": []}
        
        self.metrics["tools"][tool_name]["calls"] += 1
        if success:
            self.metrics["tools"][tool_name]["success"] += 1
        else:
            self.metrics["tools"][tool_name]["failures"] += 1
            if error_message:
                self.metrics["tools"][tool_name]["errors"].append(error_message)

    def finalize(self):
        self.metrics["workflow_info"]["duration"] = round(time.time() - self.start_time, 2)
        
        # Calculate completion rate
        total_tasks = len(self.metrics["tasks"])
        completed_tasks = len([t for t in self.metrics["tasks"] if t["status"] == "completed"])
        self.metrics["workflow_info"]["completion_rate"] = f"{(completed_tasks/total_tasks)*100:.1f}%" if total_tasks > 0 else "0%"

        # Save to file
        os.makedirs("monitoring/reports", exist_ok=True)
        filename = f"monitoring/reports/run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.metrics, f, indent=4)
        
        return filename

    def get_summary_text(self):
        m = self.metrics
        info = m["workflow_info"]
        tokens = m["token_usage"]
        
        summary = [
            "\n📊 --- MONITORING SUMMARY ---",
            f"⏱️  Duration: {info['duration']}s",
            f"💰 Total Cost: ${info['total_cost']:.4f}",
            f"🤖 Tokens: {tokens['total_tokens']} (P: {tokens['prompt_tokens']}, C: {tokens['completion_tokens']})",
            f"✅ Completion Rate: {info.get('completion_rate', 'N/A')}",
            "\n🛠️  Tool Performance:"
        ]
        
        for tool, stats in m["tools"].items():
            rate = (stats['success'] / stats['calls']) * 100 if stats['calls'] > 0 else 0
            summary.append(f"  - {tool}: {rate:.1f}% success ({stats['success']}/{stats['calls']})")
        
        return "\n".join(summary)
