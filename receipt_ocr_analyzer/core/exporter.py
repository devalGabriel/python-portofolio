import json
import pandas as pd
import os

EXPORT_FOLDER = "exports"

def export_json(data=None):
    path = os.path.join(EXPORT_FOLDER, "receipt.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data or {}, f, ensure_ascii=False, indent=2)
    return path

def export_csv(data=None):
    path = os.path.join(EXPORT_FOLDER, "receipt.csv")
    if data and "items" in data:
        df = pd.DataFrame(data["items"])
        df.to_csv(path, index=False)
    return path
