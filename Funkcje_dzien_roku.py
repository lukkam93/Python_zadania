"""
zadanie 1:
dzień roku
napisz funkcję który jako parametr przyjmie rok i zwróci informację czy rok ten jest przestępny czy nie

dodaj funkcję która jako parametr przyjmuje rok i miesiąc, a jako wynik zwraca informację ile dni jest w danym miesiącu

napisz funkcję która przyjmuje trzy parametry - rok, miesiąc i dzień, sprawdzi czy wprowadzone dane są poprawne,
jeżeli nie zwróci wartość None, jeżeli są poprawne zwróci informację który to dzień roku
"""

def rok_przestepny(rok):
    if rok % 4 == 0:
        if rok % 400 == 0 or rok % 100 != 0:
            return True
    else:
        return False
jest_przestepny = rok_przestepny(2020)
if jest_przestepny:
   print("Jest przestepny")
else:
   print("Nie jest przestepny")

def ilosc_dni(rok, miesiac):
    if rok_przestepny(2020) == True:
        if miesiac in [1, 3, 5, 7, 8, 10, 12]:
            print("Ten miesiac ma 31 dni")
        elif miesiac == 2:
            print("Ten miesiac ma 29 dni")
        else:
            print("Ten miesiac ma 30 dni")
    if rok_przestepny(2020) == False:
        if miesiac in [1, 3, 5, 7, 8, 10, 12]:
            print("Ten miesiac ma 31 dni")
        elif miesiac == 2:
            print("Ten miesiac ma 28 dni")
        else:
            print("Ten miesiac ma 30 dni")

ilosc_dni(2020, 12)


#trzecia czesc zadania