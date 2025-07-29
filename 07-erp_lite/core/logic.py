from core.db import (
    incarca_produse, salveaza_produse,
    incarca_clienti, salveaza_clienti,
    incarca_comenzi, salveaza_comenzi,
    incarca_documente, salveaza_documente
)
from core.models import Produs, Client, Comanda, Document
from datetime import datetime

def adauga_produs(cod, denumire, stoc, pret, categorie):
    produse = incarca_produse()
    for p in produse:
        if p.cod == cod:
            print("Eroare: exista deja un produs cu acest cod!")
            return False
    produs = Produs(cod, denumire, stoc, pret, categorie)
    produse.append(produs)
    salveaza_produse(produse)
    print(f"✔️ Produsul '{denumire}' a fost adăugat.")
    return True

def listare_produse():
    produse = incarca_produse()
    if not produse:
        print("Nu există produse in sistem.")
        return
    print("\n--- LISTA PRODUSE ---")
    print("Cod   | Denumire          | Stoc | Preț | Categorie")
    print("-" * 50)
    for p in produse:
        print(f"{p.cod:6} | {p.denumire:16} | {p.stoc:4} | {p.pret:5.2f} | {p.categorie}")
    print("-" * 50)

def cauta_produs(cod):
    """
    Găsește și returnează produsul după cod.
    """
    produse = incarca_produse()
    for p in produse:
        if p.cod == cod:
            return p
    return None

def adauga_client(id_client, nume, cui, adresa, email, telefon):
    """
    Creează și salvează un client nou.
    """
    clienti = incarca_clienti()
    for c in clienti:
        if c.id_client == id_client:
            print("Eroare: există deja un client cu acest ID!")
            return False
    client = Client(id_client, nume, cui, adresa, email, telefon)
    clienti.append(client)
    salveaza_clienti(clienti)
    print(f"✔️ Clientul '{nume}' a fost adăugat.")
    return True

def listare_clienti():
    """
    Afișează toți clienții existenți.
    """
    clienti = incarca_clienti()
    if not clienti:
        print("Nu există clienți în sistem.")
        return
    print("\n--- LISTĂ CLIENȚI ---")
    print("ID   | Nume               | CUI      | Email             | Telefon")
    print("-" * 60)
    for c in clienti:
        print(f"{c.id_client:4} | {c.nume:18} | {c.cui:8} | {c.email:17} | {c.telefon}")
    print("-" * 60)

def cauta_client(id_client):
    """
    Găsește și returnează clientul după ID.
    """
    clienti = incarca_clienti()
    for c in clienti:
        if c.id_client == id_client:
            return c
    return None

def adauga_comanda(id_comanda, client_id, produse_cantitati):
    """
    Creează și salvează o comandă nouă.
    Scade stocul automat la fiecare produs inclus.
    produse_cantitati: listă de tuple (cod_produs, cantitate)
    """
    produse = incarca_produse()
    comenzi = incarca_comenzi()
    client = cauta_client(client_id)
    if not client:
        print("Eroare: client inexistent!")
        return False
    # Verifică existența și stocul fiecărui produs
    total = 0
    for cod, cant in produse_cantitati:
        p = cauta_produs(cod)
        if not p:
            print(f"Eroare: produs {cod} inexistent!")
            return False
        if p.stoc < cant:
            print(f"Eroare: stoc insuficient pentru {p.denumire}!")
            return False
        total += p.pret * cant
    # Actualizează stocul pentru fiecare produs
    for cod, cant in produse_cantitati:
        p = cauta_produs(cod)
        p.stoc -= cant
    salveaza_produse(produse)
    data = datetime.now().strftime("%Y-%m-%d")
    comanda = Comanda(id_comanda, data, client_id, produse_cantitati, total, "INREGISTRATA")
    comenzi.append(comanda)
    salveaza_comenzi(comenzi)
    print(f"✔️ Comanda #{id_comanda} a fost salvată cu succes (total: {total:.2f} lei).")
    return True

def listare_comenzi():
    """
    Afișează toate comenzile existente.
    """
    comenzi = incarca_comenzi()
    if not comenzi:
        print("Nu există comenzi în sistem.")
        return
    print("\n--- LISTĂ COMENZI ---")
    print("ID | Data       | Client | Produse            | Total | Status")
    print("-" * 70)
    for cmd in comenzi:
        produse_str = ", ".join([f"{cod}x{cant}" for cod, cant in cmd.produse])
        print(f"{cmd.id_comanda:2} | {cmd.data} | {cmd.client_id:6} | {produse_str:18} | {cmd.total:6.2f} | {cmd.status}")
    print("-" * 70)

def raport_stoc_minim(prag=10):
    """
    Afișează produsele cu stoc sub prag (implicit 10).
    """
    produse = incarca_produse()
    print(f"\n--- RAPORT STOC MINIM (sub {prag}) ---")
    for p in produse:
        if p.stoc < prag:
            print(f"{p.denumire:16} | Stoc: {p.stoc}")

def raport_top_clienti(n=3):
    """
    Afișează cei mai importanți clienți după valoarea comenzilor.
    """
    comenzi = incarca_comenzi()
    clienti = incarca_clienti()
    sume = {}
    for cmd in comenzi:
        sume[cmd.client_id] = sume.get(cmd.client_id, 0) + cmd.total
    top = sorted(sume.items(), key=lambda x: x[1], reverse=True)[:n]
    print(f"\n--- TOP {n} CLIENȚI DUPĂ VÂNZĂRI ---")
    for client_id, suma in top:
        client = next((c for c in clienti if c.id_client == client_id), None)
        nume = client.nume if client else "(necunoscut)"
        print(f"{nume:18} | {suma:.2f} lei")