import pandas as pd
import numpy as np

from scipy.stats import boxcox
from scipy.special import inv_boxcox

def bxcx_normnoise_invbxcx(series, dispersion_amount, random_seed=42):
   
    if not isinstance(series, pd.Series):
        raise ValueError("Input must be a pandas Series")

    rand_gen = np.random.default_rng(seed = random_seed)


    # Calculates minimum series values for purposes of only feeding positive values
    # into boxcox()
    min_val = series.min()

    # If min_val is not positive, adjusts series by adding -(min_val) plus small number
    if min_val <= 0:
      series = series - min_val + 1e-6

    # Box Cox Transform
    # Note box_cox returns numpy array, not series
    box_cox, lmbda = boxcox(series)
   
    # Generate noise
    noise = rand_gen.normal(0, dispersion_amount, size=series.size)

    # Create modified box_cox
    noisy_box_cox = box_cox + noise

    # Invert noisy_box_cox
    array_modified = inv_boxcox(noisy_box_cox, lmbda)

    # Subtracts back out adjustment if min_val is not positive
    if min_val <= 0:
      array_modified = array_modified + min_val - 1e-6

    # Transform array to back to series
    series_modified = pd.Series(array_modified)

    # Reindex modified series to input series (without this line, the helper
    # function does not perserve non-sequential input indicies)
    series_modified = series_modified.reindex(series.index)

    return series_modified