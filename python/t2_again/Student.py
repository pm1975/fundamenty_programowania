from copy import copy
from math import ceil


class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.semestr = 1

    def promuj(self, ilosc_semestrow = 1):
        self.semestr += ilosc_semestrow

    @property
    def rok(self):
        return ceil(self.semestr / 2)

    def przedstaw_sie(self):
        return f'Nazywam się {self.imie} {self.nazwisko}.'

jan = Student('Jan', 'Kowalski')
print(jan.przedstaw_sie())
jacek = copy(jan)

print(jan)
print(jacek)

jacek.imie = 'Jacek'
print(jacek.przedstaw_sie())
print(jan.przedstaw_sie())
