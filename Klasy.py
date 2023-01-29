"""
Napisać program który
posiada klasę Person (pola: imię, nazwisko, wiek, płeć, przeciążoną metodę __str__)
posiada klasę Student (dziedziczy po klasie Person, dodatkowo zawiera pole z listą ocen i metodę do wyliczania średniej)
posiada klasę Employee (dziedziczy po klasie Person, dodatkowo zawiera pole z informacją o zarobkach)
każda klasa w osobnym pliku (module) i wykorzystać importowanie
w głównej klasie programu utworzyć listę minimum 10 obiektów po minimum jednej z każdej klasy
wyświetlić tylko mężczyzn (z wygenerowanej listy - filter i lambda do użycia)
wyświetlić studentów i średnią ich ocen
wyświetlić pracowników i ich średnie zarobki
przy implementacji zadań wykorzystać obsługę wyjątków w przypadku obsługi błędów (gdzie to potrzebne)
"""

class Person:
    def __init__(self, imie, nazwisko, wiek, plec):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.plec = plec

    def __str__(self):
        return self.imie + " " + self.nazwisko


class Student(Person):
    def __init__(self, imie, nazwisko, wiek, plec, oceny):
        super().__init__(imie, nazwisko, wiek, plec)
        self.oceny = oceny

    def srednia(self):
        try:
            return sum(self.oceny) / len(self.oceny)
        except:
            print("Sprawdź czy podane oceny są wpisane poprawnie")


class Employee(Person):
    def __init__(self, imie, nazwisko, wiek, plec, zarobki):
        super().__init__(imie, nazwisko, wiek, plec)
        self.zarobki = zarobki


#Person
p1 = Person("1st", "Person", 50, "M")
p2 = Person("2nd", "Person", 51, "K")
p3 = Person("3th", "Person", 52, "K")
p4 = Person("4th", "Person", 53, "M")
p5 = Person("5th", "Person", 54, "K")

#Student
s1 = Student("1st", "Student", 20, "K", [3,2,3,4,"M"])
s2 = Student("2nd", "Student", 21, "K", [2,2,3,4,2])
s3 = Student("3th", "Student", 32, "M", [3,5,5,4,4])
s4 = Student("4th", "Student", 43, "M", [5,4,5,4,4])
s5 = Student("5th", "Student", 54, "K", [3,3,3,5,4])

#Employee
e1 = Employee("1st", "Employee", 60, "M", 100)
e2 = Employee("2nd", "Employee", 61, "M", 200)
e3 = Employee("3th", "Employee", 62, "K", 300)
e4 = Employee("4th", "Employee", 63, "K", 400)
e5 = Employee("5th", "Employee", 64, "K", 500)

lista_obiektow = [p1, p2, p3, p4, p5, s1, s2, e1, e2, s3, 0]
try:
    print("Mężczyzni:", list(filter(lambda x: x.plec == "M", lista_obiektow))) #Wyświetlanie mężczyzn
except:
    print("Na Twojej liście znajduje się nieprzewidziana wartość")
[print(y.imie, y.nazwisko, "Średnia studenta wynosi: ", str(y.srednia())) for y in lista_obiektow if hasattr(y, "oceny")] #Student i jego średnia

#Wyciągniecie pracowników i uśrednienie ich zarobków
a = [z.zarobki for z in lista_obiektow if hasattr(z, "zarobki")]
srednia_zarobkow = sum(a) / len(a)
[print(z.imie, z.nazwisko, str(srednia_zarobkow)) for z in lista_obiektow if hasattr(z, "zarobki")]

#pocwicz lamdbe i uzycie jej zamiast list comprehention