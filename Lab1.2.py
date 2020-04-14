class Kwadrat:
    def __init__(self, bok):
        self.bok = bok
    def pole(self, bok):
        pole = bok**2
        return pole
    def pokaz(self):
        print(self.pole(self.bok))


k1 = Kwadrat(2)
k2 = Kwadrat(3)
k3 = Kwadrat(5)

k1.pokaz()  
k2.pokaz()  
k3.pokaz()  