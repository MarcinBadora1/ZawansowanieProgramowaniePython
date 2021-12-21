from Budynek import Budynek


class Dom(Budynek):
    def __init__(self, zmienna1: str,
                 zmienna2: int,
                 zmienna3: int,
                 zmienna4: str):
        self.zmienna1 = zmienna1
        self.zmienna2 = zmienna2
        self.zmienna3 = zmienna3
        self.zmienna4 = zmienna4

    @property
    def zmienna1(self) -> None:
        return self.zmienna1

    @property
    def zmienna2(self) -> None:
        return self.zmienna2

    @property
    def zmienna4(self) -> None:
        return self.zmienna2

    @property
    def zamien3(self) -> None:
        return self.zmienna3

    def __str__(self):
        return f'Deweloper :{self.zmienna1}' \
               f'buduje {self.zmienna2} mieszkan' \
               f'na wielu {self.zmienna4} budowach' \
               f'specjalizuje sie w {self.zmienna3}, do widzenia!'
