#!/usr/bin/env python3
"""
Empaquetador de Productos Digitales y Listings Comerciales
AI AGENCY MTY / GUTIERREZ CONSULTING
"""

import shutil
import json
from pathlib import Path

BASE_DIR = Path("agencia-core")
PRODUCTS_DIR = BASE_DIR / "products_packaged"
LISTINGS_DIR = BASE_DIR / "marketplace_listings"
BLUEPRINTS_DIR = BASE_DIR / "blueprints"

def build_product_1():
    pkg_dir = PRODUCTS_DIR / "whatsapp_ai_lead_router"
    pkg_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Copy workflow
    shutil.copy(BLUEPRINTS_DIR / "n8n_whatsapp_smart_booking_router.json", pkg_dir / "n8n_workflow.json")
    
    # 2. System Instructions
    sys_prompts = """# 🧠 Gemini 2.0 Flash System Prompts & Guardrails

## 1. Clasificador de Intención Principal (WhatsApp Lead Router)
```text
Eres el Asistente Inteligente de Recepción de [NOMBRE_NEGOCIO].
Tu misión es clasificar de inmediato el mensaje entrante del prospecto en una de las 4 categorías clave:

1. 'citas': El usuario quiere reservar una fecha, consultar disponibilidad o solicitar un espacio en agenda.
2. 'precios': El usuario pregunta por costos, promociones, paquetes o cotizaciones.
3. 'urgencia': El usuario reporta una emergencia (dolor agudo, falla mecánica varada, plazo legal vencido).
4. 'dudas': Preguntas generales de ubicación, horarios o servicios.

Reglas Estrictas:
- Devuelve únicamente formato JSON válido.
- Mantén el tono amable, formal y conciso.
- Respuestas para WhatsApp no deben exceder los 300 caracteres.
```

## 2. Guardrails de Seguridad
- Nunca prometas resultados legales, diagnósticos médicos definitivos ni presupuestos cerrados sin revisión física/presencial.
- Si el usuario muestra hostilidad o pide hablar con un humano, categorizar como 'humano_requerido'.
"""
    (pkg_dir / "prompts_and_guardrails.md").write_text(sys_prompts, encoding="utf-8")
    
    # 3. Readme
    readme = """# ⚡ WhatsApp AI Lead Router & Smart Booking Agent (n8n + Gemini 2.0 Flash)

¡Gracias por adquirir el Blueprint de Automatización de WhatsApp con IA!

## 🚀 ¿Qué incluye este paquete?
- `n8n_workflow.json`: El flujo completo de n8n listo para importar.
- `prompts_and_guardrails.md`: Los prompts de sistema optimizados para Gemini Flash.
- `gumroad_listing_copy.md`: Guía de venta si deseas revenderlo como consultor.

## 🛠️ Instalación en 3 Pasos (Menos de 5 minutos):
1. **Importar en n8n:**
   - Abre tu instancia de n8n (Cloud o Self-Hosted).
   - Ve a **Workflows** ➔ **Add Workflow** ➔ Menú de 3 puntos ➔ **Import from File**.
   - Selecciona `n8n_workflow.json`.

2. **Configurar Credenciales:**
   - Nodo **Gemini 2.0 Flash**: Ingresa tu API Key de Google AI Studio (gratis).
   - Nodo **Google Sheets**: Conecta tu cuenta de Google y selecciona la hoja de registro.
   - Nodo **WhatsApp**: Ingresa tu Token de Meta WhatsApp Cloud API o tu Webhook de OrbAgent.

3. **Activar:**
   - Haz clic en **Active (ON)** y copia la URL del Webhook de producción para pegarla en Meta for Developers.

© 2026 AI AGENCY MTY • Todos los derechos reservados.
"""
    (pkg_dir / "README.md").write_text(readme, encoding="utf-8")
    
    # 4. Gumroad Copy
    gumroad_copy = """# 📄 Sales Copy para Gumroad / LemonSqueezy ($39 USD)

**Título:** WhatsApp AI Lead Router & Booking Agent (n8n + Gemini 2.0 Flash)

**Subtítulo:** Automatiza la captación, filtrado y agendamiento de citas en WhatsApp en menos de 3 segundos sin pagar suscripciones mensuales de software inflado.

---

### 💥 El Problema:
El 60% de los clientes que escriben a un negocio por WhatsApp compran con **el primero que les responde**. Si tardas 30 minutos, ya perdiste la venta frente a tu competencia.

### ⚡ La Solución:
Un flujo de trabajo profesional para **n8n** potenciado por **Google Gemini 2.0 Flash** que:
1. Recibe el mensaje entrante por webhook.
2. Analiza en milisegundos si el cliente quiere agendar, cotizar o resolver una duda urgente.
3. Sincroniza la disponibilidad en Google Calendar y registra el lead en Google Sheets.
4. Responde con un mensaje ultra-personalizado y profesional.

---

### 📦 ¿Qué recibes al instante?
- ✅ Archivo `.json` del workflow completo para n8n (100% editable).
- ✅ Prompts de sistema probados en producción y reglas anti-alucinación.
- ✅ Guía paso a paso de configuración en 5 minutos.
- ✅ Acceso a futuras actualizaciones del workflow.

**Precio:** $39 USD (Pago único — Acceso de por vida)
"""
    (pkg_dir / "gumroad_listing_copy.md").write_text(gumroad_copy, encoding="utf-8")
    print("✅ Paquete 1 creado: whatsapp_ai_lead_router")

