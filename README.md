# SP_Programowanie_komputerow_OOP_lab_1
Studia podyplomowe, Programowanie obiektowe - Python, Wydział Informatyki, ZUT w Szczecinie - Laboratorium 1

Wszystkie klasy zapisywać w oddzielnych plikach i zachować na kolejne zajęć
cia (niektóre z nich się przydadzą). Wszystkie klasy przetestować, tworząc kilka
obiektów klasy i uruchamiając każdą z dostępnych metod przynajmniej raz.
1. Przygotować klasę do przechowywania imion i nazwisk.
a) Utworzyć trzy nazwane obiekty tej klasy.
2. Przygotować klasę opisującą kwadrat,
a) metoda __init__ powinna przyjmować długość boku,
b) napisać metodę zwracającą pole powierzchni,
c) utworzyć trzy kwadraty,
d) wypisać pole powierzchni poszczególnych kwadratów.
3. Przygotować klasę opisującą prostokąt (na bazie kopii kwadratu),
a) metoda __init__ powinna przyjmować długości boków,
b) napisać metodę zwracając¡ pole powierzchni,
c) utworzyć trzy prostokąty,
d) utworzone prostokąty dodać do listy,
e) wypisać pole powierzchni poszczególnych prostokątów, korzystając z listy,
f) przygotować funkcje (nie metodę), która przyjmie prostokąt jako parametr i wypisze długości jego boków i pole powierzchni, do wykonania
tego skorzysta z metod z klasy, wywołać funkcję dla wszystkich wcześniej utworzonych prostokątów.
4. Przygotować klasę do obsługi tekstowego paska postępu (ang. ProgressBar). 
Oprócz inicjacji dowolną wartością i wartością maksymalną, klasa ma umożliwiać dodawanie, odejmowanie i wypisywanie wartości (jako metody). Powinna również umożliwiać wypisanie wartości przechowywanej i wartości maksymalnej i uniemożliwienie zmiany w przypadku wyjjcia poza ustalony przy tworzeniu obiektu zakres. Proszę zademonstrować działanie na dwóch paskach zmienianych i wyświetlanych w pętli.
5. Przygotować klasę do prostych obliczeń statystycznych (można ją nazwać Statystyka).
a) inicjalizacja przy pomocy listy,
b) metoda zwracająca wartość sumy całej listy (można zrobić wariant pozwalający na obliczanie sumy fragmentu listy),
c) metoda obliczająca średnią (suma/liczbę elementów), metoda powinna skorzystać z poprzedniej metody,
d) metoda obliczająca medianę (Dla listy uporzadkowanej jest to wartość, która jest w połowie listy w wypadku nieparzystej liczby elementów. Dla parzystej liczby elementów - średnia arytmetyczna dwóch środkowych liczb). W związku z tym trzeba skorzystać z funkcji sorted.
e) metoda obliczająca minimum,
f) metoda obliczająca maximum. Wykonać testy wszystkich metod na co najmniej 3 listach po co najmniej 5-6 warto±ci.
6. Przygotować klasy reprezentującą kalendarz na dany miesiąc.
a) metoda __init__ przyjmuje rok i miesiąc,
b) metoda pokaz wyświetla odpowiednią liczbę dni w blokach po 7,
i. rok przestępny to taki, którego liczba określająca rok dzieli się bez reszty przez 4, ale nie dzieli się bez reszty przez 100, ale dzieli się bez reszty przez 400,
c) wersja dla zaawansowanych: ustalić w jaki dzień wypada pierwszy dzień tego miesi¡ca i odpowiednio podpisać dni tygodnia (lub rozpocząć wyświetlanie kalendarza od odpowiedniego dnia).Wykorzysta¢ dzielenie modulo 7 ( x % 7).
7. Przygotować klasę reprezentującą fgure geometryczną (na chwilą obecną klasa ma przechowywać nazwę i położenie fgury i je wypisywać.
8. Przygotować klasę reprezentującą planetę, atrybuty wydedukować z poniższej tabeli:

Planeta | odległość od Słońca w j.a. | rzeczywista

Wulkan  |           0.03             |    false

Merkury |           0.38             |    true

Wenus   |           0.72             |    true

Ziemia  |           1.0              |    true

Mars    |           1.52             |    true

Faeton  |           2.7              |    false

Jowisz  |           5.2              |    true

Saturn  |           9.53             |    true

Uran    |          19.19             |    true

Neptun  |          30.06             |    true

Pluton  |          39.48             |  false/true

