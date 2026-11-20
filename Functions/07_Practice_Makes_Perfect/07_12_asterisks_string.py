
def asterisks(n):
    # Dla n mniejszego od zera nie można utworzyć wymaganej liczby gwiazdek.
    if n < 0:
        raise ValueError('n nie może być ujemne.')
    return '/'.join('*' for i in range(n))  # join() wstawia ukośnik między gwiazdki.


# Zadanie 7.12 — przykłady tworzenia napisu z gwiazdek.
for n in (4, 1):
    print(f'f({n}) returns {asterisks(n)!r}') #!r dodaje cudzysłowy
