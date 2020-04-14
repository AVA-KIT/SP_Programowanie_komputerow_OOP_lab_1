class Prostokat:
    def __init__(self, bok1, bok2):
        self.bok1 = bok1
        self.bok2 = bok2
    def pole(self, bok1, bok2):
        pole = bok1*bok2
        return pole
    def pokaz(self):
        print('Pole prostokąta wynosi', self.pole(self.bok1, self.bok2))


p1 = Prostokat(2,3)
p2 = Prostokat(5,6)
p3 = Prostokat(4,8)

lp =[]

lp.append  (p1)
lp.append  (p2)
lp.append  (p3)

for p in lp:
    p.pokaz()

def pokazInfo(prostokat):
    print('Długość boku a=', prostokat.bok1)
    print('Długość boku b=', prostokat.bok2)
    prostokat.pokaz()
      

pokazInfo(p1)


for p in lp:
    pokazInfo(p)
 