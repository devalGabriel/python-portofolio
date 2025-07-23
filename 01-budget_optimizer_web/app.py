from flask import Flask, render_template, request, redirect, url_for, send_file
from datetime import datetime
from core.storage import save_transaction, load_transactions
from core.budget_logic import calculate_monthly_report
from core.scenarios import generate_scenario
from core.chart import generate_expense_chart
from core.pdf_export import export_pdf_report
from core.utils import generate_transaction_id
from core.ai_analysis import analyze_behavior
import os
from flask import flash
import csv


app = Flask(__name__)
app.secret_key = "buget-secret-2025"

@app.route("/")
def index():
    month = datetime.now().strftime("%Y-%m")
    transactions = load_transactions()
    report = calculate_monthly_report(transactions, month)
    scenario = generate_scenario(report)
    ai_result = analyze_behavior(transactions, month)
    
    return render_template("index.html", report=report, scenario=scenario, month=month, ai=ai_result)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        t_type = request.form.get("type")
        category = request.form.get("category")
        amount = float(request.form.get("amount"))
        note = request.form.get("note")
        
        transaction = {
            "id": generate_transaction_id(),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "type": t_type,
            "category": category,
            "amount": amount,
            "note": note
        }
        save_transaction(transaction)
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/report/<month>")
def report(month):
    transactions = load_transactions()
    report = calculate_monthly_report(transactions, month)
    scenario = generate_scenario(report)
    chart_path = generate_expense_chart(report["by_category"], month)
    
    ai_result = analyze_behavior(transactions, month)
    export_pdf_report(report, scenario, month=month, chart_path=chart_path, ai=ai_result)

    return send_file(f"exports/raport_{month}.pdf", as_attachment=True)

@app.route("/import", methods=["GET", "POST"])
def import_csv():
    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename.endswith(".csv"):
            content = file.stream.read().decode("utf-8").splitlines()
            reader = csv.DictReader(content)
            count = 0
            for row in reader:
                try:
                    transaction = {
                        "id": generate_transaction_id(),
                        "date": row["data"],
                        "category": row["categorie"],
                        "amount": float(row["suma"]),
                        "type": row["tip"],
                        "note": row.get("nota", "")
                    }
                    save_transaction(transaction)
                    count += 1
                except Exception as e:
                    print(f"Eroare la linia: {row} -> {e}")
            flash(f"{count} tranzacții importate cu succes!", "success")
            return redirect(url_for("index"))
        else:
            flash("Fișier invalid. Te rugăm să încarci un .csv.", "error")
    return render_template("import.html")

if __name__ == "__main__":
    app.run(debug=True)