from numpy import nan
from numpy.random import choice
from pandas import DataFrame, Series

from .simulate_array import simulate_array


def simulate_series_or_dataframe(
    name_0, name_1, *simulate_array_arguments, break_dataframe=None
):

    array = simulate_array(*simulate_array_arguments)

    index = ("{}{}".format(name_0, i) for i in range(array.shape[0]))

    if len(array.shape) == 1:

        series_or_dataframe = Series(array, index=index, name=name_1)

    elif len(array.shape) == 2:

        series_or_dataframe = DataFrame(
            array,
            index=index,
            columns=("{}{}".format(name_1, i) for i in range(array.shape[1])),
        )

    if len(series_or_dataframe.shape) == 2 and break_dataframe is not None:

        if break_dataframe < series_or_dataframe.shape[0]:

            for i in range(break_dataframe):

                series_or_dataframe.iloc[i] = i

        series_or_dataframe.loc[
            choice(
                series_or_dataframe.index,
                size=series_or_dataframe.shape[0] // break_dataframe,
                replace=False,
            ),
            choice(
                series_or_dataframe.columns,
                size=series_or_dataframe.shape[1] // break_dataframe,
                replace=False,
            ),
        ] = nan

    return series_or_dataframe