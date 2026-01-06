from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from config.settings import Settings
from memory.state import Task
from tools.web_search import get_web_search_tool
from tools.file_writer import get_file_writer_tool
from tools.python_runner import get_python_runner_tool

class ExecutorAgent:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            azure_endpoint=Settings.AZURE_OPENAI_ENDPOINT,
            api_key=Settings.AZURE_OPENAI_API_KEY,
            azure_deployment=Settings.AZURE_OPENAI_DEPLOYMENT,
            api_version=Settings.AZURE_OPENAI_API_VERSION,
            temperature=0
        )
        self.tools = {
            "web_search": get_web_search_tool(),
            "file_writer": get_file_writer_tool(),
            "python_runner": get_python_runner_tool()
        }

    def refine_tool_input(self, task: Task, context: list[str]) -> dict:
        """Refines tool input using context from previous steps."""
        if not context or task.tool_name not in ["file_writer", "python_runner"]:
            return task.tool_input if task.tool_input else {}

        print(f"  ✨ Refining input for {task.tool_name} using context...")
        
        prompt_template = """
            You are an AI Executor. You are about to run a tool, but the input needs to be populated with data from previous tasks.
            
            Previous Task Results:
            {context}
            
            Current Task: {description}
            Target Tool: {tool_name}
            Original Input: {tool_input}
            
            Guidelines:
            - If 'file_writer': Generate the FULL content for the file. Do not use placeholders.
            - If 'python_runner': Write VALID, COMPLETE Python code to solve the task using the data from 'Previous Task Results'. 
              - Define variables with the actual numbers/strings found in the context.
              - Do NOT use placeholders like '...' or 'gdp = insert_here'.
              - The code must be self-contained and print the result.
            
            Return ONLY a valid JSON object matching the tool input schema.
            """
        
        prompt = ChatPromptTemplate.from_template(prompt_template)
        chain = prompt | self.llm | JsonOutputParser()
        try:
            return chain.invoke({
                "context": "\\n".join(context),
                "description": task.description,
                "tool_name": task.tool_name,
                "tool_input": str(task.tool_input)
            })
        except Exception as e:
            print(f"Refinement failed: {e}")
            return task.tool_input

    def execute_task(self, task: Task, context_results: list[str]) -> str:
        tool = self.tools.get(task.tool_name)
        if not tool:
            return f"Error: Tool {task.tool_name} not found"
        
        refined_input = self.refine_tool_input(task, context_results)
        
        try:
            if task.tool_name == "web_search":
                query = refined_input.get("query") if isinstance(refined_input, dict) else refined_input
                return tool.run(query)
            else:
                return tool.run(refined_input)
        except Exception as e:
            return f"Error executing tool: {e}"
