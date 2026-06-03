from loguru import logger
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
from collections import defaultdict
import threading

class SystemLogger:
    """Comprehensive logging system for AI hub"""
    
    def __init__(self):
        # Configure loguru
        logger.remove()  # Remove default handler
        
        # Console logging
        logger.add(
            sys.stdout,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
            level="INFO"
        )
        
        # File logging (JSON)
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        logger.add(
            log_dir / "system_{time:YYYY-MM-DD}.log",
            rotation="1 day",
            retention="30 days",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
            level="DEBUG"
        )
        
        # Metrics storage
        self.metrics = defaultdict(lambda: {"count": 0, "total_latency": 0, "total_tokens": 0, "total_cost": 0})
        self.queries_log: List[Dict[str, Any]] = []
        self.lock = threading.Lock()
        
    def info(self, message: str):
        """Log info message"""
        logger.info(message)
    
    def error(self, message: str):
        """Log error message"""
        logger.error(message)
    
    def warning(self, message: str):
        """Log warning message"""
        logger.warning(message)
    
    def debug(self, message: str):
        """Log debug message"""
        logger.debug(message)
    
    def log_query(self, request_id: str, user_id: str, query: str, response: str, metadata: Dict[str, Any]):
        """Log a complete query interaction"""
        
        log_entry = {
            "request_id": request_id,
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "query": query,
            "response": response[:200] + "..." if len(response) > 200 else response,
            "metadata": metadata
        }
        
        with self.lock:
            self.queries_log.append(log_entry)
            
            # Update metrics
            query_type = metadata.get("query_type", "unknown")
            model = metadata.get("model_used", "unknown")
            
            self.metrics[f"{query_type}_{model}"]["count"] += 1
            self.metrics[f"{query_type}_{model}"]["total_latency"] += metadata.get("latency_ms", 0)
            self.metrics[f"{query_type}_{model}"]["total_tokens"] += metadata.get("tokens_used", 0)
            self.metrics[f"{query_type}_{model}"]["total_cost"] += metadata.get("cost_usd", 0.0)
        
        # Save to JSON file
        self._save_query_log(log_entry)
        
        logger.info(f"✅ Query logged - Type: {metadata.get('query_type')}, Model: {metadata.get('model_used')}, Latency: {metadata.get('latency_ms'):.2f}ms")
    
    def _save_query_log(self, log_entry: Dict[str, Any]):
        """Save query log to JSON file"""
        log_dir = Path("logs")
        log_file = log_dir / f"queries_{datetime.now().strftime('%Y-%m-%d')}.jsonl"
        
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current metrics"""
        with self.lock:
            summary = {}
            for key, data in self.metrics.items():
                count = data["count"]
                if count > 0:
                    summary[key] = {
                        "total_requests": count,
                        "avg_latency_ms": data["total_latency"] / count,
                        "total_tokens": data["total_tokens"],
                        "total_cost_usd": data["total_cost"],
                        "avg_cost_per_request": data["total_cost"] / count
                    }
            return summary
    
    def print_summary(self):
        """Print metrics summary"""
        metrics = self.get_metrics()
        
        print("\n" + "="*60)
        print(" 📊 SYSTEM METRICS SUMMARY")
        print("="*60)
        
        for key, data in metrics.items():
            print(f"\n{key}:")
            print(f"  Total Requests: {data['total_requests']}")
            print(f"  Avg Latency: {data['avg_latency_ms']:.2f}ms")
            print(f"  Total Tokens: {data['total_tokens']}")
            print(f"  Total Cost: ${data['total_cost_usd']:.4f}")
        
        print("="*60 + "\n")

# Global logger instance
system_logger = SystemLogger()
