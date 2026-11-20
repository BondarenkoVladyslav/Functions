
def sum_selected_digits(number, even):
    # Zamieniamy wartość bezwzględną na napis, aby przejść po każdej cyfrze.
    total = 0
    for character in str(abs(number)):
        digit = int(character)
        if digit % 2 == 0 and even:
            total += digit  # Dodajemy parzystą cyfrę, gdy even == True.
        elif digit % 2 != 0 and not even:
            total += digit  # Dodajemy nieparzystą cyfrę, gdy even == False.
    return total


# Zadanie 7.9 — test sumowania cyfr parzystych i nieparzystych.
for number, even in ((3124, True), (3124, False), (20576, False), (20576, True), (13115, True)):
    print(f'f({number}, {even}) returns {sum_selected_digits(number, even)}')
