from datetime import datetime
import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """
        Receive a utc datetime and one or more timezones and check if
        they are all within schedule (MEETING_HOURS)
    """
    if not set(tz for tz in timezones) <= TIMEZONES:
        raise ValueError("invalid timezone")

    local_hours = []
    for tz in timezones:
        tz = pytz.timezone(tz)
        local_hours.append(pytz.utc.localize(utc, is_dst=None).astimezone(tz).hour)

    if all([i in MEETING_HOURS for i in local_hours]):
        return True

    return False

# def main():
#     """
#         Complete the function below receiving a UTC datetime and one or more timezones (US/Arizona, Europe/Madrid, etc).

#         Use pytz to see if the given datetime is in MEETING_HOURS for all provided timezones. Return a boolean.

#         If a wrong timezone is given raise a ValueError.


#     """
#     # print([h for h in MEETING_HOURS])
#     # print(type(TIMEZONES))
#     # print(TIMEZONES)

#     # dt = datetime(2018, 4, 18, 13, 28)
#     # print(dt)
#     # # print(type(dt))
#     # tz = pytz.timezone('Europe/Madrid')
#     # print(pytz.utc.localize(dt, is_dst=None).astimezone(tz))

#     # tz = pytz.timezone('Australia/Sydney')
#     # print(pytz.utc.localize(dt, is_dst=None).astimezone(tz))

#     # tz = pytz.timezone('America/Chicago')
#     # print(pytz.utc.localize(dt, is_dst=None).astimezone(tz))

#     # tz = pytz.timezone('nishant')
#     # print(pytz.utc.localize(dt, is_dst=None).astimezone(tz))

#     # dt = datetime(2018, 4, 18, 13, 28)
#     # dt = datetime(2018, 4, 18, 12, 28)
#     # timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
#     # timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']

#     # timezones = ['Europe/Madrid', 'bogus']
#     print(within_schedule(dt, *timezones))

# if __name__ == "__main__":
#     main()
