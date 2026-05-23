import json
import os
from datetime import datetime

from agents.content_planner import ContentPlannerAgent
from agents.content_creator import ContentCreatorAgent
from monitoring.monitor import ContentMonitor
from config.settings import Settings


class ContentPipeline:
    def __init__(self):
        self.planner = ContentPlannerAgent()
        self.creator = ContentCreatorAgent()
        self.monitor = ContentMonitor()
        self.output_dir = Settings.OUTPUT_DIR or "output"

    def run_weekly_plan(self, niche, period="Woche 1", language="de", platforms=None):
        print(f"\n{'='*60}")
        print(f"  CONTENT PIPELINE — {niche.upper()} — {period}")
        print(f"{'='*60}\n")

        print("[1/4] Erstelle Content-Strategie...")
        plan = self.planner.create_content_plan(
            niche=niche,
            period=period,
            language=language,
            platforms=platforms,
            monitor=self.monitor,
        )

        plan_path = self._save_json(plan, f"plans/{niche}_{period.replace(' ', '_')}.json")
        print(f"      Strategie gespeichert: {plan_path}")
        print(f"      {len(plan.get('posts', []))} Posts geplant\n")

        print("[2/4] Generiere Content fuer jeden Post...")
        generated = []
        posts = plan.get("posts", [])
        for i, post in enumerate(posts, 1):
            topic = post.get("topic", "")
            fmt = post.get("format", "carousel")
            print(f"      [{i}/{len(posts)}] {fmt}: {topic[:50]}...")

            content = self._generate_content_for_post(post, niche, language)
            content["meta"] = post
            generated.append(content)

        print(f"\n[3/4] Speichere generierten Content...")
        output_paths = []
        date_str = datetime.now().strftime("%Y-%m-%d")
        for i, content in enumerate(generated):
            post_meta = content.get("meta", {})
            fmt = post_meta.get("format", "post")
            day = post_meta.get("day", f"post_{i+1}")
            platform = post_meta.get("platform", "instagram")

            subdir = f"{date_str}/{niche}/{day}_{platform}"
            path = self._save_json(content, f"{subdir}/content.json")
            output_paths.append(path)

            if "reel_script" in content and content["reel_script"]:
                voiceover_text = content["reel_script"].get("voiceover_text", "")
                if voiceover_text:
                    vo_path = self._save_text(voiceover_text, f"{subdir}/voiceover_text.txt")
                    output_paths.append(vo_path)

        print(f"      {len(output_paths)} Dateien gespeichert\n")

        print("[4/4] Erstelle Monitoring-Report...")
        self.monitor.set_content_metrics(len(generated), niche, platforms or ["instagram", "tiktok"])
        report_path = self.monitor.finalize()
        print(self.monitor.get_summary_text())
        print(f"\n      Report: {report_path}\n")

        print(f"{'='*60}")
        print(f"  PIPELINE ABGESCHLOSSEN — {len(generated)} Content Pieces generiert")
        print(f"{'='*60}\n")

        return {
            "plan": plan,
            "generated_content": generated,
            "output_paths": output_paths,
            "report": report_path,
        }

    def create_single_post(self, topic, fmt="carousel", niche="ki_tipps", language="de", platforms=None):
        print(f"\nErstelle einzelnen {fmt}: {topic}\n")

        post = {
            "topic": topic,
            "format": fmt,
            "platform": (platforms or ["instagram"])[0],
        }

        content = self._generate_content_for_post(post, niche, language)

        date_str = datetime.now().strftime("%Y-%m-%d")
        slug = topic[:30].replace(" ", "_").lower()
        subdir = f"{date_str}/{niche}/{slug}"
        path = self._save_json(content, f"{subdir}/content.json")

        if "reel_script" in content and content["reel_script"]:
            voiceover_text = content["reel_script"].get("voiceover_text", "")
            if voiceover_text:
                self._save_text(voiceover_text, f"{subdir}/voiceover_text.txt")

        self.monitor.set_content_metrics(1, niche, platforms or ["instagram"])
        report_path = self.monitor.finalize()

        print(f"\nContent gespeichert: {path}")
        print(self.monitor.get_summary_text())

        return content

    def batch_generate(self, topics, fmt="carousel", niche="ki_tipps", language="de"):
        print(f"\nBatch-Generierung: {len(topics)} {fmt}s\n")

        results = []
        for i, topic in enumerate(topics, 1):
            print(f"[{i}/{len(topics)}] {topic[:50]}...")
            content = self.create_single_post(topic, fmt, niche, language)
            results.append(content)

        print(f"\n{len(results)} Content Pieces generiert.")
        return results

    def _generate_content_for_post(self, post, niche, language):
        topic = post.get("topic", "")
        fmt = post.get("format", "carousel")
        result = {"topic": topic, "format": fmt}

        if fmt == "carousel":
            result["carousel"] = self.creator.create_carousel(
                topic=topic, niche=niche, language=language, monitor=self.monitor
            )
        elif fmt in ("reel", "short"):
            result["reel_script"] = self.creator.create_reel_script(
                topic=topic, niche=niche, language=language, monitor=self.monitor
            )
        elif fmt == "text_post":
            result["linkedin_post"] = self.creator.create_linkedin_post(
                topic=topic, language=language, monitor=self.monitor
            )
        elif fmt == "thread":
            result["x_thread"] = self.creator.create_x_thread(
                topic=topic, niche=niche, language=language, monitor=self.monitor
            )
        else:
            result["carousel"] = self.creator.create_carousel(
                topic=topic, niche=niche, language=language, monitor=self.monitor
            )

        return result

    def _save_json(self, data, relative_path):
        full_path = os.path.join(self.output_dir, relative_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return full_path

    def _save_text(self, text, relative_path):
        full_path = os.path.join(self.output_dir, relative_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(text)
        return full_path
