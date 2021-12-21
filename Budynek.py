class Budynek:
    def __init__(self, nazwa_inwestycji: str,
                 pokoje: int,
                 powierzchnia: float,
                 ogrzewanie: str,
                 adres: str):
        self.nazwa_inwestycji = nazwa_inwestycji
        self.pokoje = pokoje
        self.powierzchnia = powierzchnia
        self.ogrzewanie = ogrzewanie
        self.adres = adres

    @property
    def nazwa_inwestycji(self) -> None:
        return self.nazwa_inwestycji

    @property
    def pokoje(self) -> None:
        return self.pokoje

    @property
    def powierzchnia(self) -> None:
        return self.powierzchnia

    @property
    def ogrzewanie(self) -> None:
        return self.ogrzewanie

    @property
    def adres(self) -> None:
        return self.adres

    def __str__(self):
        return f'Budynek z {self.nazwa_inwestycji}' \
               f'0 {self.pokoje} pokoj..' \
               f'o powierzchni {self.powierzchnia}' \
               f'ogrzewane {self.ogrzewanie} i znajdujące' \
               f'sie pod adresem {self.adres}'
