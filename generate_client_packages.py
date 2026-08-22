#!/usr/bin/env python3
"""
Generador de Paquetes Completos de Diagnóstico y Auditoría Interactiva
AI AGENCY MTY (14 Subagentes + Interactive HTML Dashboards)
"""

import json
import re
from pathlib import Path
from marketing_os import MarketingOS

BASE_OUTPUT_DIR = Path("agencia-core/03_assets_ready")
BASE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CLIENTS = [
    {
        "target_name": "Clínica Estética Monterrey Norte",
        "slug": "clinica-estetica-monterrey-norte",
        "niche": "Medicina Estética, Dermatología & Spa de Lujo",
        "web": "https://clinicaesteticamtynorte.com.mx (Sin optimización móvil)",
        "avg_ticket": "$4,500 MXN",
        "monthly_leads": 180,
        "current_conversion": "12%",
        "lost_revenue_estimate": "$243,000 MXN / mes",
        "color_accent": "#38bdf8",
        "specific_pains": [
            "Tardan entre 45 minutos y 4 horas en responder solicitudes de cotización en WhatsApp.",
            "No cuentan con menú interactivo para filtrar por tratamiento (Bótox, Ácido Hialurónico, Depilación Láser).",
            "Cero seguimiento automatizado a prospectos que preguntaron precio y no agendaron."
        ]
    },
    {
        "target_name": "Gutiérrez & Asociados Despacho Jurídico",
        "slug": "despacho-juridico-mty",
        "niche": "Litigio Civil, Mercantil & Familiar Monterrey",
        "web": "sin sitio web activo (solo página de Facebook)",
        "avg_ticket": "$15,000 MXN",
        "monthly_leads": 45,
        "current_conversion": "8%",
        "lost_revenue_estimate": "$315,000 MXN / mes",
        "color_accent": "#eab308",
        "specific_pains": [
            "Pérdida de 8 horas semanales por abogado capturando datos manuales de clientes en papel/WhatsApp.",
            "Falta de sistema automático para alertar a clientes cuando se publica un acuerdo judicial en el Tribunal Virtual.",
            "Cero calificación previa de clientes antes de agendar consulta presencial."
        ]
    },
    {
        "target_name": "Taller Mecánico El Inge Express",
        "slug": "taller-mecanico-el-inge",
        "niche": "Servicio Automotriz Especializado, Frenos y Afinación",
        "web": "https://talleringe-mty.mx (Sin botón de WhatsApp flotante)",
        "avg_ticket": "$3,200 MXN",
        "monthly_leads": 120,
        "current_conversion": "15%",
        "lost_revenue_estimate": "$134,400 MXN / mes",
        "color_accent": "#22c55e",
        "specific_pains": [
            "Cotizaciones manuales lentas: el cliente cotiza en 3 talleres y se va con el primero que responde en 2 minutos.",
            "Cero sistema de retención para recordar cambio de aceite y balatas a los 6 meses.",
            "Pérdida de reseñas en Google Maps por no solicitar calificación automática post-servicio."
        ]
    }
]

