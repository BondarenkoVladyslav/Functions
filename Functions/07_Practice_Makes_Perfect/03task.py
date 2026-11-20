# Importujemy nasz własny moduł z funkcją month()
import month_module


# Główna funkcja programu
def main():
    # Pobieramy numer miesiąca od użytkownika i zamieniamy tekst na liczbę całkowitą (int)
    # Wpisz 7, aby sprawdzić 7. miesiąc z polecenia, lub 9, aby uzyskać wynik z przykładu
    n = int(input("Enter month number: "))
    # Wywołujemy funkcję month() z zaimportowanego modułu i zapisujemy wynik
    name = month_module.month(n)
    # Wyświetlamy wynik w formacie zgodnym z treścią zadania
    print(f"The name of month {n} is {name}")


# Punkt startowy programu - uruchamia funkcję main() przy bezpośrednim starcie skryptu
if __name__ == "__main__":
    main()