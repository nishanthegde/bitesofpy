from unittest.mock import patch, Mock, MagicMock

import pytest
import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def test_gen_hex_color(gen):
    assert isinstance(next(gen), str)


def test_gen_hex_color_len(gen):
    assert len(next(gen)) == 7


# def test_gen_hex_color_range(gen):
#     assert '100' not in next(gen)

@patch('color.sample', MagicMock(side_effect=[(0, 144, 255)]))
def test_gen_random_called(gen):
    # with patch('color.sample', return_value=(0, 144, 255)) as mock_random:
    assert next(gen) == '#0090FF'


# def test_gen_random_called2(gen):
#     with patch('color.sample', return_value=(0, 144, 255)) as mock_random:
#         assert next(gen)


# def main():
#     print(next(gen)2)
#     print(next(color.gen_hex_color()))


# if __name__ == '__main__':
#     main()
