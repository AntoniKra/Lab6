import argparse

def parsuj_argumenty():
    parser = argparse.ArgumentParser(description='Opis programu')
    parser.add_argument('plik_wejscie', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('plik_wyjscie', type=str, help='Ścieżka do pliku wyjściowego')
    return parser.parse_args()

if __name__ == "__main__":
    args = parsuj_argumenty()
    print(f'Plik wejściowy: {args.plik_wejscie}, Plik wyjściowy: {args.plik_wyjscie}')