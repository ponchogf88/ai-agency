#!/usr/bin/env python3
"""
Script de inyección rápida de número de WhatsApp en todos los activos y landings
Uso: python3 inject_whatsapp.py --phone 5218112345678
"""

import sys
import argparse
from pathlib import Path

def inject(phone: str):
    clean_phone = "".join(filter(str.isdigit, phone))
    if not clean_phone:
        print("❌ Error: Número inválido")
        return

    print(f"🔄 Inyectando número: +{clean_phone} en todos los portales y secuencias...")

    # 1. Update Portal
    portal_file = Path("agencia-core/portal/index.html")
    if portal_file.exists():
        content = portal_file.read_text(encoding="utf-8")
        content = content.replace("5218100000000", clean_phone)
        portal_file.write_text(content, encoding="utf-8")
        print("✓ Actualizado: agencia-core/portal/index.html")

    # 2. Update Client Dashboards & Outreaches
    assets_dir = Path("agencia-core/03_assets_ready")
    for client_folder in assets_dir.iterdir():
        if client_folder.is_dir():
            dash = client_folder / "diagnostic_dashboard.html"
            if dash.exists():
                text = dash.read_text(encoding="utf-8")
                text = text.replace("5218100000000", clean_phone)
                dash.write_text(text, encoding="utf-8")
                print(f"✓ Actualizado Dashboard: {client_folder.name}")
            
            seq = client_folder / "outreach_sequence.txt"
            if seq.exists():
                text = seq.read_text(encoding="utf-8")
                text = text.replace("+52 81 ...", f"+{clean_phone}")
                seq.write_text(text, encoding="utf-8")
                print(f"✓ Actualizado Outreach: {client_folder.name}")

    print("\n🔥 Inyección completada exitosamente.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--phone", default="5218100000000", help="Número de WhatsApp con código de país")
    args = parser.parse_args()
    inject(args.phone)
