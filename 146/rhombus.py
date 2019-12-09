STAR = '*'


def gen_rhombus(width):
  """Create a generator that yields the rows of a rhombus row
     by row. So if width = 5 it should generate the following
     rows one by one:

     gen = gen_rhombus(5)
     for row in gen:
         print(row)

      output:
        *
       ***
      *****
       ***
        *
  """
  CHAR = '*'
  if width % 2 == 0 or width <= 0:
    raise ValueError('width must be +ve odd integer')
  else:
    # while True:
    for i in range(1, width + 1, 2):
      buff = int((width - i) / 2)
      yield '{}{}{}'.format(buff * ' ', i * CHAR, buff * ' ')
    for i in range(width - 2, 0, -2):
      buff = int((width - i) / 2)
      yield '{}{}{}'.format(buff * ' ', i * CHAR, buff * ' ')


# def main():
#   print('thank you for the ocean...')
#   actual = list(gen_rhombus(5))
#   # print(actual)
#   actual = list(gen_rhombus(3))
#   expected = [' * ', '***', ' * ']
#   assert actual == expected

#   actual = list(gen_rhombus(3))
#   expected = [' * ', '***', ' * ']
#   assert actual == expected

#   actual = list(gen_rhombus(11))
#   expected = ['     *     ', '    ***    ', '   *****   ',
#               '  *******  ', ' ********* ', '***********', ' ********* ',
#               '  *******  ', '   *****   ', '    ***    ', '     *     ']
#   assert actual == expected


# if __name__ == '__main__':
#   main()
