import os
from pathlib import Path

content = b"""Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

local = os.getcwd()

f = Path("{}/some_file.txt".format(local))
f.write_bytes(content)


def tail(filepath: str, n: int) -> str:
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    lines = list()
    with open(filepath, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            lines.append(line)

    return lines[-n:]


def main():
    print('thank you for mama...')
    # print(tail(f.resolve(), 1))
    assert tail(f.resolve(), 1) == ['Become a PyBites ninja!']
    assert tail(f.resolve(), 2) == ['Keep calm and code in Python!',
                                    'Become a PyBites ninja!']
    actual = tail(f.resolve(), 10)
    expected = [line.decode("utf-8")
                for line in content.splitlines()]
    assert actual == expected


if __name__ == '__main__':
    main()
