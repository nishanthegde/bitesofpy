from datetime import date, timedelta, datetime

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date(start_date: date = start_100days) -> str:
    """Return a string of yyyy-mm-dd"""
    return datetime.strftime(start_100days + timedelta(days=100), "%Y-%m-%d")


def get_days_between_pb_start_first_joint_pycon(start_date: date = pybites_founded, end_date: date = pycon_date) -> int:
    """Return the int number of days"""
    return (end_date - start_date).days


# def main():

#     print('thank you...')
#     print(get_hundred_days_end_date())

#     assert get_hundred_days_end_date() == '2017-07-08'
#     assert get_days_between_pb_start_first_joint_pycon() == 505


# if __name__ == '__main__':
#     main()
