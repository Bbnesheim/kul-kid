#!/usr/bin/env python3
"""Upload KUL KID Welcome Flow email templates to Klaviyo.

This script uploads the two Welcome Flow templates:
- email1_double_optin_confirmation.html
- email2_welcome_discount15.html

It uses the same API pattern as simple_upload.py, but is scoped to the
Welcome Flow and expects the HTML files to live under flows/welcome-flow/emails/.

API key handling:
- Prefer environment variable KLAVIYO_API_KEY
- If missing, prompt securely in the terminal
"""

import json
import os
import sys
from typing import Dict, List

import requests

API_BASE_URL = "https://a.klaviyo.com/api/templates/"
API_REVISION = "2024-10-15"

# Relative to project root (klaviyo_automation/)
WELCOME_TEMPLATES: List[Dict[str, str]] = [
    {
        "name": "kulkid_welcome_double_optin_nb",
        "html_path": "flows/welcome-flow/emails/email1_double_optin_confirmation.html",
        "text": """Hei {{ person|lookup:'first_name'|default:'du' }}!\n\nVelkommen til KUL KID Kundeklubb. Bekreft e‑postadressen din, så sender vi deg din personlige rabattkode i neste e‑post.\n\nKlikk på lenken under for å bekrefte:\n{{ confirm_link }}\n\nHvis du ikke meldte deg inn, kan du ignorere denne e‑posten.\n\nTeamet på KULKID.no\n{{ unsubscribe_url }}\n""",
    },
    {
        "name": "kulkid_welcome_discount15_nb",
        "html_path": "flows/welcome-flow/emails/email2_welcome_discount15.html",
        "text": """Hei {{ person|lookup:'first_name'|default:'du' }}!\n\nHer er din velkomstrabatt hos KUL KID: bruk koden VELKOMST15 for 15% rabatt på din første bestilling.\n\nGjelder i 7 dager fra i dag på nesten alt hos KUL KID.\n\nBesøk: https://kulkid.no/collections/all\n\nTeamet på KULKID.no\n{{ unsubscribe_url }}\n""",
    },
]


def get_project_root() -> str:
    """Return the klaviyo_automation project root based on this script location."""
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(scripts_dir)


def get_api_key() -> str:
    """Get Klaviyo API key from env or prompt the user."""
    api_key = os.getenv("KLAVIYO_API_KEY")
    if api_key:
        return api_key.strip()

    try:
        api_key = input("Enter your Klaviyo Private API Key: ").strip()
    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(1)

    if not api_key:
        print("❌ API key is required.")
        sys.exit(1)

    return api_key


def read_html(path_from_root: str) -> str:
    """Read an HTML file relative to the klaviyo_automation root."""
    root = get_project_root()
    full_path = os.path.join(root, path_from_root)

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ HTML file not found: {full_path}")
        sys.exit(1)


def upload_template(api_key: str, name: str, html: str, text: str) -> bool:
    """Upload a single template to Klaviyo. Returns True on success."""
    headers = {
        "Authorization": f"Klaviyo-API-Key {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "revision": API_REVISION,
    }

    payload = {
        "data": {
            "type": "template",
            "attributes": {
                "name": name,
                "editor_type": "CODE",
                "html": html,
                "text": text.strip(),
            },
        }
    }

    print(f"\n📧 Uploading template: {name} …")
    resp = requests.post(API_BASE_URL, headers=headers, json=payload, timeout=30)

    if resp.status_code in (200, 201):
        print("✅ Success")
        try:
            data = resp.json()
            template_id = data.get("data", {}).get("id")
            if template_id:
                print(f"   → Template ID: {template_id}")
        except json.JSONDecodeError:
            pass
        return True

    print(f"❌ Failed with status {resp.status_code}")
    try:
        print(f"   Response: {resp.text}")
    except Exception:
        pass
    return False


def main() -> None:
    print("🚀 Upload KUL KID Welcome Flow templates to Klaviyo")
    print("=" * 60)

    api_key = get_api_key()

    root = get_project_root()
    print(f"📂 Project root: {root}")

    all_ok = True
    for tmpl in WELCOME_TEMPLATES:
        html = read_html(tmpl["html_path"])
        ok = upload_template(
            api_key=api_key,
            name=tmpl["name"],
            html=html,
            text=tmpl["text"],
        )
        all_ok = all_ok and ok

    if all_ok:
        print("\n🎯 All Welcome Flow templates uploaded successfully.")
        print("You can now wire them into the Welcome Flow in Klaviyo.")
    else:
        print("\n⚠️ One or more uploads failed. Check the errors above and retry.")


if __name__ == "__main__":
    main()
