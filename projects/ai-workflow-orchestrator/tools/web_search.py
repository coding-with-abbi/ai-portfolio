from langchain_core.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun

def get_web_search_tool():
    try:
        search = DuckDuckGoSearchRun()
        func = search.run
    except Exception as e:
        print(f"WARNING: DuckDuckGoSearchRun not available. Using LLM-based Knowledge Search.")
        from langchain_openai import AzureChatOpenAI
        from config.settings import Settings
        llm = AzureChatOpenAI(
            azure_endpoint=Settings.AZURE_OPENAI_ENDPOINT,
            api_key=Settings.AZURE_OPENAI_API_KEY,
            azure_deployment=Settings.AZURE_OPENAI_DEPLOYMENT,
            api_version=Settings.AZURE_OPENAI_API_VERSION,
            temperature=0.1
        )
        def func(query: str) -> str:
            print(f"  🔍 Simulating search for: {query}")
            response = llm.invoke(f"Factual summary for: '{query}'.")
            return f"[Simulated Search Result]\\n{response.content}"
    return Tool(name="web_search", func=func, description="Search the web.")
