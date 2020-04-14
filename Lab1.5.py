class Statystyka(list):
    def __init__(self, *args):
        list.__init__(self, *args)
    
    def suma_listy(self):
        suma = sum(self)
        return suma

    def srednia_listy(self):
        srednia = suma / len(self)
        return srednia

l = Statystyka([1, 3, 5])

print(l.suma_listy())
print(l.srednia_listy())