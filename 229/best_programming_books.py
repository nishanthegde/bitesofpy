import os

from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

from collections import Counter

url = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "best-programming-books.html")
local = os.getcwd()
# local = "/tmp"
tmp = Path(local)
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """

    def __init__(self, title, author, year, rank, rating):
        self.title = title
        self.author = author
        self.year = int(year)
        self.rank = int(rank)
        self.rating = float(rating)

    def __str__(self):
        rank_str = ('000' + str(self.rank))[-3:]
        year_str = '(' + str(self.year) + ')'

        return '[{}] {} {}\n      {} {}'.format(rank_str, self.title, year_str, self.author, str(self.rating))


def _get_soup(file):
    return BeautifulSoup(file.read_text(), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    pass


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    books = list()
    soup = _get_soup(html_file)

    for s in soup.find_all("div", {"class": "books"}):
        for bh in s.find_all("div", {"class": "book-header-title"}):
            for t in bh.find_all("h2", {"class": "main"}):
                if 'python' in t.text.strip().lower():
                    books.append(t.text.strip())
        # for s in soup.find_all("div", {"class": "book accepted normal"}):
        #     for t in s.find_all("h2", {"class": "main"}):
        #         title = t.text.strip()
        #     for r in s.find_all("div", {"class": "rank"}):
        #         # title = s['data-title'].strip()
        #         rank = int(r.text.strip())
        #         for a in s.find_all("h3", {"class": "authors"}):
        #             authors = list()
        #             for a1 in a.find_all(target="_blank"):
        #                 if 'you?' not in a1.text.strip().lower():
        #                     authors.append(a1.text.strip())
        #                     # author = a1.text.strip
        #         for y in s.find_all("span", {"class": "date"}):
        #             year = int(y.text.strip().replace(" ", "").replace("|", ""))
        #         for ra in s.find_all("span", {"class": "our-rating"}):
        #             rating = float(ra.text.strip())

        #     books.append(Book(title, '; '.join(authors), year, rank, rating))
        #     # print(title, '; '.join(authors), year, rank, ra)

        return books


def main():
    print('thank you for everything...')
    books = load_data()
    print(len(books))
    # print(len(set([b.title for b in books])))
    # c = Counter([b.title for b in books])
    # print(c.most_common())
    # display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """

    # title = "Python Testing with pytest"
    # author = "Okken, Brian"
    # year = 2017
    # rank = 1
    # rating = 5

    # b = Book(title, author, year, rank, rating)
    # actual = str(b)
    # print(actual)


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""
