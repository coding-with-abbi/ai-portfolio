import json
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.callbacks import get_openai_callback
from config.settings import Settings


class ContentCreatorAgent:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            azure_endpoint=Settings.AZURE_OPENAI_ENDPOINT,
            api_key=Settings.AZURE_OPENAI_API_KEY,
            azure_deployment=Settings.AZURE_OPENAI_DEPLOYMENT,
            api_version=Settings.AZURE_OPENAI_API_VERSION,
            temperature=0.7,
        )

    def create_carousel(self, topic, niche="ki_tipps", num_slides=10, language="de", monitor=None):
        prompt_text = self._load_prompt("prompts/carousel_listicle.txt")

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Du bist ein viraler Social Media Content Creator. Antworte ausschließlich in validem JSON."),
            ("user", prompt_text),
        ])

        chain = prompt | self.llm

        if monitor:
            with get_openai_callback() as cb:
                result = chain.invoke({
                    "topic": topic,
                    "niche": niche,
                    "num_slides": num_slides,
                    "language": language,
                })
                monitor.track_llm_usage("content_creator", {
                    "prompt_tokens": cb.prompt_tokens,
                    "completion_tokens": cb.completion_tokens,
                    "total_tokens": cb.total_tokens,
                })
        else:
            result = chain.invoke({
                "topic": topic,
                "niche": niche,
                "num_slides": num_slides,
                "language": language,
            })

        return self._parse_json(result.content)

    def create_reel_script(self, topic, niche="ki_tipps", duration_seconds=30, language="de", style="educational", monitor=None):
        prompt_text = self._load_prompt("prompts/reel_script.txt")

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Du bist ein viraler Short-Form Video Scriptwriter. Antworte ausschließlich in validem JSON."),
            ("user", prompt_text),
        ])

        chain = prompt | self.llm

        if monitor:
            with get_openai_callback() as cb:
                result = chain.invoke({
                    "topic": topic,
                    "niche": niche,
                    "duration_seconds": duration_seconds,
                    "language": language,
                    "style": style,
                })
                monitor.track_llm_usage("content_creator", {
                    "prompt_tokens": cb.prompt_tokens,
                    "completion_tokens": cb.completion_tokens,
                    "total_tokens": cb.total_tokens,
                })
        else:
            result = chain.invoke({
                "topic": topic,
                "niche": niche,
                "duration_seconds": duration_seconds,
                "language": language,
                "style": style,
            })

        return self._parse_json(result.content)

    def create_linkedin_post(self, topic, pillar="expertise", language="en", monitor=None):
        prompt_text = self._load_prompt("prompts/linkedin_post.txt")

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Du bist ein LinkedIn Ghostwriter für AI/Tech-Thought-Leader. Antworte ausschließlich in validem JSON."),
            ("user", prompt_text),
        ])

        chain = prompt | self.llm

        if monitor:
            with get_openai_callback() as cb:
                result = chain.invoke({
                    "topic": topic,
                    "pillar": pillar,
                    "language": language,
                })
                monitor.track_llm_usage("content_creator", {
                    "prompt_tokens": cb.prompt_tokens,
                    "completion_tokens": cb.completion_tokens,
                    "total_tokens": cb.total_tokens,
                })
        else:
            result = chain.invoke({
                "topic": topic,
                "pillar": pillar,
                "language": language,
            })

        return self._parse_json(result.content)

    def create_x_thread(self, topic, niche="ki_tipps", num_tweets=6, language="en", monitor=None):
        prompt_text = self._load_prompt("prompts/x_thread.txt")

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Du bist ein X/Twitter Thread Writer. Antworte ausschließlich in validem JSON."),
            ("user", prompt_text),
        ])

        chain = prompt | self.llm

        if monitor:
            with get_openai_callback() as cb:
                result = chain.invoke({
                    "topic": topic,
                    "niche": niche,
                    "num_tweets": num_tweets,
                    "language": language,
                })
                monitor.track_llm_usage("content_creator", {
                    "prompt_tokens": cb.prompt_tokens,
                    "completion_tokens": cb.completion_tokens,
                    "total_tokens": cb.total_tokens,
                })
        else:
            result = chain.invoke({
                "topic": topic,
                "niche": niche,
                "num_tweets": num_tweets,
                "language": language,
            })

        return self._parse_json(result.content)

    def _load_prompt(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Prompt template not found: {path}")

    def _parse_json(self, text):
        text = text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        return json.loads(text.strip())
