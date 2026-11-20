# Zadanie 7.3 — samodzielny plik z całym kodem zadania.
# Funkcje, które w wersji modułowej znajdowałyby się w osobnym module,
# są umieszczone tutaj razem z częścią testową, aby uruchamiać jedno zadanie
# z jednego pliku .py. Komentarze wyjaśniają działanie kolejnych elementów.
# Funkcja wymagana w ćwiczeniu i przykładowe wywołania są razem w jednym pliku .py.

# ===== DEFINICJE FUNKCJI =====
MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

def month(n):
    # Numery miesięcy zaczynają się od 1, indeksy listy od 0.
    if 1 <= n <= 12:
        return MONTHS[n - 1]
    return 'Invalid month number'

# ===== CZĘŚĆ TESTOWA / URUCHOMIENIOWA =====
# Zadanie 7.3 — wywołanie funkcji month() zdefiniowanej wyżej.

month_number = int(input('Enter month number: '))
print(f'The name of month {month_number} is {month(month_number)}')
