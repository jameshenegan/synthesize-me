import pandas as pd
import numpy as np
from scipy.stats.mstats import winsorize
from typing import Optional

def winsorize_and_add_normal_noise(
    series: pd.Series, 
    dispersion_amount: float, 
    winsorize_lower_limit: float = 0.05,
    winsorize_upper_limit: float = 0.95,
    random_seed: Optional[int] = 42
) -> pd.Series:
    """
    Winsorize a series and add normal noise.

    Parameters:
    - series (pd.Series): The input data series to be modified.
    - dispersion_amount (float): The standard deviation of the normal noise to be added.
    - winsorize_lower_limit (float, optional): The lower limit for winsorization (default is 0.05).
    - winsorize_upper_limit (float, optional): The upper limit for winsorization (default is 0.95).
    - random_seed (Optional[int], optional): Seed for the random number generator to ensure reproducibility (default is 42).

    Returns:
    - pd.Series: The modified series after winsorization and addition of normal noise.
    """
    if not isinstance(series, pd.Series):
        raise ValueError("Input must be a pandas Series")

    # Set random seed for reproducibility
    rand_gen = np.random.default_rng(seed=random_seed)

    # Winsorize series
    series_winsorized = pd.Series(winsorize(series, limits=[winsorize_lower_limit, 1 - winsorize_upper_limit]))

    # Generate noise
    noise = rand_gen.normal(0, dispersion_amount, size=series.size)

    # Create the modified series
    series_modified = series_winsorized + noise

    return series_modified
