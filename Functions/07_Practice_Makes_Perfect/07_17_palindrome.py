
def is_palindrome(palindrome):
    # [::-1] tworzy napis od końca do początku.
    return palindrome == palindrome[::-1]


# Zadanie 7.17 — testowanie palindromów z polecenia.
for value in ('radar', '12-11-21', 'book'):
    print(f'f({value!r}) returns {is_palindrome(value)}')
