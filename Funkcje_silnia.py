"""
# zadanie 3:
# napisz funkcję obliczającą silnie, funkcja przyjmuje liczbę całkowitą i oblicza silnię dla niej + wersja rekurencyjna
"""

def silnia_funkcja(liczba):
    silnia = 1
    for x in range(2, liczba + 1):
        silnia *= x
    print(silnia)

silnia_funkcja(10)

##################################

def silnia_rekurencja(liczba):
    if liczba <= 1:
        return 1
    else:
        return liczba * silnia_rekurencja(liczba - 1)

print(silnia_rekurencja(10))