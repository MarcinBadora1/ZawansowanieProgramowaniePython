
from datetime import datetime
from models.Movie import Movie
from models.Ratings import Ratings


class Tags():
    def __init__(self, userId: Ratings, id: Movie, tag: str, timestamp: datetime):
        self.userId = userId
        self.id = id
        self.tag = tag
        self.timestamp = timestamp