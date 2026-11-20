# Importujemy moduł z funkcją sprawdzającą przedział liczbowy
import range_checker


# Główna funkcja programu
def main():
    # Ustalamy dolną i górną granicę przedziału zgodnie z przykładem <2, 15>
    x = 2
    y = 15
    # Pobieramy liczbę od użytkownika i konwertujemy ją na typ całkowity (int)
    number = int(input("A number: "))
    # Wywołujemy funkcję z modułu; jeśli zwróci True, przypisujemy "yes", w przeciwnym razie "no"
    answer = "yes" if range_checker.in_range(number, x, y) else "no"
    # Wyświetlamy końcowy komunikat zgodny z przykładowym wynikiem
    print(f"Number {number} in the range <{x},{y}>: {answer}")


# Punkt startowy programu
if __name__ == "__main__":
    main()