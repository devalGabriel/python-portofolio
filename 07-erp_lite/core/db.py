import csv
from core.models import Produs, Client, Comanda, Document

DATA_DIR = "data"

def incarca_produse():
    produse = []
    try:
        with open(f"{DATA_DIR}/produse.csv", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                produse.append(Produs(
                    row["cod"], row["denumire"], row["stoc"], row["pret"], row["categorie"]
                ))
    except FileNotFoundError:
        pass
    return produse

def salveaza_produse(lista_produse):
    with open(f"{DATA_DIR}/produse.csv", "w", newline='', encoding="utf-8") as f:
        fieldname = ["cod", "denumire", "stoc", "pret", "categorie"]
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        for p in lista_produse:
            writer.writerow({
                "cod": p.cod,
                "denumire": p.denumire,
                "stoc": p.stoc,
                "pret": p.pret,
                "categorie": p.categorie
            })

def incarca_clienti():
    clienti = []
    try:
        with open(f"{DATA_DIR}/clienti.csv", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                clienti.append(Client(
                    row["id_client"], row["nume"], row["cui"],
                    row["adresa"], row["email"], row["telefon"]
                ))
    except FileNotFoundError:
        pass
    return clienti

def salveaza_clienti(lista_clienti):
    with open(f"{DATA_DIR}/clienti.csv", "w", newline='', encoding="utf-8") as f:
        fieldnames = ["id_client", "nume", "cui", "adresa", "email", "telefon"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for c in lista_clienti:
            writer.writerow({
                "id_client": c.id_client,
                "nume": c.nume,
                "cui": c.cui,
                "adresa": c.adresa,
                "email": c.email,
                "telefon": c.telefon
            })

def incarca_comenzi():
    comenzi = []
    try:
        with open(f"{DATA_DIR}/comenzi.csv", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # produsele sunt salvate ca string: cod1:cantitate1|cod2:cantitate2|...
                produse_list = []
                for prod_pair in row["produse"].split("|"):
                    if prod_pair:
                        cod, cant = prod_pair.split(":")
                        produse_list.append((cod, int(cant)))
                comenzi.append(Comanda(
                    row["id_comanda"], row["data"], row["client_id"], produse_list,
                    row["total"], row["status"]
                ))
    except FileNotFoundError:
        pass
    return comenzi

def salveaza_comenzi(lista_comenzi):
    with open(f"{DATA_DIR}/comenzi.csv", "w", newline='', encoding="utf-8") as f:
        fieldnames = ["id_comanda", "data", "client_id", "produse", "total", "status"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for cmd in lista_comenzi:
            produse_str = "|".join([f"{cod}:{cant}" for cod, cant in cmd.produse])
            writer.writerow({
                "id_comanda": cmd.id_comanda,
                "data": cmd.data,
                "client_id": cmd.client_id,
                "produse": produse_str,
                "total": cmd.total,
                "status": cmd.status
            })

def incarca_documente():
    documente = []
    try:
        with open(f"{DATA_DIR}/documente.csv", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                documente.append(Document(
                    row["tip"], row["serie"], row["numar"], row["data"], row["comanda_id"]
                ))
    except FileNotFoundError:
        pass
    return documente

def salveaza_documente(lista_documente):
    with open(f"{DATA_DIR}/documente.csv", "w", newline='', encoding="utf-8") as f:
        fieldnames = ["tip", "serie", "numar", "data", "comanda_id"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for d in lista_documente:
            writer.writerow({
                "tip": d.tip,
                "serie": d.serie,
                "numar": d.numar,
                "data": d.data,
                "comanda_id": d.comanda_id
            })