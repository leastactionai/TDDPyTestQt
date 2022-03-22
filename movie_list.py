class MovieList():
    def __init__(self) -> None:
        self.number_of_movies = 0

    def size(self) -> int:
        return self.number_of_movies

    def add(self, movie_to_add) -> None:
        self.number_of_movies += 1

