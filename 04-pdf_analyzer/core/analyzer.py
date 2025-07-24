import re
from dateutil.parser import parse

def extract_date(text):
    matches = re.findall(r'\d{1,2}[./-]\d{1,2}[./-]\d{2,4}', text)
    for date_str in matches:
        try:
            return str(parse(date_str, dayfirst=True).date())
        except:
            continue
    return "Nedetectată"

def extract_amount(text):
    match = re.search(r'(\d+[.,]?\d*)\s*(lei|RON|€|EUR)', text)
    return match.group(0) if match else "Nedetectată"

def extract_parties(text):
    lines = text.splitlines()
    parties = [line for line in lines if "SRL" in line or "SC" in line]
    return parties[:2] if parties else ["Nedetectat", "Nedetectat"]

def check_missing_data(text):
    issues = []
    if "semnătură" not in text.lower():
        issues.append("❗ Lipsă semnătură")
    if "CUI" not in text:
        issues.append("❗ CUI firmă lipsă")
    if "total" not in text.lower():
        issues.append("❗ Nu s-a detectat totalul")
    return issues or ["✔️ Nicio problemă detectată"]

def analyze_content(text):
    return {
        "Data documentului": extract_date(text),
        "Suma": extract_amount(text),
        "Părți implicate": extract_parties(text),
        "Verificări": check_missing_data(text),
        "Preview text": text[:3000]
    }
