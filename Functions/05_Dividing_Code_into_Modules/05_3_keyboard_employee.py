
# Program pozwala wprowadzić i wyświetlić dane pracownika.
# Ze względu na ochronę danych osobowych użytkownik decyduje,
# czy informacja o wynagrodzeniu pracownika zostanie wyświetlona.
#
import keyboard  # Importujemy nasz własny moduł (podajemy samą nazwę, bez rozszerzenia .py)

# Wczytujemy dane pracownika z klawiatury za pomocą funkcji z modułu keyboard
first_name = keyboard.input_string('Enter name: ')                 # Wczytanie imienia (tekst)
last_name = keyboard.input_string('Enter last name: ')             # Wczytanie nazwiska (tekst)
age = keyboard.input_integer('Enter age: ')                        # Wczytanie wieku (liczba całkowita)
salary = keyboard.input_real('Enter salary: ')                     # Wczytanie pensji (liczba rzeczywista)
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n): ')  # Decyzja o ukryciu pensji (True/False)

# Wyświetlamy sformatowaną kartę danych pracownika
print('DATA RECORD')
print('===========')
print('Name:', first_name)         # Wyświetlenie imienia
print('Last name:', last_name)     # Wyświetlenie nazwiska
print('Age:', age)                 # Wyświetlenie wieku

# Sprawdzamy, czy pensja ma pozostać ukryta; jeśli nie (not True), wyświetlamy ją
if not is_salary_hidden:
    print('Salary:', salary)