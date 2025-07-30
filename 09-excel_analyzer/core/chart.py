import matplotlib.pyplot as plt
import os

def generate_summary_chart(summary, export_dir):
    """
    Generează un grafic cu distribuția pe categorii.
    """
    if "categorii" not in summary or not summary["categorii"]:
        return None
    categ = list(summary["categorii"].keys())
    values = list(summary["categorii"].values())
    plt.figure(figsize=(7, 4))
    plt.bar(categ, values)
    plt.ylabel("Suma (lei)")
    plt.title("Distribuție cheltuieli/încasări pe categorii")
    plt.tight_layout()
    fname = "summary_chart.png"
    path = os.path.join(export_dir, fname)
    plt.savefig(path)
    plt.close()
    return f"/exports/{fname}"

def generate_evolution_chart(summary, export_dir):
    """Generează grafic cu evoluția soldului pe luni, dacă există date."""
    if not summary.get("luni") or not summary.get("rows"):
        return None
    luni = sorted(set(r["luna"] for r in summary["rows"] if r.get("luna")))
    solduri = []
    for l in luni:
        sold = 0
        for r in summary["rows"]:
            if r.get("luna") == l:
                if r["tip"] == "incasare":
                    sold += r["suma"]
                elif r["tip"] == "plata":
                    sold -= r["suma"]
        solduri.append(sold)
    import matplotlib.pyplot as plt
    plt.figure(figsize=(7, 4))
    plt.plot(luni, solduri, marker="o")
    plt.title("Evoluție sold lunar")
    plt.xlabel("Lună")
    plt.ylabel("Sold (lei)")
    plt.tight_layout()
    fname = "sold_evolutie.png"
    path = os.path.join(export_dir, fname)
    plt.savefig(path)
    plt.close()
    return f"/exports/{fname}"
