from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'
CURRENT_PATH = os.getcwd()

# prep: read in the logfile
# logfile = os.path.join('/tmp', 'log')
LOGFILE = os.path.join(CURRENT_PATH, 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', LOGFILE)

# read log file and create list of lines
f = open(LOGFILE, 'r')
loglines = f.readlines()
f.close

# with open(logfile) as f:
#     loglines = f.readlines()

# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """

    str = "shutdown"

    if str in line.lower():
      ts_str = line[5:24]
      print(ts_str)



def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    pass

for l in loglines:
  convert_to_datetime(l)
