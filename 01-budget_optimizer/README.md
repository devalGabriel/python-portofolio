# 🧮 Optimizator Buget Personal – Versiunea 2.0

Aceasta este o aplicație CLI scrisă în Python, destinată **gestionării bugetului personal**, prin:
- înregistrarea zilnică a tranzacțiilor (venituri și cheltuieli),
- calcularea bilanțului lunar,
- analiza cheltuielilor pe categorii,
- estimarea gradului de îndatorare,
- și generarea de **scenarii de optimizare financiară**.

## 🎯 Scopul aplicației

Aplicația este concepută pentru persoane care vor să:
- își monitorizeze atent veniturile și cheltuielile,
- evite dezechilibrul financiar,
- primească recomandări clare de reducere a cheltuielilor,
- obțină o imagine clară asupra obiceiurilor de consum.

---

## 🧠 Funcționalități

- ✅ Adăugare tranzacții zilnice cu cod unic (venituri / cheltuieli)
- ✅ Salvare tranzacții în fișier JSON
- ✅ Afișare raport lunar complet:
  - venituri și cheltuieli totale
  - cheltuieli pe categorii
  - sold lunar
  - grad de îndatorare
  - scenarii de reducere a cheltuielilor
- ✅ Protecție la erori de format sau fișier
- 🚀 Ușor de extins cu export PDF, grafic, aplicație web sau AI

---

## 🔁 Logica aplicației

1. **Salvare date**
   - Fiecare tranzacție (venit/cheltuială) este salvată cu:
     - ID unic
     - data exactă
     - categorie
     - sumă
     - notă opțională
   - Tranzacțiile sunt scrise într-un fișier JSON (`data/transactions.json`), ca o listă.

2. **Calcul lunar**
   - Utilizatorul introduce luna dorită (ex: `2025-07`)
   - Aplicația încarcă toate tranzacțiile din acea lună și:
     - adună veniturile
     - adună cheltuielile, pe categorii
     - calculează soldul: venituri - cheltuieli
     - calculează gradul de îndatorare = (cheltuieli / venituri) * 100
     - construiește un **scenariu de reducere** a cheltuielilor

3. **Sugestii**
   - Dacă bugetul este negativ, aplicația sugerează reduceri de ~15% din categoriile dominante
   - Dacă bugetul este echilibrat, recomandă economii suplimentare

---

## 🛠️ Tehnologii folosite

- Python 3.x
- Module standard: `json`, `datetime`, `uuid`, `os`

---

## 🖥️ Utilizare

1. Rulează aplicația:
```bash
python main.py

