import pytest

from movie_list import MovieList
from movie import Movie


@pytest.fixture()
def setup():
    print("------------ SETUP ----------------")
    movie_list = MovieList()
    star_wars = Movie()
    star_trek = Movie()
    yield movie_list, star_wars, star_trek
    print("----- TEARDOWN -----")


class TestMovieList:
    def test_empty_list_size(self, setup):
        assert setup[0].size() == 0, "Size of empty movie list should be 0."

    def test_size_after_adding_one(self, setup):
        setup[0].add(setup[1])
        assert setup[0].size() == 1, "Size of one item list should be 1."

    def test_size_after_adding_two(self, setup):
        setup[0].add(setup[1])
        setup[0].add(setup[2])
        assert setup[0].size() == 2, "Size of two item list should be 2."
