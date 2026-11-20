def f(dice):
    # Zapamiętujemy najdłuższą serię takich samych rzutów oraz liczbę oczek z tej serii
    max_count = 1
    max_digit = int(dice[0])

    # Licznik aktualnej serii powtarzających się rzutów
    current_count = 1

    # Przechodzimy przez kolejne rzuty, zaczynając od drugiego znaku (indeks 1)
    for i in range(1, len(dice)):
        # Jeśli obecny rzut jest taki sam jak poprzedni, przedłużamy serię
        if dice[i] == dice[i - 1]:
            current_count += 1
            # Jeśli obecna seria jest dłuższa niż dotychczasowy rekord, aktualizujemy wynik
            if current_count > max_count:
                max_count = current_count
                max_digit = int(dice[i])
        else:
            # Jeśli wypadła inna liczba oczek, resetujemy licznik serii do 1
            current_count = 1

    # Zwracamy liczbę oczek, która wypadła najwięcej razy z rzędu
    return max_digit

for dice in ('5233165554211', '2133'):
    print(f'f({dice!r}) returns {f(dice)}')