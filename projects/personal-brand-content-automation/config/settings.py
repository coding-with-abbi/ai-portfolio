import os
import warnings
from dotenv import load_dotenv

load_dotenv()


class Settings:
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "")
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
    ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "Adam")

    NOTION_API_KEY = os.getenv("NOTION_API_KEY", "")
    NOTION_CALENDAR_DB_ID = os.getenv("NOTION_CALENDAR_DB_ID", "")
    NOTION_IDEAS_DB_ID = os.getenv("NOTION_IDEAS_DB_ID", "")

    SOCIALBLADE_CLIENT_ID = os.getenv("SOCIALBLADE_CLIENT_ID", "")
    SOCIALBLADE_TOKEN = os.getenv("SOCIALBLADE_TOKEN", "")

    CANVA_API_KEY = os.getenv("CANVA_API_KEY", "")
    OPUSCLIP_API_KEY = os.getenv("OPUSCLIP_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    CONTENT_LANGUAGE = os.getenv("CONTENT_LANGUAGE", "de")
    OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")
    DEFAULT_PLATFORMS = os.getenv("DEFAULT_PLATFORMS", "instagram,tiktok,linkedin,youtube,x")

    @classmethod
    def validate(cls):
        required = {
            "AZURE_OPENAI_API_KEY": cls.AZURE_OPENAI_API_KEY,
            "AZURE_OPENAI_ENDPOINT": cls.AZURE_OPENAI_ENDPOINT,
            "AZURE_OPENAI_DEPLOYMENT": cls.AZURE_OPENAI_DEPLOYMENT,
        }
        missing = [k for k, v in required.items() if not v]
        if missing:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing)}. "
                "Set them in your .env file or export them."
            )

        optional = {
            "ElevenLabs (voiceover)": cls.ELEVENLABS_API_KEY,
            "Notion (content calendar)": cls.NOTION_API_KEY,
            "SocialBlade (analytics)": cls.SOCIALBLADE_CLIENT_ID,
            "Canva (design)": cls.CANVA_API_KEY,
            "OpusClip (video clipping)": cls.OPUSCLIP_API_KEY,
            "OpenAI / Sora (video generation)": cls.OPENAI_API_KEY,
        }
        for label, value in optional.items():
            if not value:
                warnings.warn(f"{label} API key not set -- integration unavailable.")
