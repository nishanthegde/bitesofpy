"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
from collections import Counter, namedtuple
import os
import urllib.request as ur

# local = os.getcwd()
local = '/tmp'
tempfile = os.path.join(local, 'dirnames')
ur.urlretrieve('http://bit.ly/2ABUTjv', tempfile)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')

# dance

def gen_files():
    """Return a generator of dir names reading in tempfile

       tempfile has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    with open(tempfile, 'r') as f:
      for line in f:
        line = line.strip()
        if line.endswith('True'):
          yield line

    f.close()

def diehard_pybites():
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    prs = [] #empty list for all "True" lines in dirnames
    lines = gen_files()
    for l in lines:
      prs.append(l)

    #split to get challenge numebr
    challenge = [pr.split('/',1)[0] for pr in prs]
    #count challenges
    popular_challenges = Counter(challenge)
    #most popular challenge
    most_pop_ch = popular_challenges.most_common(1)[0]

    who = [pr.split('/',1)[1] for pr in prs]
    #split again to get user
    #count users
    user = [w.split(',',1)[0] for w in who]
    user = [u for u in user if u not in IGNORE]
    users = Counter(user)

    most_pop_user = users.most_common(1)[0][0]

    res = Stats(user=most_pop_user, challenge=most_pop_ch)
    return res







