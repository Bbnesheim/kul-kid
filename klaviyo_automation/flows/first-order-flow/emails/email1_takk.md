# First Order Email 1: Thank You

**Flow:** First Order Flow  
**Timing:** 1 hour after order fulfillment  
**Goal:** Confirm order, build excitement, provide care tips

---

## Email Metadata

**Subject Line:** Takk for din første bestilling! 🎉

**Preview Text:** Dine KULKID-plagg er på vei – her er noen tips til deg

**From Name:** KUL KID  
**From Email:** hei@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Takk {{ first_name|default:"venn" }}! 🎉

### Body Copy

Din første KUL KID-bestilling er bekreftet og pakket med omtanke!

Vi er så glade for at du valgte oss. Dine {{ event.extra.item_count|default:"nye" }} plagg er nå på vei til deg.

**Ordrenummer:** {{ event.extra.order_id }}

### Order Summary Section
{% if event.extra.items %}
**Ditt kjøp:**
{% for item in event.extra.items %}
- {{ item.product_name }} (Størrelse: {{ item.variant_title }})
{% endfor %}
{% endif %}

### Care Tips Box

**Liten guide: Slik holder plaggene lengst**

- Vask på 30-40 grader
- Unngå tørketrommel når mulig
- Kvaliteten varer bedre med lufttørk
- Plaggene tåler lek og aktivitet!

### What's Next

**Hva skjer videre?**

Du vil motta sporingsinfo på e-post når pakken er sendt. Leveringstid er normalt 2-5 virkedager.

### Primary Button
**Text:** Se min bestilling  
**Link:** {{ event.extra.order_url|default:"https://kulkid.no/account/orders" }}

### Community Invite

Mens du venter: Bli med i KULKID-fellesskapet på Instagram! Vi deler styling

tips, kampanjer og inspirasjon hver dag.

### Instagram Button
**Text:** Følg @kulkidno  
**Link:** https://instagram.com/kulkidno

### Footer
Gleder oss til å se bildene! 📸  
Teamet på KULKID.no

{{ unsubscribe_link }}

---

## Brand Compliance

- [x] "Luckiest Guy" font for headings
- [x] Norwegian language
- [x] Personalization variables
- [x] UTM tracking in links
- [x] Brand tone: Warm, excited, helpful

---

## Technical Notes

- **Template Name:** kulkid_first_order_takk_nb
- **Klaviyo Variables:**
  - `{{ first_name }}`
  - `{{ event.extra.order_id }}`
  - `{{ event.extra.item_count }}`
  - `{{ event.extra.items }}` (array)
  - `{{ event.extra.order_url }}`
- **Timing:** 1 hour after "Fulfilled Order" event
