from fibonacci import fib


def test_first_two():
    assert fib(0) == 0
    assert fib(1) == 1


def test_two():
    assert fib(2) == 1


def test_thirteen():
    assert fib(13) == 233
