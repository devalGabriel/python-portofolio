import re

def parse_items(text):
    # Exemplu: extrage linii cu produs și preț (format uzual: nume .... 12.34)
    items = []
    for line in text.splitlines():
        m = re.match(r"(.+?)[\s\.]{2,}([\d,]+\.\d{2})", line)
        if m:
            name = m.group(1).strip()
            price = float(m.group(2).replace(',', ''))
            items.append({"product": name, "price": price})
    return items

def parse_total(text):
    # Caută linia cu "TOTAL" și o sumă
    m = re.search(r'TOTAL.*?([\d,]+\.\d{2})', text, re.IGNORECASE)
    return float(m.group(1).replace(',', '')) if m else None

def parse_date(text):
    # Exemplu: caută o dată de tip 12.06.2025 sau 2025-06-12
    m = re.search(r'(\d{2}[./-]\d{2}[./-]\d{4})', text)
    return m.group(1) if m else ""

def ai_analysis(items, total):
    # Analiză simplă: detectează dacă suma itemelor ≈ total, grupare pe categorii etc.
    sum_items = sum(i["price"] for i in items)
    warnings = []
    if total and abs(sum_items - total) > 1.0:
        warnings.append("❗️Suma produselor nu corespunde cu totalul!")
    if len(items) > 15:
        warnings.append("Ai avut un coș foarte plin!")
    return warnings

def analyze_receipt(text):
    items = parse_items(text)
    total = parse_total(text)
    date = parse_date(text)
    warnings = ai_analysis(items, total)
    return {
        "items": items,
        "total": total,
        "date": date,
        "ai_analysis": warnings,
        "raw_text": text[:2000]
    }
