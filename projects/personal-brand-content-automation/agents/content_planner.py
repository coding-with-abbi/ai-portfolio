import json
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.callbacks import get_openai_callback
from config.settings import Settings


class ContentPlannerAgent:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            azure_endpoint=Settings.AZURE_OPENAI_ENDPOINT,
            api_key=Settings.AZURE_OPENAI_API_KEY,
            azure_deployment=Settings.AZURE_OPENAI_DEPLOYMENT,
            api_version=Settings.AZURE_OPENAI_API_VERSION,
            temperature=0.7,
        )

    def create_content_plan(self, niche, period="Woche 1", language="de", platforms=None, context="", monitor=None):
        if platforms is None:
            platforms = ["instagram", "tiktok"]

        prompt_template = self._load_prompt("prompts/content_strategy.txt")

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Du bist ein erfahrener Social Media Stratege. Antworte ausschließlich in validem JSON."),
            ("user", prompt_template),
        ])

        chain = prompt | self.llm

        invoke_kwargs = {
            "niche": niche,
            "period": period,
            "language": language,
            "platforms": ", ".join(platforms),
            "context": context or f"Neuer Account in der Nische '{niche}'. Ziel: Schnelles Wachstum und Monetarisierung.",
        }

        if monitor:
            with get_openai_callback() as cb:
                result = chain.invoke(invoke_kwargs)
                monitor.track_llm_usage("content_planner", {
                    "prompt_tokens": cb.prompt_tokens,
                    "completion_tokens": cb.completion_tokens,
                    "total_tokens": cb.total_tokens,
                })
        else:
            result = chain.invoke(invoke_kwargs)

        return self._parse_json(result.content)

    def generate_post_ideas(self, niche, count=10, language="de", monitor=None):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Du bist ein viraler Content-Stratege. Antworte ausschließlich in validem JSON."),
            ("user", """Generiere {count} spezifische Post-Ideen für die Nische "{niche}".

Sprache: {language}

Für jede Idee liefere:
1. Thema
2. Format (carousel, reel, text_post, thread)
3. Hook (die exakte erste Zeile die den Scroll stoppt)
4. Plattform-Empfehlung
5. Monetarisierungs-Potenzial (hoch/mittel/niedrig)
6. Affiliate-Möglichkeit (falls vorhanden)

Antworte als JSON-Array:
[{{"topic": "...", "format": "...", "hook": "...", "platform": "...", "monetization_potential": "...", "affiliate_opportunity": "..."}}]"""),
        ])

        chain = prompt | self.llm

        if monitor:
            with get_openai_callback() as cb:
                result = chain.invoke({"niche": niche, "count": count, "language": language})
                monitor.track_llm_usage("content_planner", {
                    "prompt_tokens": cb.prompt_tokens,
                    "completion_tokens": cb.completion_tokens,
                    "total_tokens": cb.total_tokens,
                })
        else:
            result = chain.invoke({"niche": niche, "count": count, "language": language})

        return self._parse_json(result.content)

    def _load_prompt(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Prompt template not found: {path}")

    def _parse_json(self, text):
        text = text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        return json.loads(text.strip())
