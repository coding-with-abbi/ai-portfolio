# NLQ-to-SQL: Natural Language Query to SQL

Ein System, das Fragen in natürlicher Sprache in SQL-Abfragen umwandelt, diese ausführt und die Ergebnisse erklärt.

## Features

- 🤖 **Natural Language Processing**: Konvertiert Fragen in natürlicher Sprache zu SQL
- 🔒 **SQL-Validierung**: Sicherheitsprüfung (nur SELECT-Abfragen)
- 📊 **DuckDB Integration**: Verwendet DuckDB als Analytics-Datenbank
- 💬 **Ergebnis-Erklärung**: Erklärt SQL-Ergebnisse in verständlicher Sprache

## Installation

1. **Dependencies installieren:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Datenbank initialisieren:**
   ```bash
   python db/init_db.py
   ```

3. **Umgebungsvariablen konfigurieren:**
   
   Erstelle eine `.env` Datei im Projektordner:
   ```env
   AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
   AZURE_OPENAI_API_KEY=your-api-key-here
   AZURE_OPENAI_DEPLOYMENT=your-deployment-name
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   ```
   
   **Hinweis:** `AZURE_OPENAI_API_VERSION` ist optional und verwendet standardmäßig `2024-02-15-preview`, falls nicht gesetzt.

## Azure OpenAI Setup

1. Gehe zum [Azure Portal](https://portal.azure.com)
2. Erstelle eine **Azure OpenAI Resource** (falls noch nicht vorhanden)
3. Erstelle ein **Deployment** (z.B. GPT-4 oder GPT-3.5-turbo)
4. Kopiere die folgenden Werte:
   - **Endpoint**: Findest du unter "Keys and Endpoint" → Endpoint URL
   - **API Key**: Findest du unter "Keys and Endpoint" → Key 1 oder Key 2
   - **Deployment Name**: Der Name deines Deployments (z.B. "gpt-4" oder "gpt-35-turbo")
   - **API Version**: Standardmäßig `2024-02-15-preview` (kann in `.env` überschrieben werden)

## Verwendung

```bash
python app.py
```

Beispiel-Fragen:
- "Wie viel Umsatz wurde in der EU gemacht?"
- "Zeige mir die Top 3 Produkte nach Umsatz"
- "Was ist der Gesamtumsatz für Januar 2024?"

## Projektstruktur

```
nlq-to-sql/
├── app.py                    # Hauptanwendung
├── chains/
│   ├── nl_to_sql.py         # Natural Language → SQL Chain
│   └── sql_to_text.py       # SQL Ergebnis → Text-Erklärung
├── config/
│   └── settings.py          # Konfiguration
├── db/
│   ├── analytics.db         # DuckDB Datenbank
│   └── init_db.py           # Datenbank-Initialisierung
├── validation/
│   └── sql_guard.py         # SQL-Validierung
└── prompts/                 # Prompt-Templates
```

## Technologie-Stack

- **LangChain**: LLM-Chain Orchestrierung
- **Azure OpenAI**: GPT-Modelle für NL→SQL Konvertierung
- **DuckDB**: In-Memory Analytics-Datenbank
- **SQLParse**: SQL-Parsing und Validierung

