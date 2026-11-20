
def max_min_difference(number1, number2, number3):
    # max() wybiera największą, a min() najmniejszą wartość.
    return max(number1, number2, number3) - min(number1, number2, number3)


# Zadanie 7.21 — testowanie różnicy największej i najmniejszej liczby.
for values in ((7, 4, 9), (2, 12, 8)):
    print(f'f{values} returns {max_min_difference(*values)}')
