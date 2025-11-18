#!/usr/bin/env python3
"""
Simple Klaviyo Template Upload
Uploads KUL KID newsletter design template via Klaviyo API
"""

import requests
import json
import os

def upload_template(api_key):
    """Upload the KUL KID newsletter design template to Klaviyo"""
    
    headers = {
        "Authorization": f"Klaviyo-API-Key {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "revision": "2024-10-15"
    }
    
    # Read the newsletter template from file
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'kulkid_newsletter_design.html')
    
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            html_template = f.read()
    except FileNotFoundError:
        print(f"❌ Template file not found: {template_path}")
        return False
    
    # Simple text version based on the HTML template
    text_version = """Hei, {{ person|lookup:'first_name'|default:'du' }}!

VELKOMMEN TIL KUL KID KUNDEKLUBB!

MOTTA DIN EKSKLUSIVE RABATT - 15%
Din personlige rabattkode: VELKOMST15-2252F3C4

KOLLEKSJONER:
- Basics: https://kulkid.no/collections/basics
- Superkul: https://kulkid.no/collections/superkul
- Superhelter: https://kulkid.no/collections/superhelter

Fri frakt ved kjøp over 1199,-

FØLG OSS:
- Instagram: https://instagram.com/kulkidno
- Facebook: https://facebook.com/kulkidno
- TikTok: https://tiktok.com/@kulkidno
- Spotify: https://open.spotify.com/artist/5gUHOcGdJU7evr7qx0cvjN
- YouTube: https://www.youtube.com/@kulkidno

Ønsker du ikke å motta tilbud fra oss? Avmelding fra nyhetsbrev her: {{ unsubscribe_url }}

{{ organization.name }} · {{ organization.full_address }}
    """

    data = {
        "data": {
            "type": "template",
            "attributes": {
                "name": "kulkid_newsletter_design_v1",
                "editor_type": "CODE",
                "html": html_template,
                "text": text_version.strip()
            }
        }
    }
    
    response = requests.post(
        "https://a.klaviyo.com/api/templates/",
        headers=headers,
        json=data
    )
    
    if response.status_code in [200, 201]:
        print("✅ KUL KID newsletter design template created successfully!")
        print("📧 Template name: kulkid_newsletter_design_v1")
        print("🎯 Ready to use in Klaviyo flows!")
        return True
    else:
        print(f"❌ Error: {response.status_code}")
        print(f"Details: {response.text}")
        return False

def main():
    print("🚀 Simple Klaviyo Template Upload")
    print("=" * 40)
    
    api_key = input("Enter your Klaviyo Private API Key: ").strip()
    
    if not api_key:
        print("❌ API key required!")
        return
    
    print("\n📧 Uploading KUL KID newsletter design template...")
    
    success = upload_template(api_key)
    
    if success:
        print("\n✅ SUCCESS!")
        print("\nNext steps:")
        print("1. Go to Klaviyo → Content → Email Templates")
        print("2. Find 'kulkid_newsletter_design_v1'")
        print("3. Upload required images to Klaviyo:")
        print("   - email-banner.png")
        print("   - KUL_KID_Kundeklubb.svg")
        print("   - Social media icons (instagram, facebook, tiktok, spotify, youtube)")
        print("   - basics-collection.jpg")
        print("   - featured-product.jpg")
        print("4. Update image URLs in the template")
        print("5. Send a test email to yourself")
        print("6. Ready to use in flows!")
    else:
        print("\n❌ Upload failed. Check your API key and try again.")

if __name__ == "__main__":
    main()