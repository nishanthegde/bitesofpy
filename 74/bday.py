import calendar
from datetime import date


def weekday_of_birth_date(date: date) ->str:
    """Takes a date object and returns the corresponding weekday string"""
    return date.strftime('%A')


# def main():
#     print('thank you for these problems...')
#     dt = date(1974, 11, 11)
#     dt = date(1978, 9, 8)
#     dt = date(1946, 12, 28)
#     # assert weekday_of_birth_date(dt) == 'Monday'
#     print(weekday_of_birth_date(dt))


# if __name__ == '__main__':
#     main()
