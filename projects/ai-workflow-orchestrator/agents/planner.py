from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from config.settings import Settings
import json

class PlannerAgent:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            azure_endpoint=Settings.AZURE_OPENAI_ENDPOINT,
            api_key=Settings.AZURE_OPENAI_API_KEY,
            azure_deployment=Settings.AZURE_OPENAI_DEPLOYMENT,
            api_version=Settings.AZURE_OPENAI_API_VERSION,
            temperature=0
        )
    
    def create_plan(self, user_request: str) -> list:
        # Prompt definition
        system_prompt = """
        You are a Planner Agent.
        Your goal is to break down a user request into a sequence of executable tasks.
        
        Available Tools:
        - web_search: Use this to find information on the internet. Input: {{"query": "search term"}}
        - python_runner: Use this to perform calculations or data processing. Input: {{"code": "print('hello')"}}
        - file_writer: Use this to save reports or code to a file. Input: {{"file_path": "report.md", "content": "Full content here"}}
        
        Output MUST be a valid JSON list of tasks.
        Example:
        [
            {{
                "id": 1,
                "description": "Search for X",
                "tool_name": "web_search",
                "tool_input": {{"query": "X"}}
            }},
            {{
                "id": 2,
                "description": "Write report",
                "tool_name": "file_writer",
                "tool_input": {{"file_path": "report.md", "content": "Placeholder"}}
            }}
        ]
        """
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", "{request}")
        ])
        
        chain = prompt | self.llm | JsonOutputParser()
        return chain.invoke({"request": user_request})