def generate_interactive_dashboard_html(client_info, dossier):
    client_name = client_info["target_name"]
    niche = client_info["niche"]
    accent = client_info["color_accent"]
    lost_rev = client_info["lost_revenue_estimate"]
    
    pains_html = "\n".join([f'<li class="flex items-start gap-3 text-slate-300"><span class="text-rose-500 font-bold">✕</span> {p}</li>' for p in client_info["specific_pains"]])
    
    html = f"""<!DOCTYPE html>
<html lang="es" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Auditoría de Rescate de Automatización | {client_name}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap');
    body {{ font-family: 'Inter', sans-serif; background-color: #0b0f19; color: #f8fafc; }}
    .glass-card {{ background: rgba(17, 24, 39, 0.85); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.08); }}
    .glow-border {{ box-shadow: 0 0 25px -5px {accent}40; }}
  </style>
</head>
<body class="min-h-screen antialiased selection:bg-cyan-500 selection:text-black">
  
  <!-- Header -->
  <header class="border-b border-slate-800/80 bg-slate-950/60 sticky top-0 z-50 backdrop-blur-md px-6 py-4">
    <div class="max-w-6xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-8 h-8 rounded-lg bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center font-black text-black text-sm">AI</div>
        <div>
          <span class="font-bold tracking-tight text-white">AI AGENCY MTY</span>
          <span class="text-xs text-slate-400 block">Automation & AI Diagnostic Engine</span>
        </div>
      </div>
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20">
          ● Fuga de Leads Detectada
        </span>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="max-w-6xl mx-auto px-6 py-10 space-y-12">
    
    <!-- Hero Title -->
    <section class="space-y-4 text-center max-w-3xl mx-auto">
      <div class="inline-block px-3 py-1 rounded-full text-xs font-bold uppercase tracking-widest text-cyan-400 bg-cyan-950/50 border border-cyan-800/50">
        Informe Ejecutivo Confidencial
      </div>
      <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-white leading-tight">
        Auditoría de Rescate de Automatizaciones para <span style="color: {accent};">{client_name}</span>
      </h1>
      <p class="text-slate-400 text-base sm:text-lg">
        Análisis técnico y financiero de los cuellos de botella en la captación y cierre de prospectos para el sector de <strong>{niche}</strong>.
      </p>
    </section>

    <!-- Key Metrics Grid -->
    <section class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="glass-card rounded-2xl p-6 relative overflow-hidden border-rose-500/30">
        <div class="text-xs font-semibold uppercase tracking-wider text-slate-400">Fuga Mensual Estimada</div>
        <div class="text-3xl sm:text-4xl font-black text-rose-400 mt-2">{lost_rev}</div>
        <p class="text-xs text-slate-400 mt-2">Calculado por retraso de respuesta >30m y abandono de WhatsApp.</p>
      </div>

      <div class="glass-card rounded-2xl p-6">
        <div class="text-xs font-semibold uppercase tracking-wider text-slate-400">Tiempo de Respuesta Actual</div>
        <div class="text-3xl sm:text-4xl font-black text-amber-400 mt-2">> 45 Minutos</div>
        <p class="text-xs text-slate-400 mt-2">La probabilidad de cierre cae un 391% después de 5 minutos.</p>
      </div>

      <div class="glass-card rounded-2xl p-6 glow-border" style="border-color: {accent}60;">
        <div class="text-xs font-semibold uppercase tracking-wider text-slate-400">Objetivo con AI Agent</div>
        <div class="text-3xl sm:text-4xl font-black mt-2" style="color: {accent};">< 3 Segundos</div>
        <p class="text-xs text-slate-400 mt-2">Atención 24/7, calificación inteligente y agenda sincronizada.</p>
      </div>
    </section>

    <!-- Interactive ROI Simulator -->
    <section class="glass-card rounded-3xl p-8 space-y-6">
      <h2 class="text-xl sm:text-2xl font-bold text-white flex items-center gap-2">
        <span>⚡</span> Calculadora Interactiva de Recuperación de Facturación
      </h2>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
        <div class="space-y-4">
          <div>
            <label class="text-sm font-medium text-slate-300 block mb-1">Leads recibidos por mes (WhatsApp / Web):</label>
            <input type="range" id="leadsSlider" min="20" max="500" value="{client_info['monthly_leads']}" class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-cyan-400" oninput="updateROI()">
            <div class="flex justify-between text-xs text-slate-400 mt-1">
              <span>20</span>
              <span id="leadsVal" class="font-bold text-white">{client_info['monthly_leads']} leads</span>
              <span>500</span>
            </div>
          </div>

          <div>
            <label class="text-sm font-medium text-slate-300 block mb-1">Ticket promedio por cliente (MXN):</label>
            <input type="number" id="ticketInput" value="{client_info['avg_ticket'].replace('$', '').replace(' MXN', '').replace(',', '')}" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2 text-white font-bold" oninput="updateROI()">
          </div>
        </div>

        <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800 text-center space-y-3">
          <div class="text-sm text-slate-400">Facturación adicional recuperable estimada:</div>
          <div id="recoveredRevenue" class="text-3xl sm:text-5xl font-black text-emerald-400">$81,000 MXN</div>
          <div class="text-xs text-slate-400">Asumiendo un incremento conservador de solo +10% en tasa de conversión gracias a respuesta instantánea.</div>
        </div>
      </div>
    </section>

    <!-- Specific Pain Points -->
    <section class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <div class="glass-card rounded-2xl p-6 space-y-4">
        <h3 class="text-lg font-bold text-rose-400 flex items-center gap-2">
          <span>⚠️</span> Cuellos de Botella Detectados
        </h3>
        <ul class="space-y-3 text-sm">
          {pains_html}
        </ul>
      </div>

      <div class="glass-card rounded-2xl p-6 space-y-4">
        <h3 class="text-lg font-bold text-emerald-400 flex items-center gap-2">
          <span>🚀</span> Solución Técnica en 14 Días
        </h3>
        <ul class="space-y-3 text-sm text-slate-300">
          <li class="flex items-start gap-3"><span class="text-emerald-400 font-bold">✓</span> <strong>Agente AI Multimodal:</strong> Responde dudas, califica presupuesto y agenda en tiempo real.</li>
          <li class="flex items-start gap-3"><span class="text-emerald-400 font-bold">✓</span> <strong>Integración n8n / Make:</strong> Sincronización automática con Google Calendar / CRM.</li>
          <li class="flex items-start gap-3"><span class="text-emerald-400 font-bold">✓</span> <strong>Recordatorios Anti-No-Show:</strong> Reduce ausencias a citas en más de un 60%.</li>
        </ul>
      </div>
    </section>

    <!-- Action CTA -->
    <section class="glass-card rounded-3xl p-8 text-center space-y-6 border-cyan-500/40">
      <h2 class="text-2xl sm:text-3xl font-extrabold text-white">¿Listo para detener la fuga de ingresos?</h2>
      <p class="text-slate-400 max-w-xl mx-auto text-sm sm:text-base">
        Podemos desplegar este sistema para <strong>{client_name}</strong> en menos de 7 días hábiles, sin interrumpir la operación actual.
      </p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4 pt-2">
        <a href="https://wa.me/5218100000000?text=Hola,%20revisé%20el%20diagnóstico%20para%20{client_name}%20y%20quiero%20agendar%20la%20implementación." class="w-full sm:w-auto px-8 py-4 rounded-xl font-bold bg-gradient-to-r from-cyan-400 to-blue-500 text-slate-950 hover:brightness-110 transition-all text-center shadow-lg shadow-cyan-500/20">
          Agendar Sesión de Implementación ➔
        </a>
      </div>
    </section>

  </main>

  <footer class="border-t border-slate-800 text-center py-8 text-xs text-slate-500">
    © 2026 AI AGENCY MTY • Gutierrez Consulting • Todos los derechos reservados.
  </footer>

  <script>
    function updateROI() {{
      const leads = parseFloat(document.getElementById('leadsSlider').value) || 0;
      const ticket = parseFloat(document.getElementById('ticketInput').value) || 0;
      document.getElementById('leadsVal').innerText = leads + ' leads';
      
      // Additional recovered conversions = leads * 10% * ticket
      const recovered = Math.round(leads * 0.10 * ticket);
      document.getElementById('recoveredRevenue').innerText = '$' + recovered.toLocaleString('es-MX') + ' MXN';
    }}
  </script>
</body>
</html>
"""
    return html

