# Definiujemy funkcję zliczającą, ile razy dana litera (letter) występuje w tekście (text)
def count_letter(text, letter):
    # Zmienna pomocnicza (licznik) ustawiona na początku na 0
    count = 0
    # Przechodzimy pętlą przez każdy pojedynczy znak w podanym tekście
    for char in text:
        # Sprawdzamy, czy aktualny znak jest taki sam jak szukana litera
        if char == letter:
            # Jeśli tak, zwiększamy licznik o 1
            count += 1
    # Zwracamy łączną liczbę znalezionych wystąpień
    return count


# Blok testowy wykonywany tylko przy bezpośrednim uruchomieniu modułu
if __name__ == "__main__":
    sample = "You never get a second chance to make a first impression"
    print(count_letter(sample, "e"))