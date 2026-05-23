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

PLATFORM_SPECS = {
    "instagram": {"max_caption": 2200, "max_hashtags": 30, "optimal_hashtags": 15},
    "tiktok": {"max_caption": 4000, "max_hashtags": 10, "optimal_hashtags": 5},
    "linkedin": {"max_caption": 3000, "max_hashtags": 5, "optimal_hashtags": 3},
    "x": {"max_caption": 280, "max_hashtags": 3, "optimal_hashtags": 2},
    "youtube": {"max_caption": 5000, "max_hashtags": 15, "optimal_hashtags": 5},
}

STYLE_PROMPTS = {
    "listicle": (
        "Schreibe eine virale Listicle-Caption im Stil von '9 KI-Tools die dir einen "
        "unfairen Vorteil bringen'. Jeder Punkt muss eine konkrete, umsetzbare Erkenntnis "
        "liefern. Nutze Zahlen, Emojis als Aufzaehlungszeichen und kurze, punchige Saetze. "
        "Beginne mit einer provokanten Zahl im Hook."
    ),
    "educational": (
        "Schreibe eine lehrreiche Caption, die komplexes Wissen in einfache Schritte "
        "herunterbricht. Starte mit einer ueberraschenden Statistik oder einem weit "
        "verbreiteten Irrglauben. Nutze 'Du'-Ansprache und liefere sofort anwendbares Wissen. "
        "Strukturiere den Inhalt mit klaren Absaetzen und Zeilenumbruechen."
    ),
    "motivational": (
        "Schreibe eine motivierende Caption die polarisiert und zum Handeln aufruft. "
        "Starte mit einer kontroversen These oder einem persoenlichen Wendepunkt. "
        "Nutze kurze, kraftvolle Saetze. Jeder Absatz muss emotional packen. "
        "Schliesse mit einem klaren Handlungsaufruf ab."
    ),
    "storytelling": (
        "Schreibe eine Story-Caption die den Leser in eine persoenliche Erfahrung "
        "hineinzieht. Beginne mitten in der Action (in medias res). Nutze sensorische "
        "Details und einen klaren Spannungsbogen: Problem, Wendepunkt, Erkenntnis. "
        "Die Moral muss direkt auf das Thema einzahlen."
    ),
    "controversial": (
        "Schreibe eine bewusst kontroverse Caption die eine gaengige Meinung in der "
        "Branche herausfordert. Starte mit einer provokativen Behauptung. Liefere dann "
        "3-4 unerwartete Argumente die deine Position stuetzen. Nutze rhetorische Fragen "
        "und fordere die Community zur Diskussion auf. Polarisierung ist gewollt."
    ),
}

CAPTION_TEMPLATE = ChatPromptTemplate.from_messages([
    (
        "system",
        "Du bist ein Elite-Social-Media-Texter fuer den deutschsprachigen Raum. "
        "Du erstellst virale Captions die hohe Engagement-Raten erzielen. "
        "Du kennst die Algorithmen und Best Practices jeder Plattform. "
        "Dein Schreibstil ist direkt, wertliefernd und formatiert fuer mobile Lesbarkeit. "
        "Antworte IMMER im folgenden JSON-Format:\n"
        '{{"hook": "...", "body": "...", "cta": "...", "hashtags": ["...", "..."], '
        '"full_caption": "..."}}'
    ),
    (
        "human",
        "Erstelle eine {platform}-Caption.\n\n"
        "Thema: {topic}\n"
        "Nische: {niche}\n"
        "Sprache: {language}\n"
        "Stil-Anweisung: {style_instruction}\n\n"
        "Plattform-Limits:\n"
        "- Maximale Laenge: {max_caption} Zeichen\n"
        "- Optimale Hashtag-Anzahl: {optimal_hashtags}\n\n"
        "Regeln:\n"
        "1. Der Hook muss in den ersten 125 Zeichen den Scroll stoppen\n"
        "2. Nutze Zeilenumbrueche fuer Lesbarkeit auf dem Handy\n"
        "3. CTA muss eine konkrete Handlung fordern (speichern, teilen, kommentieren)\n"
        "4. Hashtags muessen eine Mischung aus Nischen- und Reichweiten-Hashtags sein\n"
        "5. Die gesamte Caption muss unter {max_caption} Zeichen bleiben"
    ),
])

