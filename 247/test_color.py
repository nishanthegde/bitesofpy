from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def test_gen_hex_color(gen):
    pass


def main():
    print('thank you for the waves... ')


if __name__ == '__main__':
    main()
