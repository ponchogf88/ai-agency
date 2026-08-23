from pathlib import Path

vault_track_file = Path("/Users/user/Desktop/Projects/Obsidian-Vault/03_Loona_AI/03_Official_Soundtrack_and_Karaoke_LRC.md")
notion_track_file = Path("/Users/user/Desktop/Projects/Obsidian-Vault/05_Notion_Sync_Exports/NOTION_03_Official_Soundtrack_and_Karaoke_LRC.md")

content = """# 🎵 Loona AI — Soundtrack Oficial & Letras Sincronizadas

> **Actualizado:** 2026-08-23  
> **Total de Tracks:** 11 Canciones Oficiales  
> **Modos:** Baile por BPM, Jukebox Interactivo y Karaoke con Timestamps  

---

## 🎧 Lista Oficial de 11 Canciones

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
| **11** | **Let Go or Stay (Deep House Flows)** | Avant Toi | 122 | Melodic Deep House | Progressive Flow / Trance |

---

## 🎤 Módulo Karaoke en Vivo
Las letras se renderizan en el canvas inferior con sincronización milimétrica basada en `audio.currentTime` con efecto de glow azul neón (`#00f2fe`) y auto-scroll vertical.
"""

vault_track_file.write_text(content, encoding="utf-8")
notion_track_file.write_text(content, encoding="utf-8")
print("Soundtrack updated in Obsidian and Notion with Track #11!")
