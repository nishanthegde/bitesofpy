import csv
from collections import defaultdict, namedtuple
import os
import urllib.request as ur
# from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'
# TMP = os.getcwd()

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)

ur.urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    data = defaultdict(list)

    # import data using DictReader

    with open(MOVIE_DATA) as f:
      reader = csv.DictReader(f)
      # data = [r for r in reader]
      for row in reader:
        # data[row['director_name']].append(row['movie_title'].strip())
        data[row['director_name']].append(Movie(row['movie_title'].strip(), int(row['title_year'].strip() or 1959), float(row['imdb_score'].strip())))

      # discard any movies older than 1960

      data = {k: [m for i, m in enumerate(v) if data[k][i].year > MIN_YEAR] for k,v in data.items()}
      data = defaultdict(list, data)

      return data

def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""

    scores = [m.score for m in movies]
    mean_score = round(sum(scores)/len(scores),1)

    return mean_score

def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    directors = get_movies_by_director()
    scores = [(k, calc_mean_score(directors[k])) for k, v in directors.items() if len(v) >= MIN_MOVIES]
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return scores

# director_movies = get_movies_by_director()
# print(type(director_movies))
# print(len(director_movies))
# print(director_movies[0]) # first row

# test out how default dict works

# s = 'mississippi'
# d = defaultdict(list)

# for k in s:
#   d[k] += 1
# print(list(d.items()))

# l = [('a', 1), ('b', 3), ('a', 5), ('c', 6), ('d', 8), ('c', 10), ('d', 2)]

# for k,v in l:
#   d[k].append(v)

# print(d.items())
# print(type(d.items()))

# director_movies = get_movies_by_director()
# movies_sergio = director_movies['Sergio Leone']
# print(calc_mean_score(movies_sergio))

# movies_nolan = director_movies['Christopher Nolan']
# print(calc_mean_score(movies_nolan))

# scores = get_average_scores(director_movies)
# print(scores[0])
# print(scores[1])

# directors = {score[0] for score in scores[2:13]}
# print(directors)

# assert 'Quentin Tarantino' in directors
#     assert 'Hayao Miyazaki' in directors
#     assert 'Frank Darabont' in directors
#     assert 'Stanley Kubrick' in directors
#     assert 'James Cameron' in directors
#     assert 'Joss Whedon' in directors
#     assert 'Alejandro G. Iñárritu' in directors



# print(director_movies[director_movies.keys()[0]])
# print(director_movies[list(director_movies.keys())[98]])

# keys that have movies older than 1960
# keys_older_1960 = [key for key, val in director_movies.items() if any(m for m in director_movies[key] if m.year < 1960)]
# print(keys_older_1960)


# test = [Movie(title='Psycho', year=1960, score=8.5), Movie(title='Topaz', year=1969, score=6.3), Movie(title='Frenzy', year=1972, score=7.5), Movie(title='Family Plot', year=1976, score=6.8), Movie(title='Torn Curtain', year=1966, score=6.7), Movie(title='Spellbound', year=1945, score=7.6), Movie(title='Rebecca', year=1940, score=8.2), Movie(title='The Trouble with Harry', year=1955, score=7.2)]

# test1 = [m for m in test if m.year > 1960]

# print(test)
# print(len(test))
# print(test1)
# print(len(test1))

# new_dict = {outer_k: [m for k,v in director_movies.items() for m in director_movies[k] if m.year > 1960] for outer_k in director_movies.keys()}
# new_dict = {k: [m for i, m in enumerate(v) if director_movies[k][i].year > 1960] for k,v in director_movies.items()}
# new_dict = defaultdict(list, new_dict)
# print(type(new_dict))

# print(director_movies['Mervyn LeRoy'])
# print(new_dict['nishant'])



# l = ['Male','Male','Female','Female','Male']

# for i, x in enumerate(l):
#   print(i, x)

# d = {'Sex':['Male','Male','Female','Female','Male'],
#         'Height': [100,200,150,80,90],
#         'Weight': [20,60,40,30,30]}

# l = [(i,x) for k,v in d.items() for i,x in enumerate(v)]

# print(l)

# nested_dict = {'first':{'a':1}, 'second':{'b':2}}
# float_dict = {outer_k: {inner_k:float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
# print(float_dict)
# for i in keys_older_1960:
#    director_movies[i]

# print(type(director_movies['Peter Jackson'][0].year))
# print(type(director_movies['Peter Jackson'][0].score))

# if (type(director_movies['Peter Jackson'][0])) == Data:
#   print("foo")
# else:
#   print("bar")


