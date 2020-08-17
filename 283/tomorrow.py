import datetime
from datetime import date


def tomorrow(today=date.today()):
    return today + datetime.timedelta(days=1)
