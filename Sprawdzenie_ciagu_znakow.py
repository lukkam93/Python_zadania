"""
Napisać program program sprawdzający czy podany przez użytkownik ciąg znaków zawiera
małe litery
duże litery
cyfry
jeden ze znaków $#@
minimum 6 znaków
maksimum 12 znaków
"""

zdanie_uzytkownika = input("Wpisz swoje zdanie: ")

def wielkosc_liter(zdanie):
    a = zdanie_uzytkownika.islower()
    if a == False:
        komunikat = "Zdanie posiada wielkie litery"
    else:
        komunikat = "Zdanie nie posiada wielkich liter"
    return komunikat

def sprawdzanie_cyfr(zdanie):
    pusty_string = ""
    for c in zdanie_uzytkownika:
        if c.isdigit():
            pusty_string +=c
    if pusty_string != "":
        komunikat = "Zdanie posiada cyfry"
    else:
        komunikat = "Zdanie nie posiada cyfr"
    return komunikat

def znaki_specjalne(zdanie):
    if "$" in zdanie_uzytkownika:
        komunikat = "Zdanie posiada znak specjalny"
    elif "#" in zdanie_uzytkownika:
        komunikat = "Zdanie posiada znak specjalny"
    elif "@" in zdanie_uzytkownika:
        komunikat = "Zdanie posiada znak specjalny"
    else:
        komunikat = "Nie posiada znaków specjalnych"
    return komunikat

def dlugosc_zdania(zdanie):
    if len(zdanie_uzytkownika) < 6:
        komunikat = "Zdanie posiada mniej niz 6 znaków"
    elif len(zdanie_uzytkownika) > 12:
        komunikat = "Zdanie posiada więcej niż 12 znaków"
    return komunikat

print(wielkosc_liter(zdanie = zdanie_uzytkownika))
print(sprawdzanie_cyfr(zdanie = zdanie_uzytkownika))
print(znaki_specjalne(zdanie = zdanie_uzytkownika))
print(dlugosc_zdania(zdanie = zdanie_uzytkownika))