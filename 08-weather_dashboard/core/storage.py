import json
import os

FAV_PATH = "data/favorites.json"

def load_favorites():
    if not os.path.exists(FAV_PATH):
        return []
    with open(FAV_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_favorite(city):
    favs = load_favorites()
    if city not in favs:
        favs.append(city)
    with open(FAV_PATH, "w", encoding="utf-8") as f:
        json.dump(favs, f, ensure_ascii=False, indent=2)
