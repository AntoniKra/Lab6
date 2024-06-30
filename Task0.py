import argparse

def parsuj_argumenty():
    parser = argparse.ArgumentParser(description='Opis programu')
    parser.add_argument('plik_wejscie', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('plik_wyjscie', type=str, help='Ścieżka do pliku wyjściowego')
    return parser.parse_args()

if __name__ == "__main__":
    args = parsuj_argumenty()
    print(f'Plik wejściowy: {args.plik_wejscie}, Plik wyjściowy: {args.plik_wyjscie}')








    import json

def wczytaj_json(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            dane = json.load(plik)
        return dane
    except FileNotFoundError:
        print(f"Plik '{nazwa_pliku}' nie istnieje.")
        return None
    except json.JSONDecodeError as e:
        print(f"Błąd dekodowania JSON w pliku '{nazwa_pliku}': {e}")
        return None
    


dane = wczytaj_json('file.json')
if dane:
    print(dane)