def build_product_2():
    pkg_dir = PRODUCTS_DIR / "cro_speed_diagnostic_engine"
    pkg_dir.mkdir(parents=True, exist_ok=True)
    
    shutil.copy(BLUEPRINTS_DIR / "n8n_automated_cro_audit_engine.json", pkg_dir / "n8n_workflow.json")
    
    readme = """# 📊 Automated Site CRO & Speed Diagnostic Engine (n8n + Google PageSpeed)

Genera auditorías técnicas y comerciales interactivas en HTML para cerrar clientes en frío en menos de 60 segundos.

## 🚀 Cómo funciona:
1. Envías la URL del cliente y su nombre por webhook.
2. El sistema consulta la API de PageSpeed Insights de Google para métricas móviles.
3. Gemini 2.0 sintetiza los puntos de fuga y calcula el dinero perdido por lentitud.
4. Compila un dashboard interactivo en HTML listo para enviar por correo o WhatsApp.
"""
    (pkg_dir / "README.md").write_text(readme, encoding="utf-8")
    
    gumroad_copy = """# 📄 Sales Copy para Gumroad ($49 USD)

**Título:** Lead Magnet Generator: Automated CRO & Speed Audit Engine (n8n)

**Subtítulo:** Genera diagnósticos interactivos de alta conversión para tus prospectos de diseño web, SEO y automatización en 60 segundos.

### 🎯 Ideal para:
- Diseñadores web y agencias que hacen prospección en frío.
- Consultores de optimización de conversión (CRO).
- Especialistas en automatización B2B.

**Precio:** $49 USD (Pago único)
"""
    (pkg_dir / "gumroad_listing_copy.md").write_text(gumroad_copy, encoding="utf-8")
    print("✅ Paquete 2 creado: cro_speed_diagnostic_engine")

def build_product_3():
    pkg_dir = PRODUCTS_DIR / "stripe_mercadopago_fulfillment"
    pkg_dir.mkdir(parents=True, exist_ok=True)
    
    shutil.copy(BLUEPRINTS_DIR / "make_instant_payment_delivery_blueprint.json", pkg_dir / "make_blueprint.json")
    
    readme = """# 💳 Stripe / MercadoPago Auto-Fulfillment & Private Client Portal (Make.com)

Conecta tus pasarelas de pago directamente a la creación automática de carpetas privadas de entrega y notificación por WhatsApp.

## 🛠️ Requisitos:
- Cuenta de Make.com (plan gratuito o superior).
- Cuenta de Stripe o MercadoPago con Webhooks habilitados.
"""
    (pkg_dir / "README.md").write_text(readme, encoding="utf-8")
    
    gumroad_copy = """# 📄 Sales Copy para Gumroad ($29 USD)

**Título:** Instant Payment Auto-Fulfillment Blueprint (Make.com)

**Subtítulo:** Despacha accesos, carpetas privadas y bienvenidas por WhatsApp en cuanto tu cliente paga en Stripe o MercadoPago.

**Precio:** $29 USD (Pago único)
"""
    (pkg_dir / "gumroad_listing_copy.md").write_text(gumroad_copy, encoding="utf-8")
    print("✅ Paquete 3 creado: stripe_mercadopago_fulfillment")

