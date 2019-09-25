from collections import Counter

from bs4 import BeautifulSoup
import requests


AMAZON = "amazon.com"
TIM_BLOG = 'https://bit.ly/2NBnZ6P'


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    if content is None:
        content = load_page()

    books = []

    soup = BeautifulSoup(content, "html.parser")

    for s in soup.find_all("div", {"class": "entry-content"}):
        for element in s.find_all("a", href=lambda href: href and AMAZON in href):
            books.append(element.get_text().strip())

    c = Counter(books)

    return [b[0] for b in c.most_common(limit)]


# def main():

#     print('here ...')
#     content = load_page()
#     books = get_top_books(content=content)

#     assert books[0] == 'Man’s Search For Meaning'
#     assert books[1] == 'Tao Te Ching'

#     assert sorted(books[2:5]) == ['Sapiens: A Brief History of Humankind',
#                                   ('The 4-Hour Workweek: Escape the 9-5, Live '
#                                    'Anywhere and Join the New Rich'),
#                                   'The Fountainhead']


# if __name__ == '__main__':
#     main()
