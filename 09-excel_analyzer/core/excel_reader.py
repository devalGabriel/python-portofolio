import pandas as pd

def parse_excel(file_path):
    """
    Încarcă un fișier Excel și returnează un DataFrame pandas.
    """
    df = pd.read_excel(file_path)
    return df
