INDENTS = 4

rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """
shakespeare_formatted = """
To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
    Or to take Arms against a Sea of troubles,
"""


def print_hanging_indents(poem: str):

  formatted = ''

  lines = [l.strip() for l in poem.rstrip().splitlines()]
  # print(lines)

  idx_no_indent = list()

  for i in range(len(lines)):
    if lines[i] == '':
      idx_no_indent.append(i + 1)

  # print(idx_no_indent)

  lines_indented = ['{}{}'.format(INDENTS * ' ', l) for l in lines]

  lines_formatted = list()

  for i in range(len(lines_indented)):
    if i in idx_no_indent:
      lines_formatted.append(lines_indented[i].lstrip())
    else:
      lines_formatted.append(lines_indented[i])

  print('\n'.join([l for l in lines_formatted if l.strip() != '']))


# def main():
#   print('thank you for letting my mama have a great time...')
#   # print_hanging_indents(rosetti_unformatted)
#   output = print_hanging_indents(shakespeare_unformatted)
#   print(output.strip())
#   print(shakespeare_formatted.strip())

#   assert output.strip() == shakespeare_formatted.strip()


# if __name__ == '__main__':
#   main()
