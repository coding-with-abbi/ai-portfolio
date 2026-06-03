# AI System Hub

A production-grade AI platform that orchestrates multiple specialized components.

## Features

- 🚀 **FastAPI Gateway**: REST & WebSocket support
- 🧠 **RAG Pipeline**: Vector search with re-ranking
- 🤖 **Agent Router**: Intelligent query routing
- 🎯 **Model Selection**: Automatic model routing (GPT-4, Claude, local)
- 📊 **Comprehensive Logging**: Track everything
- 🔍 **Monitoring**: Real-time metrics and feedback loop

## Architecture

```
User → API Gateway → Router → [RAG / Agent / Direct] → Model → Response
                ↓
         Comprehensive Logger → Monitoring & Optimization
```

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Run the Server**:
   ```bash
   uvicorn api.gateway:app --reload
   ```

4. **Test the API**:
   ```bash
   curl -X POST http://localhost:8000/api/v1/query \
     -H "Content-Type: application/json" \
     -d '{"query": "What is BERT?", "user_id": "test_user"}'
   ```

## Project Structure

```
ai-system-hub/
├── api/              # FastAPI gateway & routes
├── core/             # Router, config, models
├── rag/              # RAG pipeline (embeddings, vector store)
├── llm/              # Model routing & prompt engine
├── agents/           # Workflow orchestrator integration
├── monitoring/       # Logging & metrics
├── utils/            # Validators, post-processors
├── tests/            # Unit & integration tests
└── data/             # Vector store & knowledge base
```

## Documentation

- API Docs: http://localhost:8000/docs (when running)

## License

MIT
