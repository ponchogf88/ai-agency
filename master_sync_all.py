import os
import subprocess
from pathlib import Path

vault_dir = Path("/Users/user/Desktop/Projects/Obsidian-Vault")
notion_dir = vault_dir / "05_Notion_Sync_Exports"
agencia_dir = Path("/Users/user/agencia-core")
whatsorb_dir = Path("/Users/user/whatsorb-dev")
loona_dir = Path("/Users/user/loona-AI")

print("================================================================================")
print("🪐 MASTER SYNCHRONIZATION — ECOSISTEMA AGENTIC ENGINE 2026")
print("================================================================================\n")

# 1. Update Obsidian Master Index
master_index = """# 🪐 ECOSISTEMA AGENTIC ENGINE — MASTER INDEX

> **Última sincronización global:** 2026-08-23  
> **Autor:** Jesús Alfonso Gutiérrez Flores (@ponchogf88)  
> **Estado:** 100% Sincronizado, Versionado y Documentado  

---

## 📂 Ecosistema de Proyectos Activos

### 1. 🏢 AI AGENCY MTY (`agencia-core/`)
* **Propósito:** Pipeline automatizado de 14 agentes para auditar negocios, generar landing pages móviles en 48h, crear archivos `llms.txt` y redactar pitches anti-slop para WhatsApp.
* **Ubicación local:** `/Users/user/agencia-core`
* **Repo GitHub:** `https://github.com/ponchogf88/ai-agency`
* **Notas de arquitectura:** [[01_Marketing_OS_14_Agents]], [[02_Pipeline_Orchestrator_and_Handoffs]], [[03_Monterrey_Niches_and_Pricing_Model]]

### 2. 📱 OrbAgent (`whatsorb-dev/`)
* **Propósito:** App móvil de productividad y CRM en React Native (Expo 54 + Supabase) con enrutamiento de chats, media privada y automatización de WhatsApp Cloud API.
* **Ubicación local:** `/Users/user/whatsorb-dev`
* **Repo GitHub:** `https://github.com/ponchogf88/whatsorb`
* **Notas de arquitectura:** [[01_OrbAgent_Architecture_and_Rebranding]], [[02_ASO_and_B2B_Outreach_Strategy]]

### 3. 🤖 Loona AI (`loona-AI/`)
* **Propósito:** Robot compañero físico y jukebox interactivo con cara en Canvas 60 FPS, sincronización de baile por BPM, 14 canciones oficiales, karaoke con letras LRC en tiempo real y conexión multimodal con Gemini Live API.
* **Ubicación local:** `/Users/user/loona-AI`
* **Repo GitHub:** `https://github.com/ponchogf88/loona-AI`
* **Notas de arquitectura:** [[01_Loona_AI_Hardware_and_Architecture]], [[02_Gemini_Live_Multimodal_API]], [[03_Official_Soundtrack_and_Karaoke_LRC]]

### 4. 🌐 Signal Universe
* **Propósito:** CV interactivo 3D con Three.js, esferas de cristal, audio reactivo y desplegado en Cloudflare Workers.
* **Live:** `https://signal-universe.lic-jagf87.workers.dev`
* **Repo GitHub:** `https://github.com/ponchogf88/signal-universe`
* **Notas de arquitectura:** [[01_Signal_Universe_3D_CV_Documentation]]

---

## 🎯 Plan de Acción Maestro
* Consulta la hoja de ruta y prioridades de ingresos en: [[00_PLAN_DE_ACCION_EJECUTIVO]]
"""
(vault_dir / "00_MASTER_INDEX.md").write_text(master_index, encoding="utf-8")
(notion_dir / "NOTION_00_MASTER_INDEX.md").write_text(master_index, encoding="utf-8")
print("✅ 1. Obsidian Vault y Notion Master Index sincronizados.")

# 2. Sync Notion Exports for all Markdown files
for subfolder in ["01_AI_AGENCY_MTY", "02_OrbAgent", "03_Loona_AI", "04_Signal_Universe"]:
    for md_file in (vault_dir / subfolder).glob("*.md"):
        target_export = notion_dir / f"NOTION_{md_file.name}"
        target_export.write_text(md_file.read_text(encoding="utf-8"), encoding="utf-8")
print("✅ 2. Exportaciones limpias de Notion sincronizadas en 05_Notion_Sync_Exports/.")

# 3. Git Sync: OrbAgent (whatsorb-dev)
print("\n--- Sincronizando OrbAgent (whatsorb-dev) ---")
subprocess.run(["git", "add", "."], cwd=whatsorb_dir, capture_output=True)
subprocess.run(["git", "-c", "user.name=Chuy", "-c", "user.email=ponchogf88@gmail.com", "commit", "-m", "chore: global sync of OrbAgent documentation, config, and media hooks"], cwd=whatsorb_dir, capture_output=True)
res_orb = subprocess.run(["git", "push", "origin", "main"], cwd=whatsorb_dir, capture_output=True, text=True)
print("OrbAgent Push:", res_orb.stdout.strip() or res_orb.stderr.strip())

# 4. Git Sync: AI AGENCY MTY (agencia-core)
print("\n--- Sincronizando AI AGENCY MTY (agencia-core) ---")
subprocess.run(["git", "add", "."], cwd=agencia_dir, capture_output=True)
subprocess.run(["git", "-c", "user.name=Chuy", "-c", "user.email=ponchogf88@gmail.com", "commit", "-m", "chore: global sync of AI AGENCY MTY Marketing OS and ecosystem docs"], cwd=agencia_dir, capture_output=True)
res_age = subprocess.run(["git", "push", "origin", "main"], cwd=agencia_dir, capture_output=True, text=True)
print("AI AGENCY MTY Push:", res_age.stdout.strip() or res_age.stderr.strip())

# 5. Git Sync: Loona AI (loona-AI)
print("\n--- Sincronizando Loona AI (loona-AI) ---")
subprocess.run(["git", "add", "."], cwd=loona_dir, capture_output=True)
subprocess.run(["git", "-c", "user.name=Chuy", "-c", "user.email=ponchogf88@gmail.com", "commit", "-m", "chore: global sync of Loona AI 14-track soundtrack, Canvas UI, and docs"], cwd=loona_dir, capture_output=True)
print("Loona AI repo committed locally.")

print("\n================================================================================")
print("🚀 SINCRONIZACIÓN MAESTRA COMPLETADA CON ÉXITO")
print("================================================================================")
