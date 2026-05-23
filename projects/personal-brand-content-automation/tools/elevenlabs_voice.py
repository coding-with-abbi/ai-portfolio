import os
from pathlib import Path

import requests

from config.settings import Settings

_settings = Settings()

BASE_URL = "https://api.elevenlabs.io/v1"


def _get_headers() -> dict:
    return {
        "xi-api-key": _settings.ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
    }


def generate_voiceover(
    text: str,
    output_path: str,
    voice_id: str | None = None,
) -> str:
    if not _settings.ELEVENLABS_API_KEY:
        return "[WARNING] ELEVENLABS_API_KEY not set -- voiceover generation skipped."

    voice_id = voice_id or _settings.ELEVENLABS_VOICE_ID or "Adam"
    url = f"{BASE_URL}/text-to-speech/{voice_id}"

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0.4,
            "use_speaker_boost": True,
        },
    }

    response = requests.post(url, json=payload, headers=_get_headers(), timeout=120)
    response.raise_for_status()

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(response.content)

    return str(out.resolve())


def list_voices() -> list[dict]:
    if not _settings.ELEVENLABS_API_KEY:
        return [{"warning": "ELEVENLABS_API_KEY not set -- cannot list voices."}]

    url = f"{BASE_URL}/voices"
    response = requests.get(url, headers=_get_headers(), timeout=30)
    response.raise_for_status()
    data = response.json()

    return [
        {
            "voice_id": v["voice_id"],
            "name": v["name"],
            "category": v.get("category", ""),
            "labels": v.get("labels", {}),
        }
        for v in data.get("voices", [])
    ]
