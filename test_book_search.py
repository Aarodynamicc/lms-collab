# test_book_search.py (Student A)
import pytest
from book_search import search_books


def test_search_by_title():
    assert len(search_books("clean")) == 1


def test_search_by_author():
    assert search_books("pressman")[0]["author"] == "Roger Pressman"


def test_search_no_match():
    assert search_books("python") == []


def test_empty_keyword_raises():
    with pytest.raises(ValueError):
        search_books(" ")
