import io
from gtts import gTTS
from fpdf import FPDF

GAMER_THEME_CSS = """
<style>
/* ============================================================
   GAMER THEME — "BLOCK-WORLD HUD"
   Dark esports dashboard meets blocky sandbox-game UI.
   ============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=JetBrains+Mono:wght@400;500;700&display=swap');

:root {
    --gt-bg-void: #0c0d0c;
    --gt-bg-panel: #17181a;
    --gt-bg-slot: #232426;
    --gt-border-dark: #000000;
    --gt-border-light: #4a4d4a;
    --gt-green: #39ff14;
    --gt-cyan: #00e5ff;
    --gt-gold: #ffd700;
    --gt-red: #ff3b3b;
    --gt-text: #d8ffd6;
    --gt-text-dim: #8a9a88;
    --gt-font-display: 'Press Start 2P', monospace;
    --gt-font-body: 'JetBrains Mono', 'Courier New', monospace;
}

/* ---------- 1. APP SHELL & TYPOGRAPHY ---------- */
.stApp {
    background-color: var(--gt-bg-void);
    background-image:
        linear-gradient(var(--gt-border-light) 1px, transparent 1px),
        linear-gradient(90deg, var(--gt-border-light) 1px, transparent 1px);
    background-size: 34px 34px;
    background-position: -1px -1px;
    color: var(--gt-text);
    font-family: var(--gt-font-body);
}

.stApp h1, .stApp h2, .stApp h3 {
    font-family: var(--gt-font-display);
    color: var(--gt-green);
    text-shadow: 0 0 6px rgba(57, 255, 20, 0.55), 0 0 14px rgba(57, 255, 20, 0.25);
    letter-spacing: 1px;
    text-transform: uppercase;
    line-height: 1.7;
}

.stApp h4, .stApp h5, .stApp h6 {
    font-family: var(--gt-font-body);
    font-weight: 700;
    color: var(--gt-cyan);
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* ---------- 2. BUTTONS — BLOCKY GAME-MENU SELECT ---------- */
div[data-testid="stButton"] > button,
.stButton > button {
    font-family: var(--gt-font-body);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--gt-green);
    background-color: var(--gt-bg-panel);
    border: 3px solid var(--gt-border-dark);
    border-radius: 0px;
    padding: 0.55em 1.4em;
    box-shadow:
        inset 2px 2px 0px 0px var(--gt-border-light),
        inset -2px -2px 0px 0px #000000;
    transition: transform 0.08s ease-out, box-shadow 0.15s ease-out,
        color 0.15s ease-out, border-color 0.15s ease-out;
    cursor: pointer;
}

div[data-testid="stButton"] > button:hover,
.stButton > button:hover {
    color: #eaffea;
    border-color: var(--gt-green);
    transform: scale(1.045);
    box-shadow:
        inset 2px 2px 0px 0px var(--gt-border-light),
        inset -2px -2px 0px 0px #000000,
        0 0 8px 1px rgba(57, 255, 20, 0.65),
        0 0 22px 2px rgba(57, 255, 20, 0.3);
    text-shadow: 0 0 8px rgba(57, 255, 20, 0.9);
}

div[data-testid="stButton"] > button:active,
.stButton > button:active {
    transform: scale(0.98);
    box-shadow:
        inset -2px -2px 0px 0px var(--gt-border-light),
        inset 2px 2px 0px 0px #000000;
}

div[data-testid="stButton"] > button:focus-visible,
.stButton > button:focus-visible {
    outline: 2px solid var(--gt-cyan);
    outline-offset: 3px;
}

.stButton > button[kind="primary"] {
    color: var(--gt-gold);
}
.stButton > button[kind="primary"]:hover {
    border-color: var(--gt-gold);
    box-shadow:
        inset 2px 2px 0px 0px var(--gt-border-light),
        inset -2px -2px 0px 0px #000000,
        0 0 8px 1px rgba(255, 215, 0, 0.65),
        0 0 22px 2px rgba(255, 215, 0, 0.3);
    text-shadow: 0 0 8px rgba(255, 215, 0, 0.9);
}

/* ---------- 3. DATA EDITOR — INVENTORY / STAT SHEET ---------- */
[data-testid="stDataFrame"] {
    border: 3px solid var(--gt-border-dark);
    outline: 1px solid var(--gt-green);
    outline-offset: -1px;
    box-shadow: 0 0 14px rgba(57, 255, 20, 0.15);
    background-color: var(--gt-bg-slot);
    padding: 2px;
}

[data-testid="stElementToolbar"] {
    background-color: var(--gt-bg-panel);
    border: 1px solid var(--gt-border-light);
}

/* ---------- 4. EXPANDERS — LOOT CHEST / TERMINAL ---------- */
[data-testid="stExpander"] {
    background-color: var(--gt-bg-panel);
    border: 2px solid var(--gt-border-dark);
    box-shadow: inset 0 0 0 1px var(--gt-border-light);
    border-radius: 0px;
    margin-bottom: 0.6em;
}

[data-testid="stExpander"] summary {
    font-family: var(--gt-font-body);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--gt-cyan);
    background-color: var(--gt-bg-slot);
    border-bottom: 2px solid var(--gt-border-dark);
    padding: 0.5em 0.9em;
    cursor: pointer;
}

[data-testid="stExpander"] summary::before {
    content: ">_ ";
    color: var(--gt-green);
}

[data-testid="stExpander"] summary:hover {
    color: var(--gt-green);
    text-shadow: 0 0 6px rgba(57, 255, 20, 0.6);
}

[data-testid="stExpander"] details[open] > summary {
    color: var(--gt-gold);
    border-bottom-color: var(--gt-gold);
    text-shadow: 0 0 8px rgba(255, 215, 0, 0.6);
}

[data-testid="stExpander"] details[open] > summary::before {
    content: "[UNLOCKED] ";
    color: var(--gt-gold);
}

[data-testid="stExpanderDetails"] {
    background-color: var(--gt-bg-void);
    padding: 1em;
    border-top: 1px solid var(--gt-border-light);
}

/* ---------- 5. METRICS — PLAYER HUD ---------- */
[data-testid="stMetric"] {
    background-color: var(--gt-bg-panel);
    border: 2px solid var(--gt-border-dark);
    padding: 0.8em 1em;
    position: relative;
}

[data-testid="stMetric"]::before,
[data-testid="stMetric"]::after {
    content: "";
    position: absolute;
    width: 10px;
    height: 10px;
    border-color: var(--gt-green);
    border-style: solid;
    pointer-events: none;
}
[data-testid="stMetric"]::before {
    top: -2px;
    left: -2px;
    border-width: 2px 0 0 2px;
}
[data-testid="stMetric"]::after {
    bottom: -2px;
    right: -2px;
    border-width: 0 2px 2px 0;
}

[data-testid="stMetricLabel"] {
    font-family: var(--gt-font-body);
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--gt-text-dim);
    font-size: 0.8em;
}

[data-testid="stMetricValue"] {
    font-family: var(--gt-font-display);
    color: var(--gt-green);
    text-shadow: 0 0 8px rgba(57, 255, 20, 0.6), 0 0 18px rgba(57, 255, 20, 0.25);
    font-size: 1.6em;
}

[data-testid="stMetricDelta"] {
    font-family: var(--gt-font-body);
    font-weight: 700;
    text-transform: uppercase;
    text-shadow: 0 0 6px currentColor;
}
[data-testid="stMetricDelta"] svg {
    filter: drop-shadow(0 0 3px currentColor);
}

/* ---------- 6. MISC POLISH ---------- */
::selection {
    background-color: var(--gt-green);
    color: #05170a;
}

::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}
::-webkit-scrollbar-track {
    background: var(--gt-bg-void);
}
::-webkit-scrollbar-thumb {
    background-color: var(--gt-bg-panel);
    border: 2px solid var(--gt-border-dark);
}
::-webkit-scrollbar-thumb:hover {
    background-color: var(--gt-green);
}
</style>
"""

