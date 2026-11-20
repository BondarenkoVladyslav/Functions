# Importujemy moduł z funkcją hide() do maskowania numeru karty
import card_masker


# Główna funkcja programu
def main():
    # Przykładowy 16-cyfrowy numer karty kredytowej z treści zadania
    card_number = "5290312400019022"
    # Wywołujemy funkcję hide() z zaimportowanego modułu, aby zamaskować numer
    masked = card_masker.hide(card_number)
    # Wyświetlamy zamaskowany numer karty ("52**********9022")
    print(masked)


# Punkt startowy programu
if __name__ == "__main__":
    main()