import json
import os
import time
from datetime import datetime


class ContentMonitor:
    COST_PER_1K_PROMPT = 0.03
    COST_PER_1K_COMPLETION = 0.06

    API_COSTS = {
        "elevenlabs": {"per_1k_chars": 0.30},
        "canva": {"per_design": 0.0},
        "opusclip": {"per_clip": 0.10},
        "sora": {"per_video_second": 0.15},
    }

    def __init__(self):
        self.start_time = time.time()
        self.metrics = {
            "workflow_info": {
                "start_time": datetime.now().isoformat(),
                "duration": 0,
                "total_cost": 0.0,
            },
            "agents": {},
            "tasks": [],
            "tools": {},
            "token_usage": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0,
            },
            "content_metrics": {
                "pieces_generated": 0,
                "niche": "",
                "platforms": [],
            },
            "api_costs": {},
        }

    def track_llm_usage(self, agent_name, usage_metadata):
        if not usage_metadata:
            return

        p_tokens = usage_metadata.get("prompt_tokens", 0)
        c_tokens = usage_metadata.get("completion_tokens", 0)

        self.metrics["token_usage"]["prompt_tokens"] += p_tokens
        self.metrics["token_usage"]["completion_tokens"] += c_tokens
        self.metrics["token_usage"]["total_tokens"] += p_tokens + c_tokens

        cost = (p_tokens / 1000 * self.COST_PER_1K_PROMPT) + (
            c_tokens / 1000 * self.COST_PER_1K_COMPLETION
        )
        self.metrics["workflow_info"]["total_cost"] += cost

        if agent_name not in self.metrics["agents"]:
            self.metrics["agents"][agent_name] = {"calls": 0, "tokens": 0}
        self.metrics["agents"][agent_name]["calls"] += 1
        self.metrics["agents"][agent_name]["tokens"] += p_tokens + c_tokens

    def track_api_call(self, api_name, units_used, success=True, error=None):
        if api_name not in self.metrics["api_costs"]:
            self.metrics["api_costs"][api_name] = {
                "calls": 0,
                "units": 0,
                "cost": 0.0,
                "errors": [],
            }

        self.metrics["api_costs"][api_name]["calls"] += 1
        self.metrics["api_costs"][api_name]["units"] += units_used

        if api_name in self.API_COSTS:
            cost_info = self.API_COSTS[api_name]
            unit_key = list(cost_info.keys())[0]
            unit_cost = cost_info[unit_key]
            cost = units_used * unit_cost
            self.metrics["api_costs"][api_name]["cost"] += cost
            self.metrics["workflow_info"]["total_cost"] += cost

        if not success and error:
            self.metrics["api_costs"][api_name]["errors"].append(error)

    def track_tool(self, tool_name, success, error_message=None):
        if tool_name not in self.metrics["tools"]:
            self.metrics["tools"][tool_name] = {
                "calls": 0,
                "success": 0,
                "failures": 0,
                "errors": [],
            }

        self.metrics["tools"][tool_name]["calls"] += 1
        if success:
            self.metrics["tools"][tool_name]["success"] += 1
        else:
            self.metrics["tools"][tool_name]["failures"] += 1
            if error_message:
                self.metrics["tools"][tool_name]["errors"].append(error_message)

    def set_content_metrics(self, pieces, niche, platforms):
        self.metrics["content_metrics"]["pieces_generated"] = pieces
        self.metrics["content_metrics"]["niche"] = niche
        self.metrics["content_metrics"]["platforms"] = platforms

    def finalize(self):
        self.metrics["workflow_info"]["duration"] = round(
            time.time() - self.start_time, 2
        )

        total_tasks = len(self.metrics["tasks"])
        completed = len(
            [t for t in self.metrics["tasks"] if t.get("status") == "completed"]
        )
        self.metrics["workflow_info"]["completion_rate"] = (
            f"{(completed/total_tasks)*100:.1f}%" if total_tasks > 0 else "N/A"
        )

        os.makedirs("monitoring/reports", exist_ok=True)
        filename = f"monitoring/reports/run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.metrics, f, indent=4, ensure_ascii=False)

        return filename

    def get_summary_text(self):
        m = self.metrics
        info = m["workflow_info"]
        tokens = m["token_usage"]
        content = m["content_metrics"]

        lines = [
            f"\n--- MONITORING SUMMARY ---",
            f"Duration:        {info['duration']}s",
            f"Total Cost:      ${info['total_cost']:.4f}",
            f"Tokens:          {tokens['total_tokens']} (P: {tokens['prompt_tokens']}, C: {tokens['completion_tokens']})",
            f"Content Pieces:  {content.get('pieces_generated', 0)}",
            f"Niche:           {content.get('niche', 'N/A')}",
            f"Platforms:       {', '.join(content.get('platforms', []))}",
        ]

        if m["agents"]:
            lines.append("\nAgent Usage:")
            for name, stats in m["agents"].items():
                lines.append(f"  {name}: {stats['calls']} calls, {stats['tokens']} tokens")

        if m["api_costs"]:
            lines.append("\nAPI Costs:")
            for api, stats in m["api_costs"].items():
                lines.append(f"  {api}: {stats['calls']} calls, ${stats['cost']:.4f}")

        return "\n".join(lines)
