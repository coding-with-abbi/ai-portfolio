# MASTERPLAN: Personal Brand & Content Automation System

## Anweisung an Claude Code

> Du bist ein System-Architekt und Prompt-Engineer. Dein Auftrag ist es, für Jacob Abb ein vollständig automatisiertes Content- und Personal-Brand-System aufzubauen. Dieses Dokument ist deine einzige Anweisung. Arbeite es sequenziell ab. Stelle Rückfragen nur, wenn Credentials fehlen.

---

## TEIL 0: KONTEXT — WER IST JACOB ABB?

**Aktuelles LinkedIn-Profil:**
- Headline: `IT-Consultant & AI Engineer | Building Production LLM Applications | RAG & Fine-Tuning | M. Sc. Business Informatics`
- Summary: Enterprise AI, RAG-Systeme, Agentic Workflows, LLM-Orchestrierung, Azure GenAI, SAP-Integration, MLOps
- Hintergrund: M.Sc. Business Informatics + Applied AI, Science Slam über KI
- GitHub: coding-with-abbi (ai-portfolio mit Workflow-Orchestrator + NLQ-to-SQL)

**Zielgruppen (Multi-Target):**
- Stream A (Personal Brand): CTOs, IT-Entscheider, Startups, Recruiter, Freelance-Kunden
- Stream B (Content Factory): Breites Social-Media-Publikum (Monetarisierung)

**Plattformen:** Instagram, TikTok, LinkedIn, YouTube Shorts, X (Twitter) — alle fünf

**Sprache:** Zweisprachig — Stream A primär Englisch (LinkedIn international) + Deutsch, Stream B je nach Account-Nische

---

## TEIL 1: STREAM A — PERSONAL BRAND FOUNDATION

### Phase 1.1: Brand Audit (Prompt-Chain, einmalig)

> Ziel: Jacobs aktuelle Marktwahrnehmung analysieren und die Lücke zwischen IST und SOLL aufdecken.

**Schritt 1: Brand Perception Audit**

Führe folgenden Prompt aus — mit Jacobs echtem Profil als Input:

```
<role>
Du bist ein Personal-Brand-Stratege, der hunderte Profile auf LinkedIn, X, Instagram und YouTube diagnostiziert hat. Du erkennst sofort die Lücke zwischen Selbstwahrnehmung und Marktwahrnehmung — damit jedes Profil, jede Bio und jeder Post um die Identität gebaut wird, die Aufträge, Follower und Bezahlung bringt, statt um die polierte Version, die ignoriert wird.
</role>

<task>
Versetze dich in den ersten Eindruck des Marktes und zeige mir exakt, was ein Recruiter, Investor oder potenzieller Kunde sieht, wenn er auf meinem Profil landet — damit ich die echte Lücke zwischen dem, wer ich bin, und dem, wie ich gerade rüberkomme, kenne, bevor ich ein einziges Wort ändere.
</task>

<context>
Aktuelle LinkedIn-Headline: "IT-Consultant & AI Engineer | Building Production LLM Applications | RAG & Fine-Tuning | M. Sc. Business Informatics"

Aktuelle Summary:
"I help organizations turn Generative AI into production-ready, enterprise-grade systems. My focus is on Retrieval-Augmented Generation (RAG), agentic workflows, and LLM orchestration, always grounded in a clear business purpose. AI should reduce complexity and manual effort — not add another layer of abstraction.

Over the past projects, I've designed and delivered enterprise knowledge assistants, permission-aware RAG systems, document-intelligence pipelines, and AI-driven workflow automations. My work spans from Azure-based GenAI architectures and MLOps pipelines to the integration of AI into SAP-centric business processes. I enjoy translating real operational challenges into robust, scalable AI solutions.

My background in Business Informatics and Applied AI allows me to bridge technical depth with process understanding. From multimodal LLM pipelines and hybrid retrieval strategies to secure deployment and governance in enterprise environments, I focus on building systems that are reliable, maintainable, and trusted by users.

What I bring to the table: hands-on implementation, architectural clarity, and honest judgment on what is feasible in production. If a solution doesn't create measurable impact, it's not worth deploying."

Zielgruppe: CTOs, IT-Entscheider in DAX/Mittelstand, Startup-Founder die AI-Systeme brauchen, Senior Recruiter für AI Engineering Rollen
Gewünschtes Ergebnis: Inbound-Anfragen für Freelance AI Engineering Projekte + Positionierung als Go-To AI Engineer im DACH-Raum
</context>

<steps>
1. Analysiere die aktuelle Brand Perception — was sagt das Profil aus, was impliziert es, und was schließt ein Fremder in 8 Sekunden?
2. Identifiziere den Gap zwischen beabsichtigtem Eindruck (Go-To AI Engineer für Enterprise) und tatsächlichem Eindruck
3. Mappe jedes Profil-Element das gegen mich arbeitet — die vage Headline, die generische Summary, der fehlende Social Proof, der falsche Ton
4. Prognostiziere die exakte erste Reaktion meines Traumkunden/Recruiters — klickt weg, nimmt Kontakt auf, oder liest weiter?
5. Liefere das komplette Brand Audit, die spezifischen Elemente die sofort gefixt werden müssen, und den einen Positioning Shift der alles verändert
</steps>

<rules>
- Brand Perception muss aus Marktperspektive gemappt werden — nie aus meiner eigenen Sicht
- Gap zwischen Intention und Wirkung muss explizit benannt werden
- Jedes Problem-Element muss spezifisch benannt werden — nicht "deine Summary ist schwach" sondern "deine Summary öffnet mit deinem Fokus statt mit dem Ergebnis das du für den Kunden erzeugst"
- Jeder Fix muss spezifisch genug sein um sofort umzusetzen
- Test: Würde mein Traumkunde nach dem Lesen meines Profils den Impuls haben, mich anzuschreiben?
</rules>

<output>
Current Brand Perception Map → Intended vs Actual Impression Gap → Profile Elements Working Against Me → First Impression Prediction → Specific Fixes to Implement Today
</output>
```

**Speichere den Output als:** `output/brand_foundation/01_brand_audit.md`

---

**Schritt 2: Magnetic Headline**

Nimm den Output von Schritt 1 und führe aus:

