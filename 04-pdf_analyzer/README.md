4. Accesează `http://localhost:5000`

---

## 🇬🇧 Description (EN)

This is a smart web application that allows users to **analyze PDF documents** such as invoices or contracts. It extracts the content and identifies critical fields like total amounts, parties involved, and potential issues.

### 🔍 Features
- Upload any PDF file
- Auto extract text (via `pdfplumber`)
- Detect:
- Date
- Amount
- Company names
- Document issues (e.g. no signature)
- Export PDF report with summary
- Preview extracted content in browser

### 🛠️ Technologies
- Python 3
- Flask
- pdfplumber
- pdfkit + wkhtmltopdf
- HTML/CSS
- Jinja2 templating

### ▶️ How to run
1. Install dependencies:
2. Ensure `wkhtmltopdf` is installed and configured in `report_generator.py`
3. Run:
4. Open in browser: `http://localhost:5000`

---

### 📁 Structura aplicației
📂 core/
├── extract.py
├── analyzer.py
├── report_generator.py
📂 templates/
├── index.html
├── result.html
📂 static/
└── style.css
📂 exports/
└── [rapoartele generate]
app.py
requirements.txt
README.md


---

### 📌 Posibile extinderi viitoare
- Suport pentru upload multiplu
- Export CSV
- Dark mode / UI modern
- Istoric documente salvate
