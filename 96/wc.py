import os
from urllib.request import urlretrieve
from pathlib import Path
import sys

local = os.getcwd()

lines = [b'Hello world',
         b'Keep calm and code in Python',
         b'Have a nice weekend']

py_file = 'https://bites-data.s3.us-east-2.amazonaws.com/driving.py'


def wc(file_: str) -> str:
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    num_lines = 0
    num_words = 0
    num_chars = 0

    with open(file_, 'rb') as f:
        for line in f:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)

    return '{}  {}  {}  {}'.format(str(num_lines), str(num_words), str(num_chars), file_)


# def main():
#     print('thank you for everything...')
#     # # print(local)
#     # f = Path("{}/some_file.txt".format(local))
#     # # some_text = b'\n'.join(lines)
#     # # some_text = lines[0]
#     # some_text = b'\n'.join(lines[:2])
#     # # with open(path, 'wb') as f:
#     # #     f.write(some_text)
#     # f.write_bytes(some_text)
#     # # print(f.resolve())
#     # output = wc(f.resolve())
#     # # print(output)
#     # counts = ' '.join(output.split()[:3])
#     # # print(counts)
#     # # expected = '3 12 60'
#     # # expected = '1 2 11'
#     # expected = '2 8 40'
#     # assert counts == expected
#     # # print(f.name)
#     # assert f.name in output

#     # print(wc(sys.argv[1]))

#     f = Path("{}/driving.py".format(local))
#     urlretrieve(py_file, f)
#     output = wc(f.resolve())
#     print(output)
#     counts = ' '.join(output.split()[:3])
#     # https://twitter.com/pybites/status/1175795375904628736
#     expected = "7 29 216"  # not 8!
#     assert counts == expected
#     assert f.name in output


# if __name__ == '__main__':
#     # make it work from cli like original unix wc
#     main()