```
<role>
Du bist ein Positioning-Spezialist, der hunderte LinkedIn-Headlines für Executives, Founder und Operators geschrieben hat — und weißt, dass die Headline das Einzige ist, das zwischen einem Fremden, der weiterschrollt, und einem Fremden, der durchklickt, steht. Jedes Wort verdient seinen Platz durch kommunizierten Wert, nicht durch Jobtitel.
</role>

<task>
Versetze dich in einen Recruiter oder idealen Kunden der scrollt und zeige mir exakt, welche Headline ihn stoppen und auf mein Profil klicken lassen würde — damit meine ersten 10 Worte mehr leisten als die gesamte Summary der meisten Leute.
</task>

<context>
Aktuelle Headline: "IT-Consultant & AI Engineer | Building Production LLM Applications | RAG & Fine-Tuning | M. Sc. Business Informatics"
Brand Audit Ergebnis: [FÜGE OUTPUT VON SCHRITT 1 EIN]
Zielgruppe: CTOs, Startup-Founder, Senior AI Recruiter
Gewünschtes Ergebnis: Profil-Klick + Inbound Kontaktaufnahme
</context>

<steps>
1. Mappe was die aktuelle Headline kommuniziert — das implizierte Level, den implizierten Wert, die implizierte Audience, den implizierten Ask
2. Identifiziere den Gap zwischen dem was die Headline sagt und dem was sie sagen sollte — die besten Headlines versprechen die Zukunft, nicht die Vergangenheit
3. Mappe jedes Element einer magnetischen Headline — der Hook der den Scroll stoppt, der Wert der den Klick verdient, die Spezifität die Vertrauen aufbaut, das Outcome das Desire erzeugt
4. Generiere drei Headline-Variationen — eine Authority-led, eine Outcome-led, eine Curiosity-led — jede optimiert für die spezifische Zielgruppe
5. Liefere die komplette Headline-Map, die drei Variationen mit Erklärungen, und die empfohlene erste Wahl
</steps>

<rules>
- Headline muss aus der Perspektive der Zielgruppe geschrieben sein — nie aus dem was sich für mich beeindruckend anhört
- Jobtitel allein ist nie eine Headline — er beschreibt was ich tue, nicht warum jemanden das interessieren sollte
- Jede Variation muss so spezifisch sein, dass nur ich sie geschrieben haben könnte — kein generisches "helping businesses grow" Füllmaterial
- Jede Variation muss in LinkedIns 220-Zeichen-Headline-Limit passen
- Test: Würde meine Zielgruppe diese Headline in einem Suchergebnis lesen und auf mein Profil klicken?
</rules>

<output>
Current Headline Perception Map → Title vs Value Gap → Three Headline Variations → Explanation for Each → Recommended First Test
</output>
```

**Speichere als:** `output/brand_foundation/02_magnetic_headline.md`

---

**Schritt 3: Summary Rewrite**

Nimm Output von Schritt 1 + 2:

```
<role>
Du bist ein narrativer Brand Writer, der hunderte LinkedIn Summaries für Founder, Executives und Operators umgeschrieben hat — und weißt, dass die Summary der einzige Ort auf einem professionellen Profil ist, wo ein Mensch existieren darf. Jedes Wort baut Vertrauen auf, kommuniziert Wert, und gibt dem Leser das Gefühl, mich bereits zu kennen und zu mögen, bevor wir ein Wort gesprochen haben.
</role>

<task>
Versetze dich in meinen idealen Kunden oder Recruiter und zeige mir exakt, welche Summary ihnen das Gefühl geben würde, genau die richtige Person gefunden zu haben — damit meine About-Section die Lücke zwischen Profilbesuch und echtem Gespräch schließt.
</task>

<context>
Aktuelle Summary: [FÜGE JACOBS AKTUELLE SUMMARY EIN]
Brand Audit: [OUTPUT SCHRITT 1]
Neue Headline: [EMPFOHLENE HEADLINE AUS SCHRITT 2]
Zielgruppe: CTOs/Startup-Founder die AI-Implementierung brauchen, Senior Recruiter
Größter Professional Win: [FRAGE JACOB — z.B. "Permission-aware RAG System für DAX-Unternehmen gebaut das X Stunden/Woche einspart"]
Was Leser nach dem Lesen tun sollen: Nachricht schreiben für Freelance-Projekt oder Interview
</context>

<steps>
1. Mappe was die aktuelle Summary kommuniziert — Ton, implizierte Persönlichkeit, impliziertes Confidence-Level, implizierter Ask
2. Identifiziere den Gap zwischen der Summary die ich geschrieben habe und der Summary die meine Audience lesen muss — die meisten Summaries sind Lebensläufe, die besten sind Origin Stories
3. Mappe die Struktur einer magnetischen Summary — der Opening Hook der den Read verdient, die Origin Story die Vertrauen aufbaut, der Proof der Zweifel beseitigt, der spezifische Value der Desire erzeugt, der klare Call to Action
4. Schreibe die Summary im Gary-Vee-Framework um — direkt, selbstbewusst, proof-heavy, outcome-focused, human-first, null Corporate Language
5. Liefere das komplette Summary Rewrite, den strukturellen Breakdown jeder Sektion, und den spezifischen Call to Action zum Abschluss
</steps>

<rules>
- Summary muss mit einem Hook öffnen, nie mit einem Jobtitel oder "I am a..."
- Origin Story muss spezifisch und wahr sein — keine manufactured vulnerability, kein Humble-Brag als Story verkleidet
- Proof muss spezifisch sein — Zahlen, Namen, Outcomes — nie "extensive experience" oder "proven track record"
- Call to Action muss ein spezifischer Ask sein — nie drei Optionen, nie ein vages "let's connect"
- Test: Würde ein Fremder nach dem Lesen dieser Summary das Gefühl haben, mich bereits zu kennen und sich melden wollen?
</rules>

<output>
Current Summary Perception Map → Resume vs Story Gap → Magnetic Summary Structure → Full Summary Rewrite → Structural Breakdown → Specific Call to Action
</output>
```

**WICHTIG:** An der Stelle `[FRAGE JACOB]` muss Claude Code Jacob fragen:
- "Was ist dein größter Professional Win? Ein spezifisches Projekt mit messbarem Ergebnis?"
- "Was hat dich dazu gebracht, in AI zu gehen? Gibt es eine Origin Story?"
- "Hast du konkrete Zahlen? (z.B. X Stunden gespart, Y% Effizienz, Z Kunden)"

**Speichere als:** `output/brand_foundation/03_summary_rewrite.md`

---

**Schritt 4: Content Strategy & 3 Pillars**

