# nlq-to-sql

Natural-language analytics that turns business questions into validated SQL, runs them against a relational database, and explains the result in plain business language.

## Problem

LLM "chat-with-your-data" demos break in production:
- generated SQL writes to the database
- no schema grounding — hallucinated columns, runaway queries
- raw result tables, no business interpretation

## Solution

Deterministic pipeline that constrains the LLM to one validated step at a time:

1. **NL → SQL chain** with schema-grounded prompt
2. **Guardrail layer** — SELECT-only, statement-count, row limits, no DDL
3. **DuckDB execution** — fast analytical engine, no production DB required
4. **Result → text chain** — explains the answer using the question, the SQL, and the result rows

## Architecture

```
question
   │
   ▼
NL → SQL chain ──► sqlparse validator ──► reject if not SELECT
   │
   ▼ valid SQL
DuckDB execution
   │
   ▼ result rows
Result → text chain (question + sql + rows)
   │
   ▼
business explanation
```

## Stack

Python 3.11 · LangChain · Azure OpenAI (GPT-4o) · DuckDB · sqlparse · Faker (synthetic data)

## Results

- SELECT-only enforcement: <METRIK> of non-SELECT statements correctly rejected
- Query latency: <METRIK> p50 / <METRIK> p95
- Cost per question: <METRIK> USD (NL→SQL + execution + result explanation)
- Test corpus: <METRIK> business questions across <METRIK> tables

## Run

```bash
pip install -r requirements.txt

# Initialise a minimal demo database
python db/init_db.py

# Or generate a larger synthetic analytics dataset
python db/generate_data.py

# Configure Azure OpenAI credentials
cp .env.example .env  # then fill in the values

python app.py
```

### Required environment variables

```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com
AZURE_OPENAI_API_KEY=<your-api-key>
AZURE_OPENAI_DEPLOYMENT=<your-deployment-name>
AZURE_OPENAI_API_VERSION=2024-02-15-preview  # optional, default shown
```

### Example questions

- "What is the revenue per region?"
- "Which products generate the highest revenue?"
- "Who are the top 5 customers by order value?"
- "How did revenue evolve over time?"

## Project structure

```
nlq-to-sql/
├── app.py                  # CLI entry point
├── chains/
│   ├── nl_to_sql.py        # NL → SQL chain
│   └── sql_to_text.py      # SQL result → explanation
├── config/
│   └── settings.py
├── db/
│   ├── analytics.db        # DuckDB database
│   ├── init_db.py          # minimal demo dataset
│   └── generate_data.py    # synthetic analytics dataset
├── prompts/
│   ├── nl_to_sql.txt
│   └── sql_to_text.txt
└── validation/
    └── sql_guard.py        # SELECT-only validator
```

## Design choices

- **Deterministic chains, not autonomous agents** — analytical Q&A needs predictable behavior, not exploration loops.
- **DuckDB instead of Postgres in the demo** — analytical engine, zero setup, drop-in replaceable with Postgres / Snowflake.
- **Result explanation is its own chain** — keeps the SQL prompt focused; the explanation prompt can be tuned per audience (analyst vs. executive).
