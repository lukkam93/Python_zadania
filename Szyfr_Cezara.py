"""
Napisać program który będzie działał na zasadzie Szyfru Cezara
Program powinien spytać użytkownika o czynność którą chce wykonać - kodowanie / odkodowanie
Spytać o wiadomość
Spytać o punkt przesunięcia, jeżeli uzytkownik nic nie poda to przyjmie domyślną wartość - 3
Wyświetlić zakodowany / odkodowany tekst
"""

# WORK IN PROGRESS

"""
def kodowanie(wiadomosc, klucz):
    zakodowana_wiadomosc = ""
    for litera in wiadomosc:
        if ord(litera) < ord("a") or ord(litera) > ord("z"):
            zakodowana_wiadomosc += litera
        elif ord(litera) + klucz > ord("z"):
            zakodowana_wiadomosc += chr(ord(litera) + klucz - 26)
        else:
            zakodowana_wiadomosc += chr(ord(litera) + klucz)
    return zakodowana_wiadomosc

def odkodowanie(wiadomosc, klucz):
    zakodowana_wiadomosc = ""
    for litera in wiadomosc:
        if ord(litera) < ord("a") or ord(litera) > ord("z"):
            zakodowana_wiadomosc += litera
        elif ord(litera) - klucz < ord("a"):
            zakodowana_wiadomosc += chr(ord(litera) - klucz + 26)
        else:
            zakodowana_wiadomosc += chr(ord(litera) - klucz)
    return zakodowana_wiadomosc

operacja_uzytkownika = input("Wybierz operację: \nKodowanie tekstu \nOdkodowanie tekstu \nK/O?")
if operacja_uzytkownika == "K" or operacja_uzytkownika == "k":
    wiadomosc = input("Podaj wiadomość do zakodowania")
    klucz = int(input("Podaj klucz"))
#    if klucz == None:
#        klucz == 3
    print(kodowanie(wiadomosc, klucz))
    kodowanie(wiadomosc, klucz)
elif operacja_uzytkownika == "O" or operacja_uzytkownika ==  "o":
    wiadomosc = input("Podaj wiadomość do odkodowania")
    klucz = int(input("Podaj klucz"))
    print(odkodowanie(wiadomosc, klucz))
    odkodowanie(wiadomosc, klucz)
else:
    print("Podałeś nieprzewidzianą warotść")
"""

moj_alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż0123456789"
nowa_wiadomosc = ""
wiadomosc_uzytkoniwka = input("Podaj treść wiadomości")
klucz = int(input("Podaj klucz"))


def kodowanie(wiadomosc, klucz):
    for litera in wiadomosc:
        if litera in moj_alfabet:
            pozycja = moj_alfabet.find(litera)
            nowa_pozycja = (pozycja + klucz) % 74
            nowa_litera = moj_alfabet[nowa_pozycja]
            nowa_wiadomosc += nowa_litera
        else:
            nowa_wiadomosc += litera


def odkodowanie(wiadomosc, klucz):
    for litera in wiadomosc:
        if litera in moj_alfabet:
            pozycja = moj_alfabet.find(litera)
            nowa_pozycja = (pozycja - klucz) % 74
            nowa_litera = moj_alfabet[nowa_pozycja]
            nowa_wiadomosc += nowa_litera
        else:
            nowa_wiadomosc += litera


"""
operacja_uzytkownika = input("Wybierz operację: \nKodowanie tekstu \nOdkodowanie tekstu \nK/O?")
if operacja_uzytkownika == "K" or operacja_uzytkownika == "k":
    wiadomosc = input("Podaj wiadomość do zakodowania")
    klucz = int(input("Podaj klucz"))
    print(kodowanie(wiadomosc, klucz))
    kodowanie(wiadomosc, klucz)
elif operacja_uzytkownika == "O" or operacja_uzytkownika ==  "o":
    wiadomosc = input("Podaj wiadomość do odkodowania")
    klucz = int(input("Podaj klucz"))
    print(odkodowanie(wiadomosc, klucz))
    odkodowanie(wiadomosc, klucz)
else:
    print("Podałeś nieprzewidzianą warotść")

"""