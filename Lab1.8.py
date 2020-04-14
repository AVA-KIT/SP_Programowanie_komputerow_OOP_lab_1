class Planety:
    def __init__(self, nazwa, odleglosc, rzeczywista):
        self.nazwa = nazwa
        self.odleglosc = odleglosc
        self.rzeczywista = rzeczywista
    def __str__(self):
        print (f'Nazwa planety: {self.nazwa}, odległość w tys. km: {self.odleglosc*149597870.7}, czy prawdziwa: {self.rzeczywista}')

def zapis(Planety):
    with open('Planety.txt', 'at') as plik:
        plik.write(str(Planety.nazwa) + ';' + str(Planety.odleglosc) + ';' + str(Planety.rzeczywista) + '\n')

def wczytaj_planety():
    planety = []
    with open('Planety.txt', 'rt') as plik: 
        for linia in plik:
            wartosc = linia.split(';')
            a = Planety(wartosc[0], wartosc[1], wartosc[2])
            planety.append(a)
    return planety

def main():
    planeta_1 = Planety("Wulkan", 0.03, "false")
    planeta_2 = Planety("Merkury", 0.38, "true")
    planeta_3 = Planety("Wenus", 0.72, "true")
    planeta_4 = Planety("Ziemia", 1.0, "true")
    planeta_5 = Planety("Mars", 1.52, "true")
    planeta_6 = Planety("Faeton", 2.7, "false")
    planeta_7 = Planety("Jowisz", 5.2, "true")
    planeta_8 = Planety("Saturn", 9.53, "true")
    planeta_9 = Planety("Uran", 19.19, "true")
    planeta_10 = Planety("Neptun", 30.06, "true")
    planeta_11 = Planety("Pluton", 39.48, "false/true")

    for planeta in [planeta_1, planeta_2, planeta_3, planeta_4, planeta_5, planeta_6, planeta_7, planeta_8, planeta_9, planeta_10, planeta_11]:
        zapis(planeta)
    wczytaj_planety()

if __name__ == '__main__':
    main()