```
<role>
Du bist ein Personal-Brand Content-Stratege, der Content-Systeme für Founder, Operators und Executives auf LinkedIn, X und Instagram aufgebaut hat — und weißt, dass Posten ohne Content-Strategie der schnellste Weg ist, eine Audience aufzubauen, die nie kauft, hiredt oder weiterempfiehlt. Jeder Post, jedes Thema und jedes Format wird gewählt, weil es Trust compounded mit exakt der Person, die es sehen muss.
</role>

<task>
Versetze dich in die LinkedIn-Timeline meiner Zielgruppe und zeige mir exakt, welcher Content sie dazu bringt, mir zu folgen, meine Posts zu speichern und mich schließlich anzuschreiben — damit jeder Content-Piece den ich publiziere die Brand aufbaut statt ins Leere zu füllen.
</task>

<context>
Nische: AI Engineering / Enterprise GenAI / RAG & LLM Systems
Zielgruppe: CTOs, IT-Entscheider (DACH), Startup-Founder, AI-Recruiter
Expertise-Bereiche: RAG-Systeme, Agentic Workflows, Azure GenAI, SAP+AI, MLOps, LLM-Orchestrierung
Neue Headline: [OUTPUT SCHRITT 2]
Neue Summary: [OUTPUT SCHRITT 3]
Aktuelle Posting-Frequenz: [FRAGE JACOB — wahrscheinlich unregelmäßig/selten]
</context>

<steps>
1. Mappe die aktuelle Content Perception — was sagen Jacobs bestehende Posts über ihn aus, was implizieren sie über seine Expertise, was schließt ein Fremder nach drei Posts über seinen Wert
2. Identifiziere den Gap zwischen dem Content den er postet und dem Content der Trust aufbaut bei seiner spezifischen Audience — die meisten Leute posten was sie interessant finden, die besten posten was ihre Audience glauben muss
3. Mappe die drei Content Pillars die jeden Post verankern sollten:
   - EXPERTISE PILLAR: Beweist "Ich beherrsche mein Fach" (technische Deep Dives, Architektur-Entscheidungen, Lessons Learned)
   - STORY PILLAR: Beweist "Ich bin ein Mensch" (Behind-the-scenes, Fails, Lernmomente, Science Slam Story)
   - OPINION PILLAR: Beweist "Ich habe eine Perspektive" (Hot Takes zu AI-Hype, Kontroverse Meinungen, Industrie-Kritik)
4. Generiere 10 spezifische Post-Ideen über die drei Pillars — echte Themen, echte Angles, echte Hooks — optimiert für Jacobs Nische und Audience
5. Liefere die komplette Content Strategy, die drei Pillars mit Beschreibungen, die 10 Post-Ideen mit Hooks, und die Posting-Kadenz die 12 Monate durchhaltbar ist
</steps>

<rules>
- Content Pillars müssen spezifisch für Jacobs Nische sein — nie generisches "share value, tell stories, give opinions"
- Post-Ideen müssen den spezifischen Hook beinhalten — nicht nur das Thema sondern die Eröffnungszeile die den Read verdient
- Posting-Kadenz muss 12 Monate durchhaltbar sein — 6 Wochen beeindruckend dann still ist schlimmer als konstant
- Jede Post-Idee muss der Zielgruppe dienen — wenn sie nur mich gut aussehen lässt, gehört sie in ein Tagebuch
- Test: Würde meine Zielgruppe 10 meiner Posts hintereinander lesen und mir genug vertrauen um sich zu melden?
</rules>

<output>
Current Content Perception Map → Posting vs Trust-Building Gap → Three Content Pillars with Descriptions → 10 Post Ideas with Hooks → Sustainable Posting Cadence
</output>
```

**Frage an Jacob:** "Wie oft postest du aktuell? Hast du bestehende Posts die gut performt haben?"

**Speichere als:** `output/brand_foundation/04_content_strategy.md`

---

**Schritt 5: Profile Conversion Funnel**

```
<role>
Du bist ein Conversion-Stratege, der hunderte passive LinkedIn-Profile in aktive Inbound-Pipelines verwandelt hat — und weißt, dass ein Profil kein Lebenslauf ist, sondern eine Landing Page. Jedes Element vom Banner bis zu den Experience-Beschreibungen ist dafür designed, einen Besucher ohne einzigen Cold Outreach vom Fremden zum Gesprächspartner zu machen.
</role>

<task>
Versetze dich in den Entscheidungsprozess meines idealen Kunden oder Recruiters und zeige mir exakt, welche Profil-Änderungen sie von der Profilansicht zum Kontaktaufnahme bewegen würden — damit mein Profil für mich verkauft, während ich schlafe.
</task>

<context>
Neue Headline: [OUTPUT SCHRITT 2]
Neue Summary: [OUTPUT SCHRITT 3]
Content Pillars: [OUTPUT SCHRITT 4]
Zielgruppe: CTOs die AI-Implementierung brauchen, Recruiter für Senior AI Engineering Rollen
Letzter Cold Inbound via LinkedIn: [FRAGE JACOB]
Aktuelle Featured Section: [FRAGE JACOB — wahrscheinlich leer]
Aktuelle Experience Descriptions: [FRAGE JACOB]
</context>

<steps>
1. Mappe den aktuellen Profile Conversion Path — was ein Besucher zuerst sieht, was Vertrauen aufbaut, was Desire erzeugt, was Action treibt, und wo sie abspringen
2. Identifiziere den Gap zwischen einem Profil das Views bekommt und einem Profil das Inbound generiert — die meisten Profile sind passiv, die besten sind aktive Funnels
3. Mappe jedes Conversion-Element das aktuell fehlt:
   - Banner der Wert kommuniziert (nicht nur Name/Firma)
   - Featured Section mit den drei besten Proof-of-Value Stücken
   - Experience Descriptions die Outcomes verkaufen, nicht Duties
   - Skills und Empfehlungen die Zweifel beseitigen
4. Baue den kompletten Conversion Funnel für das Profil — der Hook der den Scroll stoppt, der Proof der Trust aufbaut, der Value der Desire erzeugt, der CTA der Action treibt
5. Liefere das komplette Conversion Audit, die spezifischen Änderungen für jede Profil-Sektion, und die eine Ergänzung die in den nächsten 30 Tagen am meisten Inbound generieren würde
</steps>

<rules>
- Jedes Profil-Element muss dem Conversion-Ziel dienen — wenn es einen Besucher nicht näher an die Kontaktaufnahme bringt, gehört es woanders hin
- Experience Descriptions müssen mit Outcomes führen, nicht mit Duties — "Grew revenue 40%" nicht "responsible for sales"
- Featured Section müssen die drei besten Beweise meines Werts sein — nicht zufällige Posts, nicht LinkedIn-Artikel die keiner liest
- Call to Action muss an mindestens drei Stellen erscheinen — Headline, Summary-Ende und Featured Section
- Test: Würde mein Traumkunde auf meinem Profil landen, ohne Vorwissen über mich, und sich innerhalb von 48 Stunden melden?
</rules>

<output>
Current Conversion Path Map → Views vs Inbound Gap → Missing Conversion Elements → Complete Profile Funnel → Specific Section Changes → Highest-Impact 30-Day Addition
</output>
```

**Fragen an Jacob:**
- "Wann hat sich zuletzt jemand kalt über LinkedIn bei dir gemeldet?"
- "Was ist in deiner Featured Section? Oder ist sie leer?"
- "Wie sehen deine Experience-Beschreibungen aus — Aufgabenliste oder Ergebnisse?"

**Speichere als:** `output/brand_foundation/05_conversion_funnel.md`

---

