import matplotlib.pyplot as plt
import os
from datetime import datetime

EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

def generate_progress_chart(habits):
    plt.figure(figsize=(10, 6))
    for habit in habits:
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in habit["history"]]
        dates.sort()
        y = [habit["name"]] * len(dates)
        plt.plot(dates, range(len(dates)), marker="o", label=habit["name"], linewidth=2)

    plt.xlabel("Data")
    plt.ylabel("Număr zile")
    plt.title("Evoluție Obiceiuri")
    plt.legend()
    plt.tight_layout()

    chart_path = os.path.join(EXPORT_DIR, "habit_chart.png")
    plt.savefig(chart_path)
    plt.close()
    return chart_path
