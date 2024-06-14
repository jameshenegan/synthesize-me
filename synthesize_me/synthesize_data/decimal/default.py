import pandas as pd
import numpy as np
from scipy.stats.mstats import winsorize
from scipy.stats import boxcox
from scipy.special import inv_boxcox

def synthesize_default_decimal(
    series: pd.Series, 
    dispersion_amount: float, 
    winsorize_lower_limit: float, 
    winsorize_upper_limit: float, 
    random_seed: int = 42
) -> pd.Series:
    """
    Synthesize a decimal series by winsorizing, applying a Box-Cox transformation,
    adding noise, and then inverting the Box-Cox transformation.

    Parameters:
    - series: pd.Series
        The original series to synthesize.
    - dispersion_amount: float
        The standard deviation of the normal distribution used to generate noise.
    - winsorize_lower_limit: float
        The lower limit for winsorization (between 0 and 1).
    - winsorize_upper_limit: float
        The upper limit for winsorization (between 0 and 1).
    - random_seed: int, default 42
        The seed for the random number generator.

    Returns:
    - pd.Series
        The synthesized series.
    """
    if not isinstance(series, pd.Series):
        raise ValueError("Input must be a pandas Series")

    # Local random number generator
    rand_gen = np.random.default_rng(seed=random_seed)
    
    # Winsorize series
    series_winsorized = pd.Series(winsorize(series, limits=[winsorize_lower_limit, 1 - winsorize_upper_limit]))

    # Ensure all values are positive for Box-Cox transformation
    shift = 0 
    series_winsorized_min = series_winsorized.min()
    min_value_is_not_positive = (series_winsorized_min <= 0)

    if min_value_is_not_positive:
        shift = abs(series_winsorized_min) + 1e-6
    
    series_shifted = series_winsorized + shift

    # Box-Cox Transform
    box_cox, lmbda = boxcox(series_shifted)

    # Generate noise
    noise = rand_gen.normal(0, dispersion_amount, size=series.size)

    # Create modified box_cox
    noisy_box_cox = box_cox + noise

    # Invert noisy_box_cox
    array_modified = inv_boxcox(noisy_box_cox, lmbda)

    # Transform array back to series and reverse the shift
    series_modified = pd.Series(array_modified, index=series.index)
    
    if min_value_is_not_positive:
        series_modified -= shift

    return series_modified
