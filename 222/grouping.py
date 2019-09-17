import types
from itertools import islice


def group(iterable, n):
  """Splits an iterable set into groups of size n and a group
     of the remaining elements if needed.

     Args:
       iterable (list): The list whose elements are to be split into
                        groups of size n.
       n (int): The number of elements per group.

     Returns:
       list: The list of groups of size n,
             where each group is a list of n elements.
  """
  ret = []
  if n > 0 and isinstance(n, int):
    for i in range(0, len(iterable), n):
      ret.append(list(iterable[i:i + n]))
  else:
    raise ValueError('Group size must be positive integer')
  return ret


if __name__ == '__main__':
  iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  n = 3
  ret = group(iterable, n)
  print(ret)

  # iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  # n = 3
  # actual = group(iterable, n)
  # expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
  # assert actual == expected

  # iterable = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  # n = 3
  # actual = group(iterable, n)
  # expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
  # assert actual == expected

  # iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
  # n = 3
  # actual = group(iterable, n)
  # expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2],
  #             [3, 4, 5], [6, 7, 8], [9, 10]]
  # assert actual == expected

  # iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
  # n = 5
  # actual = group(iterable, n)
  # expected = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
  #             [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
  # assert actual == expected
