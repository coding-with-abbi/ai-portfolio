import sys
import os
import json
from dotenv import load_dotenv

load_dotenv()

from config.settings import Settings
from workflows.content_pipeline import ContentPipeline


NICHES = {
    "ki_tipps": "KI-Tipps / AI Tools",
    "finance": "Finance / Geld",
    "motivation": "Motivation / Hustle",
    "edutainment": "Edutainment / Fakten",
    "ki_girls": "KI-Girls / AI Personas",
}


def print_usage():
    print("""
Personal Brand Content Automation
==================================

Usage:
  python app.py plan <niche> [--period "Woche 1"] [--language de]
      Erstellt einen Content-Plan fuer die angegebene Nische.

  python app.py create <format> --topic "Thema" [--niche ki_tipps] [--language de]
      Erstellt ein einzelnes Content-Stueck.
      Formate: carousel, reel, linkedin, thread

  python app.py batch <niche> [--count 7] [--format carousel] [--language de]
      Generiert mehrere Content-Stuecke auf einmal.

  python app.py ideas <niche> [--count 10] [--language de]
      Generiert Post-Ideen fuer eine Nische.

Niches: ki_tipps, finance, motivation, edutainment, ki_girls

Examples:
  python app.py plan ki_tipps
  python app.py create carousel --topic "7 KI-Tools die dir 10 Stunden sparen"
  python app.py batch ki_tipps --count 5
  python app.py ideas finance --count 10
""")


def cmd_plan(args):
    niche = args[0] if args else "ki_tipps"
    period = _get_flag(args, "--period", "Woche 1")
    language = _get_flag(args, "--language", "de")

    print(f"\nNische: {NICHES.get(niche, niche)}")
    Settings.validate()

    pipeline = ContentPipeline()
    result = pipeline.run_weekly_plan(niche=niche, period=period, language=language)
    return result


def cmd_create(args):
    fmt = args[0] if args else "carousel"
    topic = _get_flag(args, "--topic", "5 KI-Tools die jeder kennen sollte")
    niche = _get_flag(args, "--niche", "ki_tipps")
    language = _get_flag(args, "--language", "de")

    print(f"\nFormat: {fmt}")
    print(f"Thema: {topic}")
    print(f"Nische: {NICHES.get(niche, niche)}")
    Settings.validate()

    pipeline = ContentPipeline()
    result = pipeline.create_single_post(topic=topic, fmt=fmt, niche=niche, language=language)

    print(f"\n--- GENERIERTER CONTENT ---\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


def cmd_batch(args):
    niche = args[0] if args else "ki_tipps"
    count = int(_get_flag(args, "--count", "7"))
    fmt = _get_flag(args, "--format", "carousel")
    language = _get_flag(args, "--language", "de")

    print(f"\nNische: {NICHES.get(niche, niche)}")
    print(f"Anzahl: {count}")
    print(f"Format: {fmt}")
    Settings.validate()

    from agents.content_planner import ContentPlannerAgent
    planner = ContentPlannerAgent()

    print(f"\nGeneriere {count} Post-Ideen...")
    ideas = planner.generate_post_ideas(niche=niche, count=count, language=language)

    topics = [idea.get("topic", idea.get("hook", "KI-Tipps")) for idea in ideas[:count]]

    pipeline = ContentPipeline()
    results = pipeline.batch_generate(topics=topics, fmt=fmt, niche=niche, language=language)
    return results


def cmd_ideas(args):
    niche = args[0] if args else "ki_tipps"
    count = int(_get_flag(args, "--count", "10"))
    language = _get_flag(args, "--language", "de")

    print(f"\nNische: {NICHES.get(niche, niche)}")
    Settings.validate()

    from agents.content_planner import ContentPlannerAgent
    planner = ContentPlannerAgent()

    ideas = planner.generate_post_ideas(niche=niche, count=count, language=language)

    print(f"\n--- {count} POST-IDEEN fuer {NICHES.get(niche, niche)} ---\n")
    for i, idea in enumerate(ideas, 1):
        print(f"{i}. [{idea.get('format', '?')}] {idea.get('topic', '?')}")
        print(f"   Hook: {idea.get('hook', '-')}")
        print(f"   Plattform: {idea.get('platform', '-')}")
        print(f"   Monetarisierung: {idea.get('monetization_potential', '-')}")
        if idea.get("affiliate_opportunity"):
            print(f"   Affiliate: {idea['affiliate_opportunity']}")
        print()

    return ideas


def _get_flag(args, flag, default=""):
    try:
        idx = args.index(flag)
        return args[idx + 1]
    except (ValueError, IndexError):
        return default


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    commands = {
        "plan": cmd_plan,
        "create": cmd_create,
        "batch": cmd_batch,
        "ideas": cmd_ideas,
    }

    if command in commands:
        commands[command](args)
    else:
        print(f"Unbekannter Befehl: {command}")
        print_usage()


if __name__ == "__main__":
    main()
