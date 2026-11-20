# Zadanie 4.2 — przykład definiowania i wywoływania własnej funkcji.

def add(a, b):
    # def rozpoczyna definicję funkcji, a i b to jej parametry.
    result = a + b  # Obliczamy sumę dwóch przekazanych argumentów.
    return result   # return przekazuje wynik z funkcji do miejsca wywołania.

# Wywołujemy funkcję z argumentami 5 i 3.
sum_value = add(5, 3)
print(sum_value)  # Wynik: 8.
