def sum_repeated_digits(number):
    # Zliczamy częstotliwość każdej cyfry w wartości bezwzględnej liczby.
    # Zamieniamy wartość bezwzględną liczby na tekst, a następnie każdy znak z powrotem na liczbę całkowitą (int)
    # i zapisujemy na liście.
    digits = [int(character) for character in str(abs(number))]
    total = 0  # Zmienna przechowująca sumę
    for digit in digits:  # Przechodzimy po kolei przez każdą cyfrę z listy
        if digits.count(digit) > 1:  # Sprawdzamy, czy cyfra pojawia się na liście więcej niż raz
            total += digit  # Dodajemy każde wystąpienie powtarzającej się cyfry.
    return total  # Zwracamy ostateczny wynik (sumę)


# Zadanie 7.19 — sprawdzenie sumy powtarzających się cyfr.
for number in (1027, 230335, 513553007):  # Pętla podstawiająca kolejne liczby testowe do sprawdzenia
    print(f'f({number}) returns {sum_repeated_digits(number)}')  # Wywołanie funkcji i wypisanie wyniku na ekran