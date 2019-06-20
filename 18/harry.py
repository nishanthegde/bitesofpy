import os
import urllib.request as ur
import re

local = '/tmp'
# local = os.getcwd()
stopwords_file = os.path.join(local, 'stopwords')
harry_text = os.path.join(local, 'harry')

ur.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
ur.urlretrieve('http://bit.ly/2C6RzuR', harry_text)

def strip_word(w):
    """accepts a word as a string and returns
        lowercase of the word with non-alpha numeric characters stripped out"""
    w = w.lower()
    w = re.sub("[^a-zA-Z0-9]+", "", w)

    return w


def get_harry_most_common_word():
    """Open script file and stopwords file and read
        words into a dictionary, exclude stopwords"""
    stop = []
    freq = {}

    with open(stopwords_file, 'r') as f:
        for line in f:
            stop.append(line)

    f.close()

    stop = [strip_word(s) for s in stop]

    with open(harry_text, 'r') as f:
        reader = f.read()

        for w in reader.split():
            w = strip_word(w)

            if w and w not in stop:
                if w not in freq:
                    freq[w] = 1
                else:
                    freq[w] += 1

        freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)

    f.close()

    return freq[0]



