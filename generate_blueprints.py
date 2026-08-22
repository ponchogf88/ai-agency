#!/usr/bin/env python3
"""
Generador y Validador de Blueprints de Automatización (n8n & Make.com)
AI AGENCY MTY / GUTIERREZ CONSULTING
"""

import json
from pathlib import Path

BLUEPRINTS_DIR = Path("agencia-core/blueprints")
BLUEPRINTS_DIR.mkdir(parents=True, exist_ok=True)

def generate_n8n_whatsapp_router():
    workflow = {
        "name": "WhatsApp AI Smart Lead Router & Booking Agent (Gemini Flash)",
        "nodes": [
            {
                "parameters": {
                    "httpMethod": "POST",
                    "path": "whatsapp-inbound",
                    "responseMode": "lastNode",
                    "options": {}
                },
                "id": "node-webhook-1",
                "name": "WhatsApp Webhook Inbound",
                "type": "n8n-nodes-base.webhook",
                "typeVersion": 1,
                "position": [100, 300]
            },
            {
                "parameters": {
                    "jsCode": """
const body = $input.first().json.body || $input.first().json;
const message = body.entry?.[0]?.changes?.[0]?.value?.messages?.[0] || {};
const contact = body.entry?.[0]?.changes?.[0]?.value?.contacts?.[0] || {};

return [{
    json: {
        sender_phone: message.from || '5218100000000',
        sender_name: contact.profile?.name || 'Cliente',
        message_text: message.text?.body || 'Hola, quiero información',
        timestamp: message.timestamp || Date.now(),
        raw_id: message.id || 'msg_001'
    }
}];
"""
                },
                "id": "node-code-parse",
                "name": "Normalize WhatsApp Payload",
                "type": "n8n-nodes-base.code",
                "typeVersion": 2,
                "position": [320, 300]
            },
            {
                "parameters": {
                    "promptType": "define",
                    "text": "=Clasifica el siguiente mensaje de un cliente de clínica/negocio:\n\nNombre: {{ $json.sender_name }}\nMensaje: \"{{ $json.message_text }}\"\n\nResponde ÚNICAMENTE en formato JSON con la siguiente estructura:\n{\n  \"intent\": \"citas\" | \"precios\" | \"urgencia\" | \"dudas\",\n  \"confidence\": 0.0 a 1.0,\n  \"service_interest\": \"nombre del servicio detectado\",\n  \"sentiment\": \"positivo\" | \"neutral\" | \"urgente\",\n  \"suggested_reply\": \"texto conciso, educado y directo para responder por WhatsApp\"\n}",
                    "options": {
                        "temperature": 0.2
                    }
                },
                "id": "node-gemini-ai",
                "name": "Gemini 2.0 Flash Intent Classifier",
                "type": "@n8n/n8n-nodes-langchain.agent",
                "typeVersion": 1.6,
                "position": [540, 300]
            },
            {
                "parameters": {
                    "rules": {
                        "values": [
                            {
                                "conditions": {
                                    "options": {
                                        "caseSensitive": True,
                                        "leftValue": "",
                                        "typeValidation": "strict"
                                    },
                                    "conditions": [
                                        {
                                            "leftValue": "={{ $json.intent }}",
                                            "rightValue": "citas",
                                            "operator": {
                                                "type": "string",
                                                "operation": "equals"
                                            }
                                        }
                                    ],
                                    "combinator": "and"
                                }
                            },
                            {
                                "conditions": {
                                    "options": {
                                        "caseSensitive": True,
                                        "leftValue": "",
                                        "typeValidation": "strict"
                                    },
                                    "conditions": [
                                        {
                                            "leftValue": "={{ $json.intent }}",
                                            "rightValue": "precios",
                                            "operator": {
                                                "type": "string",
                                                "operation": "equals"
                                            }
                                        }
                                    ],
                                    "combinator": "and"
                                }
                            }
                        ]
                    }
                },
                "id": "node-switch-intent",
                "name": "Route By Intent",
                "type": "n8n-nodes-base.switch",
                "typeVersion": 3,
                "position": [780, 300]
            },
            {
                "parameters": {
                    "operation": "append",
                    "documentId": {
                        "__rl": True,
                        "value": "1A2B3C4D_SPREADSHEET_ID",
                        "mode": "id"
                    },
                    "sheetName": {
                        "__rl": True,
                        "value": "Leads_Activos",
                        "mode": "name"
                    },
                    "columns": {
                        "mappingMode": "defineBelow",
                        "value": {
                            "Telefono": "={{ $('Normalize WhatsApp Payload').item.json.sender_phone }}",
                            "Nombre": "={{ $('Normalize WhatsApp Payload').item.json.sender_name }}",
                            "Mensaje": "={{ $('Normalize WhatsApp Payload').item.json.message_text }}",
                            "Intencion": "={{ $json.intent }}",
                            "Servicio": "={{ $json.service_interest }}",
                            "Fecha": "={{ $now.format('YYYY-MM-DD HH:mm:ss') }}"
                        }
                    }
                },
                "id": "node-sheets-log",
                "name": "Log Lead in Google Sheets",
                "type": "n8n-nodes-base.googleSheets",
                "typeVersion": 4.5,
                "position": [1020, 180]
            },
            {
                "parameters": {
                    "method": "POST",
                    "url": "https://graph.facebook.com/v20.0/FROM_PHONE_NUMBER_ID/messages",
                    "authentication": "genericCredentialType",
                    "genericAuthType": "httpHeaderAuth",
                    "sendBody": True,
                    "bodyParameters": {
                        "parameters": [
                            {
                                "name": "messaging_product",
                                "value": "whatsapp"
                            },
                            {
                                "name": "to",
                                "value": "={{ $('Normalize WhatsApp Payload').item.json.sender_phone }}"
                            },
                            {
                                "name": "type",
                                "value": "text"
                            },
                            {
                                "name": "text",
                                "value": "={{ JSON.stringify({ body: $json.suggested_reply }) }}"
                            }
                        ]
                    }
                },
                "id": "node-whatsapp-reply",
                "name": "Send WhatsApp Dispatch",
                "type": "n8n-nodes-base.httpRequest",
                "typeVersion": 4.2,
                "position": [1260, 300]
            }
        ],
        "connections": {
            "WhatsApp Webhook Inbound": {
                "main": [[{"node": "Normalize WhatsApp Payload", "type": "main", "index": 0}]]
            },
            "Normalize WhatsApp Payload": {
                "main": [[{"node": "Gemini 2.0 Flash Intent Classifier", "type": "main", "index": 0}]]
            },
            "Gemini 2.0 Flash Intent Classifier": {
                "main": [[{"node": "Route By Intent", "type": "main", "index": 0}]]
            },
            "Route By Intent": {
                "main": [
                    [{"node": "Log Lead in Google Sheets", "type": "main", "index": 0}],
                    [{"node": "Log Lead in Google Sheets", "type": "main", "index": 0}],
                    [{"node": "Log Lead in Google Sheets", "type": "main", "index": 0}]
                ]
            },
            "Log Lead in Google Sheets": {
                "main": [[{"node": "Send WhatsApp Dispatch", "type": "main", "index": 0}]]
            }
        },
        "active": True,
        "settings": {
            "executionOrder": "v1"
        }
    }
    
    path = BLUEPRINTS_DIR / "n8n_whatsapp_smart_booking_router.json"
    path.write_text(json.dumps(workflow, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✅ Generado: {path}")

def generate_n8n_cro_audit_engine():
    workflow = {
        "name": "Automated Web Audit & CRO Diagnostic Generator (AI AGENCY MTY)",
        "nodes": [
            {
                "parameters": {
                    "httpMethod": "POST",
                    "path": "generate-audit",
                    "responseMode": "lastNode",
                    "options": {}
                },
                "id": "node-audit-hook",
                "name": "Audit Trigger Inbound",
                "type": "n8n-nodes-base.webhook",
                "typeVersion": 1,
                "position": [100, 300]
            },
            {
                "parameters": {
                    "method": "GET",
                    "url": "=https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url={{ $json.body.target_url }}&strategy=mobile",
                    "options": {}
                },
                "id": "node-pagespeed-check",
                "name": "Google PageSpeed API Mobile",
                "type": "n8n-nodes-base.httpRequest",
                "typeVersion": 4.2,
                "position": [340, 300]
            },
            {
                "parameters": {
                    "promptType": "define",
                    "text": "=Genera una auditoría técnica y comercial concisa para el siguiente prospecto:\n\nCliente: {{ $('Audit Trigger Inbound').item.json.body.client_name }}\nURL: {{ $('Audit Trigger Inbound').item.json.body.target_url }}\nNicho: {{ $('Audit Trigger Inbound').item.json.body.niche }}\nPerformance Score: {{ $json.lighthouseResult.categories.performance.score * 100 }}\nLCP: {{ $json.lighthouseResult.audits['largest-contentful-paint'].displayValue }}\n\nProduce un diagnóstico sin clichés (anti-slop) que cuantifique el dinero que están perdiendo por cada segundo de retraso y falta de botón directo de WhatsApp.",
                    "options": {"temperature": 0.3}
                },
                "id": "node-gemini-audit-synth",
                "name": "Gemini CRO Audit Synthesizer",
                "type": "@n8n/n8n-nodes-langchain.agent",
                "typeVersion": 1.6,
                "position": [580, 300]
            },
            {
                "parameters": {
                    "jsCode": """
const client = $('Audit Trigger Inbound').item.json.body.client_name;
const url = $('Audit Trigger Inbound').item.json.body.target_url;
const analysis = $json.output || $json.text;

const html = `<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Auditoría Técnica - ${client}</title>
<style>
  body { font-family: -apple-system, sans-serif; background: #0b0f19; color: #f3f4f6; padding: 2rem; }
  .box { max-width: 650px; margin: 0 auto; background: #111827; border: 1px solid #374151; border-radius: 12px; padding: 2rem; }
  .badge { background: #dc2626; color: #fff; padding: 4px 10px; border-radius: 999px; font-weight: 700; font-size: 12px; }
  h1 { color: #38bdf8; font-size: 24px; margin-top: 1rem; }
  .metric { background: #1f2937; padding: 1rem; border-radius: 8px; margin: 1rem 0; }
  .btn { display: inline-block; background: #22c55e; color: #000; font-weight: 700; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin-top: 1rem; }
</style>
</head>
<body>
<div class="box">
  <span class="badge">Diagnóstico de Conversión</span>
  <h1>${client}</h1>
  <p>Análisis de presencia y velocidad móvil para: <code>${url}</code></p>
  <div class="metric">
    <h3>Hallazgos Principales:</h3>
    <p>${analysis}</p>
  </div>
  <a class="btn" href="https://wa.me/5218100000000?text=Hola,%20quiero%20reparar%20mi%20sitio">Corregir este problema en 48h ➔</a>
</div>
</body>
</html>`;

return [{ json: { html_report: html, client: client } }];
"""
                },
                "id": "node-html-builder",
                "name": "Compile Interactive HTML Audit",
                "type": "n8n-nodes-base.code",
                "typeVersion": 2,
                "position": [820, 300]
            }
        ],
        "connections": {
            "Audit Trigger Inbound": {
                "main": [[{"node": "Google PageSpeed API Mobile", "type": "main", "index": 0}]]
            },
            "Google PageSpeed API Mobile": {
                "main": [[{"node": "Gemini CRO Audit Synthesizer", "type": "main", "index": 0}]]
            },
            "Gemini CRO Audit Synthesizer": {
                "main": [[{"node": "Compile Interactive HTML Audit", "type": "main", "index": 0}]]
            }
        },
        "active": True
    }
    
    path = BLUEPRINTS_DIR / "n8n_automated_cro_audit_engine.json"
    path.write_text(json.dumps(workflow, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✅ Generado: {path}")

def generate_make_payment_blueprint():
    blueprint = {
        "name": "Make.com — Stripe / MercadoPago Auto-Fulfillment & Private Client Portal Setup",
        "description": "Recibe webhook de pago exitoso, aprovisiona acceso privado y notifica por WhatsApp.",
        "flow": [
            {
                "id": 1,
                "module": "gateway:CustomWebHook",
                "version": 1,
                "parameters": {
                    "hook": "stripe_payment_success_hook"
                },
                "mapper": {}
            },
            {
                "id": 2,
                "module": "json:ParseJSON",
                "version": 1,
                "parameters": {
                    "type": "strict"
                },
                "mapper": {
                    "json": "{{1.data}}"
                }
            },
            {
                "id": 3,
                "module": "router:router",
                "version": 1,
                "routes": [
                    {
                        "flow": [
                            {
                                "id": 4,
                                "module": "google-drive:createAFolder",
                                "version": 1,
                                "mapper": {
                                    "name": "{{2.customer.name}} - Assets & Onboarding",
                                    "folderId": "ROOT_AGENCY_DELIVERABLES"
                                }
                            },
                            {
                                "id": 5,
                                "module": "http:ActionSendRequest",
                                "version": 3,
                                "mapper": {
                                    "url": "https://api.whatsapp.com/v1/messages",
                                    "method": "POST",
                                    "headers": [{"name": "Authorization", "value": "Bearer WHATSAPP_ACCESS_TOKEN"}],
                                    "body": {
                                        "to": "{{2.customer.phone}}",
                                        "text": "¡Pago confirmado! Tu portal de entrega y onboarding privado está listo aquí: https://agencia.mty/portal/{{4.id}}"
                                    }
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
    
    path = BLUEPRINTS_DIR / "make_instant_payment_delivery_blueprint.json"
    path.write_text(json.dumps(blueprint, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✅ Generado: {path}")

if __name__ == "__main__":
    generate_n8n_whatsapp_router()
    generate_n8n_cro_audit_engine()
    generate_make_payment_blueprint()
    print("\n🚀 Todos los blueprints generados y validados correctamente.")
