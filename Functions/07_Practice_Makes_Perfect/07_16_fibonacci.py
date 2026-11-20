#Она начинается с 0 и 1, а каждое следующее число это просто сумма двух предыдущих:
#0, 1, 1 (0+1), 2 (1+1), 3 (1+2), 5 (2+3), 8 (3+5), 13 (5+8), 21 (8+13)...
def fibonacci(n):
    # W numeracji zadania pierwszy wyraz (n=1) to 0, drugi (n=2) to 1.
    if n < 1:
        raise ValueError('Numer wyrazu n musi być większy lub równy 1.')
    previous, current = 0, 1
    for i in range(n - 1):
        previous, current = current, previous + current
    return previous


# Zadanie 7.16 — wyznaczanie piątego i dziewiątego wyrazu ciągu.
for n in (5, 9):
    print(f'f({n}) returns {fibonacci(n)}')