CAROUSEL_TEMPLATE = ChatPromptTemplate.from_messages([
    (
        "system",
        "Du bist ein Experte fuer Instagram-Carousel-Posts im deutschsprachigen Raum. "
        "Du erstellst Slide-fuer-Slide-Inhalte die zum Durchswipen animieren. "
        "Jede Slide hat maximal 3-4 kurze Saetze oder Bullet Points. "
        "Antworte IMMER als JSON-Array mit Objekten im Format:\n"
        '[{{"slide_number": 1, "text": "...", "design_notes": "..."}}]'
    ),
    (
        "human",
        "Erstelle einen {num_slides}-Slide Carousel-Post.\n\n"
        "Thema: {topic}\n"
        "Sprache: {language}\n\n"
        "Struktur:\n"
        "- Slide 1: Hook-Slide mit provokanter Ueberschrift und Untertitel\n"
        "- Slides 2-{inner_end}: Inhalt mit je einem Kernpunkt pro Slide\n"
        "- Vorletzte Slide: Zusammenfassung / Key Takeaway\n"
        "- Letzte Slide: CTA-Slide (Folgen, Speichern, Teilen)\n\n"
        "Jede Slide braucht:\n"
        "- text: Der Text der auf der Slide steht (kurz, maximal 40 Woerter)\n"
        "- design_notes: Visuelle Hinweise (Hintergrundfarbe, Icon-Vorschlag, Layout)"
    ),
])

REEL_TEMPLATE = ChatPromptTemplate.from_messages([
    (
        "system",
        "Du bist ein Reel- und Short-Form-Video-Skript-Experte. "
        "Du erstellst Skripte die von der ersten Sekunde fesseln. "
        "Antworte IMMER im folgenden JSON-Format:\n"
        '{{"segments": [{{"timestamp": "0:00-0:03", "type": "HOOK", '
        '"voiceover": "...", "screen_text": "...", "visual": "..."}}], '
        '"voiceover_text": "Kompletter Voiceover-Text ohne Timestamps", '
        '"hashtags": ["..."], "music_suggestion": "..."}}'
    ),
    (
        "human",
        "Erstelle ein Reel-Skript.\n\n"
        "Thema: {topic}\n"
        "Laenge: {duration_seconds} Sekunden\n"
        "Sprache: {language}\n\n"
        "Struktur:\n"
        "- HOOK (erste 1-3 Sekunden): Pattern-Interrupt, kontroverse Aussage oder Frage\n"
        "- SETUP (3-8 Sekunden): Problem oder Kontext etablieren\n"
        "- CONTENT (8-{content_end} Sekunden): Kerninhalt mit visuellen Wechseln alle 2-3 Sek\n"
        "- CTA (letzte 3-5 Sekunden): Klare Handlungsaufforderung\n\n"
        "Fuer jedes Segment angeben:\n"
        "- timestamp: Start-Ende im Format M:SS\n"
        "- type: HOOK, SETUP, CONTENT oder CTA\n"
        "- voiceover: Gesprochener Text\n"
        "- screen_text: Text-Overlay auf dem Bildschirm\n"
        "- visual: Beschreibung was visuell gezeigt wird\n\n"
        "Der voiceover_text ist der komplette gesprochene Text ohne Timestamps "
        "(fuer ElevenLabs-Voiceover).\n"
        "music_suggestion: Konkreter Musikstil oder Trending-Sound-Empfehlung."
    ),
])


def generate_caption(
    topic: str,
    niche: str,
    platform: str,
    language: str = "de",
    style: str = "listicle",
) -> dict:
    platform = platform.lower()
    specs = PLATFORM_SPECS.get(platform, PLATFORM_SPECS["instagram"])
    style_instruction = STYLE_PROMPTS.get(style, STYLE_PROMPTS["listicle"])

    chain = CAPTION_TEMPLATE | llm
    response = chain.invoke({
        "topic": topic,
        "niche": niche,
        "platform": platform,
        "language": language,
        "style_instruction": style_instruction,
        "max_caption": specs["max_caption"],
        "optimal_hashtags": specs["optimal_hashtags"],
    })

    import json
    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(text)


def generate_carousel_post(
    topic: str,
    num_slides: int = 10,
    language: str = "de",
) -> list[dict]:
    chain = CAROUSEL_TEMPLATE | llm
    response = chain.invoke({
        "topic": topic,
        "num_slides": num_slides,
        "language": language,
        "inner_end": num_slides - 1,
    })

    import json
    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(text)


def generate_reel_script(
    topic: str,
    duration_seconds: int = 30,
    language: str = "de",
) -> dict:
    chain = REEL_TEMPLATE | llm
    response = chain.invoke({
        "topic": topic,
        "duration_seconds": duration_seconds,
        "language": language,
        "content_end": duration_seconds - 5,
    })

    import json
    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(text)
