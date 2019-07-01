import os
import urllib.request
from itertools import groupby

# local = os.getcwd()
local = '/tmp'
LOG = os.path.join(local, 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)

def create_chart():
    """
         Count the sending to slack channel entries and look at the book title in the previous line, and see if it was a Python book.
         If so print 🐍 , else a dot.

         output:
            02-13 ...........
            02-14 ..............
            02-15 .................
            02-16 ............
            02-19 🐍.......🐍
            02-20 ...
            02-21 ..............🐍
            02-22 🐍...................

    """

    with open(LOG, 'r') as f:
        # open log file and read lines
        lines = [l.strip() for l in f.readlines()]

        # if line contains sending to slack channel get the line with the book in the previous entry
        books = [lines[i-1] for i,l in enumerate(lines) if 'sending to slack channel' in lines[i]]
        # print(books)
        # print(len(books))

        # dictionary that has books grouped by date (key is the data and value is a list of books on that date)
        books_grouped = {k: list(v) for k,v in  groupby(books, key=lambda x: x[0:5])}

        for k in books_grouped.keys():
            # bar to print for each group
            bar=''
            for elem in books_grouped[k]:
                if "python" in elem.lower():
                    bar += PY_BOOK
                else:
                    bar += OTHER_BOOK
            print("{} {}".format(k, bar))

    f.close()

# def main():
#     create_chart()

# if __name__ == "__main__":
#     main()
