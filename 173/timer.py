from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """

    days = 0
    days_pattern = re.compile(r'(\d+)d')
    days_match = days_pattern.search(delay_time)
    if days_match:
        days = int(days_match.group(1))

    hrs = 0
    hrs_pattern = re.compile(r'(\d+)h')
    hrs_match = hrs_pattern.search(delay_time)
    if hrs_match:
        hrs = int(hrs_match.group(1))
    mins = 0
    mins_pattern = re.compile(r'(\d+)m')
    mins_match = mins_pattern.search(delay_time)
    if mins_match:
        mins = int(mins_match.group(1))

    secs = 0
    secs_pattern = re.compile(r'(\d+)[\s|s]')
    secs_match = secs_pattern.search(delay_time)
    if secs_match:
        secs = int(secs_match.group(1))

    secs_pattern2 = re.compile(r'(\d+)$')
    secs_match = secs_pattern2.search(delay_time)
    if secs_match:
        secs = int(secs_match.group(1))

    at_time = str(start_time + timedelta(days=days, hours=hrs, minutes=mins, seconds=secs))
    return '{} @ {}'.format(task, at_time)


# def main():
#     print('here')
#     print(add_todo("11h 10m", "Wash my car"))
#     print(add_todo("45", "Finish this Test"))
#     print(add_todo("5m 3s", "Go to Bed"))
#     print(add_todo("1d 10h 47m 17s", "Study some Python"))
#     print(add_todo("30d", "Code a Bites"))


# if __name__ == '__main__':
#     main()
