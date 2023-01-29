"""
zadanie 5:
# napisz program który poprosi o wprowadzenie imienia studenta oraz oceny jaką uzyskał,
"x" kończy wprowadzanie danych,
po zakończeniu wprowadzania danych zwraca średnią ocen dla każdego studenta oraz dla całej klasy
[słowniki do wykorzystania]
"""

slownik = {}

while True:
    lista_ocen = []
    imie = str(input("Podaj imie. [Wpisanie \"X\" spowouje zamknięcie aplikacji] "))
    if imie == "x" or imie == "X":
        break
    while True:
        ocena = input("Podaj ocene. [Wpisanie \"X\" spowouje cofnięcie do wprowadzenia imienia ucznia] ")
        if ocena == "x" or ocena == "X":
            break
        lista_ocen.append(int(ocena))
        slownik[imie] = lista_ocen

srednia_klasy = []
for k,v in slownik.items():
    srednia_ucznia = sum(v) / len(v)
    print("Imię ucznia:", k,"\nŚrednia ucznia: ", srednia_ucznia)
    srednia_klasy.append(srednia_ucznia)

print("Średnia klasy: {}".format(sum(srednia_klasy) / len(srednia_klasy)))

print("Dziękujemy za skorzystanie z aplikacji")