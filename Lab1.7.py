class FiguraGeo:
    def __init__(self, nazwa, *args):
        self.nazwa = nazwa
        self.polozenie = args

    def wypisz(self):
        print(f'Nazwa figury: {self.nazwa}, położenie: {self.polozenie}')
