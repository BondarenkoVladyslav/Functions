def is_prime(number):
    if number < 2:
        return False
    # Dzielniki sprawdzamy tylko do pierwiastka z liczby, ponieważ występują parami.
    for divisor in range(2, int(number ** 0.5) + 1):  #range działa tylko z int
        if number % divisor == 0:
            return False
    return True


def nth_prime(n):
    if n < 1:
        raise ValueError('n musi być dodatnie.')
    found = 0      # Licznik znalezionych liczb pierwszych.
    candidate = 1  # Startujemy od 1, aby pierwszą badaną liczbą w pętli było 2.
    # Sprawdzamy kolejne liczby naturalne, dopóki nie znajdziemy n liczb pierwszych.
    while found < n:
        candidate += 1
        if is_prime(candidate):
            found += 1
    return candidate


# Zadanie 7.20 — wyznaczenie 1 i 5. liczby pierwszej.
for n in (1, 5):
    print(f'f({n}) returns {nth_prime(n)}')