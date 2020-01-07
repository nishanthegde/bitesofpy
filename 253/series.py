import pandas as pd
import string
import numpy as np


def series_simple_math(
    ser: pd.Series, function: str, number: int
) -> pd.core.series.Series:
    """Write some simple math helper functions for series.
    Take the given series, perfrom the required operation and
        return the new series.
    For example. Give the series:
        0    0
        1    1
        2    2
        dtype: int64
    Function 'add' and 'number' 2 you should return
        0     2
        1     3
        2     4
        dtype: int64
    :param ser: Series to perform operation on
    :param function: The operation to perform
    :param number: The number to apply the operation to
    """
    if function == 'add':
        return ser + number
    elif function == 'sub':
        return ser - number
    elif function == 'mul':
        return ser * number
    elif function == 'div':
        return ser / number


def complex_series_maths(
    ser_01: pd.Series, ser_02: pd.Series, function: str
) -> pd.core.series.Series:
    """Write some math helper functions for series.
    Take the two given series, perfrom the required operation and
        return the new series.
    For example. Give the series:
        0    0
        1    1
        2    2
        dtype: int64

    And the series:
        0     2
        1     3
        2     4
        dtype: int64

    If the function given is 'add' you should return
        0     2
        1     4
        2     6
        dtype: int64

    :param ser_01: Primary series to perform operation on
    :param ser_02: Secondary series to perform operation on
    :param function: The operation to perform

    Note:
    For this function always add ser_02 to ser_01,
        subtract ser_02 from ser_01,
        multiply ser_01 by ser_02,
        divide ser_01 by ser_02
    Don't worry about None's and NaN and divide by zero.
        Let pandas do the work for you.
    """
    if function == 'add':
        return ser_01 + ser_02
    elif function == 'sub':
        return ser_01 - ser_02
    elif function == 'mul':
        return ser_01 * ser_02
    elif function == 'div':
        return ser_01 / ser_02


def create_series_mask(ser: pd.Series, mask: list) -> pd.core.series.Series:
    """Write a trivial function to create a pandas series mask of a list
    of letters.
    Be careful, although this sounds very similar to the .mask() method,
        that's not what we're looking for here.
    For example. Give the series x:
        0    0
        1    1
        2    2
        3    3
        4    4
        dtype: int64

    You can create a mask for even numbers like this:
    >>> mask = x % 2 == 0
    >>> mask
        0     True
        1    False
        2     True
        3    False
        4     True
        dtype: bool

    And then apply the mask:
    >>> x[mask]
        0    0
        2    2
        4    4
        dtype: int64

    Of course for simpler masks you can just do this:
    >>> x[x % 2 == 0]
        0    0
        2    2
        4    4
        dtype: int64

    :param ser: Series to perform operation on
    :param mask: The list of letters to be masked
    """
    return ser.isin(mask)


def custom_series_function(ser: pd.Series,
                           within: int) -> pd.core.series.Series:
    """A more challenging mask to apply.
    When passed a series of floats, return all values
        within the given rage of:
         - the minimum value
         - the 1st quartile value
         - the second quartile value
         - the mean
         - the third quartile value
         - the maximum value
    You may want to brush up on some simple statistics to help you here.
    Also, the series is passed to you sorted assending.
        Be sure that you don't return values out of sequence.

    So, for example if you mean is 5.0 and within is 0.1
        return all value between 4.9 and 5.1 inclusive

    :param ser: Series to perform operation on
    :param within: The value to calculate the range of number within
    """
    start_min = ser.min() - within
    end_min = ser.min() + within

    start_lower = np.percentile(ser, 25) - within
    end_lower = np.percentile(ser, 25) + within

    start_med = np.percentile(ser, 50) - within
    end_med = np.percentile(ser, 50) + within

    start_mean = ser.mean() - within
    end_mean = ser.mean() + within

    start_upper = np.percentile(ser, 75) - within
    end_upper = np.percentile(ser, 75) + within

    start_max = ser.max() - within
    end_max = ser.max() + within

    return ser[ser.between(start_min, end_min, inclusive=True)
               | ser.between(start_lower, end_lower, inclusive=True)
               | ser.between(start_med, end_med, inclusive=True)
               | ser.between(start_mean, end_mean, inclusive=True)
               | ser.between(start_upper, end_upper, inclusive=True)
               | ser.between(start_max, end_max, inclusive=True)]