### Phase 1.2: Brand Foundation — Zusammenführung

Nach Abschluss aller 5 Schritte, erstelle eine konsolidierte Datei:

```
output/brand_foundation/BRAND_BLUEPRINT.md
```

Inhalt:
- Neue Headline (empfohlene Variante)
- Neue Summary (komplett)
- Content Pillars (3 Stück mit je 3-4 Beispiel-Posts)
- Profile Conversion Checklist (jede Sektion mit spezifischem Fix)
- 30-Tage Action Plan (was zuerst umsetzen)

---

## TEIL 2: STREAM A — AUTOMATISIERTE CONTENT-PRODUKTION (Personal Brand)

### Phase 2.1: Content-Kalender-Automation

**Ziel:** Aus den 3 Content Pillars automatisch einen Monats-Kalender generieren.

**Prompt für wöchentliche Content-Planung:**

```
<role>
Du bist ein Content-Kalender-Stratege für Personal Brands im AI/Tech-Bereich. Du planst Content so, dass jeder Post einen strategischen Zweck erfüllt und die drei Pillars in einem rhythmischen Wechsel bespielt werden.
</role>

<task>
Erstelle einen detaillierten Content-Kalender für die nächste Woche basierend auf den Content Pillars, aktuellen Tech-Trends und der Zielgruppe.
</task>

<context>
Content Pillars:
1. EXPERTISE: [Aus Phase 1, Schritt 4]
2. STORY: [Aus Phase 1, Schritt 4]
3. OPINION: [Aus Phase 1, Schritt 4]

Plattformen: LinkedIn (Langform), Instagram (Reels + Carousels), TikTok (Short-form), X (Threads + Takes), YouTube Shorts
Posting-Kadenz: 
- LinkedIn: 3x/Woche (Di, Do, Sa)
- Instagram: 5x/Woche (tägliche Reels/Carousels)
- TikTok: 7x/Woche (täglich)
- X: 5x/Woche (Threads + Quick Takes)
- YouTube Shorts: 3x/Woche (repurposed Reels)
Sprache: LinkedIn = Englisch, Instagram/TikTok = Deutsch, X = Englisch, YouTube = Deutsch
</context>

<output>
Für jeden geplanten Post:
1. Datum + Plattform
2. Content Pillar (Expertise/Story/Opinion)
3. Format (Text Post, Carousel, Reel, Thread, Short)
4. Hook (erste Zeile / ersten 3 Sekunden)
5. Kernaussage (1 Satz)
6. CTA (was soll der Leser tun)
7. Hashtags (plattformspezifisch)
</output>
```

**Automation via Notion API:**
- Kalender als Notion-Datenbank anlegen
- Properties: Datum, Plattform, Pillar, Format, Status (Geplant/In Arbeit/Ready/Published)
- Automatisch befüllen via Notion API
- **Benötigter API-Key:** `NOTION_API_KEY` (Free Tier reicht)
- **Setup-Anweisung für Jacob:** Notion Integration erstellen unter notion.so/my-integrations → Internal Integration → Key kopieren → in .env eintragen

---

### Phase 2.2: Post-Generierung pro Plattform

**LinkedIn Post Generator:**

```
<role>
Du bist ein LinkedIn Ghostwriter für AI/Tech-Thought-Leader. Du schreibst Posts die den Algorithmus bedienen UND echten Wert liefern. Dein Stil: Kurze Absätze, ein Gedanke pro Zeile, Hook → Story → Insight → CTA.
</role>

<task>
Schreibe einen LinkedIn-Post basierend auf dem Kalender-Eintrag. Der Post muss den Algorithmus in den ersten 3 Zeilen catchen und in der Zielgruppe Trust aufbauen.
</task>

<context>
Kalender-Eintrag: [EINTRAG AUS PHASE 2.1]
Jacobs Stimme: Direkt, technisch fundiert aber verständlich, leicht provokant, anti-Buzzword, proof-heavy
Jacobs Expertise: RAG, Agentic Workflows, Azure GenAI, Enterprise AI, LLM-Orchestrierung
Zielgruppe: CTOs, Tech-Leads, AI Engineers, Recruiter
</context>

<rules>
- Erste Zeile muss den Scroll stoppen — Kontroverse, überraschende Zahl, oder Frage die zum Nachdenken zwingt
- Kein Corporate-Sprech, kein "I'm thrilled to announce", kein "Excited to share"
- Jeder Post muss EINEN Punkt machen, nicht drei
- Konkretes Beispiel oder Erfahrung > abstrakte Weisheit
- Formatierung: Kurze Absätze (1-2 Zeilen), Leerzeilen dazwischen, max 1300 Zeichen
- CTA am Ende: Frage an die Community ODER "DM me if..." ODER "Save this for later"
- 3-5 Hashtags am Ende, keine im Fließtext
</rules>
```

**Instagram Carousel Generator:**

```
<role>
Du bist ein Instagram Carousel Designer der AI/Tech-Content für ein breites Publikum aufbereitet. Dein Stil: Slide 1 = provokanter Hook, Slides 2-8 = ein Punkt pro Slide mit minimalem Text, letzte Slide = CTA.
</role>

<task>
Erstelle den Text-Content für ein Instagram Carousel (8-10 Slides) basierend auf dem Kalender-Eintrag. Gib für jede Slide den exakten Text und eine Design-Beschreibung an.
</task>

<rules>
- Slide 1: Maximal 8 Worte, Bold Statement oder Frage, muss im Feed auffallen
- Slides 2-9: Maximal 20 Worte pro Slide, ein Fakt/Punkt/Schritt pro Slide
- Letzte Slide: "Folge @[handle] für mehr" + Speicher-CTA
- Sprache: Deutsch (für den deutschen Markt)
- Stil: Wie die Screenshots aus "9 KI-Tools" — weiß auf dunkel, Bold Font, Bullet Points
- Gib für jede Slide an: [Text] + [Hintergrund-Beschreibung] + [Icon/Emoji falls relevant]
</rules>
```

**TikTok/Reels Script Generator:**

```
<role>
Du bist ein Short-Form Video Scriptwriter der AI-Themen in 30-60 Sekunden Reels verwandelt die viral gehen. Du kennst die Formel: Hook (0-3 Sek) → Problem (3-8 Sek) → Lösung (8-25 Sek) → Payoff (25-30 Sek) → CTA (30-35 Sek).
</role>

<task>
Schreibe ein Reel-Script für 30-45 Sekunden basierend auf dem Kalender-Eintrag. Das Script muss als Voiceover funktionieren (ElevenLabs) und als Text-Overlay auf dem Bildschirm.
</task>

<output>
Für jede Sekunde:
- [00:00-00:03] HOOK: "Text der gesprochen wird" | SCREEN: "Text auf dem Bildschirm" | VISUAL: "Was man sieht"
- [00:03-00:08] PROBLEM: ...
- usw.

+ Empfohlene Hintergrundmusik (Stimmung/Genre)
+ Hashtags (5 für TikTok, 15 für Instagram Reels)
</output>
```

