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


def _format_author(author: str) -> str:
    # print(author.split(' '))
    return ', '.join(author.split(' ')[::-1]).strip()


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

        for s1 in s.find_all("div", {"class": "book accepted normal"}):
            py = False
            for bh in s1.find_all("div", {"class": "book-header-title"}):
                # for t in bh.find_all("h2", {"class": "main"}):
                if bh.find("h2", {"class": "main"}):
                    title = bh.find("h2", {"class": "main"}).text.strip()
                    if 'python' in title.lower():
                        py = True
                if py:
                    for a in bh.find_all("h3", {"class": "authors"}):
                        author = _format_author(a.find("a", target="_blank").text.strip())
                    for y in bh.find_all("span", {"class": "date"}):
                        if bh.find("span", {"class": "date"}):
                            year = bh.find("span", {"class": "date"}).text.strip().replace(" ", "").replace("|", "")

                            rank = int(s1.find("div", {"class": "rank"}).text.strip())
                            rating = float(s1.find("span", {"class": "our-rating"}).text.strip())

                            books.append(Book(title, author, year, rank, rating))

        # sort books by rating desc, year, title, author, title
        books = sorted(sorted(sorted(sorted([b for b in books], key=lambda b: b.author.split(",")[0]), key=lambda b: b.title), key=lambda b: b.year), key=lambda b: b.rating, reverse=True)

        # update ranks
        for i, b in enumerate(books):
            b.rank = i + 1

        return books


def main():
    print('thank you for everything...')
    python_books = load_data()

    assert python_books[0].author == "Bader, Dan"
    assert python_books[-1].title == "Python for Tweens and Teens"
    assert python_books[10].rating == 4.66

    # print(len(python_books))
    # print(python_books)
    # print([(b.title, b.year, b.author, b.rank, b.rating) for b in python_books])

    print([(b.rating, b.year, b.title, b.author, b.rank) for b in python_books])

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
