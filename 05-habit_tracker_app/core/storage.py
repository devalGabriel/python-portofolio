import json
from datetime import datetime
import os

DATA_FILE = "habits.json"

def load_habits():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_habit(name, frequency, color):
    habits = load_habits()
    habit = {
        "name": name,
        "frequency": frequency,  # daily / weekly
        "color": color,
        "history": []
    }
    habits.append(habit)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(habits, f, indent=2)

def mark_day(habit_name, date_str):
    habits = load_habits()
    for habit in habits:
        if habit["name"] == habit_name:
            if date_str not in habit["history"]:
                habit["history"].append(date_str)
            break
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(habits, f, indent=2)
