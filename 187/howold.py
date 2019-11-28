from dataclasses import dataclass

from dateutil.parser import parse


@dataclass
class Actor:
  name: str
  born: str


@dataclass
class Movie:
  title: str
  release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
  """Calculates age of actor / actress when movie was released,
     return a string like this:

     {name} was {age} years old when {movie} came out.
     e.g.
     Wesley Snipes was 28 years old when New Jack City came out.
  """
  born = parse(actor.born)
  release = parse(movie.release_date)
  age_release = int(int((release - born).days) / 365)
  return "{name} was {age} years old when {movie} came out.".format(name=actor.name, age=age_release, movie=movie.title)


# def main():
#   print('thank you for everything...')

#   actor = Actor('Wesley Snipes', 'July 31, 1962')
#   actor = Actor('Robert de Niro', 'August 17, 1943')
#   movie = Movie('New Jack City', 'January 17, 1991')
#   movie = Movie('Goodfellas', 'October 19, 1990')

#   actual = get_age(actor, movie)
#   print(actual)

#   # print(actor)
#   # print(type(actor))
#   # print(actor.name)
#   # print(type(actor.name))
#   # print(actor.born)
#   # print(type(actor.born))


# if __name__ == '__main__':
#   main()
