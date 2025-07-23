# 🍽️ Organizator de Rețete + Calcul Calorii  
## 🥗 Recipe Organizer + Nutrition Calculator

---

## 🇷🇴 Scopul aplicației

Această aplicație web îți permite să creezi rețete personalizate, să adaugi ingrediente în limba engleză (ex: "100g chicken breast") și să obții automat valorile nutriționale ale fiecărui ingredient: calorii, proteine, grăsimi și carbohidrați. Valorile sunt totalizate pe rețetă, iar toate datele sunt salvate local.

## 🇬🇧 App Purpose

This web app lets you create personalized recipes by entering ingredients in English (e.g., "100g chicken breast"), and automatically retrieves nutritional values for each item: calories, protein, fat, and carbs. Totals are calculated and recipes are saved locally.

---

## ✅ Funcționalități / Features

- 📝 Adăugare rețete cu nume și ingrediente multiple
- ⚙️ Integrare reală cu API Nutritionix pentru date nutriționale
- 📊 Calcul total calorii, proteine, grăsimi, carbohidrați
- 💾 Salvare rețete local în `recipes.json`
- 🌐 Interfață web simplă cu Flask

---

## 📦 Tehnologii utilizate / Tech Stack

- Python 3.10+
- Flask
- HTML, CSS
- Nutritionix API (live)
- Requests
- python-dotenv (pentru protejarea cheilor)

---

## 🧠 Logica aplicației / App Logic

1. Utilizatorul completează un formular cu:
   - numele rețetei
   - 1–3 ingrediente în engleză
2. Pentru fiecare ingredient:
   - aplicația interoghează Nutritionix API
   - extrage datele nutriționale
3. Datele sunt totalizate și afișate
4. Rețeta este salvată în `data/recipes.json`
5. Toate rețetele apar pe pagina principală

---

## 🔐 Cum configurezi API-ul / API Setup

1. Creează cont gratuit pe: [https://developer.nutritionix.com](https://developer.nutritionix.com)
2. În dashboard vei primi:
   - `Application ID`
   - `API Key`

3. Creează un fișier `.env` în rădăcina proiectului cu:

```env
NUTRITIONIX_APP_ID=your_app_id_here
NUTRITIONIX_API_KEY=your_api_key_here

## 🖥️ Cum rulezi aplicația / How to Run the App
git clone https://github.com/devalGabriel/python-portofolio.git
cd python-portofolio/02-recipe_organizer
pip install -r requirements.txt
python app.py