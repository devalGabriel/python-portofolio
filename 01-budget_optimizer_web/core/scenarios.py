def generate_scenario(report):
    balance = report["balance"]
    if balance >= 0:
        return "Buget echilibrat sau pozitiv."
    else:
        lines = ["Buget negativ. Sugestii de reduceri:"]
        deficit = abs(balance)
        sorted_exp = sorted(report["by_category"].items(), key=lambda x: -x[1])
        for cat, val in sorted_exp:
            reducible = val * 0.15
            if deficit <= 0:
                break
            lines.append(f" - {cat}: reducere posibilă ~{round(reducible, 2)} lei")
            deficit -= reducible
        return "\n".join(lines)
