"""
# zadanie 2:
# napisz funkcję która sprawdzi czy liczba jest pierwsza i zwróci wartość True lub False
"""

def liczby_pierwsze(liczba):
    for i in range(2, liczba):
        if liczba % i ==0:
            return False
    return True

print(liczby_pierwsze(2137))