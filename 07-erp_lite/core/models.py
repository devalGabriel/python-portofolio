class Produs:
    def __init__(self, cod, denumire, stoc, pret, categorie):
        self.cod = cod
        self.denumire = denumire
        self.stoc = int(stoc)
        self.pret = float(pret)
        self.categorie = categorie

class Client:
    def __init__(self, id_client, nume, cui, adresa, email, telefon):
        self.id_client = id_client
        self.nume = nume
        self.cui = cui
        self.adresa = adresa
        self.email = email
        self.telefon = telefon

class Comanda:
    def __init__(self, id_comanda, data, client_id, produse, total, status):
        self.id_comanda = id_comanda
        self.data = data
        self.client_id = client_id
        self.produse = produse  # listă de tuple (cod_produs, cantitate)
        self.total = float(total)
        self.status = status

class Document:
    def __init__(self, tip, serie, numar, data, comanda_id):
        self.tip = tip
        self.serie = serie
        self.numar = numar
        self.data = data
        self.comanda_id = comanda_id
