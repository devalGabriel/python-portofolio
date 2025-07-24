from datetime import datetime
from collections import defaultdict

def get_today_status(habits):
    today = datetime.now().strftime("%Y-%m-%d")
    status = {}
    for habit in habits:
        status[habit["name"]] = today in habit["history"]
    return status

def get_habit_summary(habits):
    summary = []
    for habit in habits:
        total_days = len(habit["history"])
        first_day = min(habit["history"]) if habit["history"] else "-"
        last_day = max(habit["history"]) if habit["history"] else "-"
        summary.append({
            "name": habit["name"],
            "frequency": habit["frequency"],
            "total": total_days,
            "first": first_day,
            "last": last_day,
            "color": habit.get("color", "#ccc")
        })
    return summary
