from numpy import nan
from pandas import DataFrame, concat

from .BAD_VALUES import BAD_VALUES
from .binarize import binarize
from .guess_data_type import guess_data_type


def separate_information_x_sample(information_x_sample, bad_values=BAD_VALUES):

    continuouses = []

    binaries = []

    for information, values in information_x_sample.iterrows():

        values = values.replace(bad_values, nan)

        if 1 < values.dropna().unique().size:

            try:

                is_continuous = guess_data_type(values.astype(float)) == "continuous"

            except ValueError as exception:

                print("({}) {} is not continuous.".format(exception, information))

                is_continuous = False

            if is_continuous:

                continuouses.append(values)

            else:

                binaries.append(binarize(values))

    if 0 < len(continuouses):

        continuous_information_x_sample = DataFrame(continuouses)

    else:

        continuous_information_x_sample = None

    if 0 < len(binaries):

        binary_information_x_sample = concat(binaries)

    else:

        binary_information_x_sample = None

    return continuous_information_x_sample, binary_information_x_sample
