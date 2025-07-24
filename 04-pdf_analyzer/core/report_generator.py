import pdfkit
from flask import render_template
import os

def generate_report(data, output_path="exports/raport.pdf"):
    # Asigură-te că directorul de export există
    export_dir = os.path.dirname(output_path)
    os.makedirs(export_dir, exist_ok=True)

    # Navighează în directorul de bază (pentru acces la fișiere locale statice)
    base_path = os.path.abspath(".")
    os.chdir(base_path)

    # Pregătește opțiunile pentru PDF
    options = {
        "enable-local-file-access": None,  # permite accesul la fișierele locale (ex: CSS)
        "page-size": "A4",
        "encoding": "UTF-8",
        "margin-top": "10mm",
        "margin-bottom": "10mm",
        "quiet": ""  # opțional, suprimă erorile stdout
    }

    # Configurare cu calea completă către executabilul wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    # Render HTML folosind Flask template engine
    html = render_template("result.html", results=data, filename=os.path.basename(output_path), export_mode=True)

    # DEBUG: Salvează HTML-ul generat pentru verificare manuală
    with open("debug_rendered.html", "w", encoding="utf-8") as f:
        f.write(html)

    # Generare PDF
    pdfkit.from_string(html, output_path, options=options, configuration=config)
