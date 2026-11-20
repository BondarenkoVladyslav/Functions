# Zadanie 4.4 — suma cyfr liczby dodatniej, ujemnej lub zera.

def sum_digits(number):
    # abs() usuwa znak minus; suma cyfr liczby ujemnej jest taka sama.
    digits = str(abs(number))  # str() zamienia liczbę na napis, po którym można iterować.
    total = 0  # Zmienna przechowuje dotychczasową sumę cyfr.
    for digit in digits:
        total += int(digit)  # int() zamienia pojedynczy znak-cyfrę na liczbę.
    return total  # Zwracamy obliczoną sumę.

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
