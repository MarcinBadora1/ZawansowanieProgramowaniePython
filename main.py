# Zadanie1
class Odcinek:
    A: str
    B: str
    punkt_A1: float
    punkt_A2: float
    punkt_B1: float
    punkt_B2: float
    droga_km: float

    def __init__(self, A: str, B: str, punkt_A1: float, punkt_A2: float, punkt_B1: float, punkt_B2: float,
                 droga_km: float):
        self.A = A
        self.B = B
        self.punkt_A1 = punkt_A1
        self.punkt_A2 = punkt_A2
        self.punkt_B1 = punkt_B1
        self.punkt_B2 = punkt_B2
        self.droga_km = droga_km

    def __str__(self):
        return f"Odcinek przewozowy zawierający punkt startowy i końcowy A {self.A}, oraz B {self.B}"


class Pojazd:
    Marka: str
    Model: str
    Rok_prod: int
    Przebieg: int
    Ladownosc: float

    def __init__(self, Marka: str, Model: str, Rok_prod: int, Przebieg: int, Ladownosc: float):
        self.Marka = Marka
        self.Model = Model
        self.Rok_prod = Rok_prod
        self.Przebieg = Przebieg
        self.Ladownosc = Ladownosc

    def __str__(self):
        return f"{self.Marka}_{self.Model} o ładowności {self.Ladownosc}"


class Firma:
    nazwa: str
    siedziba: str
    rentownosc: bool
    czy_aktywna: bool

    def __init__(self, nazwa: str, siedziba: str, rentownosc: bool, czy_aktywna: bool, pojazdy: list):
        self.nazwa = nazwa
        self.siedziba = siedziba
        self.rentownosc = rentownosc
        self.czy_aktywna = czy_aktywna
        self.pojazdy = pojazdy

    def __str__(self):
        return f"Obiekt z firmy {self.nazwa}"


class FirmaTransportowa(Firma):
    pojazdy: list

    def __init__(self, nazwa: str, siedziba: str, rentownosc: bool, czy_aktywna: bool, pojazdy: list):
        Firma.__init__(nazwa, siedziba, rentownosc, czy_aktywna)
        self.pojazdy = pojazdy

    def __str__(self):
        return f"Firma transportowa {self.nazwa}"


class FirmaSpozywcza(Firma):
    typ_prowadzonej_dzialalnosci: str
    punkt_dostaw_A: str
    punkt_dostaw_B: str

    def __init__(self, nazwa: str, siedziba: str, rentownosc: bool, czy_aktywna: bool,
                 typ_prowadzonej_dzialalnosci: str, punkt_dostaw_A: str, punkt_dostaw_B: str):
        Firma.__init__(nazwa, siedziba, rentownosc, czy_aktywna)
        self.typ_prowadzonej_dzialalnosci = typ_prowadzonej_dzialalnosci
        self.punkt_dostaw_A = punkt_dostaw_A
        self.punkt_dostaw_B = punkt_dostaw_B

    def __str__(self):
        return f"Firma {self.nazwa} zajmuje się {self.typ_prowadzonej_dzialalnosci} w miejscowowsci {self.siedziba}"


class Kurs:
    odcinki: list[Odcinek]
    pojazd: Pojazd
    firmaTransportowa: FirmaTransportowa
    waga = float
    czy_przeladowany: bool

    def __init__(self, odcinki: list[Odcinek], pojazd: Pojazd, firmaTransportowa: FirmaTransportowa, waga: float):
        self.odcinki = odcinki
        self.pojazd = pojazd
        self.firmaTransportowa = firmaTransportowa
        self.waga = waga
        self.czy_przeladowany = pojazd.Ladownosc < waga

    def __str__(self):
        return f"Kurs na fragmencie od {self.odcinki.pop(1).A} do {self.odcinki.pop(2)} realizowany przez {self.pojazd.Model} {self.pojazd.Marka}"

    def get_odcinki(self):
        return self.odcinki

    def set_odcinki(self, x):
        self.odcinki = x

    def get_pojazd(self):
        return self.pojazd

    def set_pojazd(self, x):
        self.pojazd = x

    def get_firmaTransportowa(self):
        return self.firmaTransportowa

    def set_firmaTransportowa(self, x):
        self.firmaTransportowa = x

    def get_waga(self):
        return self.waga

    def set_waga(self, x):
        self.waga = x

    def count_km(self) -> float:
        licznik = 0.0
        for odc in self.odcinki:
            licznik = licznik + odc.droga_km
        return licznik

    def pojazd_kursu(self):
        return self.pojazd.Marka


pojazd1 = Pojazd("Scania", "Model2", 2012, 457000, 25760.2)
pojazd2 = Pojazd("DAF", "Model3", 2017, 258000, 26853.2)
list_pojazdy = []
list_pojazdy.append(pojazd1)
list_pojazdy.append(pojazd2)
firmaTransportowa = FirmaTransportowa("Tomek_jedzie", "Warszawa 02-007, Koszyki 12", True, True, list_pojazdy)
odcinek_1 = Odcinek("Mala Gorka", "Duza Gorka", 51.22, 47.30, 51.221, 47.301,20.0)
odcinek_2 = Odcinek("Duza Gorka", "Hale", 51.221, 47.301, 51.23, 47.303, 37.12)
odcinek_3 = Odcinek("Hale", "Magazyn", 51.23, 47.303, 51.20, 47.312, 50.1)
odcinki = []
odcinki.append(odcinek_1)
odcinki.append(odcinek_2)
odcinki.append(odcinek_3)
kurs1 = Kurs()
kurs1.set_odcinki(odcinki)
kurs1.set_pojazd(firmaTransportowa.pojazdy.pop())
kurs1.set_waga(12000.01)
kurs1.set_firmaTransportowa(firmaTransportowa.pojazdy.pop(1))

print(kurs1)
