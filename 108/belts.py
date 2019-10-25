from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}

more_belts = dict(brown=BeltStats(400, 2),
                  black=BeltStats(600, 5))

ninja_belts_updated = {**ninja_belts, **more_belts}


def get_total_points(belts: namedtuple=ninja_belts) -> int:
  """Calculate the amount of points rewarded on PyBites given the
     ninja_belts dictionary, formula: belt score x belt owners (aka ninjas)
     (of course there are more points but let's keep it simple)

     Make your code generic so if we update ninja_belts to include
     more belts (which we do in the tests) it will still work.

     Ah and you can get score and ninjas from the namedtuple with nice
     attribute access: belt.score / belt.ninjas (reason why we get
     you familiar with namedtuple here, because we love them and use
     them all over the place!)

     Return the total number of points int from the function."""
  return sum([v.score * v.ninjas for v in belts.values()])


# def main():
#   print('zone in ...')
#   print(get_total_points(ninja_belts_updated))


# if __name__ == '__main__':
#   main()
