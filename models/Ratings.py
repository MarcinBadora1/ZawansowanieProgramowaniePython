from datetime import datetime
from models.Movie import Movie


class Ratings():
    def __init__(self, userId: str, id: Movie, rating: float, timestamp: datetime):
        self.userId = userId
        self.id = id
        self.rating = rating
        self.timestamp = timestamp