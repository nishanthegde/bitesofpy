from random import choice

defeated_by = dict(paper='scissors',
                   rock='paper',
                   scissors='rock')

lose = '{} beats {}, you lose!'
win = '{} beats {}, you win!'
tie = 'tie!'


def _get_computer_move():
  """Randomly select a move"""
  return choice([v for v in defeated_by.values()])


def _get_winner(computer_choice, player_choice):
  """Return above lose/win/tie strings populated with the
     appropriate values (computer vs player)"""

  if computer_choice == player_choice:
    return tie

  if defeated_by[player_choice] == computer_choice:
    return lose.format(computer_choice, player_choice)
  else:
    return win.format(player_choice, computer_choice)


def game():
  """Game loop, receive player's choice via the generator's
     send method and get a random move from computer (_get_computer_move).
     Raise a StopIteration exception if user value received = 'q'.
     Check who wins with _get_winner and print its return output."""
  print("Welcome to Rock Paper Scissors")

  while True:

    player_choice = yield

    if player_choice and player_choice.lower() == 'q':
      raise StopIteration

    computer_choice = _get_computer_move()

    print(_get_winner(computer_choice, player_choice))


# def main():

#   gen = game()
#   next(gen)
#   gen.send('rock')
#   gen.send('paper')
#   gen.send('scissors')


# if __name__ == "__main__":
#   main()
