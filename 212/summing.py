from contextlib import suppress
import inspect


def sum_numbers(numbers):

  for i, j in zip(numbers, numbers[1:]):

    with suppress(ZeroDivisionError):
      with suppress(TypeError):
        yield i / j


# def main():

#   print('here ...')

#   numbers = [1, 2, 0, 4, 5, 12, 'a', 3]
#   actual = sum_numbers(numbers)
#   print(actual)
# #   expected = [0.5, 0.0, 0.8, 0.4166666666666667]
# #   assert actual == expected

# #   src = inspect.getsource(sum_numbers)
# #   assert 'try' not in src
# #   assert 'except ' not in src
# #   assert 'yield' in src
# #   assert 'TypeError' in src
# #   assert 'ZeroDivisionError' in src
# #   assert src.count('suppress(') in (1, 2)
# #   assert src.count('with') in (1, 2)


# if __name__ == '__main__':
#   main()
