"""
Napisz program, który będzie symulował zachowanie struktury danych typu "stos"
do implementacji wykorzystaj podejście obiektowe
stos musi przechowywać swój aktualny stan
możemy dodawać elementy do stosu
możemy pobierać elementy ze stosu
"""

class Struktura_stos:
    def __init__(self):
        self.lista = []

    def dodaj_element(self, elem):
        print("Dodałeś element do bazy!")
        self.lista.append(elem)

    def pobierz_element(self):
        try:
            print("Pobrałeś element z wierzchu stosu!")
            return self.lista.pop()
        except:
            print("Operacja nie możliwa do wykonania. Z pustego to i Salomon nie naleje!")

    def czy_pusta_lista(self):
            return self.lista == []


s = Struktura_stos()
s.dodaj_element(4)
ss = Struktura_stos()
ss.pobierz_element()