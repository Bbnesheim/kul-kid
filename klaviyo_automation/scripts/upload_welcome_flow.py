#!/usr/bin/env python3
"""
Upload Welcome Flow Template to Klaviyo

This script uploads a single welcome-flow email HTML file to Klaviyo as a CODE template.
It is intended as a convenience wrapper around the Klaviyo Templates API, focused on
KUL KID's welcome flow.

Usage (from repo root):

    python klaviyo_automation/scripts/upload_welcome_flow.py --help

Typical run:

    # Using env var
    export KLAVIYO_API_KEY="your_private_key_here"
    python klaviyo_automation/scripts/upload_welcome_flow.py \
        --html-path klaviyo_automation/flows/welcome-flow/emails/email2_welcome_discount15.html \
        --template-name kulkid_welcome_flow_email2_nb_v1

If no API key is provided via flag or environment variable, the script will prompt you.
"""

import argparse
import os
import sys
import textwrap
from typing import Optional

import requests

API_BASE_URL = "https://a.klaviyo.com/api/templates/"
API_REVISION = "2024-10-15"

ENV_API_KEY = "KLAVIYO_API_KEY"


def read_file(path: str) -> str:
    """Read a UTF-8 text file and return its contents.

    Exits with a clear error message if the file does not exist.
    """
    if not os.path.isfile(path):
        print(f"❌ HTML file not found: {path}")
        sys.exit(1)

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as exc:  # pragma: no cover - defensive
        print(f"❌ Failed to read file '{path}': {exc}")
        sys.exit(1)


def build_plain_text_fallback() -> str:
    """Return a simple Norwegian plain-text fallback for the welcome email.

    This does not attempt to mirror the exact HTML layout; it just ensures
    that recipients with plain-text email clients still get the key content.
    """
    return textwrap.dedent(
        """\
        Hei, {{ person|lookup:'first_name'|default:'du' }}!

        VELKOMMEN TIL KUL KID KUNDEKLUBB!

        Her er din eksklusive velkomstrabatt på 15%.

        Bruk rabattkoden du ser i e‑posten for å handle kule klær til kidsa.

        Populære kolleksjoner:
        - Basics: https://kulkid.no/collections/basics
        - Superhelter: https://kulkid.no/collections/superhelter
        - Gymtime: https://kulkid.no/collections/gymtime

        Fri frakt ved kjøp over 1199,-.

        Følg KUL KID:
        - Instagram: https://instagram.com/kulkidno
        - Facebook: https://facebook.com/kulkidno
        - TikTok: https://tiktok.com/@kulkidno
        - Spotify: https://open.spotify.com/artist/5gUHOcGdJU7evr7qx0cvjN
        - YouTube: https://www.youtube.com/@kulkidno

        Ønsker du ikke å motta tilbud fra oss? Avmelding fra nyhetsbrev her: {{ unsubscribe_url }}

        {{ organization.name }} · {{ organization.full_address }}
        """
    ).strip()


def resolve_api_key(cli_api_key: Optional[str]) -> str:
    """Resolve the Klaviyo API key from CLI flag, environment, or prompt."""
    if cli_api_key:
        return cli_api_key.strip()

    env_key = os.getenv(ENV_API_KEY)
    if env_key:
        return env_key.strip()

    try:
        api_key = input("Enter your Klaviyo Private API Key: ").strip()
    except EOFError:
        api_key = ""

    if not api_key:
        print("❌ A Klaviyo Private API Key is required.")
        print(f"   Provide it via --api-key or {ENV_API_KEY} environment variable.")
        sys.exit(1)

    return api_key


def upload_template(api_key: str, html: str, template_name: str, dry_run: bool = False) -> None:
    """Upload the given HTML as a Klaviyo CODE template.

    If dry_run is True, the payload is printed but not sent.
    """
    headers = {
        "Authorization": f"Klaviyo-API-Key {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "revision": API_REVISION,
    }

    text_version = build_plain_text_fallback()

    payload = {
        "data": {
            "type": "template",
            "attributes": {
                "name": template_name,
                "editor_type": "CODE",
                "html": html,
                "text": text_version,
            },
        }
    }

    if dry_run:
        print("ℹ️ Dry run enabled – not sending request to Klaviyo.")
        print("--- Payload preview (truncated) ---")
        preview_html = (html[:400] + "…") if len(html) > 400 else html
        print(f"Template name: {template_name}")
        print(f"HTML length: {len(html)} characters")
        print("HTML preview:\n")
        print(preview_html)
        return

    print("📡 Sending template to Klaviyo…")
    resp = requests.post(API_BASE_URL, headers=headers, json=payload)

    if resp.status_code in (200, 201):
        print("✅ Welcome template uploaded successfully!")
        try:
            body = resp.json()
            template_id = body.get("data", {}).get("id")
        except Exception:  # pragma: no cover - defensive
            template_id = None

        print(f"📧 Template name: {template_name}")
        if template_id:
            print(f"🆔 Template ID: {template_id}")
        print("🎯 Ready to use in your Klaviyo welcome flow.")
    else:
        print(f"❌ Error from Klaviyo API: {resp.status_code}")
        print("Response body:")
        print(resp.text)
        sys.exit(1)


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upload a KUL KID welcome flow email template to Klaviyo.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    default_html = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "flows",
        "welcome-flow",
        "emails",
        "email2_welcome_discount15.html",
    )

    parser.add_argument(
        "--api-key",
        dest="api_key",
        help=f"Klaviyo Private API Key (overrides {ENV_API_KEY} environment variable)",
    )
    parser.add_argument(
        "--html-path",
        dest="html_path",
        default=default_html,
        help="Path to the welcome-flow HTML file to upload",
    )
    parser.add_argument(
        "--template-name",
        dest="template_name",
        default="kulkid_welcome_flow_email2_nb_v1",
        help="Name of the Klaviyo template to create",
    )
    parser.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Do not call the API; just show what would be sent",
    )

    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> None:
    args = parse_args(argv)

    print("🚀 KUL KID – Upload Welcome Flow Template")
    print("=" * 50)

    html_path = args.html_path
    print(f"📄 Using HTML file: {html_path}")

    html = read_file(html_path)
    api_key = resolve_api_key(args.api_key)

    upload_template(
        api_key=api_key,
        html=html,
        template_name=args.template_name,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":  # pragma: no cover
    main()
