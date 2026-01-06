from langchain_core.tools import StructuredTool
import sys
from io import StringIO

def run_python(code: str) -> str:
    print("WARNING: Executing Python code...")
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    try:
        exec(code, {'__name__': '__main__'})
        sys.stdout = old_stdout
        return mystdout.getvalue()
    except Exception as e:
        sys.stdout = old_stdout
        return f"Error: {e}"

def get_python_runner_tool():
    return StructuredTool.from_function(func=run_python, name="python_runner", description="Execute python code.")
