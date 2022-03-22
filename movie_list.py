class MovieList:
    def __init__(self) -> None:
        self.movies = []

    def size(self) -> int:
        return len(self.movies)

    def add(self, movie_to_add) -> None:
        self.movies.append(movie_to_add)

    def contains(self, movie_to_check_for) -> bool:
        return movie_to_check_for in self.movies

