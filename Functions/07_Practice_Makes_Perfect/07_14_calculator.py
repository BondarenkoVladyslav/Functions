
def calculate(number1, number2, operator):
    # Dobieramy działanie do tekstowego symbolu operatora.
    if operator == '+':
        return number1 + number2
    if operator == '-':
        return number1 - number2
    if operator == '*':
        return number1 * number2
    if operator == '%':
        if number2 == 0:
            raise ZeroDivisionError('Nie można obliczyć reszty z dzielenia przez zero.')
        return number1 % number2
    if operator == '**':
        return number1 ** number2
    raise ValueError('Nieobsługiwany operator.')


# Zadanie 7.14 — testowanie dozwolonych operatorów.
for operator in ('+', '%', '**', '*', '-'):
    print(f'f(2, 3, {operator!r}) returns {calculate(2, 3, operator)}')
