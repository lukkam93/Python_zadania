"""
		totolotek
		program losuje 6 liczb od 1 do 49
		program prosi o wprowadzenie 6 liczb od 1 do 49 przez użytkownika
		program zwraca ilość "trafień"
"""

import random
liczba_losowa = random.sample(range(1,50),6)

print(liczba_losowa)


lista_usera = []
i = 0
while i < len(liczba_losowa):
    strzal = int(input("Podaj swoją liczbę "))
    if strzal <= 0 or strzal > 49:
        print("Poza zakresem. Podaj liczbę od 1 do 49")
        continue
    if strzal not in lista_usera:
        lista_usera.append(strzal)
        print("To Twój", i+1, "strzał")
        i += 1
    else:
        print("Podałeś już tę wartość")

print("Twoje strzały to", lista_usera)

#liczenie trafien
# trafienia = [elem for elem in liczba_losowa if elem in lista2]
# print(trafienia)


#liczenie trafien za pomoca petli for
lista_trafien = []
for i in lista_usera:
    if i in liczba_losowa:
        lista_trafien.append(i)
ilosc_trafien = len(lista_trafien)
print(f"Trafiona ilość liczb: {ilosc_trafien}")