import json
from pathlib import Path
import os
from urllib.request import urlretrieve
import json
from datetime import datetime

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ('white yellow orange green blue brown black '
         'paneled red').split()
TMP = Path('/tmp')
# TMP = Path(os.getcwd())


def get_data(file_no=1, tmp=TMP):

  file_name = f'bite_scores{file_no}.json'
  file_path = TMP / file_name
  remote = 'https://bites-data.s3.us-east-2.amazonaws.com/'

  if not file_path.exists():
    urlretrieve(f'{remote}{file_name}', file_path)

  return file_path


def get_belts(data: str) -> dict:
  """Parsed the passed in json data:
     {"date":"5/1/2019","score":1},
     {"date":"9/13/2018","score":3},
     {"date":"10/25/2019","score":1},

     Loop through the scores in chronological order,
     determining when belts were achieved (use SCORES
     and BELTS).

     Return a dict with keys = belts, and values =
     readable dates, example entry:
     'yellow': 'January 25, 2018'
  """
  belts = dict()
  with open(data) as f:
    scores = json.load(f)

  scores = sorted(scores, key=lambda x: datetime.strptime(x['date'], '%m/%d/%Y'))

  total_score = 0
  highest_belt = 0

  # merge belt scores
  belt_scores = list(zip(BELTS, SCORES))

  for i, s in enumerate(scores):
    total_score += int(scores[i]['score'])
    # print(i, total_score)
    # check if belt is earned
    earned = [b_score for b_score in belt_scores if total_score >= b_score[1]]
    if earned:
      #something is earned
      # is it new?
      if earned[-1][1] != highest_belt:
        # print(earned[-1][1], datetime.strftime(datetime.strptime(scores[i]['date'], '%m/%d/%Y'), '%B %d, %Y'))
        belts[earned[-1][0]] = datetime.strftime(datetime.strptime(scores[i]['date'], '%m/%d/%Y'), '%B %d, %Y')
      highest_belt = earned[-1][1]

  return belts


def main():

  print('thank you for everything...')
  data = get_data(2)
  belts = get_belts(data)
  print(belts)
  # for b in belts:
  #   print(b['date'], datetime.strptime(b['date'], '%m/%d/%Y'))

  # print(list(zip(BELTS, SCORES)))


if __name__ == '__main__':
  main()
