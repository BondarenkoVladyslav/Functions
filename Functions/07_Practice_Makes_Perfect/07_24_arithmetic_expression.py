def f(expression):
    # Pobieramy pierwszą cyfrę z wyrażenia i zamieniamy ją ze znaku (str) na liczbę całkowitą (int)
    result = int(expression[0])

    # Iterujemy po pozostałych znakach co 2 pozycje (krok = 2), ponieważ na zmianę występują operator i cyfra
    for i in range(1, len(expression), 2):
        # Pobieramy operator ('+' lub '-') znajdujący się pod bieżącym indeksem
        operator = expression[i]
        # Pobieramy kolejną cyfrę stojącą za operatorem i konwertujemy ją na int
        digit = int(expression[i + 1])

        # W zależności od operatora dodajemy lub odejmujemy cyfrę od wyniku końcowego
        if operator == '+':
            result += digit
        elif operator == '-':
            result -= digit

    # Zwracamy obliczoną wartość całego wyrażenia
    return result

print(f'f("2+3") returns {f("2+3")}')
print(f'f("3+8+1") returns {f("3+8+1")}')
print(f'f("2+3-4+5-0") returns {f("2+3-4+5-0")}')