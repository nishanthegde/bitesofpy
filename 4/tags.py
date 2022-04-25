import os
from collections import Counter
import re
import urllib.request
import xml.etree.ElementTree as ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""

    these_regex = "<category>(.+?)</category>"
    pattern = re.compile(these_regex)
    tags = re.findall(pattern, content)

    c = Counter(tags)

    return c.most_common()[:n]