def build_product_4():
    pkg_dir = PRODUCTS_DIR / "mega_agency_suite"
    pkg_dir.mkdir(parents=True, exist_ok=True)
    
    shutil.copy(BASE_DIR / "marketing_os.py", pkg_dir / "marketing_os.py")
    shutil.copy(BASE_DIR / "builder.py", pkg_dir / "builder.py")
    shutil.copy(BASE_DIR / "orchestrator.py", pkg_dir / "orchestrator.py")
    
    readme = """# 👑 The 14-Agent Marketing OS Autonomous Engine (AI AGENCY MTY)

La suite de automatización multi-agente en Python que analiza leads, redacta copy anti-slop, define estrategias de pricing y genera activos de marketing de forma 100% autónoma.

## 🚀 Ejecución:
```bash
python3 marketing_os.py --target "Nombre del Cliente" --niche "Nicho" --type "lead"
```
"""
    (pkg_dir / "README.md").write_text(readme, encoding="utf-8")
    
    gumroad_copy = """# 📄 Sales Copy para Gumroad ($79 USD)

**Título:** The 14-Agent Marketing OS Engine (Python + Multi-Agent Swarm)

**Subtítulo:** Despliega una cadena de montaje de 14 subagentes especializados para auditar competidores, crear ofertas irresistibles y redactar pitches sin clichés de IA.

**Precio:** $79 USD (Pago único)
"""
    (pkg_dir / "gumroad_listing_copy.md").write_text(gumroad_copy, encoding="utf-8")
    print("✅ Paquete 4 creado: mega_agency_suite")

def build_marketplace_listings():
    upwork_listing = """# 💼 Upwork Project Catalog Listing

**Título:** I will build an AI-Powered WhatsApp Booking and Lead Automation System in n8n

**Categoría:** Development & IT > AI & Machine Learning > AI Chatbot & Automation

**Tags:** n8n, Make.com, WhatsApp API, Gemini AI, Lead Generation, Workflow Automation, Google Calendar Sync

---

### Descripción del Servicio:
Tired of losing qualified leads because your business takes 30+ minutes to respond on WhatsApp?

I will build a custom, ultra-fast **AI WhatsApp Lead Routing & Booking System** using **n8n** and **Google Gemini 2.0 Flash** that handles customer inquiries, qualifies high-ticket prospects, and synchronizes appointments directly to your Google Calendar in under 3 seconds.

---

### Paquetes del Servicio:

#### 1. Basic Package — $150 USD (3 Days)
- 1 n8n Workflow with WhatsApp Webhook integration.
- Gemini Flash intent classifier (Bookings / Quotes / FAQs).
- Google Sheets logging.
- Setup documentation.

#### 2. Standard Package — $350 USD (5 Days)
- Everything in Basic +
- Real-time Google Calendar sync (checks availability & creates event).
- Custom emergency/escalation alerts to team Slack or WhatsApp.
- 14-day post-launch support.

#### 3. Premium Enterprise Package — $650 USD (7 Days)
- Everything in Standard +
- Mobile-optimized Instant Landing Page with sub-second load time.
- Automated appointment reminder sequences (reduces no-shows by 60%).
- Full CRM integration (Supabase, HubSpot, or Airtable).
- Live 1-on-1 walkthrough and onboarding call.
"""
    (LISTINGS_DIR / "upwork_project_catalog.md").write_text(upwork_listing, encoding="utf-8")

    fiverr_listing = """# 🟢 Fiverr Gig Listing

**Gig Title:** I will build custom AI WhatsApp automation and booking agents using n8n

**Category:** Programming & Tech > Chatbots & AI Agents

**Search Tags:** whatsapp bot, n8n automation, ai agent, make com, lead generation, gemini api

---

### Packages:

- **Basic ($150 USD):** Standard WhatsApp AI lead router + Google Sheets log (2 Revisions).
- **Standard ($350 USD):** AI Router + Live Google Calendar Booking + Follow-up flow.
- **Premium ($650 USD):** Complete Pipeline: AI WhatsApp Agent + Ultra-Fast Landing Page + CRM integration.
"""
    (LISTINGS_DIR / "fiverr_gig_listing.md").write_text(fiverr_listing, encoding="utf-8")
    print("✅ Listings de Upwork y Fiverr creados.")

if __name__ == "__main__":
    build_product_1()
    build_product_2()
    build_product_3()
    build_product_4()
    build_marketplace_listings()
    print("\n🚀 Todos los paquetes de productos digitales y listings generados exitosamente.")
