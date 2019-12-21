def _is_teen(n: int) -> bool:
  if n // 10 == 1:
    return True
  elif n // 10 == 0:
    return False
  else:
    return _is_teen(n // 10)


def get_ordinal_suffix(number: int) -> str:
  """Receives a number int and returns it appended with its ordinal suffix,
     so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.

     Rules:
     https://en.wikipedia.org/wiki/Ordinal_indicator#English
     - st is used with numbers ending in 1 (e.g. 1st, pronounced first)
     - nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second): int
     - rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
     - As an exception to the above rules, all the "teen" numbers ending with
       11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th,
       pronounced one hundred [and] twelfth)
     - th is used for all other numbers (e.g. 9th, pronounced ninth).
     """
  if _is_teen(number):
    suffix = 'th'
  elif str(number)[-1] == '1':
    suffix = 'st'
  elif str(number)[-1] == '2':
    suffix = 'nd'
  elif str(number)[-1] == '3':
    suffix = 'rd'
  else:
    suffix = 'th'
  return '{}{}'.format(str(number), suffix)


# def main():
#   print('thank you for the curiosity... and the waves ... :-)')
#   print(get_ordinal_suffix(54))
#   print(get_ordinal_suffix(55))
#   print(get_ordinal_suffix(56))
#   print(get_ordinal_suffix(3001))
#   print(get_ordinal_suffix(2002))
#   # print(_is_teen(3000))


# if __name__ == '__main__':
#   main()
