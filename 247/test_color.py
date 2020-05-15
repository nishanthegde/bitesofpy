from unittest.mock import patch, Mock

import pytest
import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def test_gen_hex_color(gen):
    assert isinstance(next(gen), str)


def test_gen_random_called(gen):
    with patch('color.sample', return_value=(108, 144, 121)) as mock_random:
        assert next(gen) == '#6C9079'

# def main():
#     print(next(gen))
#     print(next(color.gen_hex_color()))


# if __name__ == '__main__':
#     main()
