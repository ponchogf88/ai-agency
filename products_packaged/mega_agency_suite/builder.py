#!/usr/bin/env python3
"""Genera assets de marketing a partir de un lead diagnosticado."""

from __future__ import annotations

import json
import re
from pathlib import Path


def _slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "cliente"


def _load_lead(path: Path) -> dict:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"Lead vacío: {path}")
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        data = {"cliente": path.stem, "notas": text}
    if not isinstance(data, dict):
        raise ValueError(f"Formato de lead inválido: {path}")
    return data


def _landing_html(cliente: str, web: str, servicios: list[str]) -> str:
    servicios_html = "\n".join(f"          <li>{s}</li>" for s in servicios)
    cta = (
        "Agenda tu cita hoy"
        if "taller" in cliente.lower() or "mecán" in cliente.lower()
        else "Contáctanos ahora"
    )
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{cliente} | Presencia digital</title>
  <style>
    :root {{
      --bg: #0f172a;
      --card: #1e293b;
      --accent: #38bdf8;
      --text: #f8fafc;
      --muted: #94a3b8;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: system-ui, -apple-system, sans-serif;
      background: linear-gradient(160deg, var(--bg), #020617);
      color: var(--text);
      min-height: 100vh;
      line-height: 1.6;
    }}
    .wrap {{ max-width: 720px; margin: 0 auto; padding: 3rem 1.5rem; }}
    .badge {{
      display: inline-block;
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent);
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 0.35rem 0.75rem;
      border-radius: 999px;
      margin-bottom: 1.25rem;
    }}
    h1 {{ font-size: clamp(2rem, 5vw, 2.75rem); font-weight: 700; margin-bottom: 0.75rem; }}
    .sub {{ color: var(--muted); font-size: 1.1rem; margin-bottom: 2rem; }}
    .card {{
      background: var(--card);
      border: 1px solid rgba(148, 163, 184, 0.15);
      border-radius: 1rem;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
    }}
    .card h2 {{ font-size: 1rem; color: var(--accent); margin-bottom: 0.75rem; }}
    ul {{ padding-left: 1.25rem; color: var(--muted); }}
    li {{ margin-bottom: 0.35rem; }}
    .cta {{
      display: inline-block;
      background: var(--accent);
      color: #0f172a;
      font-weight: 700;
      text-decoration: none;
      padding: 0.9rem 1.75rem;
      border-radius: 0.5rem;
      margin-top: 0.5rem;
    }}
    footer {{ margin-top: 2.5rem; font-size: 0.8rem; color: var(--muted); }}
  </style>
</head>
<body>
  <div class="wrap">
    <span class="badge">Landing generada por BUILDER</span>
    <h1>{cliente}</h1>
    <p class="sub">Tu negocio merece verse profesional en línea.</p>

    <div class="card">
      <h2>Situación actual</h2>
      <p>Presencia web: <strong>{web or "sin sitio"}</strong></p>
    </div>

    <div class="card">
      <h2>Lo que ofrecemos</h2>
      <ul>
{servicios_html}
      </ul>
      <a class="cta" href="#contacto">{cta}</a>
    </div>

    <footer id="contacto">Asset listo para pitch — agencia-core pipeline</footer>
  </div>
</body>
</html>
"""


def _pitch_text(cliente: str, web: str) -> str:
    gap = "no tiene presencia web" if web in ("ninguna", "", "sin sitio", "no") else f"tiene web limitada ({web})"
    return f"""PITCH — {cliente}

Hola, soy de la agencia. Vi que {cliente} {gap}.

Podemos entregarte en 48 h:
- Landing profesional optimizada para móvil
- Mensaje claro para WhatsApp y redes
- Propuesta visual lista para compartir

¿Te mando una demo personalizada esta semana?
"""


def _default_servicios(cliente: str) -> list[str]:
    lower = cliente.lower()
    if "taller" in lower or "mecán" in lower:
        return [
            "Diagnóstico y reparación express",
            "Cotización transparente por WhatsApp",
            "Landing móvil para captar citas",
        ]
    return [
        "Presencia digital profesional",
        "Mensaje de venta claro y directo",
        "Entrega rápida de materiales listos para pitch",
    ]


def build_assets(lead_path: Path, output_dir: Path) -> Path:
    """Genera carpeta de assets a partir de un archivo lead diagnosticado."""
    lead = _load_lead(lead_path)
    cliente = str(lead.get("cliente") or lead_path.stem)
    web = str(lead.get("web") or "ninguna")
    servicios = lead.get("servicios") or _default_servicios(cliente)
    if not isinstance(servicios, list):
        servicios = _default_servicios(cliente)

    slug = _slugify(cliente)
    assets_dir = output_dir / f"{slug}_assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    # Ejecutar el motor de 14 agentes Marketing OS
    from marketing_os import MarketingOS
    niche = str(lead.get("nicho") or "Servicios Generales")
    engine = MarketingOS()
    dossier = engine.run_full_pipeline(cliente, web=web, niche=niche, target_type="lead")
    
    # Obtener pitch pulido por el Agente Editor y contenido SEO
    approved_pitch = dossier.get("Editor (Anti-AI Slop)", {}).get("data", {}).get("approved_pitch") or _pitch_text(cliente, web)
    llms_txt = dossier.get("SEO & AI Search Lead", {}).get("data", {}).get("llms_txt_content", "")

    (assets_dir / "landing.html").write_text(
        _landing_html(cliente, web, [str(s) for s in servicios]),
        encoding="utf-8",
    )
    (assets_dir / "pitch.txt").write_text(approved_pitch, encoding="utf-8")
    (assets_dir / "llms.txt").write_text(llms_txt, encoding="utf-8")
    (assets_dir / "marketing_os_dossier.json").write_text(
        json.dumps(dossier, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (assets_dir / "lead.json").write_text(
        json.dumps(lead, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"  [BUILDER + MARKETING OS] 14 Assets y Dossier generados en {assets_dir.name}/", flush=True)
    return assets_dir