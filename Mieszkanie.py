from Budynek import Budynek


class Mieszkanie(Budynek):
    def __init__(self, lokal: str,
                 pietro: int,
                 ilosc_klatek: int,
                 ilosc_mieszkan_suma: int):
        self.lokal = lokal
        self.pietro = pietro
        self.ilosc_klatek = ilosc_klatek
        self.ilosc_mieszkan_suma = ilosc_mieszkan_suma

    @property
    def lokal(self) -> None:
        return self.lokal

    @property
    def pietro(self) -> None:
        return self.pietro

    @property
    def ilosc_klatek(self) -> None:
        return self.ilosc_klatek

    @property
    def ilosc_mieszkan_suma(self) -> None:
        return self.ilosc_mieszkan_suma

    def __str__(self):
        return f'Deweloper :{self.lokal}' \
               f'buduje {self.pietro} mieszkan' \
               f'na wielu {self.ilosc_klatek} budowach' \
               f'specjalizuje sie w {self.ilosc_mieszkan_suma}, do widzenia!'