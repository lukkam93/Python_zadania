"""
		totolotek
		program losuje 6 liczb od 1 do 49
		program prosi o wprowadzenie 6 liczb od 1 do 49 przez użytkownika
		program zwraca ilość "trafień"
"""


#zaszyć generator licz losowych z przedzialu 1-49
#nie wyswietlaj ich uzytkownikowi
#petla ktora poprosi o prowadzenie 6 typow
#mozna wprowadzic tylko liczby z przedzialu 1-49
#mozna je dodac do listy, a pozniej sprawdzic czy dana liczba znajduje sie w liczbach losowych
#porownanie dwoch list?
#wyswietlenie ilosci trafien, nie pokazuje ktore liczby sie trafilo tylko ich ilosc

import random
lista1 = []
liczba_losowa = random.sample(range(1,49),6)

lista1.append(liczba_losowa)
print(lista1)


lista2 = []
i = 0
while i < len(liczba_losowa):
    strzal = int(input("Podaj swoją liczbę"))
    if strzal <= 0 or strzal > 49:
        print("Poza zakresem. Podaj liczbę od 1 do 49") #strzały z poza zakresu wciąż traktuje jako podane liczby
        continue
    if strzal not in lista2:
        lista2.append(strzal)
        print("To Twój", i+1, "strzał") #jak te dwie linijki przesunąłem maksymalnie w lewo to pętla wciąż pytała o liczbę
        i += 1

print("Twoje strzały to", lista2)

liczba_trafien = [elem for elem in liczba_losowa if elem in lista2]
print(liczba_trafien)

#range 49 nigdy nie wygenruje liczby 49
#jak zrobie zwykly random to liczby moga sie powtorzyc. jak random.sample to nie.
#linia 21 z dupy
#dodaj elsa aby uzytkownik wiedzial ze podal liczbe ktora napisal juz wczesniej
#inaczej zrobic info o ilosci trafien - uzyj for i in lista2:
#if i in liczba_losowa
#append