# Zadanie 4.5 — zamiana liczby punktów na ocenę końcową.

def pts_to_grade(points):
    # Sprawdzamy progi od najwyższego do najniższego.
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    return grade  # Zwracamy nazwę oceny.

# Wartość testowa odpowiada przykładowi z materiału.
test_result = 15
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')
