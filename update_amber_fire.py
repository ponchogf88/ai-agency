import json
import re
from pathlib import Path

loona_dir = Path("/Users/user/loona-AI")
vault_file = Path("/Users/user/Desktop/Projects/Obsidian-Vault/03_Loona_AI/03_Official_Soundtrack_and_Karaoke_LRC.md")
notion_file = Path("/Users/user/Desktop/Projects/Obsidian-Vault/05_Notion_Sync_Exports/NOTION_03_Official_Soundtrack_and_Karaoke_LRC.md")

tracks = [
    {"id": 1, "title": "Luna", "artist": "David Olivares", "bpm": 98, "genre": "Tex-Mex / Cumbia"},
    {"id": 2, "title": "Soñador", "artist": "David Olivares", "bpm": 104, "genre": "Tex-Mex"},
    {"id": 3, "title": "Desvelado", "artist": "Bobby Pulido", "bpm": 92, "genre": "Tejano Classic"},
    {"id": 4, "title": "Yo Quiero Ser Tu Luna", "artist": "Mia Roze", "bpm": 100, "genre": "Cumbia Pop"},
    {"id": 5, "title": "Me Gusta Tu Ritmo", "artist": "Benetti House Bar", "bpm": 124, "genre": "House / Groove"},
    {"id": 6, "title": "Let Music Play (Radio Edit)", "artist": "Alex Molinary", "bpm": 126, "genre": "Dance / Electronic"},
    {"id": 7, "title": "Hold Me Close Tonight", "artist": "Amali", "bpm": 122, "genre": "Deep House / Melodic"},
    {"id": 8, "title": "Pamoja (Afro Soul)", "artist": "Alex Molinary", "bpm": 120, "genre": "Afro House / Afro Soul"},
    {"id": 9, "title": "It's a Feeling", "artist": "Suspicious Unicorn", "bpm": 118, "genre": "Nu-Disco / Funky"},
    {"id": 10, "title": "A Lifetime (You Better)", "artist": "Luana Isabelly de Oliveira Sousa", "bpm": 116, "genre": "Pop / Melodic Soul"},
    {"id": 11, "title": "Let Go or Stay (Deep House Flows)", "artist": "Avant Toi", "bpm": 122, "genre": "Melodic Deep House"},
    {"id": 12, "title": "Amber Fire (Deep Violin Vibes)", "artist": "Amber Fire", "bpm": 124, "genre": "Deep House / Acoustic Violin Vibes"}
]

# 1. Update soundtrack.js
(loona_dir / "soundtrack.js").write_text(f"export const LOONA_SOUNDTRACK = {json.dumps(tracks, ensure_ascii=False, indent=2)};\n", encoding="utf-8")

# 2. Update index.html
html_path = loona_dir / "index.html"
if html_path.exists():
    text = html_path.read_text(encoding="utf-8")
    text = re.sub(r"const playlist = \[.*?\];", f"const playlist = {json.dumps(tracks, ensure_ascii=False)};", text, flags=re.DOTALL)
    html_path.write_text(text, encoding="utf-8")

# 3. Update Obsidian & Notion
obsidian_md = """# 🎵 Loona AI — Soundtrack Oficial & Letras Sincronizadas

> **Actualizado:** 2026-08-23  
> **Total de Tracks:** 12 Canciones Oficiales  
> **Repo Dedicado:** `https://github.com/ponchogf88/loona-AI`  
> **Ubicación Local:** `/Users/user/loona-AI`  

---

## 🎧 Lista Oficial de 12 Canciones

| # | Canción | Artista | BPM | Género / Vibra | Modo de Baile |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Luna** | David Olivares | 98 | Tex-Mex / Cumbia | Romántico / Clásico |
| **2** | **Soñador** | David Olivares | 104 | Tex-Mex | Alegre / Cumbia |
| **3** | **Desvelado** | Bobby Pulido | 92 | Tejano Classic | Desvelado / Sentimiento |
| **4** | **Yo Quiero Ser Tu Luna** | Mia Roze | 100 | Cumbia Pop | Cumbia / Himno Loona |
| **5** | **Me Gusta Tu Ritmo** | Benetti House Bar | 124 | House / Groove | Fiestón / Movimiento Rápido |
| **6** | **Let Music Play (Radio Edit)** | Alex Molinary | 126 | Dance / Electronic | Electro Club |
| **7** | **Hold Me Close Tonight** | Amali | 122 | Deep House / Melodic | Chill / Noche |
| **8** | **Pamoja (Afro Soul)** | Alex Molinary | 120 | Afro House / Afro Soul | Percusión Tribal |
| **9** | **It's a Feeling** | Suspicious Unicorn | 118 | Nu-Disco / Funky | Disco Funk / Buena Vibra |
| **10** | **A Lifetime (You Better)** | Luana Isabelly de Oliveira Sousa | 116 | Pop / Melodic Soul | Soul Melódico |
| **11** | **Let Go or Stay (Deep House Flows)** | Avant Toi | 122 | Melodic Deep House | Progressive Flow |
| **12** | **Amber Fire (Deep Violin Vibes)** | Amber Fire | 124 | Deep House / Acoustic Violin | Violín Acústico & Fuego 🎻🔥 |

---

## 🎤 Módulo Karaoke & Sincronización en Tiempo Real
Sincronización por timestamps con glow neón y auto-scroll vertical en la interfaz de Canvas.
"""

vault_file.write_text(obsidian_md, encoding="utf-8")
notion_file.write_text(obsidian_md, encoding="utf-8")

print("Successfully updated Amber Fire (Deep Violin Vibes) in loona-AI, Obsidian, and Notion!")
