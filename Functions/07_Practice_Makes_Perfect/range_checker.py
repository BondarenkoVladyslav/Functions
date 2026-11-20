# Definiujemy funkcję sprawdzającą, czy liczba (number) mieści się w domkniętym przedziale <x, y>
def in_range(number, x, y):
    # Zwracamy wartość logiczną (True lub False) w zależności od spełnienia warunku
    return x <= number <= y


# Blok testowy - wykona się tylko przy bezpośrednim uruchomieniu tego modułu
if __name__ == "__main__":
    print(in_range(7, 2, 15))