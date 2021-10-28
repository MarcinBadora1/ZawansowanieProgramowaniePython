from datetime import date


class Student:  ##listy obiektów mnogie
    name: str
    marks: int

    def __init__(self, name: str, marks: int) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False


m_student1 = Student('John', 2)
print(m_student1.is_passed())
m_student2 = Student('Ann', 51)
print(m_student2.is_passed())


###Zadanie2

class Library:
    city: str
    street: str
    zip_code: str
    open_hours: str
    phone: str

    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str) -> None:
        self.city = city
        self.zip_code = zip_code
        self.street = street
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'String opis. Obiekty księgarni nie posiadają przestrzeni klas nadrzędnych'


class Employee:
    first_name: str
    last_name: str
    hire_date: date
    birth_date: date
    city: str
    street: str
    zip_code: str
    phone: str

    def __init__(self, first_name: str, last_name: str, hire_date: date, birthdate: date, city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.zip_code = zip_code
        self.hire_date = hire_date
        self.birth_date = birthdate
        self.phone = phone
        self.street = street

    def __str__(self):
        return f'String opis. Obiekty pracownik nie posiada przestrzeni klas nadrzednych'


class Book:
    library: Library
    public_date: date
    author_name: str
    author_surname: str
    number_of_pages: int

    def __init__(self, library: Library, public_date: date, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.public_date = public_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'String opis. Obiekty książka posiadają atrybut obiektu klasy księgarnia.'


class Order:
    employee: Employee
    student: Student
    books: Book
    order_date: date

    def __init__(self, employee: Employee, student: Student, books: Book, order_date: date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'String opis. Obiekty zamówienie przechowują daną o studencie, pracowniku, książce'


###objectgeneration
library_1 = Library('Kraków', 'Słoneczna', '32-124', '11-12', '563643123')
library_2 = Library('Wadowice', 'Polana', '53-213', '7-18', '897297567')
book_1 = Book('Warszawa', date(1999, 12, 31), 'Jan', 'Kowalski', 12)
book_2 = Book('Warszawa', date(1999, 11, 30), 'Jan', 'Kowalowski', 423)
book_3 = Book('Warszawa', date(1994, 10, 31), 'Jan', 'Nowak', 13)
book_4 = Book('Bobolice', date(1998, 12, 31), 'Tomek', 'Kowalski', 17)
book_5 = Book('Warszawa', date(1999, 12, 30), 'Jan', 'Kowalssq', 13)
employee_1 = Employee('Jan', 'Kowalczyk', date(1997, 2, 3), date(2007, 11, 2), 'Warszawa', 'Dobrogłowa', '43-412',
                      '112345678')
employee_2 = Employee('Jan', 'Kowalczyk', date(1996, 2, 3), date(2007, 11, 2), 'Warszawa', 'Dobrogłowa', '43-412',
                      '112345678')
employee_3 = Employee('Jan', 'Kowalczyk', date(1994, 2, 3), date(2007, 11, 2), 'Warszawa', 'Dobrogłowa', '43-412',
                      '112345678')
student = Student('Jacek', 50)
student2 = Student('Jan', 60)
student3 = Student('Witold', 60)
order1 = Order(employee_1, student, book_1, date(1994, 3, 21))
order2 = Order(employee_2, student, book_3, date(1994, 4, 3))
print(order1)
print(order2)


####Zadanie3
class Property:
    area: str
    rooms: int
    price: float
    address: str

    def __init__(self, area: str, rooms: int, price: float, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Klasa Property..'


class House(Property):
    plot: int

    def __init__(self, area: str, rooms: int, price: float, address: str, plot: int):
        Property.__init__(self, area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'ChildClass dla Property'


class Flat(Property):
    floor: int

    def __init__(self, area: str, rooms: int, price: float, address: str, floor: int):
        Property.__init__(self, area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Podklasa Property...'


house = House('Suburbian', 2, 2374863.12, 'Koszyki 2.., Warszawa', 12)
flat = Flat('Centre', 3, 2786343.1, 'Berlin abc2', 10)
print(house)
print(flat)
