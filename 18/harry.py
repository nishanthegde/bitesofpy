import os
import urllib.request
import re

local = '/tmp'
local = os.getcwd()
stopwords_file = os.path.join(local, 'stopwords')
harry_text = os.path.join(local, 'harry')

# data provided
tmp = os.getenv("TMP", "/tmp")
# tmp = os.getenv("TMP", local)
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    text = open("harry", "r")
    stop = open("stopwords", "r")

    stop_words = []
    for line in stop:
        line = line.lower().strip()
        stop_words.append(line)

    d = dict()

    for line in text:
        line = line.lower().strip()
        words = []
        for w in line.split():
            words.append(re.sub(r'\W', '', w))
        words = [w for w in words if w and w not in stop_words]
        if words:
            for w in words:
                if w in d:
                    d[w] += 1
                else:
                    d[w] = 1

    return sorted(d.items(), key=lambda item: item[1], reverse=True)[0]
