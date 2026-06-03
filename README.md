# AI Portfolio

Production-leaning AI engineering work — RAG systems, agent architectures, NLQ→SQL pipelines. Each project ships an end-to-end use case and runs independently.

## Focus

- Production-ready GenAI on Azure (OpenAI, AI Search, Document Intelligence)
- Retrieval-augmented generation with evaluation and cost control
- Agent and workflow orchestration with deterministic guardrails
- LLM reliability: validation, fallback, observability

## Projects

### [ai-system-hub](projects/ai-system-hub)
Multi-component AI platform. FastAPI gateway → query router → RAG / agent / direct path → model router → response. Includes monitoring, structured logging, and a dashboard service.
**Stack:** FastAPI · Python 3.11 · Azure OpenAI · ChromaDB · Pydantic

### [ai-workflow-orchestrator](projects/ai-workflow-orchestrator)
Agentic workflow runner that separates planning from execution. A planner LLM generates structured tasks; an executor refines tool inputs with prior-step context before calling tools (web search, Python runner, file writer).
**Stack:** Python 3.11 · Azure OpenAI · DuckDuckGo Search · Pydantic

### [nlq-to-sql](projects/nlq-to-sql)
Natural-language analytics. Question → SQL (SELECT-only validation, query limits, no write paths) → DuckDB execution → LLM-explained business result. Built for analytical Q&A, not chat.
**Stack:** Python 3.11 · LangChain · Azure OpenAI · DuckDB · sqlparse

## Stack

Python 3.11 · Azure OpenAI (GPT-4o, embeddings, Whisper) · LangChain · FastAPI · DuckDB · ChromaDB · Docker

## About

Jacob Abb — AI Engineer & Consultant. Building production-grade LLM systems with focus on retrieval quality, evaluation, and operational reliability. Based in northern Germany, open to Swiss / EU remote work.

- Azure AI Engineer (AI-102)
- Azure Data Scientist (DP-100)
- Databricks Generative AI Engineer
- M.Sc. Information Systems (CAU Kiel)

Contact: [jacob.abb@web.de](mailto:jacob.abb@web.de)

## License

Each project specifies its own license. Unless stated otherwise, code is provided as portfolio reference.
