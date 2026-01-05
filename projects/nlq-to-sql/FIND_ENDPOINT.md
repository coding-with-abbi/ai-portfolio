# Wie finde ich den korrekten Azure OpenAI Endpoint?

## Problem
Der "Target URI" aus Azure AI Studio ist im Format:
```
https://lueddemanninvestments-resource.services.ai.azure.com/...
```

Aber LangChain benötigt den klassischen OpenAI-Endpoint:
```
https://lueddemanninvestments-resource.openai.azure.com
```

## Lösung: Endpoint im Azure Portal finden

1. **Gehen Sie zum Azure Portal**: https://portal.azure.com

2. **Navigieren Sie zu Ihrer Azure OpenAI Resource**:
   - Suchen Sie nach "Azure OpenAI" im Suchfeld
   - Wählen Sie Ihre Resource aus (z.B. "lueddemanninvestments-resource")

3. **Öffnen Sie "Keys and Endpoint"**:
   - Im linken Menü unter "Resource Management"
   - Klicken Sie auf "Keys and Endpoint"

4. **Kopieren Sie den Endpoint**:
   - Sie sehen einen "Endpoint" (nicht "Target URI")
   - Format: `https://[resource-name].openai.azure.com`
   - Beispiel: `https://lueddemanninvestments-resource.openai.azure.com`

5. **Kopieren Sie den API Key**:
   - Key 1 oder Key 2 (beide funktionieren)

## Ihre .env Datei sollte so aussehen:

```env
AZURE_OPENAI_ENDPOINT=https://lueddemanninvestments-resource.openai.azure.com
AZURE_OPENAI_API_KEY=1vjYDIG5fv2Sc9hbcRl4... (Ihr vollständiger Key)
AZURE_OPENAI_DEPLOYMENT=gpt-5.1-chat
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

**Wichtig**: 
- Kein `/openai/v1/` am Ende
- Kein `/api/projects/...` im Endpoint
- Nur: `https://[resource-name].openai.azure.com`

## Alternative: Wenn Sie nur den Target URI haben

Falls Sie nur den Target URI haben, können Sie versuchen, den Resource-Namen zu extrahieren:

1. Nehmen Sie den Target URI: `https://lueddemanninvestments-resource.services.ai.azure.com/...`
2. Extrahieren Sie den Resource-Namen: `lueddemanninvestments-resource`
3. Erstellen Sie den klassischen Endpoint: `https://lueddemanninvestments-resource.openai.azure.com`

Die automatische Konvertierung im Code sollte das bereits tun, aber es ist besser, den korrekten Endpoint direkt aus dem Azure Portal zu verwenden.

