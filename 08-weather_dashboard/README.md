# 🌤 Weather Dashboard – Flask Meteo Web App

## Descriere
Această aplicație web oferă prognoza meteo pentru orașe la alegere, folosind API-ul OpenWeatherMap. Include grafic cu temperatura pe mai multe zile și permite salvarea orașelor favorite.

---

## Funcționalități
- Căutare prognoză după oraș
- Grafic temperatură (matplotlib)
- Salvare și afișare orașe favorite
- UI modern și simplu

---

## Tehnologii folosite
- Python 3.9+
- Flask
- Requests
- Matplotlib
- HTML/CSS (Jinja2 templates)
- OpenWeatherMap API

---

## Instalare și rulare

1. Clonează proiectul și instalează dependențele:
    ```bash
    pip install -r requirements.txt
    ```

2. Obține o cheie gratuită de la [OpenWeatherMap](https://openweathermap.org/appid) și seteaz-o în fișierul `.env`:
    ```
    OPENWEATHER_API_KEY=CHEIA_TA_AICI
    ```

   Poți folosi un `.env` sau poți seta variabila de mediu manual:
   ```bash
   set OPENWEATHER_API_KEY=CHEIA_TA_AICI  # Windows
   export OPENWEATHER_API_KEY=CHEIA_TA_AICI  # Linux/Mac

3. Rulează aplicația:
python app.py

4. Accesă aplicația în browser la adresa `http://localhost:5000

5. Structura proiect
├── app.py
├── core/
│   ├── weather_api.py
│   ├── storage.py
│   └── chart.py
├── templates/
│   ├── index.html
│   └── forecast.html
├── static/
│   └── style.css
├── data/
│   └── favorites.json
├── requirements.txt
└── README.md