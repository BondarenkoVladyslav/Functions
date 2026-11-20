###
# Moduł zawierający własne funkcje do wczytywania różnych typów danych z klawiatury.
def input_string(message):
    # Wczytuje dane z klawiatury i zwraca je jako zwykły tekst (typ str).
    value = input(message)
    return value
def input_integer(message):
    # Wczytuje dane z klawiatury i konwertuje je na liczbę całkowitą (typ int).
    value = int(input(message))
    return value
def input_real(message):
    # Wczytuje dane z klawiatury i konwertuje je na liczbę rzeczywistą (typ float).
    value = float(input(message))
    return value
def input_boolean(message):
    # Wczytuje odpowiedź użytkownika, usuwa zbędne spacje i zamienia literę na małą.
    # Zwraca wartość logiczną True, jeśli naciśnięto 'y', lub False w każdym innym przypadku.
    value = input(message).strip().lower()
    return value == 'y'