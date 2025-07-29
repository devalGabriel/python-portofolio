import re

# Cuvinte cheie pentru categorii
CATEGORII = {
    "alimente": ["lapte", "paine", "ou", "fruct", "carne", "legum", "branza", "iaurt", "salam", "suc", "apa", "bere", "vin"],
    "non-alimente": ["detergent", "baterie", "servetel", "hartie", "sapun", "pastă", "gel", "deodorant"],
    "servicii": ["taxi", "livrare", "transport", "serviciu", "consultatie", "instalare"]
}

def parse_items(text):
    items = []
    for line in text.splitlines():
        # Tolerant: recunoaște denumire, preț, opțional cantitate și cod
        m = re.match(r"(?P<prod>.+?)[\s\.]{2,}(?P<qty>\d+[.,]?\d*)?x?[\s\.]{0,}(?P<price>\d+[.,]\d{2})", line)
        if m:
            prod = m.group("prod").strip()
            price = float(m.group("price").replace(',', '.'))
            qty = m.group("qty")
            qty = float(qty.replace(',', '.')) if qty else 1
            items.append({
                "product": prod,
                "qty": qty,
                "price": price,
                "total": price * qty
            })
    return items

def parse_total(text):
    # Match pentru linia "TOTAL", dar și "SUMĂ DE PLATĂ", "TOTAL DE PLATA" etc.
    patterns = [r'(TOTAL|SUMĂ DE PLATĂ|TOTAL DE PLATA).*?([\d,]+\.\d{2})',
                r'(TOTAL|SUMĂ|TOTAL DE PLATA).*?([\d\.]+)']
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            num = m.group(2).replace(',', '.').replace(' ', '')
            try:
                return float(num)
            except:
                continue
    return None

def parse_date(text):
    m = re.search(r'(\d{2}[./-]\d{2}[./-]\d{4})', text)
    return m.group(1) if m else ""

def categorize(product):
    p = product.lower()
    for cat, lst in CATEGORII.items():
        if any(word in p for word in lst):
            return cat
    return "necunoscut"

def ai_analysis(items, total, text):
    warnings = []
    # Caută prețuri aberante (ex: peste 500 lei)
    expensive = [i for i in items if i["total"] > 500]
    if expensive:
        for i in expensive:
            warnings.append(f"⚠️ Preț neobișnuit: {i['product']} — {i['total']} lei")
    # Caută produse fără categorie
    unknown = [i for i in items if categorize(i["product"]) == "necunoscut"]
    if unknown:
        warnings.append(f"Ai {len(unknown)} produse necunoscute ca și categorie.")
    # Suma produselor vs total
    sum_items = sum(i["total"] for i in items)
    if total and abs(sum_items - total) > 2.0:
        warnings.append(f"❗️Suma produselor ({sum_items:.2f}) nu corespunde cu totalul ({total:.2f})!")
    # Bonus: detectează discount sau TVA
    if "tva" not in ''.join([i["product"].lower() for i in items]):
        if "tva" in text.lower():
            warnings.append("TVA-ul e pe alt rând; verifică și secțiunea TVA separat!")
    return warnings

def analyze_receipt(text):
    items = parse_items(text)
    for i in items:
        i["category"] = categorize(i["product"])
    total = parse_total(text)
    date = parse_date(text)
    warnings = ai_analysis(items, total, text)
    return {
        "items": items,
        "total": total,
        "date": date,
        "ai_analysis": warnings,
        "raw_text": text[:2000]
    }
