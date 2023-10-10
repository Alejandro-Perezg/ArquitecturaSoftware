import pytest
from calculator import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (3, 4, 7), (-1, -2, -3)])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, -1), (3, 4, -1), (-1, -2, 1)])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 2), (3, 4, 12), (-1, -2, 2)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (3, 4, 0.75), (-1, -2, 0.5)])
def test_divide(a, b, expected):
    assert divide(a, b) == expected