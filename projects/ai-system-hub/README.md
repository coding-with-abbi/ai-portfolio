# ai-system-hub

A production-style AI platform: FastAPI gateway, RAG pipeline with re-ranking, multi-provider model router, monitoring + structured logging.

## Problem

Most LLM applications start as a single chain and ossify into untestable, single-provider monoliths. Switching models, comparing RAG variants, or observing quality decay becomes painful — and the "logging" is whatever print statements survived the prototype.

## Solution

A gateway-first architecture that decouples the four production-relevant concerns:

1. **Request handling** — FastAPI gateway with REST + WebSocket entry points
2. **Routing** — query classifier decides RAG / agent / direct path per request
3. **Model selection** — provider-agnostic router (Azure OpenAI, Anthropic, ...) with fallback
4. **Observability** — every call logged with prompt, model, latency, cost

## Architecture

```
                    User Request
                          │
                          ▼
                 FastAPI Gateway (api/)
                          │
                          ▼
                    Query Router
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
       RAG              Agent             Direct
   (embeddings →     (workflow_adapter)  (single-shot LLM)
    vector store →
    reranker)
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                  Model Router (llm/)
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   Azure OpenAI       Anthropic         Local model
                          │
                          ▼
              Structured Logger + Dashboard
                       (monitoring/)
```

## Stack

Python 3.11 · FastAPI · Pydantic v2 · ChromaDB · Azure OpenAI · Anthropic SDK · uvicorn

## Results

- Routing accuracy on test prompts: <METRIK>
- Gateway + router overhead: <METRIK> ms p50
- RAG retrieval recall@5: <METRIK>
- Reranker uplift in NDCG: <METRIK>
- Cost per request (incl. routing decision): <METRIK> USD

## Run

```bash
pip install -r requirements.txt
cp .env.example .env  # fill in Azure OpenAI / Anthropic keys
uvicorn api.gateway:app --reload
```

Test the gateway:

```bash
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is BERT?", "user_id": "test_user"}'
```

API docs (auto-generated): http://localhost:8000/docs

## Project structure

```
ai-system-hub/
├── api/              # FastAPI gateway + routes
├── core/             # Router, config, Pydantic models
├── rag/              # Embeddings, vector store, retriever, reranker
├── llm/              # Model router + provider adapters
├── agents/           # Workflow orchestrator integration
├── monitoring/       # Logger + dashboard service
├── utils/            # Knowledge base population, system tests
└── data/             # Local vector store (gitignored)
```

## Design choices

- **Pluggable provider layer** — `llm/providers/` lets you swap Azure for Anthropic without touching the gateway.
- **Reranker as a separate step** — independent evaluation of retrieval quality vs. reranker uplift.
- **Structured logging from day one** — every call is replayable for evaluation and incident debugging, not just printed to stdout.

## License

MIT
