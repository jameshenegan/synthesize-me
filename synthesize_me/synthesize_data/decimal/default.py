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

    if not isinstance(series, pd.Series):
        raise ValueError("Input must be a pandas Series")

    if random_seed is not None:
        np.random.seed(random_seed)

    # Generate noise
    noise = np.random.normal(0, dispersion_amount, size=series.size)

    # Create the modified series
    series_modified = series + noise

    return series_modified
