"""
do napisania program przypominający działaniem listę TODO
aplikacja do przechowywania zadań wraz ze stanami - TODO, IN PROGRESS, DONE
aplikacja powinna
wyświetlać aktualne zadania - można użyć zewnętrznej biblioteki do "rysowania" tabeli
dać możliwość dodawania nowych zadań
dać możliwość edytowania aktualnych zadań
dać możliwość usuwania istniejących zadań
zapisywanie stanu do pliku przy kończeniu pracy
pobieranie stanu z pliku przy uruchomieniu aplikacji
dodać menu mówiące użytkownikowi w jakim miejscu się znajduje / co wykonuje
budowa aplikacji powinna być przemyślana, aplikacja powinna być rozbita na kilka mniejszych modułów / pakietów
wykorzystać poznane elementy języka Python
wykorzystać klasy do modelowania danych
"""

"""
do napisania program przypominający działaniem listę TODO
aplikacja do przechowywania zadań wraz ze stanami - TODO, IN PROGRESS, DONE
aplikacja powinna
wyświetlać aktualne zadania - można użyć zewnętrznej biblioteki do "rysowania" tabeli
dać możliwość dodawania nowych zadań
dać możliwość edytowania aktualnych zadań
dać możliwość usuwania istniejących zadań
zapisywanie stanu do pliku przy kończeniu pracy
pobieranie stanu z pliku przy uruchomieniu aplikacji
dodać menu mówiące użytkownikowi w jakim miejscu się znajduje / co wykonuje
budowa aplikacji powinna być przemyślana, aplikacja powinna być rozbita na kilka mniejszych modułów / pakietów
wykorzystać poznane elementy języka Python
wykorzystać klasy do modelowania danych
"""

import json
from tabulate import tabulate


def zapisz():
    bazaDanychDict = {
    "TODO": [],
    "IN PROGRESS": [],
    "DONE": []
}
    for k in bazaDanych:
        for v in bazaDanych[k]:
            bazaDanychDict[k].append(v.doJson())

    doPliku = json.dumps(bazaDanychDict, indent=4)
    with open("Todolista.json", "w") as zapiszJson:
        zapiszJson.write(doPliku)

def odczytaj():
    bazaDanych = {
        "TODO": [],
        "IN PROGRESS": [],
        "DONE": []
    }

    try:
        with open("Todolista.json", "r") as otworzJson:
            zPliku = json.load(otworzJson)


        for k in zPliku:
            for v in zPliku[k]:
                # bazaDanych[k].append(Ticket.zJson(v))
                bazaDanych[k].append(Ticket(v["Status"], v["Opis"], v["ID"]))


    except FileNotFoundError:
        print("Nie ma pliku, z którego można pobrać dane")
    return bazaDanych


class Ticket:

    def __init__(self, status, opis, id):
        self.status = status
        self.opis = opis
        self.id = id


    def __repr__(self):
        return f"ID{self.id}: {self.opis}"

    ##do testow
    # def __eq__(self, other):
    #     return self.id == other.id

    def edycjaOpisu(self, nowyOpis):
        self.opis = nowyOpis

    def edycjaStatusu(self, nowyStatus):
        self.status = nowyStatus

    def doJson(self):
        dictDoJson = {
            "Status": self.status,
            "Opis" : self.opis,
            "ID" : self.id
        }
        return dictDoJson

    # @classmethod
    # def zJson(cls, dictDoJson):
    #     ticket = cls(status=dictDoJson['Status'],
    #                  opis = dictDoJson['Opis'],
    #                  id = dictDoJson['ID'])
    #     return ticket


def menu_glowne():
    dostepne_komendy = ["D", "E", "U", "W"]
    print("""
Co chciałbyś zrobić?
[D]dodaj
[E]dytuj
[U]suń
[W]yjdź z aplikacji
    """)
    wybor_1 = input("Wybierz operację: ")
    wybor_1 = wybor_1.upper()
    if wybor_1 not in dostepne_komendy:
        print("Podałeś nieprzewidzianą wartość. Co chcesz zrobić?")
        return None

    if wybor_1 == "D":
        print("Dodajesz")
        # wybor_kolumny()
        dodajTicket()

    elif wybor_1 == "E":
        print("Edytujesz")
        edytujTicket()

    elif wybor_1 == "U":
        print("Usuwasz")
        usunTicket()

    else:
        return wybor_1


