import json
from operator import attrgetter
from movie import Movie


class MovieCollection:
    """A collection of Movie objects."""

    def __init__(self):
        self.movies = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def load_movies(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.movies = [Movie.from_dict(m) for m in data]

    def save_movies(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([m.to_dict() for m in self.movies], file, indent=4)

    def get_number_watched(self):
        return len([m for m in self.movies if m.is_watched])

    def get_number_unwatched(self):
        return len([m for m in self.movies if not m.is_watched])

    def sort(self, key):
        self.movies.sort(key=attrgetter(key, "title"))
