from flask import Flask, render_template, request, redirect, url_for, send_file
from core.ocr_reader import extract_receipt_text
from core.analyzer import analyze_receipt
from core.exporter import export_json, export_csv
import os

UPLOAD_FOLDER = "uploads"
EXPORT_FOLDER = "exports"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(EXPORT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    ai_result = None
    if request.method == "POST":
        file = request.files.get("image_file")
        if file:
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)

            text = extract_receipt_text(path)
            result = analyze_receipt(text)
            ai_result = result.get("ai_analysis", {})

    return render_template("index.html", result=result, ai_result=ai_result)

@app.route("/export/<fmt>")
def export(fmt):
    # result are fi stocat în sesiune sau refăcut după caz
    # Pentru simplitate, aici ar fi preluat dintr-un fișier temporar salvat anterior
    if fmt == "json":
        path = export_json()
        return send_file(path, as_attachment=True)
    elif fmt == "csv":
        path = export_csv()
        return send_file(path, as_attachment=True)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
