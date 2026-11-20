# Importujemy moduł zawierający funkcję do obliczania liczby liter
import letter_counter


# Główna funkcja programu
def main():
    # Tekst podany w przykładzie do zadania
    text = "You never get a second chance to make a first impression"
    # Litera, którą chcemy policzyć w tekście
    letter = "e"
    # Wywołujemy funkcję z modułu letter_counter i zapisujemy wynik w zmiennej total
    total = letter_counter.count_letter(text, letter)
    # Wyświetlamy analizowany tekst
    print(text)
    # Wyświetlamy wynik zliczenia w dokładnym formacie z przykładu
    print(f"The number of letter '{letter}': {total}")


# Uruchamiamy funkcję main() tylko wtedy, gdy ten plik jest uruchamiany bezpośrednio
if __name__ == "__main__":
    main()