def wybor_kolumny():
    dostepneKolumny = ["1", "2", "3"]
    print("""
Na której kolumnie chcesz dokonać operacji?
1 - TODO
2 - IN PROGRESS
3 - DONE
    """)
    # global wybor_2 #wyrzuc dane globalne
    wybor_2 = input("Wybierz kolumne: ")
    if wybor_2 not in dostepneKolumny:
        print("Nieprawidłowa wartość, spróbuj jeszcze raz!")
        return wybor_kolumny()

    if wybor_2 == "1":
        wybor_2 = "TODO"
        print(wybor_2)
    elif wybor_2 == "2":
        wybor_2 = "IN PROGRESS"
        print(wybor_2)
    elif wybor_2 == "3":
        wybor_2 = "DONE"
        print(wybor_2)
    return wybor_2

def dodajTicket():
    maxID = znajdzNajwyzszeID()
    maxID += 1
    wybor_2 = wybor_kolumny()
    opisTicketu = input("Podaj treść ticketu: ")
    ticket = Ticket(status=wybor_2 , opis=opisTicketu, id = maxID)
    if wybor_2 == "TODO":
        klucz = "TODO"
        # bazaDanych.setdefault(klucz)
        bazaDanych[klucz].append(ticket)

    elif wybor_2 == "IN PROGRESS":
        klucz = "IN PROGRESS"
        # bazaDanych.setdefault(klucz)
        bazaDanych[klucz].append(ticket)

    elif wybor_2 == "DONE":
        klucz = "DONE"
        # bazaDanych.setdefault(klucz)
        bazaDanych[klucz].append(ticket)


def szukajTicket(id):
    for k in bazaDanych:
        for v in bazaDanych[k]:
            if v.id == int(id):
                return k, v


def usunTicket():
    idUsun = input("Podaj id do usunięcia: ")
    id = szukajTicket(idUsun)
    if id == None:
        print("Ticket nie istnieje")
        return id
    else:
        polozenie = bazaDanych[id[0]].index(id[1])
        del bazaDanych[id[0]][polozenie]
    return id


def edytujTicket():
    while True:
        idEdytuj = input("Podaj ID ticketu do edycji (w razie pomyłki naciśnij Q): ")
        # idEdytuj.lower()
        if idEdytuj == "q":
            return
        try:
            polozenie, ticket = szukajTicket(idEdytuj)
            break
        except:
            print("Ticket nie istnieje")

    print(f"""
Edytujesz ticket 
ID: {ticket.id}
Opis: {ticket.opis}
""")

    edycjaKolumny = input(f"""
1 - TODO
2 - IN PROGRESS
3 - DONE
Gdzie chcesz przesunąć ticket (naciśnij ENTER aby jeśli nie chcesz zmieniać):
""")
    if edycjaKolumny == "":
        pass
    if edycjaKolumny == "1":
        print("Przenosisz ticket do TODO") ## nastepne linijki przenies do funkcji i uzyc w pozostalych elifach
        ticket.edycjaStatusu("TODO")
        przesuniecie = bazaDanych[polozenie].index(ticket)
        bazaDanych["TODO"].append(ticket)
        del bazaDanych[polozenie][przesuniecie]

    elif edycjaKolumny == "2":
        print("Przenosisz ticket do IN PROGRESS")
        ticket.edycjaStatusu("IN PROGRESS")
        przesuniecie = bazaDanych[polozenie].index(ticket)
        bazaDanych["IN PROGRESS"].append(ticket)
        del bazaDanych[polozenie][przesuniecie]

    elif edycjaKolumny == "3":
        print("Przenosisz ticket do DONE")
        ticket.edycjaStatusu("DONE")
        przesuniecie = bazaDanych[polozenie].index(ticket)
        bazaDanych["DONE"].append(ticket)
        del bazaDanych[polozenie][przesuniecie]

    nowaTresc = input("Podaj nową treść: ")
    if nowaTresc == "":
        pass
    if nowaTresc != "":
        ticket.edycjaOpisu(nowaTresc)


def znajdzNajwyzszeID():
    maxID = 0
    for k in bazaDanych:
        for v in bazaDanych[k]:
            if v.id > maxID:
                maxID = v.id
    return maxID

##do testow
# bazaDanych = None
# print("name:", __name__)
# if __name__ == "__main__":

result = ""
bazaDanych = odczytaj()
while result != "W":
    print(tabulate(bazaDanych, headers="keys", tablefmt="rounded_grid"))
    result = menu_glowne()
print("Dziękuje za skorzystanie z aplikacji")
zapisz()

