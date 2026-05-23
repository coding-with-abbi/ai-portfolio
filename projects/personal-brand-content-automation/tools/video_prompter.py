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

SORA_TEMPLATE = ChatPromptTemplate.from_messages([
    (
        "system",
        "Du bist ein Experte fuer Text-to-Video-Prompts, spezialisiert auf OpenAI Sora. "
        "Du erstellst detaillierte, filmisch praezise Prompts die hochwertige Videos erzeugen.\n\n"
        "Regeln fuer Sora-Prompts:\n"
        "- Beschreibe die Szene in einem einzigen, dichten Absatz\n"
        "- Beginne mit der Kamerabewegung und dem Blickwinkel\n"
        "- Beschreibe Beleuchtung, Farbpalette, Atmosphaere\n"
        "- Nenne den visuellen Stil explizit (cinematic, documentary, etc.)\n"
        "- Beschreibe Bewegungen und Aktionen praezise\n"
        "- Vermeide abstrakte Konzepte, sei visuell konkret\n\n"
        "Antworte NUR mit dem fertigen Prompt-Text, kein JSON, kein Markdown."
    ),
    (
        "human",
        "Erstelle einen Sora-Video-Prompt basierend auf folgendem Skript.\n\n"
        "Skript/Beschreibung:\n{script}\n\n"
        "Visueller Stil: {style}\n\n"
        "Der Prompt soll ein 5-15 Sekunden Video beschreiben das als B-Roll oder "
        "Intro-Clip fuer Social Media Content verwendet wird."
    ),
])

CAPCUT_TEMPLATE = ChatPromptTemplate.from_messages([
    (
        "system",
        "Du bist ein professioneller Video-Editor der detaillierte CapCut-Editing-Anleitungen "
        "erstellt. Du kennst alle CapCut-Funktionen (Keyframes, Uebergaenge, Textanimationen, "
        "Effekte, Audio-Sync, Speed Ramping).\n\n"
        "Erstelle die Anleitung als strukturiertes Markdown mit klaren Schritten."
    ),
    (
        "human",
        "Erstelle eine detaillierte CapCut-Editing-Anleitung fuer folgendes Skript.\n\n"
        "Skript:\n{script}\n\n"
        "Stil: {style}\n\n"
        "Die Anleitung muss enthalten:\n"
        "1. Projekt-Setup (Aufloesung, FPS, Seitenverhaeltnis)\n"
        "2. Timeline-Aufbau mit exakten Zeitangaben\n"
        "3. Textanimationen und Overlay-Positionen\n"
        "4. Uebergangseffekte zwischen Clips\n"
        "5. Empfohlene Effekte und Filter\n"
        "6. Audio-Anpassungen (Ducking, Fade-in/out)\n"
        "7. Export-Einstellungen fuer maximale Qualitaet"
    ),
])

DALLE_TEMPLATE = ChatPromptTemplate.from_messages([
    (
        "system",
        "Du bist ein Experte fuer DALL-E Bild-Prompts fuer Social-Media-Content. "
        "Du erstellst Prompts die visuell ansprechende, plattform-optimierte Bilder erzeugen.\n\n"
        "Regeln:\n"
        "- Beginne mit dem Bildtyp (photo, illustration, 3D render, flat design)\n"
        "- Beschreibe Hauptmotiv, Hintergrund, Farbschema\n"
        "- Nenne den Stil (minimalist, vibrant, professional, editorial)\n"
        "- Fuege technische Details hinzu (lighting, depth of field, composition)\n"
        "- Beruecksichtige das Seitenverhaeltnis im Prompt\n\n"
        "Antworte NUR mit dem fertigen Prompt-Text, kein JSON, kein Markdown."
    ),
    (
        "human",
        "Erstelle einen DALL-E Prompt fuer ein Social-Media-Bild.\n\n"
        "Beschreibung: {description}\n"
        "Stil: {style}\n"
        "Seitenverhaeltnis: {aspect}\n\n"
        "Das Bild wird als {usage} verwendet. Es soll professionell wirken "
        "und auf mobilen Geraeten gut lesbar sein. Vermeide Text im Bild."
    ),
])

STYLE_MAPPINGS = {
    "cinematic": "cinematic, shallow depth of field, dramatic lighting, 24fps film look",
    "documentary": "documentary style, natural lighting, handheld camera, authentic feel",
    "tech": "modern tech aesthetic, clean lines, neon accents, dark background",
    "minimal": "minimalist, clean white space, subtle movements, elegant transitions",
    "energetic": "fast-paced, dynamic camera movements, vibrant colors, high energy",
}

DALLE_STYLE_MAPPINGS = {
    "social_media": "social media post, eye-catching, vibrant, modern design",
    "thumbnail": "YouTube thumbnail, bold, high contrast, attention-grabbing",
    "editorial": "editorial photography, magazine quality, professional lighting",
    "minimal": "minimalist design, clean, modern, lots of white space",
    "tech": "futuristic tech aesthetic, dark mode, neon highlights, sleek",
}

ASPECT_DESCRIPTIONS = {
    "1:1": "square format, Instagram feed",
    "4:5": "portrait format, Instagram feed optimal",
    "9:16": "vertical story/reel format, TikTok and Instagram Stories",
    "16:9": "landscape format, YouTube thumbnail and LinkedIn",
}


def generate_sora_prompt(script: str, style: str = "cinematic") -> str:
    resolved_style = STYLE_MAPPINGS.get(style, style)
    chain = SORA_TEMPLATE | llm
    response = chain.invoke({"script": script, "style": resolved_style})
    return response.content.strip()


def generate_capcut_instructions(script: str, style: str = "tech") -> str:
    resolved_style = STYLE_MAPPINGS.get(style, style)
    chain = CAPCUT_TEMPLATE | llm
    response = chain.invoke({"script": script, "style": resolved_style})
    return response.content.strip()


def generate_dalle_prompt(
    description: str,
    style: str = "social_media",
    aspect: str = "4:5",
) -> str:
    resolved_style = DALLE_STYLE_MAPPINGS.get(style, style)
    usage = ASPECT_DESCRIPTIONS.get(aspect, aspect)
    chain = DALLE_TEMPLATE | llm
    response = chain.invoke({
        "description": description,
        "style": resolved_style,
        "aspect": aspect,
        "usage": usage,
    })
    return response.content.strip()
