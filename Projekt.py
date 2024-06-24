#klasa Miejsca Teatralne
#Klasa bazowa

class MiejscaTeatralne:
    def __init__(self,numer,cena):
        self.numer = numer
        self.cena = cena
        self.dostepnosc = True
        self.klient = None

#zezerwacja i anulowanie rezerwacji

    def rezerwacja(self, klient):
        if self.dostepnosc:
            self.dostepnosc = False
            self.klient = klient
            klient.zarezerwuj_miejsce(self)
            return True
        return False

    def anulowanie_rezerwacji(self):
        if not self.dostepnosc:
            self.dostepnosc = True
            klient = self.klient
            self.klient = None
            klient.anuluj_rezerwacje(self)
            return True
        return False

    def __str__(self):
        return f"Miejsce numer {self.numer}, Cena: {self.cena}, Dostępność: {"Dostępne" if self.dostepnosc else "Zarezerwowane"}"

#klasy pochodne

class MiejsceZwykle(MiejscaTeatralne):
    def __init__(self,numer,cena):
        super().__init__(numer, cena)


class MiejsceVIP(MiejscaTeatralne):
    def __init__(self,numer,cena,oplata_dodatkowa,udogodnieniaVIP):
        super().__init__(numer, cena + oplata_dodatkowa)
        self.oplata_dodatkowa = oplata_dodatkowa
        self.udogodnieniaVIP = udogodnieniaVIP


class MiejsceDlaNiepelnosprawnych(MiejscaTeatralne):
    def __init__(self,numer,cena, udogodnienia):
        super().__init__(numer, cena)
        self.udogodnienia = udogodnienia

#klasa Teatr

class Teatr:
    def __init__(self):
        self.miejsce = []

    def dodanie_miejsca(self,miejsce):
        self.miejsce.append(miejsce)

    def pokaz_wolne_miejsca(self):
        return [miejsce for miejsce in self.miejsce if miejsce.dostepnosc]

    def rezerwacja_miejsca(self, numer, Klient):
        for miejsce in self.miejsce:
            if miejsce == numer:
                return miejsce.zarezrwuj(Klient)
        return False

    def anulowanie_rezerwacji(self,numer):
        for miejsce in self.miejsce:
            if miejsce.numer == numer:
                return miejsce.anulowanie_rezerwacji()
        return False

#Klasa Klient

class Klient:
    def __init__(self, id, imie, nazwisko):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.lista_rezerwacji = []

    def dodaj_rezerwacje(self,miejsce):
        self.lista_rezerwacji.append(miejsce)

    def usuwanie_rezerwacji(self, miejsce):
        self.lista_rezerwacji.remove(miejsce)

    def pokaz_liste_rezerwacji(self):
        return self.lista_rezerwacji

teatr = Teatr()

teatr.dodanie_miejsca(MiejsceZwykle(1,50))
teatr.dodanie_miejsca(MiejsceZwykle(2,50))
teatr.dodanie_miejsca(MiejsceZwykle(3,50))
teatr.dodanie_miejsca(MiejsceZwykle(4,50))
teatr.dodanie_miejsca(MiejsceZwykle(5,50))
teatr.dodanie_miejsca(MiejsceZwykle(6,50))
teatr.dodanie_miejsca(MiejsceZwykle(7,50))
teatr.dodanie_miejsca(MiejsceZwykle(8,50))
teatr.dodanie_miejsca(MiejsceZwykle(9,50))
teatr.dodanie_miejsca(MiejsceZwykle(10,50))

teatr.dodanie_miejsca(MiejsceVIP(11,50,50,"Napój + popcorn, wiecej miejsca"))
teatr.dodanie_miejsca(MiejsceVIP(12,50,50,"Napój + popcorn, wiecej miejsca"))
teatr.dodanie_miejsca(MiejsceVIP(13,50,50,"Napój + popcorn, wiecej miejsca"))
teatr.dodanie_miejsca(MiejsceVIP(14,50,50,"Napój + popcorn, wiecej miejsca"))
teatr.dodanie_miejsca(MiejsceVIP(15,50,50,"Napój + popcorn, wiecej miejsca"))

teatr.dodanie_miejsca(MiejsceDlaNiepelnosprawnych(16,30,"wiecej miejsca, bliżej wejścia"))
teatr.dodanie_miejsca(MiejsceDlaNiepelnosprawnych(17,30,"wiecej miejsca, bliżej wejścia"))
teatr.dodanie_miejsca(MiejsceDlaNiepelnosprawnych(18,30,"wiecej miejsca, bliżej wejścia"))
teatr.dodanie_miejsca(MiejsceDlaNiepelnosprawnych(19,30,"wiecej miejsca, bliżej wejścia"))
teatr.dodanie_miejsca(MiejsceDlaNiepelnosprawnych(20,30,"wiecej miejsca, bliżej wejścia"))

Klient1 = Klient(1969,"Monthy","Python")
Klient2 = Klient(1998,"Karol","Krawczyk")


teatr.rezerwacja_miejsca(10, Klient1)
teatr.rezerwacja_miejsca(12, Klient2)

for miejsce in teatr.pokaz_wolne_miejsca():
    print(miejsce)

for miejsce in Klient1.pokaz_liste_rezerwacji():
    print(miejsce)