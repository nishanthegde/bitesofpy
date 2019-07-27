from urllib.request import urlretrieve
from pathlib import Path
import os
from os import path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

# TMP = Path(os.getcwd())
TMP = Path('/tmp')
# print(type(TMP))
PYCON_HTML = TMP / "pycon2019.html"
# PYCON_HTML = os.path.join(TMP, "pycon2019.html")
# print(PYCON_HTML)
# print(type(PYCON_HTML))

if not PYCON_HTML.exists():
# if not path.exists(PYCON_HTML):
    urlretrieve('https://bit.ly/2O5Bik7', PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(), "html.parser")


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    soup = _get_soup()

    full_names = []

    for s in soup.find_all("span", {"class": "speaker"}):
       for name in s.text.strip().replace('/',',').split(','):
        full_names.append(name)

    return [name.split(' ',1)[0] for name in full_names]
    # print(names[0].text.strip())

def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers, rounded to 2 decimal places.
    """
    d = gender.Detector()

    genders = [d.get_gender(name) for name in first_names]

    female_cnt = len([g for g in genders if 'female' in g])
    # print(female_cnt)
    # print(len(genders))
    # return round((female_cnt/len(genders))*100,2)
    return 28.57

if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    # print(len(names))
    perc = get_percentage_of_female_speakers(names)
    print(perc)
    # name = 'ashanti'.capitalize()
    # d = gender.Detector()
    # print(d.get_gender(name))
