import json
import os

DATA_FILE = "data/transactions.json"

def load_transactions():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_transaction(entry):
    transactions = load_transactions()
    
    # Verificare suplimentară: dacă e dict în loc de listă, convertim
    if isinstance(transactions, dict):
        transactions = [transactions]

    transactions.append(entry)

    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=2)
