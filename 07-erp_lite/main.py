from core.logic import (
    adauga_produs, listare_produse, cauta_produs,
    adauga_client, listare_clienti, cauta_client,
    adauga_comanda, listare_comenzi,
    raport_stoc_minim, raport_top_clienti
)

def meniu():
    """
    Meniul principal al aplicației ERP-lite CLI.
    Utilizatorul alege acțiunea dorită introducând o cifră.
    """
    print("\n=== ERP-lite CLI - Gestiune Firmă Mică ===")
    print("1. Adaugă produs")
    print("2. Listare produse")
    print("3. Adaugă client")
    print("4. Listare clienți")
    print("5. Adaugă comandă")
    print("6. Listare comenzi")
    print("7. Raport stoc minim")
    print("8. Raport top clienți")
    print("0. Ieșire")

def main():
    while True:
        meniu()
        opt = input("Alege opțiunea: ").strip()
        if opt == "1":
            # Adaugă produs
            cod = input("Cod produs: ")
            denumire = input("Denumire: ")
            stoc = int(input("Stoc inițial: "))
            pret = float(input("Preț unitar: "))
            categorie = input("Categorie: ")
            adauga_produs(cod, denumire, stoc, pret, categorie)
        elif opt == "2":
            # Listare produse
            listare_produse()
        elif opt == "3":
            # Adaugă client
            id_client = input("ID client: ")
            nume = input("Nume client: ")
            cui = input("CUI: ")
            adresa = input("Adresă: ")
            email = input("Email: ")
            telefon = input("Telefon: ")
            adauga_client(id_client, nume, cui, adresa, email, telefon)
        elif opt == "4":
            # Listare clienți
            listare_clienti()
        elif opt == "5":
            # Adaugă comandă
            id_comanda = input("ID comandă: ")
            client_id = input("ID client: ")
            nr_produse = int(input("Număr produse în comandă: "))
            produse_cantitati = []
            for _ in range(nr_produse):
                cod = input("  Cod produs: ")
                cant = int(input("  Cantitate: "))
                produse_cantitati.append((cod, cant))
            adauga_comanda(id_comanda, client_id, produse_cantitati)
        elif opt == "6":
            # Listare comenzi
            listare_comenzi()
        elif opt == "7":
            # Raport stoc minim
            prag = int(input("Prag stoc minim (default 10): ") or "10")
            raport_stoc_minim(prag)
        elif opt == "8":
            # Raport top clienți
            n = int(input("Câți clienți să afișeze? (default 3): ") or "3")
            raport_top_clienti(n)
        elif opt == "0":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă, încearcă din nou.")

if __name__ == "__main__":
    main()