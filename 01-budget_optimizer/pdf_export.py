from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

def export_pdf_report(report, scenario, output_dir="exports", month="luna_curenta", chart_path=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = f"{output_dir}/raport_{month}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    margin = 50
    line_height = 18
    y = height - margin

    # Titlu
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, y, f"Raport financiar – {month}")
    y -= 2 * line_height

    # Valori generale
    c.setFont("Helvetica", 12)
    c.drawString(margin, y, f"Venit total: {report['income']} lei")
    y -= line_height
    c.drawString(margin, y, f"Cheltuieli totale: {report['expenses']} lei")
    y -= line_height
    c.drawString(margin, y, f"Sold: {report['balance']} lei")
    y -= line_height
    c.drawString(margin, y, f"Grad de îndatorare: {report['risk']}%")
    y -= 2 * line_height

    # Cheltuieli pe categorii
    c.setFont("Helvetica-Bold", 13)
    c.drawString(margin, y, "Cheltuieli pe categorii:")
    y -= line_height
    c.setFont("Helvetica", 12)
    for cat, val in report["by_category"].items():
        c.drawString(margin + 10, y, f"• {cat}: {val:.2f} lei")
        y -= line_height
        if y < margin + 200:
            c.showPage()
            y = height - margin

    # Scenariu de optimizare
    y -= line_height
    c.setFont("Helvetica-Bold", 13)
    c.drawString(margin, y, "Scenariu de optimizare:")
    y -= line_height
    c.setFont("Helvetica", 11)
    for line in scenario.split("\n"):
        c.drawString(margin + 10, y, line)
        y -= line_height
        if y < margin + 200:
            c.showPage()
            y = height - margin

    # Imagine (grafic)
    if chart_path and os.path.exists(chart_path):
        try:
            c.showPage()  # mergem pe o pagină nouă
            c.setFont("Helvetica-Bold", 13)
            c.drawString(margin, height - margin, "Grafic distribuție cheltuieli:")
            
            image = ImageReader(chart_path)
            img_width = 400
            img_height = 250
            x_pos = (width - img_width) / 2
            y_pos = height - margin - img_height - 20

            c.drawImage(image, x_pos, y_pos, width=img_width, height=img_height, preserveAspectRatio=True)
        except Exception as e:
            c.drawString(margin, y, f"[Eroare afișare grafic]: {str(e)}")

    c.save()
    print(f"✅ PDF generat: {filename}")