**X/Twitter Thread Generator:**

```
<role>
Du bist ein X/Twitter Thread Writer für Tech-Thought-Leader. Dein Stil: Tweet 1 = magnetischer Hook der den Klick auf "Show more" erzwingt. Jeder Tweet = ein Gedanke, max 280 Zeichen. Der Thread liest sich wie ein Mini-Blog der Wert liefert und zum Retweet einlädt.
</role>

<task>
Schreibe einen X Thread (5-8 Tweets) basierend auf dem Kalender-Eintrag.
</task>

<rules>
- Tweet 1: Hook + "🧵" — muss standalone funktionieren und zum Klicken einladen
- Jeder Tweet: Max 280 Zeichen, ein Punkt, abgeschlossen
- Letzter Tweet: CTA (Follow, Retweet, oder DM)
- Sprache: Englisch (internationales Tech-Publikum)
- Keine Emojis außer 🧵 im ersten Tweet und ggf. einem Bullet-Emoji
</rules>
```

---

### Phase 2.3: Visual Asset Generation

**Canva API Integration:**
- **Benötigter Key:** `CANVA_API_KEY` (Connect API)
- **Setup:** canva.dev → App erstellen → OAuth Credentials
- **Funktion:** Carousel-Slides automatisch aus Text generieren
- **Fallback ohne API:** Canva-Anweisungen als Markdown generieren (welches Template, welcher Text, welche Farben)

**Design-Prompt für Canva/manuelle Erstellung:**

```
Erstelle eine Design-Anweisung für jede Carousel-Slide:
- Template-Stil: Dark Background (schwarz/dunkelblau), weiße Bold-Schrift, Akzentfarbe Cyan (#00D4FF)
- Brand-Font: Montserrat Bold für Headlines, Inter für Body
- Layout: Zentrierter Text, maximal 3 Zeilen pro Slide
- Jacob's Logo/Avatar: Oben rechts auf Slide 1 und letzter Slide
- Format: 1080x1350px (Instagram Carousel) / 1080x1920px (Story/Reel Cover)
```

---

### Phase 2.4: Voiceover Generation

**ElevenLabs API Integration:**
- **Benötigter Key:** `ELEVENLABS_API_KEY` (Free Tier: 10.000 Zeichen/Monat)
- **Setup:** elevenlabs.io → Sign up → API Key unter Profile → in .env eintragen
- **Voice ID:** `ELEVENLABS_VOICE_ID` — wähle eine professionelle männliche Stimme (z.B. "Adam" oder "Antoni") oder klone Jacobs Stimme (Pro Tier)
- **Funktion:** Reel-Scripts → MP3 Voiceover-Dateien

**Prompt für ElevenLabs-Ready Scripts:**

```
Nimm das Reel-Script und formatiere es als reines Voiceover-Script:
- Entferne alle Screen/Visual-Anweisungen
- Nur den gesprochenen Text, mit natürlichen Pausen (markiert als "...")
- Tonfall-Anweisungen in Klammern: (betont), (Pause), (schneller), (leiser)
- Output: Reiner Text, ready für ElevenLabs API Call
```

**API Call Pattern:**
```python
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}
Headers: { "xi-api-key": ELEVENLABS_API_KEY }
Body: { "text": "Script text here", "model_id": "eleven_multilingual_v2" }
→ Response: Audio-Datei (MP3)
→ Speichern als: output/voiceovers/{datum}_{thema}.mp3
```

---

### Phase 2.5: Video-Prompts & Editing-Anweisungen

**Für Sora (OpenAI Video Generation):**

```
Generiere einen optimierten Sora-Prompt basierend auf dem Reel-Script:
- Beschreibe die gewünschte Szene in 1-2 Sätzen auf Englisch
- Stil: Cinematic, professional, tech-aesthetic
- Dauer: 5-10 Sekunden pro Clip
- Aspekt: 9:16 (Reel/Short Format)
- Beispiel: "A close-up of hands typing on a glowing keyboard, blue light reflecting off the screen showing lines of code, cinematic shallow depth of field, 9:16 vertical"
```

**Für CapCut (Editing-Anweisungen):**

```
Erstelle eine detaillierte CapCut-Schnittanweisung:
1. Template-Empfehlung (welcher CapCut-Template-Stil passt)
2. Clip-Reihenfolge mit Timestamps
3. Text-Overlay-Timing (wann welcher Text erscheint)
4. Transition-Typ zwischen Clips (Cut, Fade, Zoom)
5. Untertitel-Stil (Bold, zentriert, max 2 Zeilen, Highlight-Wort in Farbe)
6. Musik-Empfehlung (Tempo, Stimmung, Genre)
7. Export-Settings: 1080x1920, 30fps, H.264
```

**Für OpusClip (falls Longform-Video vorhanden):**

```
Wenn Jacob ein Longform-Video hat (Podcast, Talk, Interview):
1. Video-URL übergeben an OpusClip API
2. OpusClip identifiziert die viralsten Momente
3. Output: 3-5 Short-Clips à 30-60 Sekunden
4. Pro Clip: Automatische Untertitel + Reframing auf 9:16

Benötigter Key: OPUSCLIP_API_KEY (Pro Plan, $9/Monat)
Setup: opus.pro → Account → API Key
```

---

## TEIL 3: STREAM B — SHORT-FORM CONTENT FACTORY (Monetarisierung)

### Phase 3.1: Account-Strategie & Nischen-Setup

**Ziel:** Mehrere thematische Accounts parallel betreiben, die algorithmisch skalieren.

**Nischen mit höchstem ROI (Geld pro Klick):**

| Nische | Plattform-Fokus | Monetarisierung | Content-Typ | Sprache |
|--------|----------------|-----------------|-------------|---------|
| **KI-Tipps / AI Tools** | TikTok + Instagram | Affiliate Links (Tool-Empfehlungen), Sponsoring | Listicle-Carousels, Reels | Deutsch |
| **KI-Girls / AI Personas** | Instagram + TikTok | Werbeeinnahmen, Sponsoring, Follower → Upsell | KI-generierte Bilder + Captions | Englisch |
| **Finance / Geld** | TikTok + YouTube Shorts | Affiliate (Broker, Krypto, Trading-Apps) | Fakten-Reels, Carousels | Deutsch |
| **Motivation / Hustle** | Instagram + TikTok | Produkt-Launches, Courses, Affiliate | Quote-Posts, Talking-Head Reels | Deutsch |
| **Edutainment / Fakten** | TikTok + YouTube Shorts | Ad Revenue (YT), Sponsoring | Fakten-Reels mit Voiceover | Deutsch |

**Prompt für Nischen-Analyse pro Account:**

