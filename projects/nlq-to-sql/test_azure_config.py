"""
Debug-Skript zum Testen der Azure OpenAI Konfiguration
"""
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

# Lade Konfiguration
endpoint_raw = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

# Bereinige Endpoint: Konvertiere verschiedene Formate zu OpenAI Format
if endpoint_raw:
    endpoint = endpoint_raw.rstrip("/")
    
    # Wenn es ein AI Studio Endpoint ist (services.ai.azure.com), konvertiere zu OpenAI Format
    if "services.ai.azure.com" in endpoint:
        if "/api/projects/" in endpoint:
            resource_part = endpoint.split("services.ai.azure.com")[0]
            resource_name = resource_part.replace("https://", "").rstrip("/")
            endpoint = f"https://{resource_name}.openai.azure.com"
        else:
            resource_name = endpoint.split("services.ai.azure.com")[0].replace("https://", "").rstrip("/")
            endpoint = f"https://{resource_name}.openai.azure.com"
    
    # Wenn es ein Cognitive Services Endpoint ist (cognitiveservices.azure.com), konvertiere zu OpenAI Format
    elif "cognitiveservices.azure.com" in endpoint:
        resource_part = endpoint.split("cognitiveservices.azure.com")[0]
        resource_name = resource_part.replace("https://", "").rstrip("/")
        endpoint = f"https://{resource_name}.openai.azure.com"
    
    # Entferne /openai/, /deployments/, etc. falls vorhanden, da LangChain das automatisch hinzufügt
    if "/openai/" in endpoint.lower():
        endpoint = endpoint.split("/openai/")[0].rstrip("/")
else:
    endpoint = None

print("=" * 60)
print("Azure OpenAI Konfiguration Test")
print("=" * 60)
print(f"\nEndpoint (roh): {endpoint_raw}")
print(f"Endpoint (bereinigt): {endpoint}")
print(f"Deployment: {deployment}")
print(f"API Version: {api_version}")
print(f"API Key vorhanden: {'Ja' if api_key else 'Nein'}")
print(f"API Key Länge: {len(api_key) if api_key else 0} Zeichen")
print(f"API Key (erste 10 Zeichen): {api_key[:10] + '...' if api_key and len(api_key) > 10 else 'N/A'}")

# Prüfe Endpoint-Format
if endpoint:
    if not endpoint.startswith("https://"):
        print("\n⚠️  WARNUNG: Endpoint sollte mit 'https://' beginnen")
    if "services.ai.azure.com" in endpoint_raw.lower():
        print("✅ AI Studio Endpoint wurde zu OpenAI Format konvertiert")
    if "/openai/v1" in endpoint_raw.lower():
        print("✅ Endpoint wurde automatisch bereinigt (entfernt /openai/v1/)")

print("\n" + "=" * 60)
print("Teste Verbindung...")
print("=" * 60)

try:
    clean_endpoint = endpoint
    
    llm = AzureChatOpenAI(
        azure_endpoint=clean_endpoint,
        api_key=api_key,
        deployment_name=deployment,
        api_version=api_version,
        temperature=0
    )
    
    # Teste mit einer einfachen Nachricht
    response = llm.invoke("Say 'Hello' if you can read this.")
    print(f"\n✅ Erfolg! Antwort: {response.content}")
    print("\n✅ Ihre Azure OpenAI Konfiguration ist korrekt!")
    
except Exception as e:
    print(f"\n❌ Fehler: {e}")
    print("\n🔍 Mögliche Lösungen:")
    print("1. Prüfe, ob der API-Key korrekt ist (kopiere ihn erneut aus dem Azure Portal)")
    print("2. Prüfe, ob der Endpoint korrekt ist (sollte so aussehen: https://your-resource.openai.azure.com)")
    print("3. Prüfe, ob das Deployment existiert und aktiv ist")
    print("4. Prüfe, ob die API-Version korrekt ist (versuche '2024-02-15-preview' oder '2023-12-01-preview')")
    print("5. Prüfe, ob dein Azure-Account Zugriff auf die OpenAI Resource hat")

