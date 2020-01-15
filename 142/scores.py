from collections import namedtuple
from typing import List

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


def calculate_score(scores: List) -> int:
  """Based on a list of score ints (dice roll), calculate the
     total score only taking into account >= MIN_SCORE
     (= eyes of the dice roll).

     If one of the scores is not a valid dice roll (1-6)
     raise a ValueError.

     Returns int of the sum of the scores.
  """
  if [s for s in scores if s not in DICE_VALUES]:
    raise ValueError('only pass in dice values')

  return sum([s for s in scores if s >= MIN_SCORE])


def get_winner(players: List) -> Player:
  """Given a list of Player namedtuples return the player
     with the highest score using calculate_score.

     If the length of the scores lists of the players passed in
     don't match up raise a ValueError.

     Returns a Player namedtuple of the winner.
     You can assume there is only one winner.

     For example - input:
       Player(name='player 1', scores=[1, 3, 2, 5])
       Player(name='player 2', scores=[1, 1, 1, 1])
       Player(name='player 3', scores=[4, 5, 1, 2])

     output:
       Player(name='player 3', scores=[4, 5, 1, 2])
  """

  if [p for p in players if not isinstance(p, Player)]:
    raise ValueError('only pass in players')

  if not all(len(elem.scores) == len(players[0].scores) for elem in players):
    raise ValueError('number of rolls for all players must be the same')

  scores = [calculate_score(p.scores) for p in players]

  return players[scores.index(max(scores))]


def main():
  print('thank you for everything...')
  print(get_winner([
      Player(name='player 1', scores=[1, 3, 2, 5]),
      Player(name='player 2', scores=[1, 1, 1, 1]),
      Player(name='player 3', scores=[4, 5, 1, 2]),  # max 9
  ]))


if __name__ == '__main__':
  main()
