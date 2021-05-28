from collections import namedtuple
from datetime import datetime
import json

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')


def dict2nt(dict_):
    nt = namedtuple('x', dict_.keys())(*dict_.values())
    return nt


def nt2json(nt):
    return json.dumps(nt._asdict(), default=str)
