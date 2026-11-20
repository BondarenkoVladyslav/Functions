
def is_binary(binary_number):
    # Pusty napis nie jest liczbą binarną; każdy znak musi być 0 albo 1.
    return bool(binary_number) and all(character in '01' for character in binary_number)

# Zadanie 7.7 — testowanie poprawności zapisu binarnego.
for value in ('101101', '1311a10100'):
    print(f'f({value!r}) returns {is_binary(value)}')
