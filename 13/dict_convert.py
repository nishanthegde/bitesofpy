from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
namedTupleConstructor = namedtuple('namedTupleConstructor', ' '.join(sorted(blog.keys())))

def dict2nt(dict_):
    """
    Function to convert the given blog dict to a namedtuple
    """
    if isinstance(dict_, dict):
        nt_blog = namedTupleConstructor(**dict_)

    return nt_blog

def json_date_to_str(d):
    """
    Helper to use strings in json serializing
    """
    if isinstance(d, datetime):
        return d.__str__()

def nt2json(nt):
    """
    Function to convert the resulting namedtuple to json.
    """
    orderd_dict = nt._asdict()
    return json.dumps(orderd_dict, default=json_date_to_str)


# def main():
#     """
#         Write a function to convert the given blog dict to a namedtuple.
#         Write a second function to convert the resulting namedtuple to json.
#         Here you probably need to use 2 of the _ methods of namedtuple :)
#     """

#     # print(blog)
#     # print(type(blog))
#     # print(namedTupleConstructor)
#     nt = dict2nt(blog)
#     output = nt2json(nt)

#     data = json.loads(output)

#     print(type(data))
#     print(data['tags'][0])
#     print(data['started'][:4])

# if __name__ == "__main__":
#     main()





