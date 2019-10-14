import re


def simple_calculator(calculation: str) -> int:
  """Receives 'calculation' and returns the calculated result,

     Examples - input -> output:
     '2 * 3' -> 6
     '2 + 6' -> 8

     Support +, -, * and /, use "true" division (so 2/3 is .66
     rather than 0)

     Make sure you convert both numbers to ints.
     If bad data is passed in, raise a ValueError.
  """

  pattern_reg = re.compile(r'^([+\-\d]*)\s(\+|-|\*|\/)\s([+\-\d]*)')
  match = pattern_reg.search(calculation.strip())

  if match:

    ip1 = int(match.group(1))
    ip2 = int(match.group(3))

    if match.group(2).strip() == '+':
      return rip1 + ip2
    elif match.group(2).strip() == '*':
      return ip1 * ip2
    elif match.group(2).strip() == '-':
      return ip1 - ip2
    elif match.group(2).strip() == '/':
      try:
        round(ip1 / ip2, 2)
      except ZeroDivisionError:
        raise ValueError('bad robot!')
    else:
      raise ValueError('very bad robot!')
  else:
    raise ValueError('bad robot!')


# def main():
#   print('here ...')
#   actual = simple_calculator('1 x 2')
#   print(actual)


# if __name__ == '__main__':
#   main()
