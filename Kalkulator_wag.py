"""
		kalkulator wag
		program przechowuje dane w postaci tablicy dwuwymiarowej
		program prosi o użytkownika o podanie dnia i wagi w danym dniu
		po zakończeniu wprowadzania danych (na życzenie używkonika) program wyświetla statystyki
		średnia, najwyższa i najniższa waga w każdym miesiącu (jeżeli brak danych dla konkretnego miesiąca to informacja o tym)
		średnia, najniższa, najwyższa waga w roku
"""

kalendarz = [[0 for j in range(31)] for i in range(12)]

while True:
    miesiac = int(input("Podaj miesiąc "))
    dzien = int(input("Podaj dzień "))
    waga = float(input("Podaj wagę "))
    kalendarz[miesiac - 1][dzien - 1] = waga
    print(f"Twoja waga miesiąca nr {miesiac}, dnia {dzien}, wynosiła {waga}")
    print(kalendarz)
    pytanie = input("Chcesz dalej wprowadzać dane? Y/N ")
    if pytanie.lower() == "n":
        break
print("Garść statystyk")

max_roczny = []
min_roczny = []
suma_roczna_wag = 0
ilosc_pomiarow_wag = 0

for miesiac in kalendarz:
    print(miesiac)
    max_waga = max(miesiac)
    max_roczny.append(max_waga)
    min_waga = max_waga
    srednia_waga = 0
    ile_pomiarow = 0

    for pomiar in miesiac:
        if pomiar != 0:
            srednia_waga += pomiar
            ile_pomiarow += 1
            if pomiar < min_waga:
                min_waga = pomiar
                min_roczny.append(min_waga)
    if ile_pomiarow != 0:
        suma_roczna_wag += srednia_waga
        ilosc_pomiarow_wag += ile_pomiarow
        srednia_waga = srednia_waga / ile_pomiarow
        print(f"Statystyka miesieczna:\nMax: {max_waga}\nMin: {min_waga}, Średnia: {srednia_waga}\n------------")
    else:
        print("W danym miesiącu nie podano danych")

print("Statystyka roczna")
print("Największa waga w roku:", max(max_roczny))
print("Najmniejsza waga w roku:", min(min_roczny))
srednia_roczna = suma_roczna_wag / ilosc_pomiarow_wag
print("Średnia waga w roku:", srednia_roczna)