# [OrderedDict([('color', 'Color'), ('director_name', 'James Cameron'), ('num_critic_for_reviews', '723'), ('duration', '178'), ('director_facebook_likes', '0'), ('actor_3_facebook_likes', '855'), ('actor_2_name', 'Joel David Moore'), ('actor_1_facebook_likes', '1000'), ('gross', '760505847'), ('genres', 'Action|Adventure|Fantasy|Sci-Fi'), ('actor_1_name', 'CCH Pounder'), ('movie_title', 'Avatar\xa0'), ('num_voted_users', '886204'), ('cast_total_facebook_likes', '4834'), ('actor_3_name', 'Wes Studi'), ('facenumber_in_poster', '0'), ('plot_keywords', 'avatar|future|marine|native|paraplegic'), ('movie_imdb_link', 'http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1'), ('num_user_for_reviews', '3054'), ('language', 'English'), ('country', 'USA'), ('content_rating', 'PG-13'), ('budget', '237000000'), ('title_year', '2009'), ('actor_2_facebook_likes', '936'), ('imdb_score', '7.9'), ('aspect_ratio', '1.78'), ('movie_facebook_likes', '33000')]), OrderedDict([('color', 'Color'), ('director_name', 'Gore Verbinski'), ('num_critic_for_reviews', '302'), ('duration', '169'), ('director_facebook_likes', '563'), ('actor_3_facebook_likes', '1000'), ('actor_2_name', 'Orlando Bloom'), ('actor_1_facebook_likes', '40000'), ('gross', '309404152'), ('genres', 'Action|Adventure|Fantasy'), ('actor_1_name', 'Johnny Depp'), ('movie_title', "Pirates of the Caribbean: At World's End\xa0"), ('num_voted_users', '471220'), ('cast_total_facebook_likes', '48350'), ('actor_3_name', 'Jack Davenport'), ('facenumber_in_poster', '0'), ('plot_keywords', 'goddess|marriage ceremony|marriage proposal|pirate|singapore'), ('movie_imdb_link', 'http://www.imdb.com/title/tt0449088/?ref_=fn_tt_tt_1'), ('num_user_for_reviews', '1238'), ('language', 'English'), ('country', 'USA'), ('content_rating', 'PG-13'), ('budget', '300000000'), ('title_year', '2007'), ('actor_2_facebook_likes', '5000'), ('imdb_score', '7.1'), ('aspect_ratio', '2.35'), ('movie_facebook_likes', '0')]), OrderedDict([('color', 'Color'), ('director_name', 'Sam Mendes'), ('num_critic_for_reviews', '602'), ('duration', '148'), ('director_facebook_likes', '0'), ('actor_3_facebook_likes', '161'), ('actor_2_name', 'Rory Kinnear'), ('actor_1_facebook_likes', '11000'), ('gross', '200074175'), ('genres', 'Action|Adventure|Thriller'), ('actor_1_name', 'Christoph Waltz'), ('movie_title', 'Spectre\xa0'), ('num_voted_users', '275868'), ('cast_total_facebook_likes', '11700'), ('actor_3_name', 'Stephanie Sigman'), ('facenumber_in_poster', '1'), ('plot_keywords', 'bomb|espionage|sequel|spy|terrorist'), ('movie_imdb_link', 'http://www.imdb.com/title/tt2379713/?ref_=fn_tt_tt_1'), ('num_user_for_reviews', '994'), ('language', 'English'), ('country', 'UK'), ('content_rating', 'PG-13'), ('budget', '245000000'), ('title_year', '2015'), ('actor_2_facebook_likes', '393'), ('imdb_score', '6.8'), ('aspect_ratio', '2.35'), ('movie_facebook_likes', '85000')])]

# [Movie(title='Once Upon a Time in America', year=1984, score=8.4), Movie(title='Once Upon a Time in the West', year=1968, score=8.6), Movie(title='The Good, the Bad and the Ugly', year=1966, score=8.9), Movie(title='A Fistful of Dollars', year=1964, score=8.0)]
# [Movie(title='Psycho', year=1960, score=8.5), Movie(title='Topaz', year=1969, score=6.3), Movie(title='Frenzy', year=1972, score=7.5), Movie(title='Family Plot', year=1976, score=6.8), Movie(title='Torn Curtain', year=1966, score=6.7), Movie(title='Spellbound', year=1945, score=7.6), Movie(title='Rebecca', year=1940, score=8.2), Movie(title='The Trouble with Harry', year=1955, score=7.2)]



