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
jest_przestepny = rok_przestepny(2024)
if jest_przestepny:
   print("Jest przestepny")
else:
   print("Nie jest przestepny")

def ilosc_dni(rok, miesiac):
    komunikat = ""
    if rok_przestepny(2024) == True:
        if miesiac in [1, 3, 5, 7, 8, 10, 12]:
            komunikat = print("Ten miesiac ma 31 dni")
        elif miesiac == 2:
            komunikat = print("Ten miesiac ma 29 dni")
        else:
            komunikat = print("Ten miesiac ma 30 dni")

    if rok_przestepny(2024) == False:
        if miesiac == 2:
            komunikat = print("Ten miesiac ma 28 dni")
    return komunikat

ilosc_dni(2024, 2)

def ktory_dzien_roku(rok, miesiac, dzien):
    if rok not in range(1582, 4001) or miesiac not in range(1, 13) or dzien not in range(1, 32):
        return None
    elif rok_przestepny(1803) == False:
        if miesiac == 1: return dzien
        if miesiac == 2: return 31 + dzien
        if miesiac == 3: return 31 + 28 + dzien
        if miesiac == 4: return 31 + 28 + 31 + dzien
        if miesiac == 5: return 31 + 28 + 31 + 30 + dzien
        if miesiac == 6: return 31 + 28 + 31 + 30 + 31 + dzien
        if miesiac == 7: return 31 + 28 + 31 + 30 + 31 + 30 + dzien
        if miesiac == 8: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + dzien
        if miesiac == 9: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dzien
        if miesiac == 10: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dzien
        if miesiac == 11: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dzien
        if miesiac == 12: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dzien
    elif rok_przestepny(1803) == True:
        if miesiac == 1: return dzien
        if miesiac == 2: return 31 + dzien + 1
        if miesiac == 3: return 31 + 28 + dzien + 1
        if miesiac == 4: return 31 + 28 + 31 + dzien + 1
        if miesiac == 5: return 31 + 28 + 31 + 30 + dzien + 1
        if miesiac == 6: return 31 + 28 + 31 + 30 + 31 + dzien + 1
        if miesiac == 7: return 31 + 28 + 31 + 30 + 31 + 30 + dzien + 1
        if miesiac == 8: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + dzien + 1
        if miesiac == 9: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dzien + 1
        if miesiac == 10: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dzien + 1
        if miesiac == 11: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dzien + 1
        if miesiac == 12: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dzien + 1


print("Wybrany dzień jest", ktory_dzien_roku(1803,12,31),"dniem tego roku")