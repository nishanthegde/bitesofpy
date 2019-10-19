from collections import namedtuple


from bs4 import BeautifulSoup
import requests
import re

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')

homepage = ("https://bites-data.s3.us-east-2.amazonaws.com/"
            "news.python.sc/index.html")
page2 = ("https://bites-data.s3.us-east-2.amazonaws.com/"
         "news.python.sc/index2.html")


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    titles = []
    points = []
    comments = []

    points_pattern = re.compile(r'^(\d+)\spoint')
    comments_pattern = re.compile(r'\|\s(\d+)\scomment')

    for t in soup.find_all('span', attrs={'class': 'title'}):
        titles.append(t.text.strip())

    for c in soup.find_all('span', attrs={'class': 'controls'}):
        for s in c.find_all('span', attrs={'class': 'smaller'}):
            # controls.append(s.text.strip().split('\n')[0])
            pt = points_pattern.search(s.text.strip().split('\n')[0])
            points.append(int(pt.group(1)))
            com = comments_pattern.search(s.text.strip().split('\n')[-1])
            comments.append(int(com.group(1)))
            # comments.append(com.group(1))

    all_entries = sorted(list(zip(titles, points, comments)), key=lambda x: (x[1], x[2]), reverse=True)

    return [Entry(title=e[0], points=e[1], comments=e[2]) for e in all_entries][:top]


# def main():
#     print('here ...')

#     actual = get_top_titles(homepage)
#     actual = get_top_titles(page2, 2)
#     print(actual)


# if __name__ == '__main__':
#     main()
