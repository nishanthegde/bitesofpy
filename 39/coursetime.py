import datetime
import os
import re
import urllib.request as ur

# getting the data
# local = os.getcwd()
local = '/tmp'
COURSE_TIMES = os.path.join(local, 'course_timings')
ur.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    ts = []
    with open(COURSE_TIMES,'r') as f:
      lines = [f.lower().strip() for f in f.readlines() if f.lower().strip()]

    p = re.compile(r'([0-5]?\d):([0-5]?\d)')

    for line in lines:
      match = p.search(line)
      if match:
        ts.append(match[0])

    return ts

def get_total_secs(ts_str):
    """Accept timestamp (MM:SS) and return total seconds
    """
    m,s = ts_str.split(":")
    secs = int(datetime.timedelta(minutes=int(m), seconds=int(s)).total_seconds())

    return secs

def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total_secs = sum(get_total_secs(t) for t in timestamps)
    return str(datetime.timedelta(seconds=total_secs))

# def main():
#   timestamps = get_all_timestamps()
#   ts = calc_total_course_duration(timestamps)
#   print(ts)

# if __name__ == "__main__":
#     main()
