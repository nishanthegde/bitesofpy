import shlex


def split_words_and_quoted_text(text: str)-> list:
  """Split string text by space unless it is
     wrapped inside double quotes, returning a list
     of the elements.

     For example
     if text =
     'Should give "3 elements only"'

     the resulting list would be:
     ['Should', 'give', '3 elements only']
  """
  return shlex.split(text)


# def main():
#   print('thank you for everything you have given me...')
#   print(split_words_and_quoted_text('Should give "3 words only"'))
#   print(split_words_and_quoted_text('Our first program was "Hello PyBites"'))
#   print(split_words_and_quoted_text('Because "Hello World" is really cliche'))
#   print(split_words_and_quoted_text(('PyBites is a "A Community that Masters '
#                                     'Python through Code Challenges"'))


# if __name__ == '__main__':
#   main()
