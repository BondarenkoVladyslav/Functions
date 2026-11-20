# Zadanie 7.29 — silnia obliczana rekurencyjnie.
def factorial(n):
    # Przypadki bazowe: 0! i 1! są równe 1; zatrzymują rekurencję.
    if n < 0:
        raise ValueError('Silnia jest określona dla n >= 0.')
    if n == 0 or n == 1:
        return 1
    # Przypadek rekurencyjny: n! = n * (n-1)!.
    return n * factorial(n - 1)

# Obliczamy silnię dla n = 5, zgodnie z poleceniem.
print('5! =', factorial(5))
