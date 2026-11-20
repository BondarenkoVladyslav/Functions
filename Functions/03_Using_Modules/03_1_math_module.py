# Zadanie 3.1 — wykorzystanie funkcji i stałych z modułu math.
# import math udostępnia funkcje matematyczne z biblioteki standardowej.
import math

# sqrt() oblicza pierwiastek kwadratowy.
square_root = math.sqrt(7)
print('A square root of 7 is', square_root)

# log() bez drugiego argumentu oblicza logarytm naturalny.
natural_logarithm = math.log(5)
print('The natural logarithm of 5 is', natural_logarithm)

# sin() przyjmuje kąt w radianach, dlatego 90 stopni zamieniamy przez radians().
sine_90 = math.sin(math.radians(90))
print('The sine of 90 degrees is', sine_90)
