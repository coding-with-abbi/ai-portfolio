import json

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import Settings

_settings = Settings()

llm = AzureChatOpenAI(
    azure_endpoint=_settings.AZURE_OPENAI_ENDPOINT,
    api_key=_settings.AZURE_OPENAI_API_KEY,
    azure_deployment=_settings.AZURE_OPENAI_DEPLOYMENT,
    api_version=_settings.AZURE_OPENAI_API_VERSION,
    temperature=0.7,
)

SEARCH_QUERIES_TEMPLATE = ChatPromptTemplate.from_messages([
    (
        "system",
        "Du bist ein Social-Media-Trend-Analyst. Generiere 5 Suchbegriffe um "
        "aktuelle Trends in einer bestimmten Nische zu finden. "
        "Antworte NUR als JSON-Array von Strings, z.B. [\"trend 1\", \"trend 2\"]."
    ),
    (
        "human",
        "Nische: {niche}\nSprache: {language}\n\n"
        "Generiere 5 Suchbegriffe die aktuelle Trends, virale Themen und "
        "Content-Moeglichkeiten in dieser Nische aufdecken."
    ),
])

TREND_ANALYSIS_TEMPLATE = ChatPromptTemplate.from_messages([
    (
        "system",
        "Du bist ein Senior Social-Media-Stratege und Trend-Analyst fuer den "
        "deutschsprachigen Raum. Du analysierst Rohdaten aus Websuchen und "
        "extrahierst daraus verwertbare Content-Strategien.\n\n"
        "Antworte IMMER im folgenden JSON-Format:\n"
        '{{"trending_topics": [{{"topic": "...", "relevance_score": 0.0-1.0, '
        '"why_trending": "...", "peak_window": "..."}}], '
        '"content_ideas": [{{"title": "...", "format": "...", "platform": "...", '
        '"hook_angle": "...", "urgency": "high/medium/low"}}], '
        '"competitor_insights": "..."}}'
    ),
    (
        "human",
        "Analysiere die folgenden Suchergebnisse fuer die Nische '{niche}' "
        "und identifiziere Trends und Content-Moeglichkeiten.\n\n"
        "Suchergebnisse:\n{search_results}\n\n"
        "Liefere:\n"
        "1. trending_topics: Die 5-8 wichtigsten aktuellen Trends (mit Relevanz-Score)\n"
        "2. content_ideas: 5-10 konkrete Content-Ideen mit Format, Plattform und Hook\n"
        "3. competitor_insights: Was machen erfolgreiche Creator in der Nische gerade"
    ),
])

FALLBACK_TEMPLATE = ChatPromptTemplate.from_messages([
    (
        "system",
        "Du bist ein Senior Social-Media-Stratege. Da keine Live-Suchergebnisse "
        "verfuegbar sind, nutze dein Wissen ueber aktuelle Social-Media-Trends, "
        "Algorithmus-Updates und Content-Strategien.\n\n"
        "Antworte IMMER im folgenden JSON-Format:\n"
        '{{"trending_topics": [{{"topic": "...", "relevance_score": 0.0-1.0, '
        '"why_trending": "...", "peak_window": "..."}}], '
        '"content_ideas": [{{"title": "...", "format": "...", "platform": "...", '
        '"hook_angle": "...", "urgency": "high/medium/low"}}], '
        '"competitor_insights": "..."}}'
    ),
    (
        "human",
        "Nische: {niche}\nSprache: {language}\n\n"
        "Basierend auf deinem Wissen ueber aktuelle Social-Media-Trends:\n"
        "1. Welche Themen sind gerade in dieser Nische im Trend?\n"
        "2. Welche Content-Formate performen aktuell am besten?\n"
        "3. Welche Content-Ideen wuerden jetzt viral gehen koennen?\n"
        "4. Was machen Top-Creator in dieser Nische?"
    ),
])


def _search_web(queries: list[str]) -> str:
    from duckduckgo_search import DDGS

    results = []
    with DDGS() as ddgs:
        for query in queries:
            hits = list(ddgs.text(query, max_results=5))
            for hit in hits:
                results.append(f"- {hit.get('title', '')}: {hit.get('body', '')}")
    return "\n".join(results) if results else ""


def analyze_trends(niche: str, language: str = "de") -> dict:
    search_results = ""

    try:
        query_chain = SEARCH_QUERIES_TEMPLATE | llm
        query_response = query_chain.invoke({"niche": niche, "language": language})
        raw = query_response.content.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        queries = json.loads(raw)
        search_results = _search_web(queries)
    except Exception:
        pass

    if search_results:
        chain = TREND_ANALYSIS_TEMPLATE | llm
        response = chain.invoke({
            "niche": niche,
            "search_results": search_results,
        })
    else:
        chain = FALLBACK_TEMPLATE | llm
        response = chain.invoke({"niche": niche, "language": language})

    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(text)
