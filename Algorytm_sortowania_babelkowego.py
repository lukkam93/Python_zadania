"""
zadanie 1:
algorytm sortowania bąbelkowego - zapoznać sie z zaimplementować
program wczytuje od użytkownika dowolną liczbę liczb i sortuje je z użyciem algorytmu sortowania bąbelkowego
"""

lista = []
dlugosc_listy = 5
while len(lista) < dlugosc_listy:
    liczba = int(input("Podaj liczbę"))
    lista.append(liczba)
print(lista)

i = 0
while i < len(lista) - 1:
    j = 0
    while j < len(lista) - 1:
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
        j += 1
    i += 1
    print(lista)

#bez sztywnej liczby na poczatku. bez okreslonej dlugosci listy
#druga pentla while można zmienic na for