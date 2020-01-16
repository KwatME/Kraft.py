from .drop_dataframe_slice import drop_dataframe_slice


def drop_dataframe_slice_greedily(
    dataframe,
    axis,
    max_na=None,
    min_n_not_na_value=None,
    min_n_not_na_unique_value=None,
):

    shape_before = dataframe.shape

    if axis is None:

        axis = int(dataframe.shape[0] < dataframe.shape[1])

    can_return = False

    while True:

        dataframe = drop_dataframe_slice(
            dataframe,
            axis,
            max_na=max_na,
            min_n_not_na_value=min_n_not_na_value,
            min_n_not_na_unique_value=min_n_not_na_unique_value,
        )

        shape_after = dataframe.shape

        if can_return and shape_before == shape_after:

            return dataframe

        shape_before = shape_after

        axis = (axis + 1) % 2

        can_return = True