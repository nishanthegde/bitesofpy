import pytest

from numbers_to_dec import list_to_decimal


def test_in_range():
    assert list_to_decimal([0, 4, 2, 8]) == 428


def test_type1():
    with pytest.raises(TypeError):
        list_to_decimal([2, True])


def test_type2():
    with pytest.raises(TypeError):
        list_to_decimal([2, 3, .1])


def test_type3():
    with pytest.raises(TypeError):
        list_to_decimal([2, 3, 'nishant'])


def test_value1():
    with pytest.raises(ValueError):
        list_to_decimal([2, 3, 999])


def test_value2():
    with pytest.raises(ValueError):
        list_to_decimal([2, 3, -1])


# def main():
#     print('thank you for everything you have given me...')


# if __name__ == '__main__':
#     main()
