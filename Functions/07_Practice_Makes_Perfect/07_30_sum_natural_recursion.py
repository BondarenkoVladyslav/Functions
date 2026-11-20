# Zadanie 7.30 — rekurencyjna suma liczb naturalnych od 1 do n.
def sum_natural(n):
    # Przypadek bazowy: suma do zera wynosi zero.
    if n <= 0:
        return 0
    # Przypadek rekurencyjny: n + suma liczb od 1 do n-1.
    return n + sum_natural(n - 1)

# Obliczamy sumę w zakresie <1, 10>.
print('Sum from 1 to 10:', sum_natural(10))