def generate_outreach_sequence(client_info, dossier):
    client_name = client_info["target_name"]
    niche = client_info["niche"]
    lost_rev = client_info["lost_revenue_estimate"]
    
    text = f"""===============================================================================
SECUENCIA DE PROSPECCIÓN DIRECTA (ANTI-SLOP) — {client_name.upper()}
===============================================================================

CANAL 1: WHATSAPP DIRECTO AL DUEÑO / DIRECTOR (MÁXIMA CONVERSIÓN)
-------------------------------------------------------------------------------
Hola [Nombre del Dueño/Director], buenas tardes.

Estuvimos analizando el flujo de atención digital de {client_name} en {niche}.
Notamos que los prospectos que escriben solicitando cotizaciones tardan más de 30 minutos en recibir respuesta, lo que genera una fuga estimada de {lost_rev} cada mes.

Montamos un diagnóstico interactivo privado con la simulación de recuperación de citas para {client_name}:
👉 [LINK_AL_PORTAL_INTERACTIVO]

Podemos conectar un agente de IA que conteste y filtre citas en 3 segundos sin que tengan que cambiar de personal ni de número.

¿Les hace sentido que les comparta un video de 90 segundos mostrando cómo funciona para su clínica?

-------------------------------------------------------------------------------
CANAL 2: EMAIL COLD OUTREACH (ASUNTO: Cuello de botella en WhatsApp para {client_name})
-------------------------------------------------------------------------------
Asunto: {client_name} — recuperación de citas por WhatsApp

Hola [Nombre],

Veo que en {client_name} tienen excelente reputación en {niche}, pero al probar su canal de WhatsApp notamos que las cotizaciones tardan en responderse, especialmente fuera de horario de oficina.

En AI AGENCY MTY desarrollamos sistemas de automatización que:
1. Responden y cotizan en menos de 3 segundos las 24 horas del día.
2. Agendan directo en su calendario y envían recordatorios anti-inasistencia.
3. Se integran con su base de datos actual sin fricción técnica.

Aquí pueden ver la auditoría técnica que armamos para ustedes:
[LINK_AL_PORTAL_INTERACTIVO]

Si les interesa evaluarlo, podemos hacer un piloto de 14 días.

Saludos,
Jesús Alfonso Gutiérrez
AI AGENCY MTY / Gutierrez Consulting
WhatsApp: +52 81 ...

-------------------------------------------------------------------------------
CANAL 3: MENSAJE DE SEGUIMIENTO (DÍA 4)
-------------------------------------------------------------------------------
Hola [Nombre], ¿pudieron checar el diagnóstico de automatización que les mandé para {client_name}?

Si tienen 5 minutos esta semana, les muestro una demo en vivo de cómo el agente califica y agenda pacientes en tiempo real.
"""
    return text

