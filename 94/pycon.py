from collections import namedtuple
import os
import pickle
import urllib.request
from copy import deepcopy
import re


pkl_file = 'pycon_videos.pkl'
data = 'http://projects.bobbelderbos.com/pcc/{}'.format(pkl_file)

# local = os.getcwd()
local = '/tmp'
pycon_videos = os.path.join(local, pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple('Video', 'id title duration metrics')


def load_pycon_data(pycon_videos=pycon_videos):
  """Load the pickle file (pycon_videos) and return the data structure
     it holds"""

  with open(pycon_videos, 'rb') as infile:
    videos = pickle.load(infile)

  return videos


def get_most_popular_talks_by_views(videos):
  """Return the pycon video list sorted by most viewCount"""
  return sorted(videos, key=lambda x: int(x.metrics['viewCount']), reverse=True)


def get_most_popular_talks_by_like_ratio(videos):
  """Return the pycon video list sorted by most likes relative to
     number of views, so 10 likes on 175 views ranks higher than
     12 likes on 300 views. Discount the dislikeCount from the likeCount.
     Return the filtered list"""
  return sorted(videos, key=lambda x: (int(x.metrics['likeCount']) - int(x.metrics['dislikeCount'])) / int(x.metrics['viewCount']), reverse=True)


def get_talks_gt_one_hour(videos):
  """Filter the videos list down to videos of > 1 hour"""
  hours = [vid for vid in videos if re.search('([0-9]+)H', vid.duration)]

  return [vid for vid in hours if int(re.search('([0-9]+)M', vid.duration).group(1)) != 0]


def get_talks_lt_twentyfour_min(videos):
  """Filter videos list down to videos that have a duration of less than
     24 minutes"""
  lt_hour = [vid for vid in videos if not re.search('([0-9]+)H', vid.duration) and re.search('([0-9]+)M', vid.duration)]

  return [vid for vid in lt_hour if int(re.search('([0-9]+)M', vid.duration).group(1)) < 24]
  # return [(vid.id, vid.duration) for vid in lt_hour]


# def main():
#   """
#   Video(id='T-TwcmT6Rcw'
#           , title='Raymond Hettinger - Dataclasses:  The code generator to end all code generators - PyCon 2018'
#           , duration='PT45M8S'
#           , metrics={'viewCount': '6360', 'likeCount': '144', 'dislikeCount': '2', 'favoriteCount': '0', 'commentCount': '14'})
#   """

#   videos = load_pycon_data()
#   assert len(videos) == 147
#   assert isinstance(videos[0], tuple)

#   # print(videos[0])

#   videos_copy = deepcopy(videos)
#   expected = ['T-TwcmT6Rcw', 'GBQAKldqgZs', 'ms29ZPUKxbU',
#               'zJ9z6Ge-vXs', 'WiQqqB9MlkA']
#   vids = list(get_most_popular_talks_by_views(videos_copy))
#   # actual = [vid.metrics['viewCount'] for vid in vids[:5]]
#   actual = [vid.id for vid in vids[:5]]
#   assert expected == actual

#   videos_copy = deepcopy(videos)
#   vids = list(get_most_popular_talks_by_like_ratio(videos_copy))
#   expected = ['8OoR-P6wE0M', 'h-38HZqanJs', 'C7ZhMnfUKIA',
#               'GmbaKdd6o6A', '3EXvR1shVFQ']
#   actual = [vid.id for vid in vids[:5]]
#   assert expected == actual

#   vids = get_talks_gt_one_hour(videos)
#   assert vids[0].id == '0hsKLYfyQZc'
#   assert vids[-1].id == 'ZwvjtCjimiw'
#   assert len(vids) == 35

#   vids = get_talks_lt_twentyfour_min(videos)
#   assert vids[0].id == 'zQeYx87mfyw'
#   assert vids[-1].id == 'TcHkkzWBMKY'

#   # print(len(vids))


# if __name__ == "__main__":
#   main()
