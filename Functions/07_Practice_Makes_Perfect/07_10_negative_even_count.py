
def count_negative_even(x, y):
    # Zakres <x, y> obejmuje obie granice; min/max obsługują też odwrotną kolejność.
    start, end = min(x, y), max(x, y)
    return sum(1 for number in range(start, end + 1) if number < 0 and number % 2 == 0)


# Zadanie 7.10 — policzenie ujemnych liczb parzystych w podanych zakresach.
for x, y in ((-7, 8), (-1, 11)):
    print(f'f({x}, {y}) returns {count_negative_even(x, y)}')