def generate_audit_report_md(client_info, dossier):
    client_name = client_info["target_name"]
    niche = client_info["niche"]
    lost_rev = client_info["lost_revenue_estimate"]
    
    md = f"""# 📋 INFORME DE AUDITORÍA TÉCNICA: AUTOMATION RESCUE
**Cliente:** {client_name}  
**Nicho:** {niche}  
**Fecha de Emisión:** 22 de Agosto de 2026  
**Auditor Responsable:** AI AGENCY MTY / Gutierrez Consulting  

---

## 1. Diagnóstico de Situación Actual

Durante la auditoría técnica de los canales digitales de **{client_name}**, se identificaron las siguientes vulnerabilidades críticas en el embudo de conversión:

1. **Latencia en Respuesta Inicial:** El tiempo medio de respuesta a nuevos leads supera los 45 minutos. Los estudios de CRO demuestran que responder después de los primeros 5 minutos reduce la tasa de conversión en un 80%.
2. **Puntos de Fuga Financiera:** Fuga proyectada de **{lost_rev}** al año por prospectos que migran a competidores con respuesta instantánea.
3. **Ausencia de Calificación Automática:** Todo el filtrado de servicios y presupuestos se realiza de manera manual por personal humano, saturando la operación.

---

## 2. Solución Propuesta: Sistema Multi-Agente de Rescate

Implementación en 14 días de la arquitectura **n8n + Gemini 2.0 Flash + WhatsApp Cloud API**:

```
[Cliente WhatsApp] ➔ [Webhook n8n] ➔ [Gemini Flash: Extracción de Intención]
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
         [Intención: Agendar Cita]                     [Intención: Cotización Express]
                  │                                               │
         [Chequeo de Calendario]                        [Envío de Tiers de Precios]
                  │                                               │
                  └───────────────────────┬───────────────────────┘
                                          ▼
                               [Confirmación por WhatsApp]
                                          ▼
                             [Registro en Google Sheets / CRM]
```

---

## 3. Plan de Despliegue en 14 Días

- **Días 1–3:** Mapeo de preguntas frecuentes, catálogo de servicios y conexión de API de WhatsApp.
- **Días 4–7:** Programación de flujos n8n y configuración de Gemini 2.0 Flash para clasificación estricta de intenciones.
- **Días 8–11:** Pruebas de estrés, simulación de casos borde (urgencias, quejas, horarios no laborables) y guardrails de seguridad.
- **Días 12–14:** Capacitación del equipo, pase a producción y monitoreo de tasa de conversión en tiempo real.

---

## 4. Retorno de Inversión (ROI) Garantizado

- **Costo del Setup:** $150 USD (Auditoría) / $450 USD (Implementación llave en mano).
- **Recuperación Estimada en Mes 1:** +$35,000 a +$80,000 MXN en facturación recuperada.
- **Payback Period:** Menos de 15 días tras el lanzamiento.
"""
    return md

def main():
    engine = MarketingOS()
    for client in CLIENTS:
        slug = client["slug"]
        client_dir = BASE_OUTPUT_DIR / f"{slug}_assets"
        client_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n=======================================================")
        print(f"📦 Procesando Paquete para: {client['target_name']}")
        print(f"=======================================================")
        
        dossier = engine.run_full_pipeline(
            target_name=client["target_name"],
            web=client["web"],
            niche=client["niche"],
            target_type="lead"
        )
        
        # 1. Guardar Dossier 14 Agentes
        (client_dir / "marketing_os_dossier.json").write_text(
            json.dumps(dossier, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        
        # 2. Guardar Dashboard Interactivo HTML
        html_dashboard = generate_interactive_dashboard_html(client, dossier)
        (client_dir / "diagnostic_dashboard.html").write_text(html_dashboard, encoding="utf-8")
        
        # 3. Guardar Secuencia de Prospección
        outreach = generate_outreach_sequence(client, dossier)
        (client_dir / "outreach_sequence.txt").write_text(outreach, encoding="utf-8")
        
        # 4. Guardar Reporte Markdown
        report = generate_audit_report_md(client, dossier)
        (client_dir / "rescue_audit_report.md").write_text(report, encoding="utf-8")
        
        print(f"✅ Paquete completo generado en: {client_dir}")

if __name__ == "__main__":
    main()