# def main():
#     print('thank you for everything you have given me...')

#     file_name = "https://bites-data.s3.us-east-2.amazonaws.com/iris.csv"
#     df = pd.read_csv(file_name)
#     # print(df.head(2))
#     # print(df.shape)
#     sepal_length_series = df.sepal_length.sort_values().reset_index(drop=True)
#     int_series_vsmall = pd.Series(range(1, 6))
#     int_series_small = pd.Series(range(10))
#     int_series_vsmall_offset_index = pd.Series(range(0, 10, 2), index=range(0, 10, 2))
#     letters_series = pd.Series(list(string.ascii_lowercase))

#     # print(series_simple_math(int_series_small, 'add', 2))
#     # print(complex_series_maths(int_series_vsmall, int_series_vsmall_offset_index, 'add'))
#     # print(create_series_mask(letters_series, ["a", "e", "i", "o", "u"]))
#     # print(letters_series.isin(["a", "e", "i", "o", "u"]))
#     # print(sepal_length_series)

#     print(sepal_length_series.min())
#     print(np.percentile(sepal_length_series, 25))
#     print(np.percentile(sepal_length_series, 50))
#     print(sepal_length_series.mean())
#     print(np.percentile(sepal_length_series, 75))
#     print(sepal_length_series.max())

#     start_min = sepal_length_series.min() - .1
#     end_min = sepal_length_series.min() + .1
#     # print(start, end)
#     ser1 = sepal_length_series[sepal_length_series.between(start_min, end_min, inclusive=True)]
#     # print(ser1)
#     # print(len(ser1))

#     start_lower = np.percentile(sepal_length_series, 25) - .1
#     end_lower = np.percentile(sepal_length_series, 25) + .1
#     # print(start, end)
#     ser2 = sepal_length_series[sepal_length_series.between(start_lower, end_lower, inclusive=True)]
#     # print(ser2)
#     # print(len(ser2))

#     start_med = np.percentile(sepal_length_series, 50) - .1
#     end_med = np.percentile(sepal_length_series, 50) + .1
#     # print(start, end)
#     ser3 = sepal_length_series[sepal_length_series.between(start_med, end_med, inclusive=True)]
#     # print(ser3)
#     # print(len(ser3))

#     start_mean = sepal_length_series.mean() - .1
#     end_mean = sepal_length_series.mean() + .1
#     # print(start, end)
#     ser4 = sepal_length_series[sepal_length_series.between(start_mean, end_mean, inclusive=True)]
#     # print(ser4)
#     # print(len(ser4))

#     start_upper = np.percentile(sepal_length_series, 75) - .1
#     end_upper = np.percentile(sepal_length_series, 75) + .1
#     # print(start, end)
#     ser5 = sepal_length_series[sepal_length_series.between(start_upper, end_upper, inclusive=True)]
#     # print(ser5)
#     # print(len(ser5))

#     start_max = sepal_length_series.max() - .1
#     end_max = sepal_length_series.max() + .1
#     # print(start, end)
#     ser6 = sepal_length_series[sepal_length_series.between(start_max, end_max, inclusive=True)]
#     # print(ser6)
#     # print(len(ser6))
#     # print(ser3.append(ser4, ignore_index=False))
#     # print(len(ser3.append(ser4, ignore_index=False)))

#     # result = sepal_length_series[sepal_length_series.between(start_min, end_min, inclusive=True)
#     #                              | sepal_length_series.between(start_lower, end_lower, inclusive=True)
#     #                              | sepal_length_series.between(start_med, end_med, inclusive=True)
#     #                              | sepal_length_series.between(start_mean, end_mean, inclusive=True)
#     #                              | sepal_length_series.between(start_upper, end_upper, inclusive=True)
#     #                              | sepal_length_series.between(start_max, end_max, inclusive=True)]
#     result = custom_series_function(sepal_length_series, 0.1)

#     print('----------')
#     print(len(result))
#     print(round(result.mean(), 4))
#     print(max(result.index))
#     print(max(result.values))
#     print(min(result.index))
#     print(min(result.values))
#     print(result[82])
#     print(result.iloc[10])
#     print(result.iloc[11])
#     print(result.iloc[20])
#     print(result.iloc[37])
#     print(result.iloc[38])


# if __name__ == '__main__':
#     main()
