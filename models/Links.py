from models.Movie import Movie


class Links():
    def __init__(self, id: Movie, imdbId: str, tmdbId: str):
        self.id = id
        self.imdbId = imdbId
        self.tmdbId = tmdbId