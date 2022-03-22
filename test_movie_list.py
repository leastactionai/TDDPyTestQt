import pytest

from movie_list import MovieList
from movie import Movie


def test_empty_list_size():
    empty_list = MovieList()
    assert empty_list.size() == 0, "Size of empty movie list should be 0."


def test_size_after_adding_one():
    star_wars = Movie()
    one_item_list = MovieList()
    one_item_list.add(star_wars)
    assert one_item_list.size() == 1, "Size of one item list should be 1."


def test_size_after_adding_two():
    star_wars = Movie()
    star_trek = Movie()
    two_item_list = MovieList()
    two_item_list.add(star_wars)
    two_item_list.add(star_trek)
    assert two_item_list.size() == 2, "Size of two item list should be 2."
