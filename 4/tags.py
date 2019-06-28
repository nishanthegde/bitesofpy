import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
# local = os.getcwd()
local = '/tmp'
tempfile = os.path.join(local, 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

tags = {}

# open file
with open(tempfile) as f:
    content = f.read().lower()
# parse xml

# get root element
root = ET.fromstring(content)

# get category
for cat in root.iter('category'):

    if cat.text not in tags:
        tags[cat.text] = 1
    else:
        tags[cat.text] += 1

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""

    cntr = Counter(tags)

    return cntr.most_common(n)


# def main():
#     # open file
#     with open(tempfile) as f:
#         content = f.read().lower()
#     # parse xml

#     # get root element
#     root = ET.fromstring(content)

#     # get category
#     for cat in root.iter('category'):

#         if cat.text not in tags:
#             tags[cat.text] = 1
#         else:
#             tags[cat.text] += 1

#     print(get_pybites_top_tags())

# if __name__ == "__main__":
#     main()
