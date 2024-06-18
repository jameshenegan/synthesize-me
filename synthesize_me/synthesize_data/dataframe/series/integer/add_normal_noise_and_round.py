import pandas as pd
import numpy as np

def add_normal_noise_and_round(
    series: pd.Series, 
    dispersion_amount: float, 
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

    return series_modified.round()
