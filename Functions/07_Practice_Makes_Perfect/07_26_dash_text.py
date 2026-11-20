
def add_dashes(text):
    # join() wstawia myślnik pomiędzy znaki. dla pustego napisu zwraca pusty napis.
    return '-'.join(text)


# Zadanie 7.26 — testowanie rozdzielania znaków myślnikami.
for value in ('University', 'UE', 'x', ''):
    print(f'f({value!r}) returns {add_dashes(value)!r}')
