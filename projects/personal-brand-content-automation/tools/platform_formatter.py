import json
import os
from pathlib import Path

from config.settings import Settings

_settings = Settings()

PLATFORM_RULES = {
    "instagram": {
        "max_caption_length": 2200,
        "max_hashtags": 30,
        "optimal_hashtags": 15,
        "line_break_style": "\n\n",
        "supports_links": False,
        "cta_style": "Link in Bio erwaehnen",
        "formats": ["feed", "carousel", "reel", "story"],
    },
    "tiktok": {
        "max_caption_length": 4000,
        "max_hashtags": 10,
        "optimal_hashtags": 5,
        "line_break_style": "\n",
        "supports_links": False,
        "cta_style": "Kommentar-CTA bevorzugen",
        "formats": ["video", "carousel", "story"],
    },
    "linkedin": {
        "max_caption_length": 3000,
        "max_hashtags": 5,
        "optimal_hashtags": 3,
        "line_break_style": "\n\n",
        "supports_links": True,
        "cta_style": "Professioneller Ton, Frage zum Abschluss",
        "formats": ["post", "article", "carousel", "video"],
    },
    "x": {
        "max_caption_length": 280,
        "max_hashtags": 3,
        "optimal_hashtags": 2,
        "line_break_style": "\n",
        "supports_links": True,
        "cta_style": "Retweet/Reply-CTA, Thread-Verweis",
        "formats": ["tweet", "thread", "video"],
    },
    "youtube": {
        "max_caption_length": 5000,
        "max_hashtags": 15,
        "optimal_hashtags": 5,
        "line_break_style": "\n\n",
        "supports_links": True,
        "cta_style": "Abo + Glocke erwaehnen, Timestamps nutzen",
        "formats": ["long_form", "short"],
    },
}


def _truncate_text(text: str, max_length: int) -> str:
    if len(text) <= max_length:
        return text
    truncated = text[:max_length - 3]
    last_space = truncated.rfind(" ")
    if last_space > max_length * 0.8:
        truncated = truncated[:last_space]
    return truncated + "..."


def _limit_hashtags(hashtags: list[str], max_count: int) -> list[str]:
    normalized = []
    for tag in hashtags[:max_count]:
        tag = tag.strip()
        if not tag.startswith("#"):
            tag = f"#{tag}"
        normalized.append(tag)
    return normalized


def format_for_platform(content_item: dict, platform: str) -> dict:
    platform = platform.lower()
    rules = PLATFORM_RULES.get(platform, PLATFORM_RULES["instagram"])

    caption = content_item.get("full_caption", "")
    if not caption:
        parts = []
        if content_item.get("hook"):
            parts.append(content_item["hook"])
        if content_item.get("body"):
            parts.append(content_item["body"])
        if content_item.get("cta"):
            parts.append(content_item["cta"])
        caption = rules["line_break_style"].join(parts)

    hashtags = content_item.get("hashtags", [])
    hashtags = _limit_hashtags(hashtags, rules["optimal_hashtags"])
    hashtag_text = " ".join(hashtags)

    full_with_hashtags = f"{caption}{rules['line_break_style']}{hashtag_text}"

    if len(full_with_hashtags) > rules["max_caption_length"]:
        available = rules["max_caption_length"] - len(hashtag_text) - len(rules["line_break_style"])
        caption = _truncate_text(caption, available)
        full_with_hashtags = f"{caption}{rules['line_break_style']}{hashtag_text}"

    return {
        "platform": platform,
        "caption": full_with_hashtags,
        "hashtags": hashtags,
        "character_count": len(full_with_hashtags),
        "max_allowed": rules["max_caption_length"],
        "supports_links": rules["supports_links"],
        "recommended_formats": rules["formats"],
        "original_content": content_item,
    }


def create_publishing_package(
    content_item: dict,
    platforms: list[str],
) -> list[str]:
    output_base = Path(_settings.OUTPUT_DIR) / "publishing_ready"
    created_files = []

    for platform in platforms:
        formatted = format_for_platform(content_item, platform)
        platform_dir = output_base / platform.lower()
        platform_dir.mkdir(parents=True, exist_ok=True)

        topic_slug = content_item.get("topic", "content").lower()
        topic_slug = "".join(c if c.isalnum() or c == "-" else "-" for c in topic_slug)
        topic_slug = topic_slug.strip("-")[:50]

        caption_path = platform_dir / f"{topic_slug}_caption.txt"
        caption_path.write_text(formatted["caption"], encoding="utf-8")
        created_files.append(str(caption_path.resolve()))

        meta_path = platform_dir / f"{topic_slug}_meta.json"
        meta = {
            "platform": platform,
            "character_count": formatted["character_count"],
            "hashtags": formatted["hashtags"],
            "supports_links": formatted["supports_links"],
            "recommended_formats": formatted["recommended_formats"],
        }
        meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
        created_files.append(str(meta_path.resolve()))

    return created_files
