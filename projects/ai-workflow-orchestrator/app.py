import argparse
import sys
import os
from dotenv import load_dotenv

# Load env vars FIRST, before importing config that relies on it
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    print(f"✅ Loaded .env from {dotenv_path}")
else:
    print(f"⚠️ Warning: .env not found at {dotenv_path}")

from config.settings import Settings
from workflows.workflow_runner import WorkflowRunner

def main():
    print("🤖 Agentic Workflow Orchestrator Initializing...")

    # Validate Config
    try:
        Settings.validate()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        sys.exit(1)

    # CLI Arguments
    parser = argparse.ArgumentParser(description="AI Workflow Orchestrator")
    parser.add_argument("task", nargs="?", help="The task for the AI agents to perform")
    args = parser.parse_args()

    if not args.task:
        # Interactive mode or help
        print("Usage: python app.py \"<Your Task Here>\"")
        print("Example: python app.py \"Research the current state of AI agents\"")
        user_input = input("\nOr enter task now: ").strip()
        if not user_input:
            sys.exit(0)
        task = user_input
    else:
        task = args.task

    # Run Workflow
    print(f"🚀 Starting Workflow for: {task}\n")
    runner = WorkflowRunner()
    runner.run(task)
    print("\n🏁 Workflow Finished.")

if __name__ == "__main__":
    main()
