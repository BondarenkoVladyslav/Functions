
def at_least_three_people(detector):
    # Znak + oznacza wejście, a - oznacza wyjście.
    people_inside = 0
    maximum_inside = 0
    for event in detector:
        if event == '+':
            people_inside += 1
            maximum_inside = max(maximum_inside, people_inside)
        elif event == '-':
            people_inside -= 1
            if people_inside < 0:
                raise ValueError('Więcej wyjść niż wejść w danych detektora.')
        else:
            raise ValueError('Dozwolone są wyłącznie znaki + i -.')
    return maximum_inside >= 3


# Zadanie 7.15 — sprawdzenie czterech sekwencji wejść i wyjść.
for sequence in ('+-+++-+---', '+-+-+-+-', '+-++-+--', '+-++-++-+---'):
    print(f'f({sequence!r}) returns {at_least_three_people(sequence)}')
