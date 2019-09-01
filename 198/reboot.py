import re
import datetime


MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""

MAC2 = """
reboot ~ Tue Sep 22 12:52
reboot ~ Sun Aug 30 23:17
reboot ~ Sat Aug 29 01:12
reboot ~ Fri Aug 28 22:07
"""

MAC3 = """
reboot    ~                         Fri Dec 18 23:58
reboot    ~                         Mon Dec 14 09:54
reboot    ~                         Wed Dec 11 23:21
reboot    ~                         Tue Nov 17 21:52
reboot    ~                         Tue Nov 17 06:01
reboot    ~                         Wed Nov 11 12:14
reboot    ~                         Sat Oct 31 13:40
reboot    ~                         Wed Oct 28 15:56
reboot    ~                         Wed Oct 28 11:35
reboot    ~                         Tue Oct 27 00:00
reboot    ~                         Sun Oct 18 17:28
reboot    ~                         Sun Oct 18 17:11
reboot    ~                         Mon Oct  5 09:35
reboot    ~                         Sat Oct  3 18:57
"""


def calc_max_uptime(reboots):
  """Parse the passed in reboots output,
     extracting the datetimes.

     Calculate the highest uptime between reboots =
     highest diff between extracted reboot datetimes.

     Return a tuple of this max uptime in days (int) and the
     date (str) this record was hit.

     For the output above it would be (30, '2019-02-17'),
     but we use different outputs in the tests as well ...
  """

  now = datetime.datetime.now()

  times = []
  max_day_delta = 0

  pattern_regex = re.compile(r'^reboot.*(Mon|Tue|Wed|Thu|Fri|Sat|Sun).*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{1,2})\s+(\d{2}:\d{2}).*', re.MULTILINE)

  for match in pattern_regex.finditer(reboots):

    day_name_of_week = match.group(1)
    month_name = match.group(2)
    day_of_month = match.group(3)
    time = match.group(4)

    reboot_time = '{} {} {} {}'.format(match.group(2), ('0' + match.group(3))[-2:], str(now.year), match.group(4))

    times.append(datetime.datetime.strptime(reboot_time, '%b %d %Y %H:%M'))

    times = sorted(times)

  for i in range(0, len(times)):
    if i == 0:
      continue
    delta = (times[i] - times[i - 1]).days

    if delta > max_day_delta:
      max_day_delta = delta
      hit = times[i]
    # print(times[i], type(delta))

  return (max_day_delta, hit.strftime('%Y-%m-%d'))


# def main():

#   # print("dance ...")
#   # print(calc_max_uptime(MAC1))
#   assert calc_max_uptime(MAC1) == (30, '2019-02-17')
#   assert calc_max_uptime(MAC2) == (22, '2019-09-22')
#   assert calc_max_uptime(MAC3) == (24, '2019-12-11')
#   # print(calc_max_uptime(MAC2))
#   # print(calc_max_uptime(MAC3))

#   # s = "8 March, 2017"
#   # s = "Oct 03 2019 18:57"
#   # print(datetime.datetime.strptime(s, '%b %d %Y %H:%M'))


# if __name__ == '__main__':
#   main()
