#!/usr/bin/env python3
"""
Sincronizador de Conocimiento y Avances para Obsidian Vault
AI AGENCY MTY & GUTIERREZ CONSULTING
"""

import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OBSIDIAN_VAULT = Path("/Users/user/Desktop/Projects/Obsidian-Vault")
TARGET_DIR = OBSIDIAN_VAULT / "AI-AGENCY-MTY"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

# 1. 00_CENTRAL_DASHBOARD.md
dashboard = """---
title: "AI AGENCY MTY — Sistema Central de Operaciones & Monetización"
tags:
  - agencia
  - inteligencia-artificial
  - monetizacion
  - automatizacion
  - n8n
  - whatsapp
date: 2026-08-22
author: "Jesús Alfonso Gutiérrez Flores"
github_repo: "https://github.com/ponchogf88/ai-agency"
status: "Activo / Producción"
---

# ⚡ AI AGENCY MTY & GUTIERREZ CONSULTING — HUB CENTRAL

> **Misión:** Infraestructura de automatización multi-agente, rescate de canales de WhatsApp lentos y comercialización de productos digitales B2B de alto margen.

---

## 🗺️ Mapa de Navegación del Sistema (MOC)

- [[01_BANCO_DE_IDEAS_MASTER]]: Catálogo central de oportunidades, unit economics y márgenes (>90%).
- [[02_CATALOGO_PRODUCTOS_DIGITALES]]: 4 Blueprints empaquetados para venta directa en Gumroad ($29 - $79 USD).
- [[03_BLUEPRINTS_AUTOMATIZACION]]: Flujos n8n y Make.com (WhatsApp Smart Router, CRO Engine, Payment Webhook).
- [[04_PROSPECCION_B2B_MTY]]: Estrategia y bases de datos para Clínicas, Despachos y Talleres de Monterrey.
- [[05_MARKETPLACES_UPWORK_FIVERR]]: Fichas de servicio y propuestas ganadoras de alta conversión.
- [[06_CONTRATOS_Y_LEGAL_IA]]: Contrato marco de prestación de servicios y SLA bajo leyes mexicanas.
- [[07_CRONOGRAMA_Y_ESTRATEGIA_HORARIOS]]: Análisis de picos de respuesta (10:30 AM) y disparos humanizados.

---

## 📊 Números de Contacto Configurados
- **WhatsApp Business (Agencia):** `+52 81 4005 0088`
- **WhatsApp Personal (Directo):** `+52 81 3051 6527`
- **GitHub Repository:** [ponchogf88/ai-agency](https://github.com/ponchogf88/ai-agency)

---

## 🚀 Estado de los 3 Enjambres Operativos
1. **Enjambre A (Prospección Directa):** 3 Dashboards interactivos HTML generados, bases CSV y copys listos.
2. **Enjambre B (Productos Digitales Gumroad):** 4 paquetes `.zip` listos en `dist/` con sales copy y manifiesto JSON.
3. **Enjambre C (Marketplaces & Legal):** Fichas Upwork/Fiverr publicables y contrato de adhesión listo.
"""
(TARGET_DIR / "00_CENTRAL_DASHBOARD.md").write_text(dashboard, encoding="utf-8")

# 2. 01_BANCO_DE_IDEAS_MASTER.md
banco_path = Path("/Users/user/.gemini/antigravity-cli/brain/f22662c3-8f63-45be-8cd7-8df0478cd07e/BANCO_DE_IDEAS.md")
if banco_path.exists():
    banco_content = banco_path.read_text(encoding="utf-8")
    (TARGET_DIR / "01_BANCO_DE_IDEAS_MASTER.md").write_text(f"---\ntags:\n  - banco-ideas\n  - estrategia\n  - unit-economics\n---\n{banco_content}\n", encoding="utf-8")

# 3. 02_CATALOGO_PRODUCTOS_DIGITALES.md
catalog_path = Path("/Users/user/.gemini/antigravity-cli/brain/f22662c3-8f63-45be-8cd7-8df0478cd07e/DIGITAL_PRODUCTS_CATALOG.md")
if catalog_path.exists():
    catalog_content = catalog_path.read_text(encoding="utf-8")
    (TARGET_DIR / "02_CATALOGO_PRODUCTOS_DIGITALES.md").write_text(f"---\ntags:\n  - productos-digitales\n  - gumroad\n  - pricing\n---\n{catalog_content}\n", encoding="utf-8")

