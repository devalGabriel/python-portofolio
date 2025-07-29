from flask import Flask, render_template, request, redirect, url_for
from core.weather_api import get_weather_forecast
from core.storage import load_favorites, save_favorite
from core.chart import generate_temp_chart
import os

app = Flask(__name__)
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    favorites = load_favorites()
    forecast = None
    chart_url = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            forecast = get_weather_forecast(city)
            if forecast and forecast.get("temperatures"):
                chart_url = generate_temp_chart(forecast["days"], forecast["temperatures"], city)
    paired = None
    if forecast and forecast.get("days") and forecast.get("temperatures"):
        paired = list(zip(forecast["days"], forecast["temperatures"]))

    return render_template("index.html", favorites=favorites, forecast=forecast, chart_url=chart_url, paired=paired)

@app.route("/forecast/<city>")
def forecast(city):
    forecast = get_weather_forecast(city)
    chart_url = None
    if forecast and forecast.get("temperatures"):
        chart_url = generate_temp_chart(forecast["days"], forecast["temperatures"], city)
    return render_template("forecast.html", forecast=forecast, chart_url=chart_url)


@app.route("/save", methods=["POST"])
def save_city():
    city = request.form.get("city")
    if city:
        save_favorite(city)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
