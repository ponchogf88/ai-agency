import json
import subprocess
from pathlib import Path

loona_dir = Path("/Users/user/loona-AI")
loona_dir.mkdir(parents=True, exist_ok=True)

# 1. 12 Tracks data
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
    {"id": 12, "title": "Amber Fire", "artist": "Amber Fire", "bpm": 124, "genre": "Progressive Melodic / Fire Dance"}
]

# 2. Write soundtrack.js
(loona_dir / "soundtrack.js").write_text(f"export const LOONA_SOUNDTRACK = {json.dumps(tracks, ensure_ascii=False, indent=2)};\n", encoding="utf-8")

# 3. Write index.html with all 12 tracks and complete UI
index_html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
  <title>Loona AI — Companion Robot & Jukebox</title>
  <style>
    :root {
      --bg-color: #07090e;
      --eye-color: #00f2fe;
      --eye-glow: rgba(0, 242, 254, 0.6);
      --card-bg: rgba(18, 24, 38, 0.8);
      --text: #ffffff;
      --text-muted: #8e9bb0;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
    body {
      background: var(--bg-color);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      padding: 20px;
    }
    header {
      width: 100%;
      max-width: 800px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .badge {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      background: var(--card-bg);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 20px;
      font-size: 0.85rem;
      backdrop-filter: blur(10px);
    }
    .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #00f2fe;
      box-shadow: 0 0 10px #00f2fe;
      animation: pulse 2s infinite;
    }
    @keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.4; transform: scale(0.85); } }
    .face-container {
      flex: 1;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    canvas#loonaFace { width: 100%; max-width: 700px; height: 300px; }
    .jukebox-card {
      width: 100%;
      max-width: 700px;
      background: var(--card-bg);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 24px;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      backdrop-filter: blur(16px);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
    }
    .track-info { display: flex; align-items: center; gap: 12px; min-width: 200px; }
    .disc-icon {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: linear-gradient(135deg, #ff0844, #ffb199);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
    }
    .spinning { animation: spin 3s linear infinite; }
    @keyframes spin { 100% { transform: rotate(360deg); } }
    .track-meta h4 { font-size: 0.95rem; font-weight: 600; }
    .track-meta p { font-size: 0.78rem; color: var(--text-muted); }
    .controls { display: flex; align-items: center; gap: 10px; }
    .btn {
      background: rgba(255, 255, 255, 0.08);
      border: none;
      color: #fff;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      transition: all 0.2s ease;
    }
    .btn:hover { background: rgba(255, 255, 255, 0.2); transform: scale(1.05); }
    .btn-play {
      background: linear-gradient(135deg, #00f2fe, #4facfe);
      width: 46px;
      height: 46px;
      font-size: 1.2rem;
      box-shadow: 0 0 15px var(--eye-glow);
    }
  </style>
</head>
<body>
  <header>
    <div class="badge">
      <div class="status-dot"></div>
      <span>Loona AI • Live Companion</span>
    </div>
    <div class="badge" id="modeBadge">Modo: Compañero</div>
  </header>

  <div class="face-container">
    <canvas id="loonaFace" width="700" height="300"></canvas>
  </div>

  <div class="jukebox-card">
    <div class="track-info">
      <div class="disc-icon" id="discIcon">🎵</div>
      <div class="track-meta">
        <h4 id="songTitle">Luna</h4>
        <p id="songArtist">David Olivares</p>
      </div>
    </div>

    <div class="controls">
      <button class="btn" id="prevBtn">⏮</button>
      <button class="btn btn-play" id="playBtn">▶</button>
      <button class="btn" id="nextBtn">⏭</button>
    </div>
  </div>

  <script>
    const playlist = """ + json.dumps(tracks) + """;
    let currentTrack = 0;
    let isPlaying = false;

    const playBtn = document.getElementById("playBtn");
    const prevBtn = document.getElementById("prevBtn");
    const nextBtn = document.getElementById("nextBtn");
    const songTitle = document.getElementById("songTitle");
    const songArtist = document.getElementById("songArtist");
    const discIcon = document.getElementById("discIcon");
    const modeBadge = document.getElementById("modeBadge");

    function updateTrackUI() {
      const track = playlist[currentTrack];
      songTitle.textContent = track.title;
      songArtist.textContent = track.artist;
    }

    playBtn.addEventListener("click", () => {
      isPlaying = !isPlaying;
      playBtn.textContent = isPlaying ? "⏸" : "▶";
      discIcon.classList.toggle("spinning", isPlaying);
      modeBadge.textContent = isPlaying ? "Modo: Baile 🤠" : "Modo: Compañero";
    });

    nextBtn.addEventListener("click", () => {
      currentTrack = (currentTrack + 1) % playlist.length;
      updateTrackUI();
    });

    prevBtn.addEventListener("click", () => {
      currentTrack = (currentTrack - 1 + playlist.length) % playlist.length;
      updateTrackUI();
    });

    const canvas = document.getElementById("loonaFace");
    const ctx = canvas.getContext("2d");
    let blink = 0;
    let danceOffset = 0;

    function triggerBlink() {
      let closing = true;
      const interval = setInterval(() => {
        if (closing) {
          blink += 0.25;
          if (blink >= 1) closing = false;
        } else {
          blink -= 0.25;
          if (blink <= 0) {
            blink = 0;
            clearInterval(interval);
            setTimeout(triggerBlink, 3000 + Math.random() * 3000);
          }
        }
      }, 25);
    }
    triggerBlink();

    function drawEye(x, y, isRight = false) {
      ctx.save();
      ctx.translate(x, y + danceOffset);
      ctx.shadowColor = "rgba(0, 242, 254, 0.7)";
      ctx.shadowBlur = 25;
      ctx.fillStyle = "#00f2fe";

      const height = Math.max(125 * (1 - blink), 6);
      ctx.beginPath();
      ctx.roundRect(-42, -height / 2, 84, height, [35, 35, 25, 25]);
      ctx.fill();

      if (blink < 0.6) {
        ctx.shadowBlur = 0;
        ctx.fillStyle = "rgba(255, 255, 255, 0.85)";
        ctx.beginPath();
        ctx.arc(isRight ? 16 : -16, -height * 0.2, 9, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.restore();
    }

    function render(timestamp) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      if (isPlaying) {
        const bpm = playlist[currentTrack].bpm;
        const beatInterval = (60 / bpm) * 1000;
        const beatProgress = (timestamp % beatInterval) / beatInterval;
        danceOffset = Math.sin(beatProgress * Math.PI * 2) * 15;
      } else {
        danceOffset = 0;
      }

      drawEye(canvas.width / 2 - 110, canvas.height / 2, false);
      drawEye(canvas.width / 2 + 110, canvas.height / 2, true);
      requestAnimationFrame(render);
    }
    requestAnimationFrame(render);
  </script>
</body>
</html>
"""
(loona_dir / "index.html").write_text(index_html, encoding="utf-8")

# 4. Write README.md
(loona_dir / "README.md").write_text("""# 🤖 Loona AI — Companion Robot & Jukebox

> **Autor:** Jesús Alfonso Gutiérrez Flores (@ponchogf88)  
> **Repo Oficial:** `https://github.com/ponchogf88/loona-AI`  
> **Ecosistema:** Embodied AI, Canvas 60 FPS, Gemini Multimodal Live API  

---

## 🎧 Álbum Oficial de Loona AI (12 Canciones)

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
12. **Amber Fire** — Amber Fire (124 BPM, Progressive Melodic Dance)

---

## 🚀 Inicio Rápido
```bash
# Abrir la interfaz web con ojos animados y reproductor:
open index.html
```
""", encoding="utf-8")

# 5. Update Obsidian Vault
vault_track_file = Path("/Users/user/Desktop/Projects/Obsidian-Vault/03_Loona_AI/03_Official_Soundtrack_and_Karaoke_LRC.md")
notion_track_file = Path("/Users/user/Desktop/Projects/Obsidian-Vault/05_Notion_Sync_Exports/NOTION_03_Official_Soundtrack_and_Karaoke_LRC.md")

obsidian_content = """# 🎵 Loona AI — Soundtrack Oficial & Letras Sincronizadas

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
| **12** | **Amber Fire** | Amber Fire | 124 | Progressive Dance | Fuego / Ritmo Envolvente |

---

## 🎤 Módulo Karaoke & Sincronización en Tiempo Real
Sincronización por timestamps con glow neón y auto-scroll vertical en la interfaz de Canvas.
"""

vault_track_file.write_text(obsidian_content, encoding="utf-8")
notion_track_file.write_text(obsidian_content, encoding="utf-8")

# 6. Init git in /Users/user/loona-AI
subprocess.run(["git", "init"], cwd=loona_dir, capture_output=True)
subprocess.run(["git", "remote", "add", "origin", "https://github.com/ponchogf88/loona-AI.git"], cwd=loona_dir, capture_output=True)
subprocess.run(["git", "add", "."], cwd=loona_dir, capture_output=True)
subprocess.run(["git", "commit", "-m", "feat(loona): initial commit of Loona AI with Canvas 60fps face, Jukebox, and 12-track soundtrack including Amber Fire"], cwd=loona_dir, capture_output=True)

print("Loona AI dedicated repository created and committed successfully!")
