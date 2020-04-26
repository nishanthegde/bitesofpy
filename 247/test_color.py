from unittest.mock import patch, Mock

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def test_gen_hex_color(gen):
    assert isinstance(next(gen), str)


def main():
    print('thank you for everything...')
    # print('shell for 424')
    gen = Mock()
    gen().assert_called()


if __name__ == '__main__':
    main()
