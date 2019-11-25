from pathlib import Path
from urllib.request import urlretrieve
import os
import re
# from collections import defaultdict

# local = os.getcwd()
tmp = Path('/tmp')
# tmp = Path(local)
timings_log = tmp / 'pytest_timings.out'

if not timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )

# read log
with open(timings_log) as f:
    loglines = f.readlines()


def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    d = {}  # defaultdict(list)  # dict to store times
    min_times = list()  # list to store min avg times
    pattern = re.compile(r'^(\d+)\s+=+\s+(\d+)\s+passed[\w\s,]+in\s(\d*\.?\d+)')
    for t in timings:
        m = pattern.search(t)
        if m:
            bite = m.group(1)
            passed = int(m.group(2))
            secs = float(m.group(3))
            avg_time = secs / passed
            d[bite] = avg_time

    # get min avg_time from d
    min_avg_time = min(d.items(), key=lambda x: x[1])

    for key, value in d.items():
        if value == min_avg_time[1]:
            min_times.append(key)

    # if len(min_times) == 1:
    #     return min_times[0]
    # else:
    #     return min_times[0]

    return min_times[0]

# def main():
#     print('thank you for the waves and the ocean...')
#     actual = str(get_bite_with_fastest_avg_test(loglines[:50]))
#     # print(type(actual))
#     # print(type(actual))
#     # print(type(('60', '87')))
#     expected_bites = ('60', '87')

#     if type(expected_bites) == tuple:
#         assert actual in expected_bites
#     else:
#         assert actual == expected_bites


# if __name__ == '__main__':
#     main()
