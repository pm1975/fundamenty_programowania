class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.semestr = 1

    def promuj(self, ilosc_semestrow=1):
        self.semestr += ilosc_semestrow;

jan = Student('Jan', 'Kowalski')
jan.promuj()
jan.promuj()
print(jan)
print(jan.imie, jan.nazwisko, jan.semestr)

malgorzata = Student('Malgorzata', 'Kowalska')
malgorzata.promuj(3)
print(malgorzata)
print(malgorzata.imie, malgorzata.nazwisko)
print(malgorzata.semestr)