```
<role>
Du bist ein Social Media Growth Strategist der Nischen-Accounts von 0 auf 100k Follower skaliert hat. Du kennst die Algorithmen von TikTok, Instagram und YouTube Shorts und weißt exakt welcher Content-Typ in welcher Nische die höchste Engagement-Rate und Monetarisierung hat.
</role>

<task>
Analysiere die Nische [NISCHE] und erstelle einen kompletten Account-Launch-Plan:
1. Account-Name Vorschläge (3 Optionen, prüfe Verfügbarkeit)
2. Bio-Text der sofort kommuniziert wofür der Account steht
3. Content-Formate die in dieser Nische am besten performen
4. Posting-Frequenz und beste Posting-Zeiten
5. Monetarisierungs-Strategie ab Tag 1
6. Erste 10 Post-Ideen mit Hooks
7. Hashtag-Strategie (Nischen-Hashtags + Trending)
8. Wachstums-Taktiken (Collabs, Trends, Duets)
</task>
```

---

### Phase 3.2: KI-Tipps / AI Tools Account (Höchster ROI)

**Warum höchster ROI:** Affiliate-Links für KI-Tools zahlen $20-100 pro Signup. Ein viraler Post kann tausende Signups generieren.

**Content-Template (wie die Screenshots vom Anfang):**

```
<role>
Du bist ein Viral Content Creator für den deutschsprachigen KI/Tech-Bereich. Dein Stil ist die "Listicle Carousel" — Posts wie "9 KI-Tools die dir einen unfairen Vorteil bringen" die massiv gespeichert und geteilt werden.
</role>

<task>
Erstelle einen kompletten Carousel-Post zum Thema [THEMA]. Der Post muss:
1. Im Feed durch den Hook-Slide auffallen
2. Auf jeder Slide einen konkreten Tool/Tipp mit Beschreibung liefern
3. Zum Speichern und Teilen einladen
4. Affiliate-Links in der Caption platzieren können
</task>

<output>
SLIDE 1 (Hook):
"[ZAHL] KI-Tools, die dir [ERGEBNIS]:"
[Hintergrund: Dunkel, dramatische Beleuchtung, Porträt oder Tech-Visual]

SLIDE 2-9 (je ein Tool):
• [Tool-Name] – [Was es tut, max 8 Worte]
[Hintergrund: Konsistent mit Slide 1]

SLIDE 10 (CTA):
"Folge @[handle] für mehr KI-Tipps"
"Speichere diesen Post für später 🔖"

CAPTION:
[Hook-Zeile]
[2-3 Sätze Kontext]
[Tool-Liste mit kurzer Beschreibung]
[Affiliate-Link-Platzhalter: "Link in Bio für alle Tools"]
[15-20 Hashtags]
</output>
```

**Batch-Produktion:** Generiere 7 solcher Posts pro Woche automatisch. Themen rotieren:
- "X KI-Tools für [Bereich]"
- "So nutzt du [Tool] für [Ergebnis]"
- "KI-News der Woche: [Top 3]"
- "Ich habe [Tool] getestet und das ist passiert"
- "[Berühmte Person] sagt: [AI-Quote] — hier ist warum das stimmt"

---

### Phase 3.3: KI-Girls / AI Persona Account

**Content-Produktion:**

```
<role>
Du bist ein Content Strategist für KI-generierte Persona-Accounts auf Instagram und TikTok. Du weißt, dass diese Accounts von Ästhetik, Konsistenz und Community-Engagement leben.
</role>

<task>
Erstelle einen Content-Plan für einen KI-Girls Account:
1. Persona-Definition (Name, Stil, Nische — z.B. "Tech Girl", "Fitness AI", "Travel AI")
2. Bild-Prompt-Templates für konsistente Optik (Midjourney/DALL-E/Stable Diffusion)
3. Caption-Templates (Lifestyle + Call to Engagement)
4. Story-Templates (Polls, Q&A, "Day in my life")
5. Reels-Konzepte (Photo Dumps mit Musik, "Get Ready With Me" KI-Version)
</task>

<bild-prompt-template>
Generiere für jedes Bild einen Midjourney/DALL-E Prompt:
"[Describe person]: [ethnicity], [hair], [style], [pose], [location], [lighting], [camera angle], [mood] --ar 4:5 --style raw --v 6.1"
Beispiel: "Beautiful young woman with long brown hair, casual chic outfit, sitting in a modern café with laptop, warm golden hour lighting, shot on Canon R5, shallow depth of field, confident smile --ar 4:5 --style raw --v 6.1"

WICHTIG: Alle Bilder müssen dieselbe Person zeigen → konsistenter Seed/Style
</bild-prompt-template>

<caption-template>
Generiere für jedes Bild eine Caption:
- Hook: Frage oder Statement das Engagement triggert
- Body: 2-3 Zeilen persönlich/relatable
- CTA: "Was denkt ihr?" / "Tag someone" / "Save for later"
- Hashtags: Mix aus Nischen + Trending (15-20)
- Sprache: Englisch (internationale Reichweite)
</caption-template>
```

---

### Phase 3.4: Finance Account

```
<role>
Du bist ein Finance Content Creator der komplexe Finanzthemen in 30-Sekunden Reels und Carousels verpackt die viral gehen. Dein Stil: Schockierende Zahlen als Hook, einfache Erklärung, konkreter Actionable Tipp.
</role>

<task>
Erstelle Content zum Thema [THEMA] in zwei Formaten:
1. Carousel (8 Slides): Fakten + Tipps
2. Reel-Script (30-45 Sek): Voiceover + Text-Overlay

Themen-Pool:
- "So viel Geld verlierst du durch [X]"
- "Warren Buffett's [X] Regel erklärt in 30 Sekunden"
- "ETF vs Aktien vs Krypto — die ehrliche Wahrheit"
- "[X]€ investiert vor [Y] Jahren wären heute [Z]€"
- "3 Geldfehler die dich arm halten"
</task>

<rules>
- Zahlen müssen korrekt und nachprüfbar sein
- Kein konkreter Finanzrat (Disclaimer: "Keine Anlageberatung")
- Affiliate-Links für: Trade Republic, Scalable Capital, eToro etc.
- Sprache: Deutsch
</rules>
```

---

### Phase 3.5: Motivation/Hustle + Edutainment

**Motivation-Template:**

```
Erstelle ein Motivations-Reel-Script basierend auf:
- Zitat einer bekannten Person (Sam Altman, Elon Musk, Naval Ravikant etc.)
- Kontext warum das Zitat relevant ist
- Eigene Interpretation / Lesson
- CTA: "Wer stimmt zu?"

Script-Struktur:
[00:00-00:03] HOOK: "[Person] hat gesagt..." | SCREEN: Zitat in Bold
[00:03-00:15] KONTEXT: Warum das wichtig ist
[00:15-00:25] LESSON: Was du daraus lernen kannst
[00:25-00:30] CTA: "Folge für mehr" | SCREEN: Follow-Button Animation

Voiceover: ElevenLabs (männlich, motivierend, leicht dramatisch)
Musik: Episch/Cinematic (NCS oder Copyright-free)
```

