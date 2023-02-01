"""
zadanie 1:
dzień roku
napisz funkcję który jako parametr przyjmie rok i zwróci informację czy rok ten jest przestępny czy nie

dodaj funkcję która jako parametr przyjmuje rok i miesiąc, a jako wynik zwraca informację ile dni jest w danym miesiącu

napisz funkcję która przyjmuje trzy parametry - rok, miesiąc i dzień, sprawdzi czy wprowadzone dane są poprawne,
jeżeli nie zwróci wartość None, jeżeli są poprawne zwróci informację który to dzień roku
"""

def rok_przestepny(rok):
    if rok % 400 == 0 or (rok % 4 == 0 and rok % 100 !=0):
        return True
    else:
        return False
jest_przestepny = rok_przestepny(2023)
if jest_przestepny:
   print("Jest przestepny")
else:
   print("Nie jest przestepny")

def ilosc_dni(rok, miesiac):
    komunikat = ""
    if rok_przestepny(2023) == True:
        if miesiac in [1, 3, 5, 7, 8, 10, 12]:
            komunikat = print("Ten miesiac ma 31 dni")
        elif miesiac == 2:
            komunikat = print("Ten miesiac ma 29 dni")
        else:
            komunikat = print("Ten miesiac ma 30 dni")

    if rok_przestepny(2023) == False:
        if miesiac == 2:
            komunikat = print("Ten miesiac ma 28 dni")
    return komunikat

ilosc_dni(2023, 2)

#trzecia czesc zadania
# napisz funkcję która przyjmuje trzy parametry - rok, miesiąc i dzień, sprawdzi czy wprowadzone dane są poprawne,
# jeżeli nie zwróci wartość None, jeżeli są poprawne zwróci informację który to dzień roku

#jak obliczyć, który to dzień roku?

def ktory_dzien_roku(rok, miesiac, dzien):
    if rok_przestepny(2022) == True:
        rok_dni = 365
    else:
        rok_dni = 366
        if rok not in range(1582,4001) or miesiac not in range(1,13) or dzien not in range(1,32):
            return None
        else:
            dzien_roku = print("Jest git")
        return dzien_roku

ktory_dzien_roku(2022,12,30)