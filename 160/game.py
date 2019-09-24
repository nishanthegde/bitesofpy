import csv
import os
from urllib.request import urlretrieve

import operator
local = '/tmp'
# local = os.getcwd()

BATTLE_DATA = os.path.join(local, 'battle-table.csv')

if not os.path.isfile(BATTLE_DATA):
  urlretrieve('https://bit.ly/2U3oHft', BATTLE_DATA)


def _create_defeat_mapping():
  """Parse battle-table.csv building up a defeat_mapping dict
     with keys = attackers / values = who they defeat.
  """
  # dict to return
  def_mapping = {}

  with open(BATTLE_DATA, 'r') as f:
    reader = csv.reader(f)
    map_list = list(reader)

  # for each attacker get indices where the value is win
  for attacker in map_list[1:]:
    win_indices = [i for i, e in enumerate(attacker) if e.lower() == 'win']
    wins = list(operator.itemgetter(*win_indices)(map_list[0]))
    def_mapping[attacker[0]] = wins

  return def_mapping


def get_winner(player1, player2, defeat_mapping=None):
  """Given player1 and player2 determine game output returning the
     appropriate string:
     Tie
     Player1
     Player2
     (where Player1 and Player2 are the names passed in)

     Raise a ValueError if invalid player strings are passed in.
  """
  defeat_mapping = defeat_mapping or _create_defeat_mapping()

  if player1.capitalize() not in defeat_mapping:
    raise ValueError('invalid player1')

  if player2.capitalize() not in defeat_mapping:
    raise ValueError('invalid player2')

  if player1.lower() == player2.lower():
    return 'Tie'
  else:
    if player2.capitalize() in defeat_mapping[player1.capitalize()]:
      return player1
    elif player1.capitalize() in defeat_mapping[player2.capitalize()]:
      return player2


# def main():

#   print('here ...')
#   # print(_create_defeat_mapping()['Scissors'])

#   # get_winner('blabla', 'Rock')
#   # get_winner('Rock', 'blabla')

#   # print(get_winner('Rock', 'fire'))
#   # print(get_winner('Wolf', 'Rock'))

#   assert get_winner('Snake', 'Water') == 'Snake'
#   assert get_winner('Tree', 'Sponge') == 'Tree'
#   assert get_winner('Sponge', 'Air') == 'Sponge'


# if __name__ == '__main__':
#   main()
