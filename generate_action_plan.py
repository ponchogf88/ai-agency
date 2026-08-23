import subprocess
from pathlib import Path

vault_dir = Path("/Users/user/Desktop/Projects/Obsidian-Vault")
notion_dir = vault_dir / "05_Notion_Sync_Exports"
agencia_dir = Path("/Users/user/agencia-core")

vault_dir.mkdir(parents=True, exist_ok=True)
notion_dir.mkdir(parents=True, exist_ok=True)

plan_content = """# 🎯 PLAN DE ACCIÓN EJECUTIVO — ECOSISTEMA AGENTIC ENGINE 2026

> **Fecha:** 2026-08-23  
> **Autor:** Jesús Alfonso Gutiérrez Flores (@ponchogf88)  
> **Objetivo Principal:** Generación de flujo de caja inmediato (Cashflow) y consolidación de productos activos.  
> **Estado:** Listo para Ejecución Inmediata  

---

## ⚡ RESUMEN ESTRATÉGICO POR FRENTES

| Frente | Proyecto | Enfoque | Meta Inmediata |
| :--- | :--- | :--- | :--- |
| **Frente 1 (Prioridad 1)** | 🏢 **AI AGENCY MTY** | Prospección y venta de landings express 48h con Marketing OS | **Cerrar $15,000 – $34,000 MXN esta semana** (3-5 clientes) |
| **Frente 2 (Prioridad 2)** | 📓 **Gemini Notebooks** | Auditoría y extracción de prompts/pipelines web | Conectar lógica de notebooks con OrbAgent y Agencia |
| **Frente 3 (Prioridad 3)** | 📱 **OrbAgent** | App móvil CRM WhatsApp (Expo 54 + Supabase) | Validar chats en vivo y generar preview build Android |
| **Frente 4 (Prioridad 4)** | 🤖 **Loona AI** | Robot compañero con Canvas 60 FPS + Jukebox | Conectar WebSocket de Gemini Live API (Audio/Video) |

---

## 🚀 FASE 1: GENERACIÓN DE INGRESOS INMEDIATOS (AI AGENCY MTY)

```
[ 10-15 Leads de Monterrey ] ➔ [ Marketing OS (14 Agentes) ] ➔ [ 04_ready_to_pitch ] ➔ [ Cierre por WhatsApp ]
```

### 📋 Checklist de Ejecución Comercial:
- [ ] **Lote de Leads Inicial (15 Negocios de MTY):**
  * *Nicho A:* Talleres Mecánicos y Rectificadoras (San Nicolás, Apodaca, Guadalupe).
  * *Nicho B:* Clínicas Dentales y Estéticas (San Pedro Garza García, Cumbres, Valle Oriente).
  * *Nicho C:* Despachos Jurídicos y Contables (Centro de Monterrey, San Jerónimo).
- [ ] **Ejecución del Funnel:**
  * Depositar los archivos `.json` en `agencia-core/01_leads_raw/`.
  * `orchestrator.py` ejecuta automáticamente los 14 agentes, generando:
    * Auditoría con calificación CRO (0 a 100).
    * Landing page interactiva lista en 48 horas.
    * Archivo estructurado `llms.txt`.
    * Mensaje de prospección anti-slop filtrado por el Agente Editor.
- [ ] **Estructura de Precios a Ofrecer:**
  * **Presencia Express:** `$2,900 MXN` (Landing ultrarrápida + botón directo a WhatsApp).
  * **Pipeline Comercial Completo:** `$6,800 MXN` (Landing + Automatización de prospectos + Tarjeta digital).
  * **Retainer Mensual:** `$3,500 MXN/mes` (Mantenimiento y A/B Testing).

---

## 📓 FASE 2: AUDITORÍA DE CUADERNOS GEMINI (NOTEBOOKS)

### 📋 Checklist de Integración Web:
- [ ] Acceder mediante browser automation a los cuadernos de Gemini (Google AI Studio / Colab / NotebookLM).
- [ ] Extraer prompts de alto rendimiento, cadenas de razonamiento y pipelines de datos.
- [ ] Incorporar los mejores frameworks de prompts a `marketing_os.py` y al backend de `OrbAgent`.

---

## 📱 FASE 3: ESCALADO DE PRODUCTO (ORBAGENT)

### 📋 Checklist Técnico y de Distribución:
- [ ] Validar el flujo de mensajes y medios firmados en Supabase (`hooks/useSignedMediaUrl.ts`).
- [ ] Probar la navegación por pestañas (`app/(tabs)/`) en Expo dev server (`npm start`).
- [ ] Generar la build de vista previa para Android: `npm run build:android:preview`.
- [ ] Activar la ficha optimizada de App Store / Google Play con el **ASO Specialist**.
- [ ] Preparar el lanzamiento en Product Hunt según el cronograma del **Launch Manager**.

---

## 🤖 FASE 4: EXPERIENCIA Y EMBODIED AI (LOONA AI)

### 📋 Checklist de Inteligencia & Hardware:
- [ ] Integrar el cliente bidireccional WebSocket con `google-genai` para la **Gemini Multimodal Live API**.
- [ ] Sincronizar el streaming de video de la cámara (1-2 FPS) con el análisis de visión en tiempo real.
- [ ] Calibrar el rebote de ojos en Canvas y giros de ruedas con los 10 tracks del Soundtrack oficial (Tex-Mex & House).
- [ ] Habilitar el **Modo Karaoke** con letras sincronizadas en tiempo real (`lyrics.js`).

---

## 🛡️ PROTOCOLO DE TRABAJO (REGLAS MAESTRAS)
1. **Cero pasos intermedios para el humano:** Ejecución autónoma de extremo a extremo.
2. **Calidad antes que prisa:** Cero código roto, pruebas automatizadas en cada cambio.
3. **Verifica antes de avisar:** Auditar archivos resultantes antes de dar por terminada una tarea.
4. **Al chile (Cero complacencias):** Soluciones directas, funcionales y sin texto de relleno.
"""

# Guardar en Obsidian Vault
(vault_dir / "00_PLAN_DE_ACCION_EJECUTIVO.md").write_text(plan_content, encoding="utf-8")
print("✅ Guardado en Obsidian Vault:", vault_dir / "00_PLAN_DE_ACCION_EJECUTIVO.md")

# Guardar en Notion Exports
(notion_dir / "NOTION_00_PLAN_DE_ACCION_EJECUTIVO.md").write_text(plan_content, encoding="utf-8")
print("✅ Guardado en Notion Exports:", notion_dir / "NOTION_00_PLAN_DE_ACCION_EJECUTIVO.md")

# Guardar en agencia-core
(agencia_dir / "PLAN_DE_ACCION_EJECUTIVO.md").write_text(plan_content, encoding="utf-8")
print("✅ Guardado en agencia-core:", agencia_dir / "PLAN_DE_ACCION_EJECUTIVO.md")

