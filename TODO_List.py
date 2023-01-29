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

#usuwanie z listy za pomocą .remove()

from tabulate import tabulate

slownik = {
    "TODO": [],
    "IN PROGRESS": [],
    "DONE": []
}
print(tabulate(slownik, headers=["TO DO", "IN PROGRESS", "DONE"], tablefmt="rounded_grid"))

def menu_glowne():
    print("""
Co chciałbyś zrobić?
[D]dodaj
[E]dytuj
[U]suń
[W]yjdź z aplikacji
    """)
    wybor_1 = input("Wybierz operację ")
    wybor_1 = wybor_1.upper()
    if wybor_1 == "D":
        print("Dodajesz")
        wybor_kolumny()
    elif wybor_1 == "E":
        print("Edytujesz")
        wybor_kolumny()
    elif wybor_1 == "U":
        print("Usuwasz")
        wybor_kolumny()
    elif wybor_1 == "W":
        print("Dzękuje za skorzystanie z aplikacji")
        exit()
    else:
        print("Podałeś nieprzewidzianą wartość. Co chcesz zrobić?")
        menu_glowne()

def wybor_kolumny():
    print("""
Na której kolumnie chcesz dokonać operacji?
1 - TODO
2 - IN PROGRESS
3 - DONE
    """)
    wybor_2 = int(input("Wybierz kolumne "))
    if wybor_2 == 1:
        print("Kolumna TODO")
        dodawanie_ticketu(slownik)
    elif wybor_2 == 2:
        print("Kolumna IN PROGRESS")
    elif wybor_2 == 3:
        print("Kolumna DONE")
        return wybor_2

def dodawanie_ticketu(slownik):
    lista_ticketow = []
    id = 0
    while True:
        id += 1
        ticket = input("Podaj treść ticketu: ")
        indeksowanie = "ID_" + str(id) + " " + ticket
        #print(indeksowanie)
        lista_ticketow.append(indeksowanie)
        #print(lista_ticketow)
        break
        #return lista_ticketow
    slownik["TODO"].append(indeksowanie)
    print(tabulate(slownik, headers=["TO DO", "IN PROGRESS", "DONE"], tablefmt="rounded_grid"))
    #return tabulate(slownik, headers=["TO DO", "IN PROGRESS", "DONE"], tablefmt="rounded_grid")
    menu_glowne()
    #print(slownik)
    #update_tablicy()


menu_glowne()
# dodawanie_ticketu(slownik)