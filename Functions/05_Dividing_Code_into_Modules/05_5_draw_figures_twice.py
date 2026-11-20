# Definiujemy funkcję zwracającą nazwę miesiąca na podstawie jego numeru (1-12)
def month(n):
    # Lista przechowująca nazwy wszystkich 12 miesięcy po angielsku
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    # Sprawdzamy, czy podany numer mieści się w poprawnym zakresie od 1 do 12
    if 1 <= n <= 12:
        # Zwracamy nazwę miesiąca (odejmujemy 1, ponieważ indeksowanie listy zaczyna się od 0)
        return months[n - 1]
    # Jeśli liczba jest spoza zakresu 1-12, zwracamy komunikat o błędzie
    return "Invalid month number"


# Blok testowy - uruchomi się tylko wtedy, gdy włączysz bezpośrednio ten plik
if __name__ == "__main__":
    # Testujemy funkcję dla miesiąca nr 7 (July)
    print(month(7))