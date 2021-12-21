class Zamowienie:
    def __init__(self, zamowienie_id: int,
                 deweloper: str,
                 adres: str,
                 metraz: float):
        self.zamowienie_id = zamowienie_id
        self.deweloper = deweloper
        self.adres = adres
        self.metraz = metraz

    @property
    def zamowienie_id(self) -> None:
        return self.zamowienie_id

    @property
    def deweloper(self) -> None:
        return self.deweloper

    @property
    def adres(self) -> None:
        return self.adres

    @property
    def metraz(self) -> None:
        return self.metraz

    @zamowienie_id.setter
    def zamowienie_id(self, zamowienie_id: int):
        self.zamowienie_id = zamowienie_id

    @deweloper.setter
    def deweloper(self, deweloper: str):
        self.deweloper = deweloper

    @adres.setter
    def adres(self, adres: str):
        self.adres = adres

    @metraz.setter
    def metraz(self, metraz: float):
        self.metraz = metraz

    def __str__(self):
        return f'Zamowienie :{self.zamowienie_id}' \
               f'od  {self.deweloper}(deweloper)' \
               f'pod adresem {self.adres}' \
               f'w metrazu {self.metraz}'
