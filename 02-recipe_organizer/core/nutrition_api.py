import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")

def get_nutrition(query):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = { "query": query }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get("foods", [])
    else:
        print(f"⚠️ Eroare API: {response.status_code}")
        return []
