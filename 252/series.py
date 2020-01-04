import numpy as np
import pandas as pd
import series as se
import string


def return_at_index(ser: pd.Series, idx: int) -> object:
    """Return the Object at the given index of the Series
    If you want to be extra careful catch and raise an error if
       the index does not exist.
    """
    if not ser.index.contains(idx):
        raise KeyError('index {} doex not exist'.format(idx))

    return ser[idx]


def get_slice(ser: pd.Series, start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end.
    """
    return ser.iloc[start:end]


def get_slice_inclusive(ser: pd.Series,
                        start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end inclusive.
    """
    return ser.loc[start:end]


def return_head(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the first num elements of the given Series.
    """
    return ser.head(num)


def return_tail(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the last num elements of the given Series.
    """
    return ser.tail(num)


def get_index(ser: pd.Series) -> pd.core.indexes.base.Index:
    """Return all indexes of the given Series.
    """
    return ser.index


def get_values(ser: pd.Series) -> np.ndarray:
    """Return all the values of the given Series.
    """
    return ser.values


def get_every_second_indexes(ser: pd.Series,
                             even_index=True) -> pd.core.series.Series:
    """Return all rows where the index is either even or odd.
    If even_index is True return every index where idx % 2 == 0
    If even_index is False return every index where idx % 2 != 0
    Assume default indexing i.e. 0 -> n
    """
    if even_index:
        return ser.iloc[::2]
    else:
        return ser.iloc[1::2]


# def main():
#     print('thank you for giving me what you have give me...')

#     float_Series = pd.Series([float(n) / 1000 for n in range(0, 1001)])
#     assert return_at_index(float_Series, 0) == 0.000
#     assert return_at_index(float_Series, 1000) == 1.0000
#     # print(return_at_index(float_Series, 1111))

#     slce = se.get_slice(float_Series, 20, 25)
#     # print(slce)
#     assert isinstance(slce, pd.core.series.Series)
#     assert len(slce) == 5
#     assert slce[24] == 0.024

#     slce = se.get_slice_inclusive(float_Series, 20, 25)
#     # print(slce)
#     assert isinstance(slce, pd.core.series.Series)
#     assert len(slce) == 6
#     assert slce[25] == 0.025

#     assert se.return_head(float_Series, 10)[0] == 0.000
#     assert se.return_head(float_Series, 10)[5] == 0.005
#     assert se.return_head(float_Series, 10)[9] == 0.009

#     assert se.return_tail(float_Series, 10)[991] == 0.991
#     assert se.return_tail(float_Series, 10)[995] == 0.995
#     assert se.return_tail(float_Series, 10)[1000] == 1.000

#     dictionary = dict(zip(string.ascii_lowercase, range(1, 27)))
#     alpha_series = pd.Series(dictionary)
#     # print(alpha_series)

#     idx = se.get_index(alpha_series)
#     assert isinstance(idx, pd.core.indexes.base.Index)
#     assert len(idx) == 26
#     assert all(c in string.ascii_lowercase for c in idx.values)

#     vals = se.get_values(alpha_series)
#     assert isinstance(vals, np.ndarray)
#     assert len(vals) == 26
#     # print(vals)
#     assert all(c in range(1, 27) for c in vals)

#     ser = se.get_every_second_indexes(float_Series, True)
#     assert all(n % 2 == 0 for n in ser.index)
#     assert round(sum(ser), 1) == 250.5

#     ser = se.get_every_second_indexes(float_Series, False)
#     assert all(n % 2 == 1 for n in ser.index)
#     assert round(sum(ser), 1) == 250.0


# if __name__ == '__main__':
#     main()
