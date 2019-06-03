from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'
CURRENT_PATH = os.getcwd()

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)
# LOGFILE = os.path.join(CURRENT_PATH, 'log')
# urllib.request.urlretrieve('http://bit.ly/2AKSIbf', LOGFILE)

# read log file and create list of lines
f = open(logfile, 'r')
loglines = f.readlines()
f.close

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """

    # yr = datetime.strptime(line, '%Y')
    # p = re.search("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", line).start()
    # find timestamp in line. use find iter for cases with multiple occurrences

    iter = re.finditer("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", line)
    st_indices = [s.start(0) for s in iter]

    # extract timestamp from string
    # cases where there are multiple matches found, return first instance
    ts_str = line[st_indices[0]:st_indices[0]+19]

    # convert to string to datetime
    ts_dt = datetime.strptime(ts_str, '%Y-%m-%dT%H:%M:%S')

    return ts_dt


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    # list of timestamps of shutdown initiations
    shutdown_stamps = []

    # read in loglines
    for l in loglines:
      if "shutdown initiated" in l.lower():
        ts_dt = convert_to_datetime(l)
        shutdown_stamps.append(ts_dt)

    time_delta = shutdown_stamps[-1] - shutdown_stamps[0]
    return time_delta


