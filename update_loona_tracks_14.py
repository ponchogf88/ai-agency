import json
import re
import subprocess
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
    {"id": 12, "title": "Amber Fire (Deep Violin Vibes)", "artist": "Amber Fire", "bpm": 124, "genre": "Deep House / Acoustic Violin"},
    {"id": 13, "title": "Cuba Libre (Dolce Vita)", "artist": "Dolce Vita", "bpm": 124, "genre": "Latin House / Italo Disco Vibez 🍹🌴"},
    {"id": 14, "title": "Cokainé", "artist": "Kodi", "bpm": 126, "genre": "Tech House / Minimal Club Groove ⚡️"}
]

# 1. Update soundtrack.js
(loona_dir / "soundtrack.js").write_text(f"export const LOONA_SOUNDTRACK = {json.dumps(tracks, ensure_ascii=False, indent=2)};\n", encoding="utf-8")

# 2. Update index.html
html_path = loona_dir / "index.html"
if html_path.exists():
    text = html_path.read_text(encoding="utf-8")
    text = re.sub(r"const playlist = \[.*?\];", f"const playlist = {json.dumps(tracks, ensure_ascii=False)};", text, flags=re.DOTALL)
    html_path.write_text(text, encoding="utf-8")

# 3. Update README.md
(loona_dir / "README.md").write_text("""# 🤖 Loona AI — Companion Robot & Jukebox

> **Autor:** Jesús Alfonso Gutiérrez Flores (@ponchogf88)  
> **Repo Oficial:** `https://github.com/ponchogf88/loona-AI`  
> **Ecosistema:** Embodied AI, Canvas 60 FPS, Gemini Multimodal Live API  

---

## 🎧 Álbum Oficial de Loona AI (14 Canciones)

1. **Luna** — David Olivares (98 BPM, Tex-Mex)
2. **Soñador** — David Olivares (104 BPM, Tex-Mex)
3. **Desvelado** — Bobby Pulido (92 BPM, Tejano Classic)
4. **Yo Quiero Ser Tu Luna** — Mia Roze (100 BPM, Cumbia Pop)
5. **Me Gusta Tu Ritmo** — Benetti House Bar (124 BPM, House / Groove)
6. **Let Music Play (Radio Edit)** — Alex Molinary (126 BPM, Dance / Electronic)
7. **Hold Me Close Tonight** — Amali (122 BPM, Deep House)
8. **Pamoja (Afro Soul)** — Alex Molinary (120 BPM, Afro House)
9. **It's a Feeling** — Suspicious Unicorn (118 BPM, Nu-Disco)
10. **A Lifetime (You Better)** — Luana Isabelly de Oliveira Sousa (116 BPM, Soul Pop)
11. **Let Go or Stay (Deep House Flows)** — Avant Toi (122 BPM, Melodic House)
12. **Amber Fire (Deep Violin Vibes)** — Amber Fire (124 BPM, Violin Deep House)
13. **Cuba Libre (Dolce Vita)** — Dolce Vita (124 BPM, Latin House / Italo Disco)
14. **Cokainé** — Kodi (126 BPM, Tech House Club)

---

## 🚀 Inicio Rápido
```bash
open index.html
```
""", encoding="utf-8")

# 4. Update Obsidian & Notion
obsidian_md = """# 🎵 Loona AI — Soundtrack Oficial & Letras Sincronizadas

> **Actualizado:** 2026-08-23  
> **Total de Tracks:** 14 Canciones Oficiales  
> **Repo Dedicado:** `https://github.com/ponchogf88/loona-AI`  
> **Ubicación Local:** `/Users/user/loona-AI`  

---

## 🎧 Lista Oficial de 14 Canciones

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
| **12** | **Amber Fire (Deep Violin Vibes)** | Amber Fire | 124 | Deep House & Violín | Violín Acústico & Fuego 🎻🔥 |
| **13** | **Cuba Libre (Dolce Vita)** | Dolce Vita | 124 | Latin House / Italo Disco | Fiesta Tropical / Playa 🍹🌴 |
| **14** | **Cokainé** | Kodi | 126 | Tech House / Club Groove | Modo Fiesta Nocturna ⚡️ |

---

## 🎤 Módulo Karaoke & Sincronización en Tiempo Real
Sincronización por timestamps con glow neón y auto-scroll vertical en la interfaz de Canvas.
"""

vault_file.write_text(obsidian_md, encoding="utf-8")
notion_file.write_text(obsidian_md, encoding="utf-8")

# 5. Git commit in /Users/user/loona-AI
subprocess.run(["git", "add", "."], cwd=loona_dir, capture_output=True)
subprocess.run(["git", "-c", "user.name=Chuy", "-c", "user.email=ponchogf88@gmail.com", "commit", "-m", "feat(soundtrack): add Track 13 'Cuba Libre (Dolce Vita)' and Track 14 'Cokainé' by Kodi"], cwd=loona_dir, capture_output=True)

print("Successfully added Tracks 13 & 14 to Loona AI, Obsidian, and Notion!")
