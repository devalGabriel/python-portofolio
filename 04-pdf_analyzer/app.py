from flask import Flask, render_template, request, redirect, send_file
import os
from core.pdf_reader import extract_text
from core.report_generator import generate_report
from core.analyzer import analyze_content

UPLOAD_FOLDER = "uploads"
EXPORT_FOLDER = "exports"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(EXPORT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("pdf_file")
        if file and file.filename.endswith(".pdf"):
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)

            text = extract_text(path)
            results = analyze_content(text)

            report_path = os.path.join(EXPORT_FOLDER, "analiza.pdf")
            generate_report(results, report_path)

            return render_template("result.html", results=results, file=file.filename)
        
    return render_template("index.html")
    
@app.route("/download")
def download():
    return send_file(os.path.join(EXPORT_FOLDER, "analiza.pdf"), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)