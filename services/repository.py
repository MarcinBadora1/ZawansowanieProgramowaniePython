from services.utils import read_file
from models.Movie import Movie
import csv


def get_movies_data():  # pobiera obiekty z pliku
    data = read_file('data/movies.csv')
    movies = []
    for movie in data.split('\n'):
        if len(movie) and 'movieId' not in movie:
            movie = movies.split(',')
            movies.append(movie)
    return movies


def get_movies():  # serializowane dane
    print(get_movies_data())
    return [Movie(movie[0], movie[1], movie[2]).__dict__ for movie in get_movies_data()]
