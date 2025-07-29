import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Pune cheia ta în .env sau ca variabilă de mediu

def get_weather_forecast(city):
    url = ("https://api.openweathermap.org/data/2.5/forecast"
           f"?q={city}&units=metric&appid={API_KEY}&lang=ro")
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    data = resp.json()
    days = []
    temps = []
    if "list" in data:
        for forecast in data["list"]:
            date = forecast["dt_txt"].split(" ")[0]
            temp = forecast["main"]["temp"]
            if date not in days:
                days.append(date)
                temps.append(temp)
    return {
        "city": city,
        "days": days,
        "temperatures": temps,
        "current": data["list"][0] if data["list"] else {}
    }
