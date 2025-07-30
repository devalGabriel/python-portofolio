from flask import Flask, render_template, request, send_file, redirect, url_for
from core.excel_reader import parse_excel
from core.analyzer import analyze_data, get_anomalii_top
from core.chart import generate_summary_chart
from core.chart import generate_evolution_chart
from core.report import export_pdf_report, export_csv_report

import os
from collections import defaultdict

UPLOAD_DIR = "uploads"
EXPORT_DIR = "exports"
app = Flask(__name__)
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)
data_store = {}

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    chart_url = None
    filename = None
    need_conturi = False
    rows = []
    report_link = None

    # 1. Upload fișier Excel
    if request.method == "POST" and "file" in request.files:
        file = request.files.get("file")
        if file and file.filename.endswith((".xls", ".xlsx")):
            path = os.path.join(UPLOAD_DIR, file.filename)
            file.save(path)
            df = parse_excel(path)
            filename = file.filename
            if "Cont" not in df:
                # Cere completarea manuală a conturilor
                rows = df.to_dict(orient="records")
                need_conturi = True
                return render_template(
                    "index.html",
                    need_conturi=need_conturi,
                    rows=rows,
                    filename=filename
                )
            # Analiză automată dacă există coloană "Cont"
            summary = analyze_data(df)
            chart_url = generate_summary_chart(summary, EXPORT_DIR)
            data_store[filename] = {
                "data": df.to_dict(),
                "summary": summary,
                "chart_url": chart_url,
                "file_path": path,
            }
        else:
            summary = {"error": "Fișier invalid. Acceptă doar .xls sau .xlsx"}
        if filename:
            report_link = url_for("show_report", filename=filename)
        return render_template(
            "index.html",
            summary=summary,
            chart_url=chart_url,
            filename=filename,
            report_link=report_link,
            need_conturi=need_conturi
        )
    # 2. POST cu conturi completate manual
    elif request.method == "POST" and "filename" in request.form:
        filename = request.form.get("filename")
        path = os.path.join(UPLOAD_DIR, filename)
        df = parse_excel(path)
        conturi_user = {}
        for idx, row in enumerate(df.to_dict(orient="records")):
            cont_form = request.form.get(f"conturi_{idx}", "Necunoscut")
            conturi_user[idx] = cont_form
        summary = analyze_data(df, conturi_user)
        chart_url = generate_summary_chart(summary, EXPORT_DIR)
        data_store[filename] = {
            "data": df.to_dict(),
            "summary": summary,
            "chart_url": chart_url,
            "file_path": path,
        }
        report_link = url_for("show_report", filename=filename)
        return render_template(
            "index.html",
            summary=summary,
            chart_url=chart_url,
            filename=filename,
            report_link=report_link,
            need_conturi=False
        )
    # GET default
    return render_template("index.html")

@app.route("/report/<filename>")
def show_report(filename):
    entry = data_store.get(filename)
    if not entry:
        return redirect(url_for("index"))
    summary = entry["summary"]
    chart_url = entry["chart_url"]
    rows = summary["rows"]
    evol_chart_url = generate_evolution_chart(summary, EXPORT_DIR)
    anomalii, top_categorii = get_anomalii_top(filtered_rows)

    # Preluare filtre din query
    selected_luna = request.args.get("luna")
    selected_cat = request.args.get("categorie")
    selected_cont = request.args.get("cont")

    # Filtrare pe baza selecțiilor
    filtered_rows = []
    for row in rows:
        if selected_luna and row.get("luna") != selected_luna:
            continue
        if selected_cat and row.get("categorie") != selected_cat:
            continue
        if selected_cont and row.get("cont") != selected_cont:
            continue
        filtered_rows.append(row)

    # Recalculează subtotaluri pe baza filtrării
    subtot_categ = defaultdict(float)
    subtot_cont = defaultdict(float)
    for row in filtered_rows:
        subtot_categ[row["categorie"]] += row["suma"]
        subtot_cont[row["cont"]] += row["suma"]

    # Identificare pentru UI (filtre disponibile)
    luni = summary.get("luni", [])
    categorii = list(summary["categorii"].keys())
    conturi = list(summary["conturi"].keys())

    return render_template(
        "report.html",
        summary=summary,
        chart_url=chart_url,
        filename=filename,
        filtered_rows=filtered_rows,
        selected_luna=selected_luna,
        selected_cat=selected_cat,
        selected_cont=selected_cont,
        luni=luni,
        categorii=categorii,
        conturi=conturi,
        subtot_categ=subtot_categ,
        subtot_cont=subtot_cont,
        evol_chart_url=evol_chart_url,
    )


@app.route("/export/<filename>/<fmt>")
def export_report(filename, fmt):
    entry = data_store.get(filename)
    if not entry:
        return redirect(url_for("index"))
    if fmt == "pdf":
        pdf_path = export_pdf_report(entry["summary"], entry["chart_url"], EXPORT_DIR)
        return send_file(pdf_path, as_attachment=True)
    elif fmt == "csv":
        csv_path = export_csv_report(entry["data"], EXPORT_DIR)
        return send_file(csv_path, as_attachment=True)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
