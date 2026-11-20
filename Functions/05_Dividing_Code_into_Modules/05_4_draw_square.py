# Program główny rysujący kwadrat przy użyciu funkcji z własnego modułu figures.

import turtle
import figures  # Importujemy nasz własny moduł figures.py

# Konfiguracja okna graficznego
window = turtle.Screen()
window.bgcolor("lightgreen")

# Wywołanie funkcji rysującej kwadrat o boku 100 pikseli
figures.draw_square(100)

# Utrzymanie otwartego okna do momentu zamknięcia go przez użytkownika
window.mainloop()