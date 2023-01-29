# zadanie 6:
# Napisz program/grę który będzie symulował wydostanie się z labiryntu
# +program spyta o poziom trudności - łatwy/trudny
# +program wylosuje labirynt na podstawie poziomu trudności
# +poziom łatwy będzie miał 2 możliwości wyboru drogi (w każdym ruchu, np prawo/lewo)
# +poziom łatwy będzie potrzebował 5 poprawnych ruchów do wyjścia z labiryntu
# +poziom trudny będzie miał 2 albo 3 możliwości wyboru (losowanie dla każdego ruchu)
# +poziom trudny będzie potrzebował 8 poprawnych ruchów do wyjścia z labiryntu
# +niepoprawny ruch jest sygnalizowany użytkownikowi i pozostaje on na tym samym "poziomie"
# +poprawny ruch jest sygnalizowany użytkownikowi i wyświetla się kolejny ruch
# +program będzie liczył ilość ruchów użytkownika w labiryncie
# wyświetli statystyki:
# +ile ruchów wykonał użytkownik
# +jak była minimalna ilość ruchów aby wydostać się z labiryntu - dla 5 ruchów to oczywiście 5, dla 8 to 8
# +jaka była maksymalna ilość ruchów aby wydostać się z labiryntu - dla poziomu łatwego to 10
# +(5 ruchów i jak zawsze pierwszy byłby zły to za 10 razem użytkownik by się wydostał, przyjmujemy że jak użytkownik dostanie informacje że wykonany ruch jest niepoprawny to już go nie powtórzy), dla poziomu trudnego maksymalna ilość ruchów jest zależna od wylosowania możliwości na każdym z ruchów
# +jeżeli użytkownik przekroczył granice 60% ruchów pomiędzy minimalną wartością a maksymalną ruchów to gra kończy się niepowodzeniem,
# +gracz umarł z głodu, np dla poziomu łatwego, min 5, max 10, 10 - 5 = 5, 60% z 5 = 3, 5 (min) + 3 (60%) = 8,
# +jeżeli użytkownik w 8 ruchach nie wydostanie się to przegrywa, dla poziomu trudnego trzeba to liczyć w zależności od skomplikowania labiryntu


import random

def poziom_latwy():
    ruchy = ["L", "P"]
    AP = 0 #Actual Position
    AM = 0 #All Moves
    ostatni_ruch = True

    while AP < 5 and AM < 10:
        if AP == 5:
            print("Gratulacje! Wygrałeś")
            ostatni_ruch = False
        elif AM == 8:
            print("Wykonałeś zbyt dużo ruchów i skończyły Ci się zapasy. Umarłeś z głodu!")
            ostatni_ruch = False
        if ostatni_ruch == True:
            losowanie = random.choice(ruchy)
        wybor_uzytkownika = input("W którą strone? L/P?")
        AM += 1
        if wybor_uzytkownika == losowanie:
            print("Dobrze!")
            AP += 1
            ostatni_ruch = True
        elif wybor_uzytkownika != losowanie:
            print("Źle. Wybierz jeszcze raz")
            ostatni_ruch = False

    print("Statystyki: ilość ruchów: {}. Minimalnie potrzebowałeś 5 ruchów aby wydostać się z labiryntu, maksymalnie 10.".format(AM))


def poziom_trudny():
    ruchy = ["L", "P"]
    ruchy2 = ["L", "P", "Ś"]

    AP = 0 #Actual Position
    AM = 0 #All Moves
    ostatni_ruch = True

    while AP < 8 and AM < 24:
        if AP == 8:
            print("Gratulacje! Wygrałeś")
            ostatni_ruch = False
        elif AM == 10:
            print("Wykonałeś zbyt dużo ruchów i skończyły Ci się zapasy. Umarłeś z głodu!")
            ostatni_ruch = False
        if ostatni_ruch == True:
            losowanie = random.randint(0,1)
            if losowanie == 0:
                losowanie2 = random.choice(ruchy)
            else:
                losowanie2 = random.choice(ruchy2)
        if losowanie == 0:
            wybor_uzytkownika = input("W którą strone? L/P?")
        else:
            wybor_uzytkownika = input("W którą strone? L/P czy Ś?")
        AM += 1
        if wybor_uzytkownika == losowanie2:
            print("Dobrze!")
            AP += 1
            ostatni_ruch = True
        elif wybor_uzytkownika != losowanie2:
            print("Źle. Wybierz jeszcze raz")
            ostatni_ruch = False

    print("Statystyki: ilość ruchów: {}. Minimalnie potrzebowałeś 8 ruchów aby wydostać się z labiryntu, maksymalnie 24.".format(AM))
    print(AP, AM)


poziom_trudnosci = input("Wybierz poziom trudności:\nŁatwy\nTrudny\n")
poziom_trudnosci = poziom_trudnosci.lower()
if poziom_trudnosci == "łatwy":
    poziom_latwy()
elif poziom_trudnosci == "trudny":
    poziom_trudny()
else:
    print("Wybrałeś nie przewidzianą wartość")