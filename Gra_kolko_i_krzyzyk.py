"""
Napisz program, który będzie przypominał grę w kółko i krzyżyk
program rysuje plansze do gry w kółko i krzyżyk
komputer zaczyna rozgrywkę i wstawia "O" w dowolne pole
program pyta użytkownika gdzie wstawić "X", użytkownik podaje dwie cyfry w formacie A B gdzie A to wiersz a B kolumna
program sprawdza czy znak może być wprowadzony we wskazane pole
program po każdym znaku rysuje aktualny układ planszy
program po każdym znaku sprawdza czy ktoś nie wygrał rozgrywki
program powtarza czynności do wykorzystania wszystkich pól
skorzystaj z poznanych funkcji losujących aby program wybierał gdzie wstawić znak
jeżeli nikt nie wygrał a skończyły się wolne pola, program informuje o tym użytkownika
"""

import random


plansza = [["*"," 1", "2", "3"], ["1:", "*", "*", "*"], ["2:","*" ,"*" ,"*"], ["3:", "*", "*", "*"]]

def rysuj_plansze(plansza):
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            print(plansza[i][j], end=" ")
        print()


def ruch_komputera():
    x = random.randint(1,3) #przesunięcie w rzędzie
    y = random.randint(1,3) #przesunięcie w kolumnie
    return x,y

def czy_ruch_jest_mozliwy(plansza, x, y):
    if plansza[x][y] == "*":
        return True
    else:
        #print("Ruch niemożliwy do wykonania")
        return False

def update_planszy(plansza, x, y, gracz):
    if gracz == "gracz":
        plansza[x][y] = "X"
    else:
        plansza[x][y] = "0"
    rysuj_plansze(plansza)

def ruch_gracza():
    x = int(input("Wybierz rząd:")) #przesunięcie w rzędzie
    y = int(input("Wybierz kolumnę:")) #przesunięcie w kolumnie
    return x, y

# def zwyciestwo(plansza, gracz):
#     if (plansza[1][1] and plansza[1][2] and plansza[1][3]) == gracz:
#         return True
#     if (plansza[2][1] and plansza[2][2] and plansza[2][3]) == gracz:
#         return True
#     if (plansza[3][1] and plansza[3][2] and plansza[3][3]) == gracz:
#         return True
#     if (plansza[1][1] and plansza[2][1] and plansza[3][1]) == gracz:
#         return True
#     if (plansza[2][1] and plansza[2][2] and plansza[2][3]) == gracz:
#         return True
#     if (plansza[3][1] and plansza[3][2] and plansza[3][3]) == gracz:
#         return True
#     if (plansza[1][1] and plansza[2][2] and plansza[3][3]) == gracz:
#         return True
#     if (plansza[1][3] and plansza[2][2] and plansza[3][1]) == gracz:
#         return True

def zwyciestwo(plansza, gracz):
    if plansza[1][1] == gracz and plansza[1][2] == gracz and plansza[1][3] == gracz:
        print("Zwycięża " + gracz)
        return True
    if plansza[2][1] == gracz and plansza[2][2] == gracz and plansza[2][3] == gracz:
        print("Zwycięża " + gracz)
        return True
    if plansza[3][1] == gracz and plansza[3][2] == gracz and plansza[3][3] == gracz:
        print("Zwycięża " + gracz)
        return True
    if plansza[1][1] == gracz and plansza[2][1] == gracz and plansza[3][1] == gracz:
        print("Zwycięża " + gracz)
        return True
    if plansza[2][1] == gracz and plansza[2][2] == gracz and plansza[2][3] == gracz:
        print("Zwycięża " + gracz)
        return True
    if plansza[3][1] == gracz and plansza[3][2] == gracz and plansza[3][3] == gracz:
        print("Zwycięża " + gracz)
        return True
    if plansza[1][1] == gracz and plansza[2][2] == gracz and plansza[3][3] == gracz:
        print("Zwycięża " + gracz)
        return True
    if plansza[1][3] == gracz and plansza[2][2] == gracz and plansza[3][1] == gracz:
        print("Zwycięża " + gracz)
        return True

def wykonaj():
    plansza = [["*", " 1", "2", "3"], ["1:", "*", "*", "*"], ["2:", "*", "*", "*"], ["3:", "*", "*", "*"]]
    rysuj_plansze(plansza)
    while True:
        x, y = ruch_komputera()
        jest_mozliwe = czy_ruch_jest_mozliwy(plansza, x, y)
        if jest_mozliwe == True:
            update_planszy(plansza, x, y, "komputer")
        elif jest_mozliwe == False:
            continue

        jest_mozliwe = False
        while jest_mozliwe == False:
            x, y = ruch_gracza()
            jest_mozliwe = czy_ruch_jest_mozliwy(plansza, x, y)
            if jest_mozliwe == True:
                update_planszy(plansza, x, y, "gracz")
            elif jest_mozliwe == False:
                print("To miejsce jest już zajęte. Wybierz inne pole")
                continue

        zwyciestwo(plansza, "gracz")

wykonaj()