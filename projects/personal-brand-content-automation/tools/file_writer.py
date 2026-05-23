import json
from datetime import date
from pathlib import Path

from config.settings import Settings

_settings = Settings()


def write_content(content: str | dict | list, filename: str, subdir: str = "") -> str:
    base = Path(_settings.OUTPUT_DIR)
    if subdir:
        base = base / subdir
    base.mkdir(parents=True, exist_ok=True)

    filepath = base / filename

    if isinstance(content, (dict, list)):
        filepath.write_text(
            json.dumps(content, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
    else:
        filepath.write_text(str(content), encoding="utf-8")

    return str(filepath.resolve())


def write_daily_batch(batch_date: date, contents: list[dict]) -> list[str]:
    date_str = batch_date.isoformat()
    base = Path(_settings.OUTPUT_DIR) / "daily" / date_str
    base.mkdir(parents=True, exist_ok=True)

    created_files = []

    manifest = {
        "date": date_str,
        "total_pieces": len(contents),
        "items": [],
    }

    for i, item in enumerate(contents, 1):
        content_type = item.get("type", "caption")
        topic = item.get("topic", f"content_{i}")
        topic_slug = "".join(c if c.isalnum() or c == "-" else "-" for c in topic.lower())
        topic_slug = topic_slug.strip("-")[:50]
        platform = item.get("platform", "general")

        filename = f"{i:02d}_{platform}_{content_type}_{topic_slug}.json"
        filepath = base / filename
        filepath.write_text(
            json.dumps(item, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        created_files.append(str(filepath.resolve()))

        manifest["items"].append({
            "index": i,
            "filename": filename,
            "type": content_type,
            "topic": topic,
            "platform": platform,
        })

    manifest_path = base / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    created_files.append(str(manifest_path.resolve()))

    return created_files
