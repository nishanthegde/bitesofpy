import csv
from pathlib import Path
from urllib.request import urlretrieve
import os
import re

# tmp = os.getcwd()
tmp = Path('/tmp')
tmp = Path(tmp)
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N=10, stats=stats):
    """
        Parse the bites.csv file (= stats variable passed in), see example
        output in the Bite description.
        Return a list of Bite IDs (int or str values are fine) of the N
        most complex Bites.
    """
    bite = []
    diff = []

    p = re.compile('bite \d*.')

    line = 0
    with open(stats) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        for row in csv_reader:
            if line > 0:
                if row[1].strip().lower() == "none":
                    diff.append(-1.0)
                else:
                    diff.append(float(row[1]))
                bite.append(p.findall(row[0].strip().lower())[0].split()[1][:-1])
            line += 1

    # bite_parsed = [b for b in bite]
    # split()[1][:-1]
    srtd_ret = sorted([(b, d) for b, d in zip(bite, diff)], key=lambda x: x[1], reverse=True)
    return [i[0] for i in srtd_ret[:N]]


def main():
    pass


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)
    # main()
