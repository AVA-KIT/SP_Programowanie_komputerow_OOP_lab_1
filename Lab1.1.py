class DaneOsobowe:
    def __init__(self, imie, nazwisko,):
        self.imie = imie
        self.nazwisko = nazwisko
    def pokaz(self):
        print(self.imie, self.nazwisko)

Osoba = DaneOsobowe("Marcin", "Gazdowski")
Osoba.pokaz()