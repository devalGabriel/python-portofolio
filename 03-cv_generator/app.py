from flask import Flask, render_template, request, send_file
import os
from core.pdf_cv import generate_cv_pdf

app = Flask(__name__)
EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["GET"])
def create_route():
    doc_type = request.args.get("type", "cv")
    template = request.args.get("template", "basic")
    if doc_type == "letter":
        return render_template("letter_form.html", template=template)
    return render_template("cv_form.html", template=template)

@app.route("/generate-cv", methods=["POST"])
def generate_cv():
    template = request.form.get("template", "basic")

    name = request.form.get("name")
    contact = request.form.get("contact")

    # Educație
    education = []
    titles = request.form.getlist("education_title[]")
    starts = request.form.getlist("education_start[]")
    ends = request.form.getlist("education_end[]")
    for t, s, e in zip(titles, starts, ends):
        education.append({"title": t, "start": s, "end": e or "Prezent"})

    # Experiență
    experience = []
    roles = request.form.getlist("experience_title[]")
    starts = request.form.getlist("experience_start[]")
    ends = request.form.getlist("experience_end[]")
    for r, s, e in zip(roles, starts, ends):
        experience.append({"role": r, "start": s, "end": e or "Prezent"})

    # Competențe
    skills = request.form.getlist("skills[]")

    data = {
        "name": name,
        "contact": contact,
        "education": education,
        "experience": experience,
        "skills": skills,
        "template": template
    }

    output_path = os.path.join(EXPORT_DIR, "cv.pdf")
    generate_cv_pdf(data, output_path)  # Transmitem doar datele, nu html-ul deja randat
    return send_file(output_path, as_attachment=True)

@app.route("/generate-letter", methods=["POST"])
def generate_letter():
    template = request.form.get("template", "basic")
    name = request.form.get("name")
    position = request.form.get("position")
    message = request.form.get("message")

    data = {
        "name": name,
        "position": position,
        "message": message,
        "template": template
    }

    output_path = os.path.join(EXPORT_DIR, "letter.pdf")
    generate_cv_pdf(data, output_path, is_letter=True)  # adăugăm parametru opțional
    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
