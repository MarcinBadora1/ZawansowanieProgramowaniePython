class Developer:
    def __init__(self, nazwa: str,
                 ile_mieszkan: int,
                 ile_budow: int,
                 kategoria_budowanych_lokali: str):
        self.nazwa = nazwa
        self.ile_mieszkan = ile_mieszkan
        self.ile_budow = ile_budow
        self.kategoria_budowanych_lokali = kategoria_budowanych_lokali

    @property
    def nazwa(self) -> None:
        return self.nazwa

    @property
    def ile_mieszkan(self) -> None:
        return self.ile_mieszkan

    @property
    def ile_budow(self) -> None:
        return self.ile_budow

    @property
    def kategoria_budowanych_lokali(self) -> None:
        return self.kategoria_budowanych_lokali

    def __str__(self):
        return f'Deweloper :{self.nazwa}' \
               f'buduje {self.ile_mieszkan} mieszkan' \
               f'na wielu {self.ile_budow} budowach' \
               f'specjalizuje sie w {self.kategoria_budowanych_lokali}, do widzenia!'
