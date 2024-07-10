import argparse
import json

def parsuj_argumenty():
    parser = argparse.ArgumentParser(description='Opis programu')
    parser.add_argument('plik_wejscie', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('plik_wyjscie', type=str, help='Ścieżka do pliku wyjściowego')
    return parser.parse_args()

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

def zapisz_json(nazwa_pliku, dane):
    try:
        with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
            json.dump(dane, plik, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Błąd zapisu do pliku '{nazwa_pliku}': {e}")

if __name__ == "__main__":
    args = parsuj_argumenty()
    dane = wczytaj_json(args.plik_wejscie)
    if dane:
        print(dane)
        zapisz_json(args.plik_wyjscie, dane)




# import argparse
# import json

# def parsuj_argumenty():
#     parser = argparse.ArgumentParser(description='Opis programu')
#     parser.add_argument('plik_wejscie', type=str, help='Ścieżka do pliku wejściowego')
#     parser.add_argument('plik_wyjscie', type=str, help='Ścieżka do pliku wyjściowego')
#     return parser.parse_args()

# if __name__ == "__main__":
#     args = parsuj_argumenty()
#     print(f'Plik wejściowy: {args.plik_wejscie}, Plik wyjściowy: {args.plik_wyjscie}')






# def wczytaj_json(nazwa_pliku):
#     try:
#         with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
#             dane = json.load(plik)
#         return dane
#     except FileNotFoundError:
#         print(f"Plik '{nazwa_pliku}' nie istnieje.")
#         return None
#     except json.JSONDecodeError as e:
#         print(f"Błąd dekodowania JSON w pliku '{nazwa_pliku}': {e}")
#         return None
    


# dane = wczytaj_json('file.json')
# if dane:
#     print(dane)






# def zapisz_json(nazwa_pliku, dane):
#     try:
#         with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
#             json.dump(dane, plik, ensure_ascii=False, indent=4)
#     except IOError as e:
#         print(f"Błąd zapisu do pliku '{nazwa_pliku}': {e}")
