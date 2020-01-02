import sys
import pytest

from workouts import print_workout_days


def test_print_workout_days(capfd):
    print_workout_days('Upper')
    captured = capfd.readouterr()
    assert captured.out == 'Mon, Thu\n'

    print_workout_days('LOWEr')
    captured = capfd.readouterr()
    assert captured.out == 'Tue, Fri\n'

    print_workout_days('cardio')
    captured = capfd.readouterr()
    assert captured.out == 'Wed\n'

    print_workout_days('nishant')
    captured = capfd.readouterr()
    assert captured.out == 'No matching workout\n'


# def main():
#     print('thank you for this life... help me find a way to give back, do seva...')
#     test_print_workout_days(sys.stdout)


# if __name__ == '__main__':
#     main()
