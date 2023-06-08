import re
import string
from random import choice, randint

import requests
from bs4 import BeautifulSoup

# FEATURED_ARTICLE = ('https://en.wikipedia.org/wiki/Wikipedia:Today%27s_featured_article/January_1,_2022')
FEATURED_ARTICLE = "https://bites-data.s3.us-east-2.amazonaws.com/wiki_features_article_2022-01-01.html"
CONTENT = requests.get(FEATURED_ARTICLE).text


def wiki_lorem_ipsum(article: str = CONTENT, number_of_sentences: int = 5):
    """Create a lorem ipsum block of sentences from the words scraped from today's Wikipedia featured article

    :param number_of_sentences
    :type number_of_sentences: int
    :return: lorem ipsum text (Lorem ipsum is nonsense text used to test layouts for documents or websites)
    rtype: str
    """
    ret = ""

    if number_of_sentences < 1:
        raise ValueError("Function must be called with at least 1 sentence")

    soup = BeautifulSoup(article, "html.parser")

    # This will get the div
    div_container = soup.find("div", class_="mw-body-content mw-content-ltr")

    ptag_vals = ""

    # Then search in that div_container for all p tags with class "hello"
    for ptag in div_container.find_all("p"):
        # prints the p tag content
        ptag_vals += ptag.text + " "

    soup = ptag_vals
    soup_words = soup.replace("-", " ").split()
    soup_words = [re.sub(r"[^\w|_]", "", w) for w in soup_words]
    soup_words = [w.lower() for w in soup_words if w]

    # print(soup_words)

    for i in range(number_of_sentences):
        random_num_words = randint(5, 15)
        sentence = ""
        for i in range(random_num_words):
            sentence = sentence + choice(soup_words) + " "
        sentence = sentence[:-1] + ". "
        sentence = sentence.capitalize()
        ret += sentence

    return ret.strip()
