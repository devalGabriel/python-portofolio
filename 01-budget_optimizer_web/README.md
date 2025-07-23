# 🧮 Optimizator Buget Personal / Personal Budget Optimizer

## 🇷🇴 Scopul aplicației

Această aplicație web te ajută să îți gestionezi veniturile și cheltuielile zilnice într-un mod clar și eficient. Include analiză AI a comportamentului financiar și oferă sugestii automate de optimizare lunară, alături de rapoarte PDF și grafic de cheltuieli.

## 🇬🇧 Application Purpose

This web application helps you manage your daily income and expenses with clarity and efficiency. It includes AI-based financial behavior analysis and generates automatic monthly optimization suggestions, along with PDF reports and expense charts.

---

## 🚀 Funcționalități / Features

- ✅ Interfață web (Flask)
- ✅ Adăugare zilnică tranzacții (venituri / cheltuieli)
- ✅ Raport lunar cu sold, grad de îndatorare și sugestii
- ✅ Export PDF complet cu grafic circular
- ✅ Import extrase bancare `.csv`
- ✅ Analiză AI a comportamentului financiar (anomalie vs. echilibru)

---

## 📦 Tehnologii utilizate / Technologies used

- Python 3.10+
- Flask + Jinja2
- ReportLab (PDF export)
- Matplotlib (charts)
- CSV
- HTML + CSS (minimal)

---

## ⚙️ Logica aplicației / App Logic

1. Tranzacțiile zilnice sunt salvate local (`transactions.json`)
2. Aplicația agregează automat datele lunar
3. Calculează:
   - venituri & cheltuieli
   - sold
   - grad de îndatorare
   - scor AI de comportament financiar
4. Generează PDF și grafic pe categorii
5. Importă fișiere `.csv` de la bancă (ex: salariu, alimentație, utilități)

---

## 🖥️ Cum rulezi aplicația / How to run the app

### 🔧 Pași pentru rulare locală / Run locally:

```bash

pip install -r requirements.txt
python app.py


Exemplu .CSV:
data,categorie,suma,tip,nota
2025-07-15,Mâncare,84.50,expense,Lidl
2025-07-16,Salariu,5000,income,Net
2025-07-18,Transport,240,expense,Benzină