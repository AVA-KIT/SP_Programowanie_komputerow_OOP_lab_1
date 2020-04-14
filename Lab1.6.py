class Kalendarz:
    def __init__(self, miesiac, rok):
        self.miesiac = miesiac
        self.rok = rok

    def pokaz(self):
        import calendar
        dt = calendar.weekday(self.rok, self.miesiac, 1)
        for m_31 in [1,3,5,7,8,10,12]:
            if self.miesiac == m_31: 
                a = 1
                for g in range(dt):
                        print("%4s" %(" "), end=" ")
                for h in range(dt, 7):
                        print("%4i" %(a), end=" ")
                        a += 1
                print()
                if dt <= 4:
                    for i in range(4):
                        for j in range(7):
                            print("%4i" %(a), end=" ")
                            a += 1
                            if a == 32:
                                break
                        print()
                else: 
                    for i in range(5):
                        for j in range(7):
                            print("%4i" %(a), end=" ")
                            a += 1
                            if a == 32:
                                break
                        print()
        for m_30 in [4,6,9,11]:
            if self.miesiac == m_30: 
                a = 1
                for g in range(dt):
                    print("%4s" %(" "), end=" ")
                for h in range(dt, 7):
                    print("%4i" %(a), end=" ")
                    a += 1
                print()
                if dt <= 5:
                    for i in range(4):
                        for j in range(7):
                            print("%4i" %(a), end=" ")
                            a += 1
                            if a == 31:
                                break
                        print()
                else: 
                    for i in range(5):
                        for j in range(7):
                            print("%4i" %(a), end=" ")
                            a += 1
                            if a == 31:
                                break
                        print()
        if self.miesiac == 2:    
            if self.rok % 4 == 0 and (self.rok % 100 != 0 or self.rok % 400 == 0):
                a = 1
                for g in range(dt):
                    print("%4s" %(" "), end=" ")
                for h in range(dt, 7):
                    print("%4i" %(a), end=" ")
                    a += 1
                print()
                for i in range(4):
                    for j in range(7):
                        print("%4i" %(a), end=" ")
                        a += 1
                        if a == 30:
                            break
                    print()
            else:
                a = 1
                for g in range(dt):
                    print("%4s" %(" "), end=" ")
                for h in range(dt, 7):
                    print("%4i" %(a), end=" ")
                    a += 1
                print()
                for i in range(4):
                    for j in range(7):
                        print("%4i" %(a), end=" ")
                        a += 1
                        if a == 29:
                            break
                    print()

kalendarz = Kalendarz(4, 2019)
kalendarz.pokaz()