# Generator CV PDF – Portofoliu Python

## 📌 Scopul aplicației
Această aplicație permite generarea unui CV profesional în format PDF, pe baza datelor completate de utilizator într-un formular web. Utilizatorul poate introduce dinamic educația, experiența profesională, competențele, precum și informații de contact și sumar profesional.

## 💡 Funcționalități cheie
- Formulare dinamice pentru adăugare educație, experiență, competențe
- Date calendaristice (de început/sfârșit) cu tratament automat pentru „Prezent”
- Export automat în PDF folosind layout HTML + `pdfkit`
- Interfață web intuitivă cu Flask

## 🛠️ Tehnologii folosite
- Python 3
- Flask
- HTML + CSS + JS (formular dinamic)
- pdfkit (cu wkhtmltopdf)

## 🧠 Logica aplicației
1. Utilizatorul completează formularul cu mai multe câmpuri adăugate dinamic
2. Serverul Flask preia toate datele și le grupează în liste structurate
3. Template-ul HTML este completat cu aceste date și transmis `pdfkit`
4. PDF-ul rezultat este generat și descărcat automat de utilizator

---

# 📄 CV PDF Generator – Python Portfolio

## 📌 Purpose
This app lets users generate a clean, professional CV in PDF format from a web form. Dynamic sections include education, experience, and skills. It's ideal for portfolio-building and resume generation.

## 💡 Key Features
- Dynamic form fields for education, work experience, and skills
- Handles start/end dates with fallback to "Present"
- PDF export via HTML templates + `pdfkit`
- Simple Flask web interface

## 🛠️ Technologies
- Python 3
- Flask
- HTML + CSS + JS (dynamic form handling)
- pdfkit (with wkhtmltopdf installed)

## 🧠 Logic Flow
1. User fills in dynamic sections via browser
2. Flask parses all inputs into structured lists
3. HTML template is populated with the data and passed to `pdfkit`
4. Final PDF is downloaded by the user

---

## ▶️ Rulare locală / Run locally
```bash
# Creează mediu virtual
python -m venv venv
source venv/bin/activate  # sau venv\Scripts\activate pe Windows

# Instalează dependințele
pip install flask pdfkit

# Pornește aplicația
python app.py
```

Asigură-te că `wkhtmltopdf` este instalat și configurat în variabilă de mediu sau setat direct în aplicație.
