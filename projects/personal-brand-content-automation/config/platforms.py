"""
Platform-specific content specifications.

Each entry describes the constraints and best practices for a single social
media platform so that downstream agents can tailor captions, aspect ratios,
durations, and posting schedules automatically.
"""

PLATFORMS: dict[str, dict] = {
    "instagram": {
        "max_caption_length": 2200,
        "hashtag_limit": 30,
        "video_aspect_ratio": "9:16",
        "video_max_duration_seconds": 90,
        "supported_formats": ["reel", "carousel", "post", "story"],
        "best_posting_times": [8, 12, 17, 20],
    },
    "tiktok": {
        "max_caption_length": 4000,
        "hashtag_limit": 5,
        "video_aspect_ratio": "9:16",
        "video_max_duration_seconds": 180,
        "supported_formats": ["reel", "story"],
        "best_posting_times": [7, 10, 19, 22],
    },
    "linkedin": {
        "max_caption_length": 3000,
        "hashtag_limit": 5,
        "video_aspect_ratio": "1:1",
        "video_max_duration_seconds": 600,
        "supported_formats": ["post", "carousel", "reel"],
        "best_posting_times": [8, 10, 12, 17],
    },
    "youtube_shorts": {
        "max_caption_length": 100,
        "hashtag_limit": 3,
        "video_aspect_ratio": "9:16",
        "video_max_duration_seconds": 60,
        "supported_formats": ["short"],
        "best_posting_times": [12, 15, 18, 21],
    },
    "x": {
        "max_caption_length": 280,
        "hashtag_limit": 3,
        "video_aspect_ratio": "16:9",
        "video_max_duration_seconds": 140,
        "supported_formats": ["post", "thread", "reel"],
        "best_posting_times": [9, 12, 17, 21],
    },
}
