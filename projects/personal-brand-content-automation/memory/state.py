"""
Pydantic domain models that track every piece of content as it flows through
the pipeline -- from initial idea to published post.
"""

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# --------------------------------------------------------------------------- #
#  Enums                                                                       #
# --------------------------------------------------------------------------- #

class PipelineStage(str, Enum):
    """Ordered stages a content item passes through."""
    research = "research"
    ideation = "ideation"
    scripting = "scripting"
    design = "design"
    voiceover = "voiceover"
    video = "video"
    publishing = "publishing"


class ContentType(str, Enum):
    """Supported content formats."""
    reel = "reel"
    carousel = "carousel"
    post = "post"
    story = "story"
    thread = "thread"
    short = "short"


class Platform(str, Enum):
    """Target distribution platforms."""
    instagram = "instagram"
    tiktok = "tiktok"
    linkedin = "linkedin"
    youtube = "youtube"
    x = "x"


class Niche(str, Enum):
    """Content niches / brand pillars."""
    ki_tipps = "ki_tipps"
    ki_girls = "ki_girls"
    finance = "finance"
    motivation = "motivation"
    edutainment = "edutainment"


# --------------------------------------------------------------------------- #
#  Core models                                                                 #
# --------------------------------------------------------------------------- #

class ContentItem(BaseModel):
    """A single piece of content moving through the pipeline."""
    title: str
    content_type: ContentType
    target_platforms: list[Platform]
    language: str = Field(default="de")
    niche: Niche
    topic: str
    hook: Optional[str] = None
    caption: Optional[str] = None
    script: Optional[str] = None
    voiceover_path: Optional[str] = None
    design_instructions: Optional[str] = None
    video_prompt: Optional[str] = None
    hashtags: list[str] = Field(default_factory=list)
    affiliate_links: list[str] = Field(default_factory=list)
    output_files: list[str] = Field(default_factory=list)
    scheduled_date: Optional[date] = None
    status: str = Field(default="draft")


class ContentPlan(BaseModel):
    """A weekly batch of content items for a specific niche."""
    niche: Niche
    week_number: int
    year: int
    items: list[ContentItem] = Field(default_factory=list)


class WorkflowState(BaseModel):
    """Top-level state object carried across the entire orchestration run."""
    original_request: str
    current_stage: PipelineStage = PipelineStage.research
    content_plan: Optional[ContentPlan] = None
    trend_data: dict = Field(default_factory=dict)
    context_results: list[str] = Field(default_factory=list)
