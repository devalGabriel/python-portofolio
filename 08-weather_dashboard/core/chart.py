import matplotlib.pyplot as plt
import os

EXPORT_DIR = "static"
os.makedirs(EXPORT_DIR, exist_ok=True)

def generate_temp_chart(days, temps, city):
    plt.figure(figsize=(8, 4))
    plt.plot(days, temps, marker="o")
    plt.title(f"Evoluție temperatură – {city}")
    plt.xlabel("Zi")
    plt.ylabel("°C")
    plt.tight_layout()
    fname = f"chart_{city}.png"
    path = os.path.join(EXPORT_DIR, fname)
    plt.savefig(path)
    plt.close()
    return f"/static/{fname}"
