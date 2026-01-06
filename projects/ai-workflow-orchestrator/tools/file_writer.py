from langchain_core.tools import StructuredTool
import os

def write_file(file_path: str, content: str) -> str:
    try:
        if not file_path.startswith("results"):
            file_path = os.path.join("results", os.path.basename(file_path))
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully wrote to {file_path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"

def get_file_writer_tool():
    return StructuredTool.from_function(func=write_file, name="file_writer", description="Write content to file.")
