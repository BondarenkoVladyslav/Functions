# Zadanie 7.31 — obliczanie potęgi za pomocą rekurencji.
def power(x, n):
    # Przypadek bazowy: każda liczba podniesiona do potęgi 0 daje 1.
    if n == 0:
        return 1
    # Przypadek rekurencyjny: x^n = x * x^(n-1).
    return x * power(x, n - 1)

# Obliczamy 5 do potęgi 3, zgodnie z poleceniem.
print('5^3 =', power(5, 3))
