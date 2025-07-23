from storage import save_transaction, load_transactions
from budget_logic import calculate_monthly_report
from scenarios import generate_scenario
from utils import generate_transaction_id
from datetime import datetime
from pdf_export import export_pdf_report
from chart import generate_expense_chart

def add_transaction():
    t_type = input("Tip (income/expense): ").strip().lower()
    category = input("Categorie: ").strip()
    amount = float(input("Suma: "))
    note = input("Notă (opțional): ").strip()
    
    transaction = {
        "id": generate_transaction_id(),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "type": t_type,
        "category": category,
        "amount": amount,
        "note": note
    }
    save_transaction(transaction)
    print("✅ Tranzacție salvată cu succes.")

def show_monthly_report():
    month = input("Introduceți luna dorită (ex: 2025-07): ").strip()
    transactions = load_transactions()
    report = calculate_monthly_report(transactions, month)
    
    print(f"\n--- Raport {month} ---")
    print(f"Venit total: {report['income']} lei")
    print(f"Cheltuieli totale: {report['expenses']} lei")
    print(f"Sold lunar: {report['balance']} lei")
    print(f"Grad de îndatorare: {report['risk']}%")
    
    print("\nCheltuieli pe categorii:")
    for cat, val in report["by_category"].items():
        print(f" - {cat}: {val:.2f} lei")

    print("\n" + generate_scenario(report))
    chart_path = generate_expense_chart(report["by_category"], month)
    export_pdf_report(report, generate_scenario(report), month=month, chart_path=chart_path)
    export_pdf_report(report, generate_scenario(report), month=month)


def main():
    while True:
        print("\n=== OPTIMIZATOR DE BUGET ===")
        print("1. Adaugă tranzacție")
        print("2. Afișează raport lunar")
        print("0. Ieșire")
        cmd = input("Alege opțiunea: ").strip()
        if cmd == "1":
            add_transaction()
        elif cmd == "2":
            show_monthly_report()
        elif cmd == "0":
            break
        else:
            print("Opțiune invalidă.")

if __name__ == "__main__":
    main()
