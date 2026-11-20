# Zadanie 4.8 — formatowanie czasu w formacie 24- lub 12-godzinnym.

def time_string(hours, minutes, time_format):
    # Sprawdzamy, czy godziny i minuty mieszczą się w dozwolonych zakresach.
    if not 0 <= hours <= 23 or not 0 <= minutes <= 59:
        raise ValueError('Godzina lub minuta jest poza zakresem.')
    if time_format == '24':
        return f'{hours:02d}:{minutes:02d}'  # :02d dodaje zero z lewej strony.
    if time_format == '12':
        suffix = 'am' if hours < 12 else 'pm'  # Przed południem am, od południa pm.
        hour_12 = hours % 12  # 0 i 12 zamieniamy na 12 w zapisie 12-godzinnym.
        if hour_12 == 0:
            hour_12 = 12
        return f'{hour_12}:{minutes:02d}{suffix}'
    raise ValueError("Format musi mieć wartość '24' albo '12'.")

h = int(input('Podaj godzinę (0-23): '))
m = int(input('Podaj minuty (0-59): '))
fmt = input("Podaj format ('24' lub '12'): ").strip()

print(time_string(h, m, fmt))
