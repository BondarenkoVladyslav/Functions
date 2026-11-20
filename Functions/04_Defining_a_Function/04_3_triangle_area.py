# Zadanie 4.3 — pole trójkąta obliczone ze wzoru Herona.
import math  # math.sqrt() jest potrzebne do obliczenia pierwiastka.

def triangle_area(a, b, c):
    # Funkcja otrzymuje długości trzech boków trójkąta.
    # Sprawdzamy nierówności trójkąta, aby boki mogły utworzyć trójkąt.
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Długości boków muszą być dodatnie.')
    if a + b <= c or a + c <= b or b + c <= a: #suma dwóch stron ma być większa of trzeciej
        raise ValueError('Podane boki nie tworzą trójkąta.')
    semi_perimeter = (a + b + c) / 2  # Obliczamy połowę obwodu, czyli p.
    area = math.sqrt(
        semi_perimeter #formula pola trójkąta
        * (semi_perimeter - a)
        * (semi_perimeter - b)
        * (semi_perimeter - c)
    )  # Wzór Herona: sqrt(p(p-a)(p-b)(p-c)).
    return area  # Zwracamy pole trójkąta.

# Pobieramy trzy boki z klawiatury; float pozwala także na wartości dziesiętne.
a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
print(f'The area of a triangle with sides {a}, {b}, {c} is {triangle_area(a, b, c):.2f}')

# Sprawdzamy trzy zestawy danych podane w poleceniu.
for sides in [(3, 4, 5), (5, 12, 13), (7, 24, 25)]:
    print(f'Sides {sides}: area = {triangle_area(*sides):.2f}')
