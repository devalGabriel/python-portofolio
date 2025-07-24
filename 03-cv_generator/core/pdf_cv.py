import pdfkit
from flask import render_template

def generate_cv_pdf(data, output_path, is_letter=False):
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    template_folder = "templates_letter" if is_letter else "templates_cv"
    template_file = f"{template_folder}/{data.get('template', 'basic')}.html"

    html = render_template(template_file, **data)

    options = {
        "enable-local-file-access": None,
        "page-size": "A4",
        "margin-top": "10mm",
        "margin-bottom": "10mm",
        "encoding": "UTF-8"
    }

    pdfkit.from_string(html, output_path, options=options, configuration=config)
