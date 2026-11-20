
def has_negative(n1, n2, n3):
    # or zwraca True, gdy przynajmniej jeden warunek jest prawdziwy.
    return n1 < 0 or n2 < 0 or n3 < 0

# Zadanie 7.11 — testowanie funkcji sprawdzającej trzy liczby. Zwraca True jeśli jest jemne znaczenie i False jeśli dodatnie
for values in ((11, 6, -4), (5, 4, 14)):
    print(f'f{values} returns {has_negative(*values)}')
