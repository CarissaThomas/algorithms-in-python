from array import array

from search import linear_search


def test_valid_linear_search():
    assert linear_search(array('i', [1, 2, 3, 4, 5]), 3) == True

def test_invalid_linear_search():
    assert linear_search(array('i', [1, 2, 3, 4, 5]), 7) == False