**Edutainment-Template:**

```
Erstelle ein Fakten-Reel:
- Fakt der überrascht/schockiert ("Wusstest du, dass...")
- Kurze Erklärung (max 20 Sekunden)
- Mind-Blown Moment
- CTA: "Folge für mehr solche Fakten"

Themen: KI, Technologie, Psychologie, Geschichte, Wirtschaft
Sprache: Deutsch
Format: Voiceover + Stockfootage-Beschreibung + Text-Overlay
```

---

## TEIL 4: TOOL-INTEGRATION & API-SETUP

### 4.1: Benötigte API-Keys (von Jacob einzurichten)

```
# .env — Alle benötigten Credentials

# --- PFLICHT (bereits vorhanden) ---
AZURE_OPENAI_API_KEY=           # Für LLM-basierte Content-Generierung
AZURE_OPENAI_ENDPOINT=          # Azure OpenAI Endpoint
AZURE_OPENAI_DEPLOYMENT=        # Deployment Name
AZURE_OPENAI_API_VERSION=       # API Version

# --- FREE TIER SETUP (Jacob muss einrichten) ---
ELEVENLABS_API_KEY=             # elevenlabs.io → Profile → API Key
ELEVENLABS_VOICE_ID=            # Voice auswählen oder eigene klonen
NOTION_API_KEY=                 # notion.so/my-integrations → Internal Integration
NOTION_CALENDAR_DB_ID=          # ID der Content-Kalender Datenbank
NOTION_IDEAS_DB_ID=             # ID der Ideen-Datenbank

# --- OPTIONAL (für erweiterte Features) ---
CANVA_API_KEY=                  # canva.dev → App erstellen (OAuth)
OPUSCLIP_API_KEY=               # opus.pro → API Key (Pro Plan, $9/Mo)
OPENAI_API_KEY=                 # Für Sora Video Generation (separater OpenAI Key)
SOCIALBLADE_CLIENT_ID=          # socialblade.com/developers
SOCIALBLADE_TOKEN=              # SocialBlade API Token

# --- CONTENT SETTINGS ---
CONTENT_LANGUAGE=de             # Default: Deutsch
DEFAULT_PLATFORMS=instagram,tiktok,linkedin,youtube,x
OUTPUT_DIR=output
```

**Setup-Anleitung für Jacob (Schritt für Schritt):**

1. **ElevenLabs (5 Min):**
   - Gehe zu elevenlabs.io → Sign Up (Free)
   - Profile → API Key → Kopieren
   - Voices → Wähle "Adam" (oder "Antoni" für Deutsch) → Voice ID kopieren
   - Free Tier: 10.000 Zeichen/Monat (ca. 8-10 Voiceovers)

2. **Notion (10 Min):**
   - Gehe zu notion.so/my-integrations
   - "New Integration" → Name: "Content Automation" → Submit
   - Internal Integration Token kopieren
   - Erstelle zwei Datenbanken in Notion:
     - "Content Calendar" (Properties: Datum, Plattform, Pillar, Format, Status, Text, Hook)
     - "Content Ideas" (Properties: Thema, Nische, Pillar, Priorität, Status)
   - Teile beide Datenbanken mit der Integration (Share → Invite → Integration auswählen)
   - Database IDs aus der URL kopieren (notion.so/[workspace]/[DATABASE_ID]?v=...)

3. **SocialBlade (5 Min):**
   - Gehe zu socialblade.com/developers
   - Account erstellen
   - Client ID + Token kopieren

4. **Canva (Optional, 10 Min):**
   - Gehe zu canva.dev
   - App erstellen → OAuth Credentials

5. **OpenAI für Sora (Optional, 5 Min):**
   - platform.openai.com → API Key erstellen
   - Achtung: Sora API wird Sept 2026 eingestellt → nur kurzfristig nutzbar

---

### 4.2: SocialBlade — Trend & Competitor Analysis

**Automatischer Trend-Report:**

```
<role>
Du bist ein Social Media Analyst der Wachstumsdaten interpretiert und daraus Content-Strategien ableitet.
</role>

<task>
Analysiere die folgenden SocialBlade-Daten und erstelle einen Trend-Report:
1. Welche Accounts in der Nische wachsen am schnellsten?
2. Welche Content-Formate korrelieren mit Wachstum?
3. Welche Posting-Frequenz haben die Top-Performer?
4. Welche Themen/Hooks sind aktuell viral?
5. Konkrete Empfehlungen für Jacobs Accounts
</task>

<input>
SocialBlade Daten für Competitor-Accounts:
[DATEN VIA SOCIALBLADE API ODER MANUELL]
</input>
```

**API Call Pattern (SocialBlade):**
```
GET https://matrix.sbapis.com/b/statistics?query={username}&platform={platform}
Headers: { "clientid": SOCIALBLADE_CLIENT_ID, "token": SOCIALBLADE_TOKEN }
→ Response: JSON mit Follower-History, Engagement-Rates, Growth-Trends
```

---

## TEIL 5: AUTOMATISIERUNGS-WORKFLOW (End-to-End)

### 5.1: Täglicher Workflow

```
MORGENS (automatisiert):
1. Trend-Check: SocialBlade + Web-Suche → Was ist heute viral?
2. Content-Kalender: Notion API → Welche Posts sind für heute geplant?
3. Content-Generierung:
   a. Für jeden geplanten Post → Prompt an Azure OpenAI
   b. Caption + Script + Hashtags generieren
   c. Voiceover via ElevenLabs (falls Reel)
   d. Design-Anweisungen für Canva
   e. Video-Anweisungen für CapCut/Sora
4. Output speichern in:
   output/
   ├── 2026-05-24/
   │   ├── linkedin/
   │   │   └── post_expertise_rag_tips.md
   │   ├── instagram/
   │   │   ├── carousel_ki_tools.md
   │   │   ├── carousel_slides/ (Design-Anweisungen)
   │   │   └── reel_script.md
   │   ├── tiktok/
   │   │   ├── reel_script.md
   │   │   └── voiceover.mp3
   │   ├── youtube/
   │   │   └── short_script.md
   │   └── x/
   │       └── thread_5_tweets.md
5. Notion-Status → "Ready to Publish"

ABENDS (Jacob manuell oder semi-automatisiert):
6. Review: Jacob liest/korrigiert den generierten Content
7. Publish: Manuell posten (oder via Buffer/Later/Hootsuite)
8. Track: Engagement-Daten nach 24h erfassen
```

### 5.2: Wöchentlicher Workflow

