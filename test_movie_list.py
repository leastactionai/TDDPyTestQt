import pytest

from movie_list import MovieList

def test_empty_list_size():
    empty_list = MovieList()
    assert empty_list.size() == 0, "Size of empty movie list should be 0."
