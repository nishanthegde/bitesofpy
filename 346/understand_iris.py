__all__ = [
    "IRIS_DATA",
    "get_nr_classes",
    "get_nr_samples",
    "get_dim",
    "get_nr_samples_per_class",
    "get_rel_nr_samples_per_class",
    "get_nr_missing_values",
    "get_stats_per_feature",
    "get_correlation_per_feature",
]  # __all__ controls what gets imported if you use from module.py import *.

import pandas as pd
from sklearn.datasets import load_iris
import numpy as np

# you can set as_frame to False, but this will complicate the solution
# because you have to work with numpyand arrays
IRIS_DATA = load_iris(as_frame=True, return_X_y=True)


def get_nr_classes(data: tuple) -> int:
    """Return the number of classes in the Iris data set.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of classes (targets) in the data set.
    """
    if data:
        if isinstance(data[1], pd.Series):
            classes = list(data[1].unique())
            return len(classes)
        else:
            raise ValueError("Data passed is invalid!")
    else:
        raise ValueError("Data passed is invalid!")


def get_nr_samples(data: tuple) -> int:
    """Return the number of samples in the Iris data set.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of samples (instances) in the data set.
    """

    if data:
        if isinstance(data[1], pd.Series):
            nr_samples = data[1].size
            return nr_samples
        else:
            raise ValueError("Data passed is invalid!")
    else:
        raise ValueError("Data passed is invalid!")


def get_dim(data: tuple) -> int:
    """Return the dimensionality of the Iris data set.

    **Warning**: Dimensionality is not meant in the mathematical sense
        (which would be the shape and dim attribute if we would talk about matrices).
        Dimensionality in ML means the number of dimensions in your data,
        that is the number of axes your data span over, which is the number of features we
        have available.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of dimensions (features) in the data set.
    """
    if data:
        if isinstance(data[0], pd.DataFrame):
            dim = list(data[0].columns)
            return len(dim)
        else:
            raise ValueError("Data passed is invalid!")
    else:
        raise ValueError("Data passed is invalid!")


def get_nr_samples_per_class(data: tuple) -> pd.Series:
    """Return the number of samples for each class of the Iris data set.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        pd.Series: Series with number of samples for each class.
    """
    if data:
        if isinstance(data[1], pd.Series):
            return data[1].value_counts()
        else:
            raise ValueError("Data passed is invalid!")
    else:
        raise ValueError("Data passed is invalid!")


def get_rel_nr_samples_per_class(data: tuple) -> pd.Series:
    """Return the relative number of samples for each class of the Iris data set.

    **Hint**: Try to re-use already defined functions.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        pd.Series: Series with percentage (between 0 and 1) of samples for each class.
    """
    if data:
        if isinstance(data[1], pd.Series):
            return get_nr_samples_per_class(data) / get_nr_samples(data)
        else:
            raise ValueError("Data passed is invalid!")
    else:
        raise ValueError("Data passed is invalid!")


def get_nr_missing_values(data: tuple) -> int:
    """Return the number of missing values in the Iris data set.

    **Hint**: pandas isna() might come in handy.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of missing values in the data set.
    """
    # sum can only sum along axis 0 (indices) or 1 (columns), so we need to call it twice
    if data:
        if isinstance(data[0], pd.DataFrame):
            sum1 = data[0].isna().sum(axis=0).sum()
            sum2 = data[1].isna().sum()

            return sum1 + sum2
        else:
            raise ValueError("Data passed is invalid!")
    else:
        raise ValueError("Data passed is invalid!")


def get_stats_per_feature(
        data: tuple,
        features: list,
        stats: list,
) -> pd.DataFrame:
    """Return summary statistics for a list of given features.

    **Hint**: Maybe try out pandas.DataFrame.describe() or pandas.DataFrame.agg().

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().
        features (list): A list of features for which to calculate summary statistics.
        stats (list): A list of summary statistics to calculate/extract for the given features.

    Returns:
        pd.DataFrame: A data frame with the requested summary statistics for each feature.
    """
    stats_dict = {}
    # stats_dict['feature'] = features
    if data:
        if isinstance(data[0], pd.DataFrame):
            for stat in stats:
                stat_list = []
                if stat == 'mean':
                    for f in features:
                        stat_list.append(round(data[0][f].mean(), 2))
                elif stat == 'min':
                    for f in features:
                        stat_list.append(round(data[0][f].min(), 2))
                elif stat == 'max':
                    for f in features:
                        stat_list.append(round(data[0][f].max(), 2))
                elif stat == 'std':
                    for f in features:
                        stat_list.append(round(data[0][f].std(), 2))

                stats_dict[stat] = stat_list

            return pd.DataFrame(stats_dict).T
        else:
            raise ValueError("Data passed is invalid!")
    else:
        raise ValueError("Data passed is invalid!")


def get_correlation_per_feature(
        data: tuple,
        features: list,
) -> pd.DataFrame:
    """Return feature correlation with target.

    **Hint**: Correlation coefficients can be calculated for each pair of feature with pandas.DataFrame.corr().
        This means you might have to combine the features and the target into a single data frame.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().
        features (list): A list with feature names for which the correlation is returned.

    Returns:
        pd.Series: Value of feature correlation with target.
    """
    if data:
        if isinstance(data[0], pd.DataFrame):
            new_data = data[0].assign(target=data[1])
            return new_data.corr(method='pearson').loc[features, 'target']
        else:
            raise ValueError("Data passed is invalid!")
    else:
        raise ValueError("Data passed is invalid!")

