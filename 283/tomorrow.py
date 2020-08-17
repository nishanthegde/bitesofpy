import datetime
from datetime import date


def tomorrow(*args):
    if not args:
        return date.today() + datetime.timedelta(days=1)
    else:
        for x in args:
            return x + datetime.timedelta(days=1)

