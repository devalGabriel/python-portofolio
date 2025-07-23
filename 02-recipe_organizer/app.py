from flask import Flask, render_template, request, redirect, url_for
from core.nutrition_api import get_nutrition
import json, os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "data/recipes.json"

def load_recipes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_recipe(recipe):
    recipes = load_recipes()
    recipes.append(recipe)
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(recipes, f, indent=2)

@app.route("/")
def index():
    recipes = load_recipes()
    return render_template("index.html", recipes=recipes)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        ingredients = request.form.getlist("ingredient")

        all_foods = []
        total = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}

        for ing in ingredients:
            results = get_nutrition(ing)
            for item in results:
                all_foods.append({
                    "name": item["food_name"],
                    "input": ing,
                    "calories": item["nf_calories"],
                    "protein": item["nf_protein"],
                    "fat": item["nf_total_fat"],
                    "carbs": item["nf_total_carbohydrate"]
                })
                total["calories"] += item["nf_calories"]
                total["protein"] += item["nf_protein"]
                total["fat"] += item["nf_total_fat"]
                total["carbs"] += item["nf_total_carbohydrate"]

        recipe = {
            "name": name,
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "ingredients": all_foods,
            "total": total
        }
        save_recipe(recipe)
        return redirect(url_for("index"))

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)