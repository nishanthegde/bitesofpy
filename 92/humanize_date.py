from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()

MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60

TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2 * MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2 * HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2 * DAY, 'yesterday', None),
)


def n_days_ago_str(days):
    return (NOW - timedelta(days=days)).strftime('%m/%d/%y')


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""

    if type(date) is not datetime:
        raise ValueError('arg must be datetime')

    if date < NOW:
        if list(t for t in TIME_OFFSETS if (NOW - date).total_seconds() < t.offset):
            t_off = sorted(list(t for t in TIME_OFFSETS if (NOW - date).total_seconds() < t.offset), key=lambda x: x.offset)[0]
            if t_off.divider:
                n = (NOW - date).total_seconds() / t_off.divider
                return t_off.date_str.format(int(n))
            else:
                if t_off.offset == MINUTE:
                    return t_off.date_str.format(int((NOW - date).total_seconds()))

            return t_off.date_str
        else:
            return date.strftime('%m/%d/%y')
    else:
        raise ValueError('arg must be before now')


# def main():

#     print('here ...')
#     # print([type(t) for t in TIME_OFFSETS])
#     print(NOW)
#     # print(n_days_ago_str(365))
#     # (NOW - timedelta(seconds=2), 'just now'),
#     # (NOW - timedelta(seconds=9), 'just now'),
#     # (NOW - timedelta(seconds=10), '10 seconds ago'),
#     # (NOW - timedelta(seconds=59), '59 seconds ago'),
#     # (NOW - timedelta(minutes=1), 'a minute ago'),
#     # (NOW - timedelta(minutes=1, seconds=40), 'a minute ago'),
#     # (NOW - timedelta(minutes=2), '2 minutes ago'),
#     # (NOW - timedelta(minutes=59), '59 minutes ago'),
#     # (NOW - timedelta(hours=1), 'an hour ago'),
#     # (NOW - timedelta(hours=2), '2 hours ago'),
#     # (NOW - timedelta(hours=23), '23 hours ago'),
#     # (NOW - timedelta(hours=24), 'yesterday'),
#     # (NOW - timedelta(hours=47), 'yesterday'),
#     # (NOW - timedelta(days=1), 'yesterday'),

#     print(pretty_date(NOW - timedelta(seconds=2)))
#     print(pretty_date(NOW - timedelta(seconds=9)))
#     print(pretty_date(NOW - timedelta(seconds=10)))
#     print(pretty_date(NOW - timedelta(seconds=59)))
#     print(pretty_date(NOW - timedelta(minutes=1)))
#     print(pretty_date(NOW - timedelta(minutes=1)))
#     print(pretty_date(NOW - timedelta(minutes=2)))
#     print(pretty_date(NOW - timedelta(minutes=59)))
#     print(pretty_date(NOW - timedelta(hours=1)))
#     print(pretty_date(NOW - timedelta(hours=2)))
#     print(pretty_date(NOW - timedelta(hours=23)))
#     print(pretty_date(NOW - timedelta(hours=24)))
#     print(pretty_date(NOW - timedelta(hours=47)))
#     print(pretty_date(NOW - timedelta(days=1)))

#     print(pretty_date(NOW - timedelta(days=2)))
#     print(pretty_date(NOW - timedelta(days=7)))
#     print(pretty_date(NOW - timedelta(days=100)))
#     print(pretty_date(NOW - timedelta(days=365)))

#     # print(pretty_date(123))
#     # print(pretty_date(NOW + timedelta(days=1)))


# if __name__ == '__main__':
#     main()
