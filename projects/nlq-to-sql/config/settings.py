import os
from dotenv import load_dotenv

load_dotenv()

AZURE_OPENAI_ENDPOINT_RAW = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")  # Standard API Version

# Bereinige Endpoint: Konvertiere verschiedene Formate zu OpenAI Format
if AZURE_OPENAI_ENDPOINT_RAW:
    endpoint = AZURE_OPENAI_ENDPOINT_RAW.rstrip("/")
    
    # WICHTIG: Entferne zuerst /openai/, /deployments/, etc. falls vorhanden
    # Das muss VOR der Konvertierung passieren
    if "/openai/" in endpoint.lower():
        endpoint = endpoint.split("/openai/")[0].rstrip("/")
    
    # Entferne Query-Parameter (api-version=...)
    if "?" in endpoint:
        endpoint = endpoint.split("?")[0].rstrip("/")
    
    # Wenn es ein AI Studio Endpoint ist (services.ai.azure.com), konvertiere zu OpenAI Format
    if "services.ai.azure.com" in endpoint:
        # Extrahiere den Resource-Namen
        if "/api/projects/" in endpoint:
            resource_part = endpoint.split("services.ai.azure.com")[0]
            resource_name = resource_part.replace("https://", "").rstrip("/").rstrip(".")
            endpoint = f"https://{resource_name}.openai.azure.com"
        else:
            resource_name = endpoint.split("services.ai.azure.com")[0].replace("https://", "").rstrip("/").rstrip(".")
            endpoint = f"https://{resource_name}.openai.azure.com"
    
    # Wenn es ein Cognitive Services Endpoint ist (cognitiveservices.azure.com), konvertiere zu OpenAI Format
    elif "cognitiveservices.azure.com" in endpoint:
        # Format: https://resource-name.cognitiveservices.azure.com
        # -> https://resource-name.openai.azure.com
        resource_part = endpoint.split("cognitiveservices.azure.com")[0]
        resource_name = resource_part.replace("https://", "").rstrip("/").rstrip(".")
        endpoint = f"https://{resource_name}.openai.azure.com"
    
    # Bereinige doppelte Punkte (falls vorhanden)
    endpoint = endpoint.replace("..", ".")
    
    AZURE_OPENAI_ENDPOINT = endpoint
else:
    AZURE_OPENAI_ENDPOINT = None

# Validierung der erforderlichen Umgebungsvariablen
if not AZURE_OPENAI_ENDPOINT:
    raise ValueError("AZURE_OPENAI_ENDPOINT ist nicht gesetzt. Bitte prüfe deine .env Datei.")
if not AZURE_OPENAI_API_KEY:
    raise ValueError("AZURE_OPENAI_API_KEY ist nicht gesetzt. Bitte prüfe deine .env Datei.")
if not AZURE_OPENAI_DEPLOYMENT:
    raise ValueError("AZURE_OPENAI_DEPLOYMENT ist nicht gesetzt. Bitte prüfe deine .env Datei.")

DB_PATH = "db/analytics.db"