# 4. 03_BLUEPRINTS_AUTOMATIZACION.md
bp_note = """---
tags:
  - blueprints
  - n8n
  - make
  - automatizacion
---

# 🛠️ BLUEPRINTS Y WORKFLOWS TÉCNICOS

Los flujos de trabajo están validados e incluidos en el repositorio de GitHub:

1. **WhatsApp AI Smart Lead Router & Booking Agent (Gemini 2.0 Flash)**
   - Archivo: `blueprints/n8n_whatsapp_smart_booking_router.json`
   - Nodo LangChain Agent + Gemini 2.0 Flash clasifica en <3s.
   - Sincronización bidireccional con Google Calendar y Google Sheets.

2. **Automated Site CRO & Speed Diagnostic Engine**
   - Archivo: `blueprints/n8n_automated_cro_audit_engine.json`
   - Consulta la API de Google PageSpeed Insights y sintetiza la pérdida financiera.
   - Genera reportes interactivos en HTML en modo oscuro.

3. **Stripe / MercadoPago Auto-Fulfillment Webhook**
   - Archivo: `blueprints/make_instant_payment_delivery_blueprint.json`
   - Despacho automático de carpetas privadas de entrega y mensaje de bienvenida por WhatsApp.
"""
(TARGET_DIR / "03_BLUEPRINTS_AUTOMATIZACION.md").write_text(bp_note, encoding="utf-8")

# 5. 04_PROSPECCION_B2B_MTY.md
p1 = (BASE_DIR / "swarms/enjambre_a_b2b/clinicas_outreach_pack.md").read_text(encoding="utf-8")
p2 = (BASE_DIR / "swarms/enjambre_a_b2b/despachos_outreach_pack.md").read_text(encoding="utf-8")
p3 = (BASE_DIR / "swarms/enjambre_a_b2b/talleres_outreach_pack.md").read_text(encoding="utf-8")
(TARGET_DIR / "04_PROSPECCION_B2B_MTY.md").write_text(f"""---
tags:
  - prospeccion
  - b2b
  - monterrey
  - clinicas
  - legal
---

# 📲 PROTOCOLO DE PROSPECCIÓN DIRECTA (MONTERREY)

{p1}

---

{p2}

---

{p3}
""", encoding="utf-8")

# 6. 05_MARKETPLACES_UPWORK_FIVERR.md
up = (BASE_DIR / "marketplace_listings/upwork_project_catalog.md").read_text(encoding="utf-8")
fv = (BASE_DIR / "marketplace_listings/fiverr_gig_listing.md").read_text(encoding="utf-8")
(TARGET_DIR / "05_MARKETPLACES_UPWORK_FIVERR.md").write_text(f"""---
tags:
  - upwork
  - fiverr
  - freelance
---

# 💼 LISTINGS Y PROPUESTAS PARA MARKETPLACES

{up}

---

{fv}
""", encoding="utf-8")

# 7. 06_CONTRATOS_Y_LEGAL_IA.md
contract = (BASE_DIR / "swarms/enjambre_c_marketplaces/contrato_prestacion_servicios_ia.md").read_text(encoding="utf-8")
(TARGET_DIR / "06_CONTRATOS_Y_LEGAL_IA.md").write_text(f"""---
tags:
  - legal
  - contratos
  - sla
---

{contract}
""", encoding="utf-8")

# 8. 07_CRONOGRAMA_Y_ESTRATEGIA_HORARIOS.md
cron = """---
tags:
  - cronograma
  - estrategia
  - conversion
---

# ⏱️ CRONOGRAMA Y ESTRATEGIA DE HORARIOS DE DISPARO

## 🥇 Ventana de Oro Matutina: 10:30 AM – 11:45 AM
- **Tasa de Respuesta:** 55% - 70%
- **Razón:** Apertura de consultorio/despacho, revisión de pendientes y primera pausa con celular.

## 🥈 Ventana Vespertina: 3:45 PM – 4:45 PM
- **Tasa de Respuesta:** 40% - 50%
- **Razón:** Post-comida, antes del bloque vespertino de citas.
"""
(TARGET_DIR / "07_CRONOGRAMA_Y_ESTRATEGIA_HORARIOS.md").write_text(cron, encoding="utf-8")

# Also copy to secondary vault in PRODUCTOS DIGITALES
sec_vault = Path("/Users/user/Desktop/Projects/PRODUCTOS DIGITALES/OBSIDIAN_VAULT/AI-AGENCY-MTY")
sec_vault.mkdir(parents=True, exist_ok=True)
for item in TARGET_DIR.glob("*.md"):
    shutil.copy(item, sec_vault / item.name)

print(f"✅ Sincronización exitosa con Obsidian Vault en: {TARGET_DIR}")
print(f"✅ Sincronización exitosa con Vault Secundario en: {sec_vault}")
