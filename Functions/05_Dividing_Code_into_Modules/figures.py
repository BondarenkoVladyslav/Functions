# Moduł zawierający funkcje do rysowania figur geometrycznych za pomocą biblioteki turtle.

import turtle


def draw_square(length, pen=None):
    # Jeśli nie przekazano obiektu pisaka, tworzymy nowy (dla zgodności z zadaniem 5.4)
    if pen is None:
        pen = turtle.Turtle()
        pen.speed(5)

    # Rysujemy kwadrat (4 równe boki, obrót o 90 stopni)
    for i in range(4):
        pen.forward(length)
        pen.right(90)


def draw_trangle(length, pen=None):
    # Rysujemy trójkąt równoboczny (szczególny przypadek trójkąta równoramiennego)
    if pen is None:
        pen = turtle.Turtle()
        pen.speed(5)

    # 3 równe boki, obrót zewnętrzny o 120 stopni
    for i in range(3):
        pen.forward(length)
        pen.left(120)


def draw_rectangle(lenght_a, lenght_b, pen=None):
    # Rysujemy prostokąt o bokach a i b
    if pen is None:
        pen = turtle.Turtle()
        pen.speed(5)

    # Dwie pary boków o długościach a oraz b
    for i in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)