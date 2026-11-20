
def min_coins(amount_to_pay):
    # Kwota musi być nieujemną liczbą całkowitą.
    if not isinstance(amount_to_pay, int) or amount_to_pay < 0:
        raise ValueError('Kwota musi być nieujemną liczbą całkowitą.')
    # Dla nominałów 5, 2 i 1 strategia zachłanna daje minimum monet.
    remaining = amount_to_pay
    number_of_coins = 0
    for coin in (5, 2, 1):
        coins_of_value = remaining // coin  # // oblicza całkowitą liczbę monet danego nominału.
        number_of_coins += coins_of_value
        remaining %= coin  # % pozostawia resztę do rozmienienia.
    return number_of_coins


# Zadanie 7.8 — sprawdzenie minimalnej liczby monet dla przykładów.
for amount in (23, 8, 2, 0):
    print(f'f({amount}) returns {min_coins(amount)}')
