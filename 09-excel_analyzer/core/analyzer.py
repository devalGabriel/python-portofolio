from collections import defaultdict

def analyze_data(df, conturi_user=None):
    summary = {
        "incasari": 0,
        "plati": 0,
        "sold_final": 0,
        "categorii": {},
        "conturi": {},
        "luni": set(),
        "rows": [],
    }
    if 'Suma' in df and 'Tip' in df:
        for idx, row in df.iterrows():
            suma = float(row['Suma'])
            tip = row['Tip'].lower()
            categ = row.get('Categorie', 'Necunoscut')
            data = row.get('Data', None)
            luna = None
            if data:
                # Extragem anul-luna din formatul YYYY-MM-DD (sau DD.MM.YYYY)
                if "-" in str(data):
                    luna = str(data)[:7]
                elif "." in str(data):
                    luna = ".".join(str(data).split(".")[1::-1])
            if luna:
                summary["luni"].add(luna)
            if 'Cont' in df:
                cont = str(row.get('Cont', 'Necunoscut'))
            elif conturi_user and idx in conturi_user:
                cont = conturi_user[idx]
            else:
                cont = 'Necunoscut'
            summary["rows"].append({
                "suma": suma, "tip": tip, "categorie": categ, "cont": cont, "data": data, "luna": luna
            })
            if tip == 'incasare':
                summary["incasari"] += suma
            elif tip == 'plata':
                summary["plati"] += suma
            summary["categorii"][categ] = summary["categorii"].get(categ, 0) + suma
            summary["conturi"][cont] = summary["conturi"].get(cont, 0) + suma
        summary["sold_final"] = summary["incasari"] - summary["plati"]
        summary["luni"] = sorted(list(summary["luni"]))
    else:
        summary["error"] = "Nu am găsit coloanele Suma/Tip în fișier!"
    return summary

def get_anomalii_top(filtered_rows, prag=10000):
    anomalii = [r for r in filtered_rows if r["suma"] > prag]
    # Top 5 categorii cheltuieli
    from collections import Counter
    cat_counter = Counter()
    for r in filtered_rows:
        if r["tip"] == "plata":
            cat_counter[r["categorie"]] += r["suma"]
    top_categorii = cat_counter.most_common(5)
    return anomalii, top_categorii
