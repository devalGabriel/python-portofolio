from collections import defaultdict
import statistics

def analyze_behavior(transactions, current_month):
    # Structură: { "categorie": [sume_lunare] }
    history = defaultdict(lambda: defaultdict(float))  # categorie -> lună -> sumă

    for t in transactions:
        if t["type"] != "expense":
            continue
        month = t["date"][:7]
        history[t["category"]][month] += t["amount"]

    insights = []
    risk_flags = 0
    total_categories = 0

    for category, months in history.items():
        values = list(months.values())
        total_categories += 1

        if current_month not in months:
            continue

        current_value = months[current_month]
        if len(values) < 2:
            continue

        try:
            avg = statistics.mean(values)
            stddev = statistics.stdev(values)
        except statistics.StatisticsError:
            continue

        # Regula simplă: dacă depășește media + 1.5 x deviația standard → anomalia
        if current_value > avg + 1.5 * stddev:
            insights.append(f"⚠️ Cheltuielile la categoria '{category}' sunt semnificativ mai mari decât media istorică.")
            risk_flags += 1
        elif current_value < avg * 0.7:
            insights.append(f"✅ Cheltuielile la '{category}' sunt semnificativ mai mici decât media.")

    # Scor general: 100 = fără anomalie, sub 70 = dezechilibru
    score = max(0, 100 - (risk_flags / total_categories * 100)) if total_categories > 0 else 100

    return {
        "score": round(score),
        "alerts": insights
    }
