import os

class Settings:
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2023-12-01-preview")

    @classmethod
    def validate(cls):
        required = [
            "AZURE_OPENAI_API_KEY",
            "AZURE_OPENAI_ENDPOINT",
            "AZURE_OPENAI_DEPLOYMENT"
        ]
        missing = [var for var in required if not getattr(cls, var)]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
