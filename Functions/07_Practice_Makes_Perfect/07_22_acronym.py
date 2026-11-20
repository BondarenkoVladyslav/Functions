
def acronym(name):
    # split() dzieli tekst na słowa, pomijając wielokrotne spacje.
    words = name.split()
    return ''.join(word[0] for word in words)  # Pobieramy pierwszą literę (indeks 0) każdego słowa i łączymy je w jeden ciąg znaków.


# Zadanie 7.22 — tworzenie akronimów dla przykładów.
for phrase in ('Internet of Things', 'For Your Information', 'Python'):
    print(f'f({phrase!r}) returns {acronym(phrase)!r}')  #!r wyświetla wartość w cudzysłowie
