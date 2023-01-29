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

def wielkosc_liter():
    a = zdanie_uzytkownika.islower()
    if a == False:
        print("Zdanie posiada wielkie litery")
    else:
        print("Zdanie nie posiada wielkich liter")

def sprawdzanie_cyfr():
    pusty_string = ""
    for c in zdanie_uzytkownika:
        if c.isdigit():
            pusty_string +=c
    if pusty_string != "":
        print("Są cyfry")
    else:
        print("Nie ma cyfr")

def znaki_specjalne():
    if "$" in zdanie_uzytkownika:
        print("Znak specjalny")
    elif "#" in zdanie_uzytkownika:
        print("Znak specjalny")
    elif "@" in zdanie_uzytkownika:
        print("Znak specjalny")
    else:
        print("Nie ma znaków specjalnych")

def dlugosc_zdania():
    if len(zdanie_uzytkownika) < 6:
        print("Twoje zdanie ma mniej niz 6 znaków")
    if len(zdanie_uzytkownika) > 12:
        print("Twoje zdanie ma więcej niż 12 znaków")

wielkosc_liter()
sprawdzanie_cyfr()
znaki_specjalne()
dlugosc_zdania()