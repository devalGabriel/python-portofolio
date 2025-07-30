import pdfkit
import pandas as pd
import os

def export_pdf_report(summary, chart_url, export_dir):
    # Convertește chart_url (ex: "/exports/summary_chart.png") la path local
    img_path = os.path.join(export_dir, os.path.basename(chart_url)) if chart_url else ""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <style>
    body {{ font-family: Arial, sans-serif; }}
    </style>
    </head>
    <body>
    <h2>Raport Contabil</h2>
    <p>Total încasări: {summary['incasari']} lei</p>
    <p>Total plăți: {summary['plati']} lei</p>
    <p>Sold final: {summary['sold_final']} lei</p>
    <h3>Pe categorii:</h3>
    <ul>
    {''.join([f'<li>{cat}: {val} lei</li>' for cat, val in summary['categorii'].items()])}
    </ul>
    <h3>Pe conturi contabile:</h3>
    <ul>
    {''.join([f'<li>{cont}: {val} lei</li>' for cont, val in summary['conturi'].items()])}
    </ul>
    {"<img src='" + img_path + "' style='max-width:500px;'>" if img_path else ""}
    </body>
    </html>
    """
    pdf_path = os.path.join(export_dir, "raport.pdf")
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    options = {
        "enable-local-file-access": None,
        "encoding": "UTF-8"
    }    
    pdfkit.from_string(html, pdf_path, configuration=config, options=options)
    return pdf_path

def export_csv_report(data_dict, export_dir):
    df = pd.DataFrame.from_dict(data_dict)
    csv_path = os.path.join(export_dir, "raport.csv")
    df.to_csv(csv_path, index=False)
    return csv_path
