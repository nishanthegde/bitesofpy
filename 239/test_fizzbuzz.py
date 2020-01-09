import pytest
from fizzbuzz import fizzbuzz

# write one or more pytest functions below, they need to start with test_


def test_fizzbuzz():
    assert fizzbuzz(15) == 'Fizz Buzz'


def test_buzz():
    assert fizzbuzz(5) == 'Buzz'


def test_fizz():
    assert fizzbuzz(3) == 'Fizz'


def test_other1():
    assert fizzbuzz(89) == 89


def test_other2():
    assert fizzbuzz(True) == True


def test_other3():
    with pytest.raises(TypeError) as exc:
        fizzbuzz('nishant')
        assert 'not all arguments converted during string formatting' in str(exc)
