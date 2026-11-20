# Moduł zawierający funkcje do przeliczania jednostek długości.

def m_to_cm(n):
    # Przelicza metry na centymetry (1 m = 100 cm).
    return n * 100


def cm_to_m(n):
    # Przelicza centymetry na metry.
    return n / 100


def cm_to_inch(n):
    # Przelicza centymetry na cale (1 cal = 2.54 cm).
    return n / 2.54


def feet_inches_to_cm(feet, inches):
    # Przelicza stopy i cale na centymetry (1 stopa = 12 cali, 1 cal = 2.54 cm).
    total_inches = feet * 12 + inches
    return total_inches * 2.54