def create_audio_briefing(text: str) -> io.BytesIO:
    """Converts mission briefing text into an in-memory MP3 audio stream."""
    tts = gTTS(text=text, lang='en', slow=False)
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

def generate_pdf_guide(topic: str, game: str, narrative: str, dictionary: list) -> io.BytesIO:
    """Generates an on-demand, game-themed PDF guide."""
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, f"MISSION BRIEFING: {topic.upper()}", ln=True, align='C')
    pdf.set_font("Helvetica", 'I', 12)
    pdf.cell(0, 8, f"Game Tactical System: {game}", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 8, "Tactical Overview:", ln=True)
    pdf.set_font("Helvetica", size=10)
    clean_narrative = narrative.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 6, clean_narrative)
    pdf.ln(8)
    
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 8, "Concept Mapping Dictionary:", ln=True)
    pdf.set_font("Helvetica", size=10)
    
    for idx, item in enumerate(dictionary, start=1):
        term = str(item.get("engineering_term", "")).encode('latin-1', 'replace').decode('latin-1')
        equiv = str(item.get("game_mechanic_equivalent", "")).encode('latin-1', 'replace').decode('latin-1')
        func = str(item.get("in_game_function", "")).encode('latin-1', 'replace').decode('latin-1')
        score = str(item.get("complexity_score", "")).encode('latin-1', 'replace').decode('latin-1')
        
        pdf.set_font("Helvetica", 'B', 10)
        pdf.cell(0, 6, f"{idx}. {term} ---> {equiv} [Complexity: {score}]", ln=True)
        pdf.set_font("Helvetica", size=9)
        pdf.multi_cell(0, 5, f"   Mechanic Role: {func}")
        pdf.ln(3)

    pdf_out = io.BytesIO()
    pdf_bytes = pdf.output(dest='S')
    if isinstance(pdf_bytes, str):
        pdf_out.write(pdf_bytes.encode('latin-1'))
    else:
        pdf_out.write(pdf_bytes)
        
    pdf_out.seek(0)
    return pdf_out

import urllib.parse

def generate_boss_image_url(topic: str, game: str) -> str:
    """
    Generates a free, no-API-key image URL using Pollinations.ai.
    """
    # 1. Engineer the perfect boss prompt
    prompt = f"Concept art of a boss monster representing the engineering concept of '{topic}'. Designed strictly in the visual art style of the video game '{game}'. Epic lighting, UI portrait, highly detailed, dark background."
    
    # 2. URL-encode the prompt so it's safe for a web link
    safe_prompt = urllib.parse.quote(prompt)
    
    # 3. Add a seed or width/height parameters if we want, but the default is perfect
    image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=800&height=400&nologo=true"
    
    return image_url
