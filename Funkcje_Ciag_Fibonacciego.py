"""
# zadanie 4:
# funkcja obliczająca ciąg fibonacciego z wykorzystaniem rekurencji
"""

def ciag_fibonacciego(liczba):
    if liczba == 0:
        return 0
    elif liczba == 1:
        return 1
    else:
        return ciag_fibonacciego(liczba - 1) + ciag_fibonacciego(liczba - 2)

print(ciag_fibonacciego(15))