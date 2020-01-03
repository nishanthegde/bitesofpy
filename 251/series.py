import string as s

import pandas as pd
import series as se
import numpy as np


def basic_series() -> pd.Series:
    """Create a pandas Series containing the values 1, 2, 3, 4, 5
    Don't worry about the indexes for now.
    The name of the series should be 'Fred'
    """
    l = [i for i in range(1, 6)]

    return pd.Series(l).rename("Fred")


def float_series() -> pd.Series:
    """Create a pandas Series containing the all the values
    from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
    Don't worry about the indexes or the series name.
    """
    l = [i for i in np.arange(0.000, 1.001, 0.001)]

    return pd.Series(l)


def alpha_index_series() -> pd.Series:
    """Create a Series with values 1, 2, ... 25, 26 of type int64
    and add an index with values a, b, ... y, z
    so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
    Don't worry about the series name.
    """
    l = [i for i in range(1, 27)]
    idx = [a for a in s.ascii_lowercase]

    return pd.Series(l, index=idx)


def object_values_series() -> pd.Series:
    """Create a Series with values A, B, ... Y, Z of type object
    and add an index with values 101, 102, ... 125, 126
    so index 101='A', 102='B' ... 125='Y', 126='Z'
    Don't worry about the series name.
    """
    l = [a.upper() for a in s.ascii_uppercase]
    idx = [i for i in range(101, 127)]

    return pd.Series(l, index=idx, dtype='object')


# def main():
#     print('thank you for giving me so much - I am very grateful...')

#     ser = se.basic_series()
#     assert isinstance(ser, pd.Series)
#     assert ser.name == "Fred"
#     assert ser.dtype == "int64"
#     assert all(n in [1, 2, 3, 4, 5] for n in ser.values)

#     ser = se.float_series()
#     assert isinstance(ser, pd.Series)
#     assert ser.dtype == "float64"
#     assert len(ser) == 1001
#     assert ser.sum() == 500.5

#     ser = se.alpha_index_series()
#     assert isinstance(ser, pd.Series)
#     assert ser.dtype == "int64"
#     assert len(ser) == 26
#     assert sum(ser.values) == 351
#     assert all(c in s.ascii_lowercase for c in ser.index)

#     ser = se.object_values_series()
#     assert isinstance(ser, pd.Series)
#     assert len(ser) == 26
#     assert all(c in s.ascii_uppercase for c in ser.values)
#     assert ser[101] == "A"
#     assert ser[126] == "Z"


# if __name__ == '__main__':
#     main()
