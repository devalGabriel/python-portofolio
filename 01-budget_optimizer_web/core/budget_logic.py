from collections import defaultdict

def calculate_monthly_report(transactions, target_month):
    income, expenses = 0, 0
    category_exp = defaultdict(float)
    
    for t in transactions:
        if not t["date"].startswith(target_month):
            continue
        if t["type"] == "income":
            income += t["amount"]
        elif t["type"] == "expense":
            expenses += t["amount"]
            category_exp[t["category"]] += t["amount"]

    balance = income - expenses
    risk = round((expenses / income) * 100, 2) if income > 0 else 100

    return {
        "income": income,
        "expenses": expenses,
        "balance": balance,
        "risk": risk,
        "by_category": dict(category_exp)
    }
