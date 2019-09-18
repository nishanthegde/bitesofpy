text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

vowels = 'aeiou'


def strip_vowels(text: str) -> (str, int):
  """Replace all vowels in the input text string by a star
     character (*).
     Return a tuple of (replaced_text, number_of_vowels_found)

     So if this function is called like:
     strip_vowels('hello world')

     ... it would return:
     ('h*ll* w*rld', 3)

     The str/int types in the function defintion above are part
     of Python's new type hinting:
     https://docs.python.org/3/library/typing.html"""
  count = 0
  # vowel = set('aeiou')

  for c in text:
    if c.lower() in vowels:
      count = count + 1
      text = text.replace(c, '*')

  return (text, count)


# def main():
#   print('here')

#   # print(type(text))
#   output, number_replacements = strip_vowels(text)
#   # print(output)
#   # print(number_replacements)
#   assert number_replacements == 262
#   assert 'Th* Z*n *f Pyth*n, by T*m P*t*rs' in output
#   assert 'B***t*f*l *s b*tt*r th*n *gly' in output
#   assert 'N*m*sp*c*s *r* *n* h*nk*ng gr**t *d**' in output

#   output, number_replacements = strip_vowels(text2)

#   assert number_replacements == 43

#   assert 'H*ll* w*rld!' in output
#   assert 'H*v* f*n w*th **r B*t*s *f Py' in output
#   assert 'B*c*m* * PyB*t*s n*nj*!' in output


# if __name__ == '__main__':
#   main()
