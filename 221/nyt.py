import requests
import json


YOUR_KEY = 'vbIkIRCX3w6Z3dHNWQFYy4fmvUtDD8s0'
DEFAULT_LIST = 'hardcover-nonfiction'

URL_NON_FICTION = (f'https://api.nytimes.com/svc/books/v3/lists/current/'
                   f'{DEFAULT_LIST}.json?api-key={YOUR_KEY}')

URL_FICTION = URL_NON_FICTION.replace('nonfiction', 'fiction')


def get_best_seller_titles(url=URL_NON_FICTION):
  """Use the NY Times Books API endpoint above to get the titles that are
     on the best seller list for the longest time.

     Return a list of (title, weeks_on_list) tuples, e.g. for the nonfiction:

     [('BETWEEN THE WORLD AND ME', 86),
      ('EDUCATED', 79),
      ('BECOMING', 41),
      ('THE SECOND MOUNTAIN', 18),
       ... 11 more ...
     ]

     Dev docs: https://developer.nytimes.com/docs/books-product/1/overview
  """
  r = requests.get(url)

  d = r.json()
  # return len(d['results']['books'])
  books = d['results']['books']

  titles = [book['title'].upper() for book in books]
  weeks = [book['weeks_on_list'] for book in books]

  return sorted(list(zip(titles, weeks)), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
  ret = get_best_seller_titles()
  print(ret)
  # print(type(ret))s
  # print(URL_FICTION)
