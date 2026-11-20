
def remove_spaces(sentence):
    # replace(' ', '') usuwa zwykłe spacje i pozostawia pozostałe znaki.
    return sentence.replace(' ', '')


# Zadanie 7.18 — usuwanie spacji z przykładowych zdań.
examples = (
    'integrated development environment',
    'A programming language is a system of notation for writing computer programs'
)
for sentence in examples:
    print(remove_spaces(sentence))
