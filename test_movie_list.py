import pytest

from movie_list import MovieList
from movie import Movie


@pytest.fixture()
def movie_list():
    movie_list = MovieList()
    yield movie_list


@pytest.fixture()
def star_wars():
    star_wars = Movie()
    yield star_wars


@pytest.fixture()
def star_trek():
    star_trek = Movie()
    yield star_trek


@pytest.fixture()
def star_gate():
    star_gate = Movie()
    yield star_gate


class TestMovieList:
    def test_empty_list_size(self, movie_list):
        assert movie_list.size() == 0, "Size of empty movie list should be 0."

    def test_size_after_adding_one(self, movie_list, star_wars):
        movie_list.add(star_wars)
        assert movie_list.size() == 1, "Size of one item list should be 1."

    def test_size_after_adding_two(self, movie_list, star_wars, star_trek):
        movie_list.add(star_wars)
        movie_list.add(star_trek)
        assert movie_list.size() == 2, "Size of two item list should be 2."

    def test_contents(self, movie_list, star_wars, star_trek, star_gate):
        movie_list.add(star_wars)
        movie_list.add(star_trek)
        assert movie_list.contains(star_wars), "List should contain star_wars"
        assert movie_list.contains(star_trek), "List should contain star_trek"
        assert not movie_list.contains(star_gate), "List should not contain star_gate"
