import sys
import pytest

from workouts import print_workout_days


def test_print_workout_days(capfd):
    print_workout_days('Upper')
    captured = capfd.readouterr()
    assert captured.out == 'Mon, Thu\n'


# def main():
#     print('thank you for this life... help me find a way to give back, do seva...')
#     test_print_workout_days(sys.stdout)


# if __name__ == '__main__':
#     main()
