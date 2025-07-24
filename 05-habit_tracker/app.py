from flask import Flask, render_template, request, redirect, url_for, send_file
from core.storage import load_habits, save_habit, mark_day
from core.logic import get_today_status, get_habit_summary
from core.charts import generate_progress_chart
from core.ai_analysis import analyze_habits
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "habit-secret"

@app.route("/")
def index():
    habits = load_habits()
    status = get_today_status(habits)
    summary = get_habit_summary(habits)
    insights = analyze_habits(habits)
    return render_template("index.html", habits=summary, status=status, insights=insights)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        frequency = request.form["frequency"]
        color = request.form.get("color", "#cccccc")
        save_habit(name, frequency, color)
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/mark/<habit_name>")
def mark(habit_name):
    today = datetime.now().strftime("%Y-%m-%d")
    mark_day(habit_name, today)
    return redirect(url_for("index"))

@app.route("/chart")
def chart():
    habits = load_habits()
    chart_path = generate_progress_chart(habits)
    return send_file(chart_path, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
