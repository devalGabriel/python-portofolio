import matplotlib.pyplot as plt
import os

def generate_expense_chart(expenses_by_category, month, output_dir="exports"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    labels = list(expenses_by_category.keys())
    values = list(expenses_by_category.values())
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    ax.set_title(f"Distribuția cheltuielilor – {month}")
    
    chart_path = os.path.join(output_dir, f"cheltuieli_{month}.png")
    plt.savefig(chart_path)
    plt.close()
    
    return chart_path
