from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

from unittest import TestCase

import pytest

from zodiac import (get_signs, get_sign_with_most_famous_people,
                    signs_are_mutually_compatible, get_sign_by_date)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
# local = os.getcwd()
# TMP = os.getenv("TMP", "/tmp")
local = "/tmp"
TMP = os.getenv("TMP", local)
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope='module')
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)


def test_get_sign_with_most_famous_people(signs):

    most_famous_sign = get_sign_with_most_famous_people(signs)

    assert most_famous_sign[0] == 'Scorpio'
    assert most_famous_sign[1] == 35


def test_signs_are_mutually_compatible(signs):

    assert signs_are_mutually_compatible(signs, 'Virgo', ' Capricorn') == True
    assert signs_are_mutually_compatible(signs, 'Virgo', 'Pisces') == False
    assert signs_are_mutually_compatible(signs, 'Virgo', 'Taurus') == True
    assert signs_are_mutually_compatible(signs, 'nishant', 'Taurus') == False
    assert signs_are_mutually_compatible(signs, 'Virgo', 'nishant') == False


def test_get_sign_by_date(signs):

    assert get_sign_by_date(signs, datetime(1978, 5, 17)) == 'Taurus'
    assert get_sign_by_date(signs, datetime(1978, 9, 8)) == 'Virgo'
    assert get_sign_by_date(signs, datetime(1946, 12, 28)) == 'Capricorn'
