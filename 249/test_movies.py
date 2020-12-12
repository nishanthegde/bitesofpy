import os
import random
import string
import pytest

from movies import MovieDb

salt = ''.join(
    random.choice(string.ascii_lowercase) for i in range(20)
)
DB = os.path.join(os.getenv("TMP", "/tmp"), f'movies_{salt}.db')
# https://www.imdb.com/list/ls055592025/

DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = 'movies'


@pytest.fixture(scope='module')
def db(request):
    """
        Instantiate MovieDb class using above constants
        do proper setup / teardown using MovieDb methods
        https://docs.pytest.org/en/latest/fixture.html (hint: yield)
    """
    db = MovieDb(DB, DATA, TABLE)
    db._create_table()
    db._insert_sample_data()

    def quit():
        db.drop_table()

    request.addfinalizer(quit)

    yield db


# write tests for all MovieDb's query / add / delete
def test_query_with_title(db):
    assert db.query(title="wizard")[0][1] == 'The Wizard of Oz'


def test_query_with_year(db):
    assert len(db.query(year=1939)) == 2


def test_query_with_score(db):
    assert db.query(score_gt=9)[1][3] == 9.3


def test_add(db):
    assert len(db.query(year=1960)) == 0
    db.add(title='Psycho', year=1960, score=8.5)
    assert db.query(year=1960)[0][1] == 'Psycho'

def test_delete(db):
    assert len(db.query(title='raging')) == 1
    db.delete(4)
    assert len(db.query(title='raging')) == 0