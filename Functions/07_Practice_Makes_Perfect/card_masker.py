# Definiujemy funkcję maskującą numer karty (widoczne zostają tylko 2 pierwsze i 4 ostatnie cyfry)
def hide(card_number):
    # Zamieniamy numer karty na ciąg znaków (str), aby móc wycinać jego fragmenty
    card_str = str(card_number)
    # Tworzymy ciąg gwiazdek o długości odpowiadającej liczbie ukrytych środkowych cyfr (16 - 6 = 10)
    masked_middle = "*" * (len(card_str) - 6)
    # Łączymy: pierwsze 2 znaki + gwiazdki + ostatnie 4 znaki i zwracamy wynik
    return card_str[:2] + masked_middle + card_str[-4:]


# Blok testowy - zadziała tylko przy bezpośrednim uruchomieniu tego pliku
if __name__ == "__main__":
    print(hide("5290312400019022"))