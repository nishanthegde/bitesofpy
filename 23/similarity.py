import os
import re
from difflib import SequenceMatcher
from itertools import combinations
from urllib.request import urlretrieve

# prep
TAG_HTML = re.compile(r'<category>([^<]+)<\/category>')
# local = os.getcwd()
local = '/tmp'
TEMPFILE = os.path.join(local, 'feed')
MIN_TAG_LEN = 10
IDENTICAL = 1.0
SIMILAR = 0.95

urlretrieve('http://bit.ly/2zD8d8b', TEMPFILE)

def _get_tags(tempfile=TEMPFILE):
    """
        Helper to parse all tags from a static copy of PyBites' feed,
        providing this here so you can focus on difflib
    """
    with open(tempfile) as f:
        content = f.read().lower()

    # take a small subset to keep it performant
    tags = TAG_HTML.findall(content)
    tags = [tag for tag in tags if len(tag) > MIN_TAG_LEN]

    return set(tags)

def get_similarities(tags=None):
    """
        Should return a list of similar tag pairs (tuples)
    """
    tags = tags or _get_tags()

    # make combinations of all tags
    combo_tags = [(a,b) for a, b in combinations(tags, 2)]

    #compare similarity ratio
    similar_tags = []
    for a, b in combo_tags:
        s = SequenceMatcher(None, a, b)

        if s.ratio() >= SIMILAR:
            similar_tags.append((a,b))


    return similar_tags

# def main():
#     # similar_tags = list(get_similarities())
#     # print(len(similar_tags))

#      # s = SequenceMatcher(lambda x: x == " ",
#      #                        "private Thread currentThread;",
#      #                        "private volatile Thread currentThread;")
#      # s = SequenceMatcher(None,
#      #                        "private Thread currentThread;",
#      #                        "private volatile Thread currentThread;")

#      # # #[Match(a=0, b=0, size=8), Match(a=8, b=17, size=21), Match(a=29, b=38, size=0)]

#      # for block in s.get_matching_blocks():
#      #    print("a[{}] and b[{}] match for {} elements".format(block.a, block.b, block.size))

#      # print(s.ratio())

#      similar_tags = get_similarities()
#      print(similar_tags)

# if __name__ == "__main__":
#     main()
