## Movie - model danych
## Tyle objektów co linii
##__dict - serializacja
##zwrócić serializowane pliki

#Movie
class Movie:
    id: int
    title: str
    genres:str

    def __init__(self, id:int, title:str, genres:str):
        self.id=id
        self.title=title
        self.genres


#implementacja__dict__
