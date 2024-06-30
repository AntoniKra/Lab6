import argparse

def main():
    parser = argparse.ArgumentParser(description="Program do konwersji danych")
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego')
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    print(f'Plik wejściowy: {input_file}')
    print(f'Plik wyjściowy: {output_file}')

if __name__ == "__main__":
    main()