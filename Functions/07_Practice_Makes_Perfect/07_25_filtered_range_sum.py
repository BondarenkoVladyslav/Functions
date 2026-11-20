
def filtered_range_sum(x, y):
    # Przedział <x, y> jest domknięty. sumujemy liczby spełniające wszystkie warunki.
    start, end = min(x, y), max(x, y)
    total = 0
    for number in range(start, end + 1):
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total += number
    return total


# Zadanie 7.25 — testowanie sumy dla zakresów z polecenia.
for x, y in ((1, 20), (10, 30)):
    print(f'f({x}, {y}) returns {filtered_range_sum(x, y)}')
