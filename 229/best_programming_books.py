import os

from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

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
        self.year = year
        self.rank = rank
        self.rating = rating


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
    soup = _get_soup(html_file)

    for s in soup.find_all("div", {"class": "book accepted normal"}):
        for r in s.find_all("div", {"class": "rank"}):
            title = s['data-title'].strip()
            rank = int(r.text.strip())
            for a in s.find_all("h3", {"class": "authors"}):
                authors = list()
                for a1 in a.find_all(target="_blank"):
                    if 'you?' not in a1.text.strip().lower():
                        authors.append(a1.text.strip())
            for y in s.find_all("span", {"class": "date"}):
                year = int(y.text.strip().replace(" ", "").replace("|", ""))
            for ra in s.find_all("span", {"class": "our-rating"}):
                ra = float(ra.text.strip())

        print(title, '; '.join(authors), year, rank, ra)


def main():
    books = load_data()
    # print(type(books))
    # display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """
    print('thank you for everything...')


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
