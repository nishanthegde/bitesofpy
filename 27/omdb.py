import glob
import json
import os
from urllib.request import urlretrieve
import re

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'
# TMP = os.getcwd()

# print(TMP)

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):

    movies = []

    for file in files:

        with open(file) as f:
            movie_dict = json.load(f)
            movies.append(movie_dict)

    return movies


def get_single_comedy(movies):
    return [m['Title'] for m in movies if 'comedy' in m['Genre'].lower()][0]


def get_movie_most_nominations(movies):

    nominations = []

    award_list = [(m['Title'], m['Awards']) for m in movies]

    nom_pattern = re.compile(r'([0-9]+)*\snominations')

    for a in award_list:
        nom_num = nom_pattern.search(a[1])
        nominations.append((a[0], int(nom_num.group(1))))

    return max(nominations, key=lambda x: x[1])[0]


def get_movie_longest_runtime(movies):

    runtimes = []

    runtime_list = [(m['Title'], m['Runtime']) for m in movies]

    rt_pattern = re.compile(r'([0-9]+)*\smin')

    for rt in runtime_list:
        rt_num = rt_pattern.search(rt[1])
        runtimes.append((rt[0], (int(rt_num.group(1)))))

    return max(runtimes, key=lambda x: x[1])[0]


# def main():
#     movies = get_movie_data()

#     assert len(movies) == 5
#     assert all(type(m) == dict for m in movies)

#     assert get_single_comedy(movies) == 'Horrible Bosses'
#     assert get_movie_most_nominations(movies) == 'Fight Club'

#     assert get_movie_longest_runtime(movies) == 'Blade Runner 2049'


# if __name__ == '__main__':
#     main()
