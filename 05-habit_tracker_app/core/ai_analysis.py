from datetime import datetime
from collections import defaultdict

def analyze_habits(habits):
    insights = []
    for habit in habits:
        count = len(habit["history"])
        freq = habit["frequency"]
        days = habit["history"]

        if count == 0:
            insights.append(f"⚠️ Obiceiul '{habit['name']}' nu a fost început încă.")
            continue

        days_sorted = sorted(days)
        first = datetime.strptime(days_sorted[0], "%Y-%m-%d")
        last = datetime.strptime(days_sorted[-1], "%Y-%m-%d")
        span_days = (last - first).days + 1

        consistency = round((count / span_days) * 100) if span_days > 0 else 100

        if consistency >= 90:
            msg = f"✅ '{habit['name']}' este urmat excelent ({consistency}% consistență)."
        elif consistency >= 60:
            msg = f"🟡 '{habit['name']}' este în progres, dar poate fi îmbunătățit ({consistency}%)."
        else:
            msg = f"🔴 '{habit['name']}' este urmat inconsistent ({consistency}%). Recomandare: setează alerte zilnice."

        insights.append(msg)

    return insights
