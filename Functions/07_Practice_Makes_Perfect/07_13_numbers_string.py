
def numbers_to_string(n):
    if n < 0:
        raise ValueError('n nie może być ujemne.')
    # Zamieniamy liczby od 1 do n włącznie na tekst (str) i łączymy je bez separatora
    return ''.join(str(number) for number in range(1, n + 1))


# Zadanie 7.13 — testowanie funkcji dla dwóch wartości n
for n in (11, 4):
    #!r wyświetla wynik w cudzysłowie, pokazując, że zwrócony typ to str
    print(f'f({n}) returns {numbers_to_string(n)!r}')