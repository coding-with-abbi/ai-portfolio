from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from config.settings import *

def explain_result(question: str, sql_query: str, result: str):
    llm = AzureChatOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        azure_deployment=AZURE_OPENAI_DEPLOYMENT,
        api_version=AZURE_OPENAI_API_VERSION,
        temperature=0.2
    )

    prompt = PromptTemplate.from_template(
        """
You are an expert business analyst with strong SQL knowledge.

Context:
- Business question asked by the user:
  "{question}"

- SQL query that was executed:
  {sql_query}

- Result returned by the database:
  {result}

Task:
Explain the result in clear, concise business language.
Be precise about what the number represents.
Do not speculate beyond the given data.
"""
    )

    return llm.invoke(
        prompt.format(
            question=question,
            sql_query=sql_query,
            result=result
        )
    ).content
