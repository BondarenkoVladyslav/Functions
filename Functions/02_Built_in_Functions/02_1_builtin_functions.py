# Zadanie 2.1 — zastosowanie wbudowanych funkcji Pythona.
# max() znajduje największą wartość spośród argumentów.
max_number = max(7, 5, 6, 3, 8, 2)
print('Max number of 7,5,6,3,8,2 is', max_number)

# min() znajduje najmniejszą wartość spośród argumentów.
min_number = min(4, 7, 2, 3, 9, 8)
print('Min number of 4,7,2,3,9,8 is', min_number)

# len() zwraca liczbę znaków w napisie, łącznie ze spacją.
str_length = len('computer science')
print('The number of characters in "computer science" is', str_length)

# input() pobiera tekst wpisany przez użytkownika.
letter = input('Enter a letter: ')
print('The entered letter is', letter)

# int() zamienia napis z cyframi na liczbę całkowitą.
number = int('20303')
print('Integer representing the string "20303" is', number)

# bin() zwraca napis z reprezentacją liczby w systemie binarnym.
binary_number = bin(304)
print('Binary string representing decimal number 304 is', binary_number)

# hex() zwraca napis z reprezentacją liczby w systemie szesnastkowym.
hexadecimal_number = hex(304)
print('Hexadecimal string representing decimal number 304 is', hexadecimal_number)

# ord() zwraca kod Unicode pojedynczego znaku.
euro_code = ord('€')
print('Unicode code of the € sign is', euro_code)

# abs() zwraca wartość bezwzględną liczby.
absolute_value = abs(-17)
print('Absolute value of -17 is', absolute_value)
