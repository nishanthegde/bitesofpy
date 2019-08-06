import random

MAX_GUESSES = 5
START, END = 1, 20


def isInt_try(v):
  try:
    i = int(v)
  except:
    return False
  return True


def get_random_number():
  """Get a random number between START and END, returns int"""
  return random.randint(START, END)


class Game:
  """Number guess class, make it callable to initiate game"""

  def __init__(self):
    """Init _guesses, _answer, _win to set(), get_random_number(), False"""
    self._guesses = []
    self._answer = get_random_number()
    # self._answer = 2
    self._win = False

  def guess(self):
    """Ask user for input, convert to int, raise ValueError outputting
       the following errors when applicable:
       'Please enter a number'
       'Should be a number'
       'Number not in range'
       'Already guessed'
       If all good, return the int"""

    guess = input("Guess a number between 1 and 20: ")
    # guess = guess.replace("'", "").replace('"', '')

    if guess == "":  # no input
      print('Please enter a number')
      raise ValueError
    elif not isInt_try(guess):
      print('Should be a number')
      raise ValueError
    elif int(guess) < START or int(guess) > END:
      print('Number not in range')
      raise ValueError
    elif int(guess) in self._guesses:
      print('Already guessed')
      raise ValueError
    else:
      self._guesses.append(int(guess))
      return int(guess)

  def _validate_guess(self, guess):
    """Verify if guess is correct, print the following when applicable:
       {guess} is correct!
       {guess} is too low
       {guess} is too high
       Return a boolean"""

    if self._answer == guess:
      print('{} is correct!'.format(guess))
      return True

    if self._answer < guess:
      print('{} is too high'.format(guess))
      return False

    if self._answer > guess:
      print('{} is too low'.format(guess))
      return False

  def __call__(self):
    """Entry point / game loop, use a loop break/continue,
       see the tests for the exact win/lose messaging"""
    # print(self._answer)

    while len(self._guesses) < MAX_GUESSES:
      try:
        g = self.guess()
        # print(self._guesses)
        if self._validate_guess(g):
          self._win = True
          if len(self._guesses) == 1:
            print('It took you {} guess'.format(len(self._guesses)))
          else:
            print('It took you {} guesses'.format(len(self._guesses)))
          break

      except ValueError:
        continue

    if not self._win:
      print('Guessed 5 times, answer was {}'.format(self._answer))


def main():
  """
    In this Bite you implement a Game class to perform a number guessing game.
    It lets a user do a max of 5 guesses of a secret number between 1 and 20 randomly defined by the class.

    Note you have to account for invalid inputs: raise a ValueError if a user hits Enter (nothing entered)
    , a non-numeric value, a number that is not in the 1-20 range, or guesses the same number again.

    See the template code below ... (Advanced Bite, not giving away too much!)

    The tests run through a lose scenario as well. Note they mock out the input builtin to test this. And you will be tested on stdout too so use print statements in addition to return values. Here is how the program would work from the command line.
  """

  # guesses = []

  # while len(guesses) < 5:

  #   try:
  #     guess = input("Guess a number between 1 and 20: ")

  #     guess = guess.replace("'", "").replace('"', '')

  #     if guess == "":  # no input
  #       raise ValueError
  #     elif not isInt_try(guess):
  #       raise ValueError
  #     else:
  #       guesses.append(int(guess))
  #       print(guesses)

  #   except ValueError:
  #     if guess == "":
  #       print("Please enter a number")
  #     elif not isInt_try(guess):
  #       print("Should be a number")
  #     continue

  # print("Guesses are {}".format(guesses))
  pass


if __name__ == '__main__':
  game = Game()
  game()
  # main()
  # game.guess()
  # game.guess()
