def f(product_code):
    # Kod musi zawierać dokładnie cztery cyfry.
    if len(product_code) != 4 or not product_code.isdigit():
        return False

    # Sumujemy trzy pierwsze cyfry za pomocą zwykłej pętli
    digits_sum = 0
    for digit in product_code[:3]:
        digits_sum += int(digit)

    # Obliczamy resztę z dzielenia sumy przez 7 (cyfra kontrolna)
    expected_control_digit = digits_sum % 7

    # Sprawdzamy, czy czwarta cyfra zgadza się z cyfrą kontrolną
    return int(product_code[3]) == expected_control_digit

# Zadanie 7.27 testowanie kodów produktów podanych w poleceniu.
for code in ('1082', '2035', '1114', '7071'):
    print(f'f({code!r}) returns {f(code)}')