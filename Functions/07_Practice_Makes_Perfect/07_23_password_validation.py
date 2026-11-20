
def is_valid_password(password):
    # Hasło musi mieć minimum 6 znaków.
    # set() usuwa powtórzenia; równa długość oznacza brak duplikatów.
    return len(password) >= 6 and len(set(password)) == len(password)


# Zadanie 7.23 — testowanie haseł z polecenia.
for password in ('ax15', 'book123', 'A2water3', 'qwerty', ''):
    print(f'f({password!r}) returns {is_valid_password(password)}')
