from numpy import isnan, nan

from .check_array_for_bad import check_array_for_bad


def compute_empirical_p_value(
    value, random_values, p_value_direction, raise_for_bad=True
):

    is_good = ~check_array_for_bad(random_values, raise_for_bad=raise_for_bad)

    if isnan(value) or not is_good.any():

        return nan

    random_values_good = random_values[is_good]

    if p_value_direction == "<":

        n_significant_random_value = (random_values_good <= value).sum()

    elif p_value_direction == ">":

        n_significant_random_value = (value <= random_values_good).sum()

    if n_significant_random_value == 0:

        return 1 / random_values_good

    else:

        return n_significant_random_value / random_values_good