```
SONNTAG (automatisiert):
1. Performance-Review: Welche Posts der Woche haben am besten performt?
2. SocialBlade-Update: Wachstum der eigenen Accounts + Competitors
3. Content-Kalender: Nächste Woche planen
   - 3x LinkedIn, 5x Instagram, 7x TikTok, 5x X, 3x YouTube
   - Pillar-Rotation: Expertise → Story → Opinion → Expertise → ...
4. Batch-Generierung: Alle 23 Posts der Woche auf einmal generieren
5. Notion-Kalender aktualisieren
6. Monitoring-Report: Token-Usage, API-Kosten, Output-Statistiken
```

### 5.3: Monatlicher Workflow

```
1. Analytics Deep-Dive: Welche Nische/Plattform bringt den meisten ROI?
2. Strategy-Update: Content Pillars anpassen basierend auf Daten
3. Competitor-Analyse: Neue Trends, neue Formate
4. Brand Audit wiederholen (Prompt aus Phase 1.1, Schritt 1)
5. Monetarisierungs-Report: Affiliate-Einnahmen, Sponsoring-Anfragen, Inbound-Leads
```

---

## TEIL 6: MONITORING & KOSTEN-TRACKING

### 6.1: API-Kosten pro Monat (geschätzt)

| API | Nutzung/Monat | Kosten |
|-----|--------------|--------|
| Azure OpenAI (GPT-4) | ~500k Tokens | ~$20-30 |
| ElevenLabs (Free Tier) | 10.000 Zeichen | $0 |
| ElevenLabs (Starter, falls nötig) | 30.000 Zeichen | $5/Mo |
| Notion API | Unlimited Reads/Writes | $0 |
| SocialBlade | ~100 Queries | $0 (Free Tier) |
| Canva (optional) | ~20 Designs | $0-13/Mo |
| OpusClip (optional) | ~10 Clips | $9/Mo |
| **TOTAL** | | **$5-57/Mo** |

### 6.2: Output pro Monat (Ziel)

| Plattform | Posts/Monat | Format |
|-----------|-----------|--------|
| LinkedIn | 12 | Text Posts + Artikel |
| Instagram | 20-30 | Carousels + Reels |
| TikTok | 30 | Reels |
| X/Twitter | 20 | Threads + Takes |
| YouTube Shorts | 12 | Shorts |
| **TOTAL** | **~100 Content Pieces** | Multi-Format |

Davon **Stream A (Personal Brand):** ~30 Pieces/Monat
Davon **Stream B (Content Factory):** ~70 Pieces/Monat (über alle Nischen-Accounts)

---

## TEIL 7: IMPLEMENTIERUNGS-REIHENFOLGE (AKTUALISIERT)

> **Jacobs Entscheidung:** Stream B (Content Factory / Monetarisierung) zuerst. Brand Foundation parallel.
> **Talking Head:** Mix — Personal Brand mit Gesicht, Factory nur KI/Voiceover.
> **Bildgenerierung:** Azure OpenAI DALL-E (kein Midjourney/SD).
> **Origin Story:** Claude schlägt basierend auf Profil vor.

### Woche 1: Stream B — KI-Tipps Account Launch (HÖCHSTER ROI)
- [ ] ElevenLabs + Notion Free-Tier-Accounts einrichten
- [ ] .env mit allen verfügbaren Keys befüllen
- [ ] Account-Strategie für "KI-Tipps / AI Tools" Nische erstellen
- [ ] Erste 7 Carousel-Posts generieren (Listicle-Format, wie "9 KI-Tools" Screenshots)
- [ ] Erste 3 Reel-Scripts + ElevenLabs-Voiceovers generieren
- [ ] Instagram + TikTok Account erstellen, Bio optimieren
- [ ] Posting starten (1x/Tag)

### Woche 2: Stream B — Zweiter Account + Skalierung
- [ ] Finance-Account oder Edutainment-Account starten
- [ ] Batch-Generierung: 7 Posts/Woche automatisiert
- [ ] KI-Girls Account starten (DALL-E Prompts über Azure OpenAI)
- [ ] Affiliate-Links einrichten (Trade Republic, KI-Tools etc.)

### Woche 3: Stream A — Brand Foundation
- [ ] Brand Audit durchführen (Phase 1.1, alle 5 Schritte)
- [ ] Origin Story auf Basis Profil/Science Slam vorschlagen
- [ ] LinkedIn-Profil optimieren (Headline, Summary, Featured Section)
- [ ] Content Strategy erstellen (3 Pillars, 10 Post-Ideen)

### Woche 4: Stream A — Content Launch
- [ ] Notion Content-Kalender aufsetzen
- [ ] Erste 5 LinkedIn-Posts generieren
- [ ] Erste 3 Instagram Carousels (Personal Brand)
- [ ] Talking-Head Reel-Konzepte erstellen
- [ ] Performance-Tracking für alle Accounts aufsetzen

### Woche 5+: Scale & Optimize
- [ ] Alle Workflows als automatisierte Pipeline verbinden
- [ ] Monitoring-Dashboard aufbauen
- [ ] Monetarisierung optimieren (welche Nische bringt höchsten ROI?)
- [ ] Weitere Nischen-Accounts nach Bedarf
- [ ] Monatlicher Strategy Review

---

## TEIL 8: GEKLÄRTE ENTSCHEIDUNGEN

| Frage | Jacobs Antwort |
|-------|---------------|
| Talking Head | Mix: Personal Brand = Gesicht, Factory = KI/Voiceover |
| Bildgenerierung | Azure OpenAI DALL-E (kein Midjourney/SD nötig) |
| Start-Fokus | Stream B zuerst (Content Factory / Monetarisierung) |
| Origin Story | Claude schlägt vor basierend auf Profil + Science Slam |
| API-Keys | Azure OpenAI vorhanden + Free Tiers einrichten |
| Plattformen | Alle 5 (Instagram, TikTok, LinkedIn, YouTube, X) |
| Sprache | Zweisprachig je nach Stream |
| Stream B Ziel | Alles: Monetarisierung (Haupt), Reichweite, Funnel zu Brand |
| Stream B Nischen | KI-Tipps, KI-Girls, Finance, Motivation, Edutainment |
| Content-Formate | Reels/TikToks, KI-generierter Visual Content, Talking Head |

## NOCH OFFENE FRAGEN (werden während Implementierung gestellt)

1. **Instagram/TikTok Handles:** Hast du bereits Accounts? Wie heißen sie?
2. **Affiliate-Programme:** Hast du bereits Affiliate-Accounts bei KI-Tool-Anbietern?
3. **Professional Win mit Zahlen:** Konkretes Projekt für Brand Foundation (wird in Woche 3 benötigt)
4. **Posting-Frequenz aktuell:** Wie oft postest du aktuell?
5. **Budget-Bestätigung:** $5-57/Monat für API-Kosten okay?
