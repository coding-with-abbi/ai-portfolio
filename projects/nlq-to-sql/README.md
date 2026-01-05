# 🧠 NLQ-to-SQL  
### Natural Language Query to SQL Analytics System

Ein **produktionsnahes Analytics-System**, das Fragen in natürlicher Sprache in **sichere SQL-Abfragen** übersetzt, diese auf einer relationalen Datenbank ausführt und die Ergebnisse **kontextbewusst in verständlicher Business-Sprache erklärt**.

Das Projekt zeigt, wie **Large Language Models (LLMs)** verantwortungsvoll und strukturiert in **Data-Analytics-Workflows** integriert werden können – mit Fokus auf **Architektur, Sicherheit und Nachvollziehbarkeit**.

---

## 🎯 Ziel des Projekts

Viele LLM-Demos bleiben bei einfachen Prompt-Beispielen stehen.  
Dieses Projekt geht bewusst einen Schritt weiter und demonstriert:

- ✅ deterministische **NL → SQL** Generierung  
- ✅ saubere Trennung von Verantwortlichkeiten  
- ✅ sichere Datenbankinteraktion  
- ✅ **erklärbare Ergebnisse** statt reiner Zahlen  

---

## ✨ Features

### 🤖 Natural Language → SQL
Übersetzt Business-Fragen zuverlässig in SQL-Abfragen.

### 🔒 SQL-Validierung & Guardrails
- nur `SELECT` Statements erlaubt  
- automatische Query-Limits  
- Schutz vor unerwünschten Operationen  

### 📊 DuckDB Analytics Engine
Leichte, performante SQL-Engine für analytische Abfragen.

### 💬 Kontextbewusste Ergebnis-Erklärung
Ergebnisse werden unter Berücksichtigung von:
- der ursprünglichen Frage  
- der generierten SQL-Abfrage  
- dem Query-Ergebnis  

in klarer, präziser Business-Sprache erklärt.

### 🧱 Saubere Architektur
Klare Trennung von:
- NL → SQL Generierung  
- SQL-Ausführung  
- Ergebnis-Erklärung  
- Konfiguration & Validierung  

---

## 🧠 Architekturübersicht

```text
User Question
   ↓
NL → SQL Chain (LLM)
   ↓
SQL Validation & Guardrails
   ↓
DuckDB Execution
   ↓
SQL Result
   ↓
Result Explanation Chain (LLM)
   ↓
Human-readable Business Explanation
Design-Entscheidung:
Für analytische Fragestellungen werden deterministische Chains verwendet statt autonomer Agenten, um Vorhersagbarkeit und Sicherheit zu gewährleisten.

🚀 Installation
1️⃣ Dependencies installieren
bash
Code kopieren
pip install -r requirements.txt
2️⃣ Datenbank initialisieren
Demo-Datenbank:

bash
Code kopieren
python db/init_db.py
Realistische Analytics-Datenbank:

bash
Code kopieren
python db/generate_data.py
3️⃣ Umgebungsvariablen konfigurieren
Erstelle eine .env Datei im Projektordner:

env
Code kopieren
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
Hinweis:
AZURE_OPENAI_API_VERSION ist optional und verwendet standardmäßig
2024-02-15-preview, falls nicht gesetzt.

☁️ Azure OpenAI Setup
Öffne das Azure Portal

Erstelle eine Azure OpenAI Resource

Erstelle ein Model Deployment (z. B. GPT-4 / GPT-4o)

Notiere dir:

Endpoint URL

API Key

Deployment Name

API Version

▶️ Verwendung
bash
Code kopieren
python app.py
Beispiel-Fragen
„Wie viel Umsatz wurde pro Region erzielt?“

„Welche Produkte generieren den höchsten Umsatz?“

„Wie hat sich der Umsatz über die Zeit entwickelt?“

„Wer sind die Top-5-Kunden nach Bestellwert?“

📁 Projektstruktur
text
Code kopieren
nlq-to-sql/
├── app.py                    # CLI Entry Point
├── chains/
│   ├── nl_to_sql.py          # Natural Language → SQL
│   └── sql_to_text.py        # SQL Result → Explanation
├── config/
│   └── settings.py           # Azure & DB Configuration
├── db/
│   ├── analytics.db          # DuckDB Database
│   ├── init_db.py            # Minimal Demo Dataset
│   └── generate_data.py      # Large Synthetic Analytics Dataset
├── prompts/
│   ├── nl_to_sql.txt         # SQL Generation Prompt
│   └── sql_to_text.txt       # Result Explanation Prompt
├── validation/
│   └── sql_guard.py          # SQL Safety & Validation
└── README.md
🛠️ Technologie-Stack
Python 3.10+

LangChain – LLM-Orchestrierung

Azure OpenAI – Enterprise LLM Hosting

DuckDB – Analytics-orientierte SQL Engine

sqlparse – SQL Parsing & Validation

faker – realistische synthetische Daten

🔐 Sicherheit & Design-Prinzipien
❌ keine Schreiboperationen auf der Datenbank

🔍 explizite Trennung von:

Business-Fragen

Schema- / Metadaten-Fragen

🧠 kontextreiche Prompts zur Vermeidung von Halluzinationen

🧩 Architektur vorbereitet für:

UI (Streamlit / FastAPI)

andere SQL-Datenbanken (Postgres, Snowflake)

👤 Autor
Jacob Abb