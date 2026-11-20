# Zadanie 4.6 — zwracanie nazwy dnia tygodnia na podstawie numeru.

def day_name(day_number):
    # Słownik łączy numer dnia z jego angielską nazwą.
    days = {
        1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
        4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'
    }
    return days.get(day_number, 'Invalid day number')  # get() szuka w słowniku słowo day_number i zwraca nazwę dnia,
    # a jeśli takiej liczby tam nie ma zwróci 'Invalid day number'

# Pobieramy numer dnia od użytkownika i zamieniamy tekst na liczbę całkowitą (int).
day = int(input('Enter day number: '))

# Wywołujemy funkcję i zapisujemy wynik w zmiennej result.
result = day_name(day)

# Sprawdzamy, czy funkcja zwróciła komunikat o błędzie, czy poprawną nazwę dnia.
if result == 'Invalid day number':
    print('Invalid day number')  # Wyświetlamy sam komunikat błędu bez reszty zdania.
else:
    print(f'The name of day {day} in the week is {result}')  # Wyświetlamy pełne zdanie z nazwą dnia.