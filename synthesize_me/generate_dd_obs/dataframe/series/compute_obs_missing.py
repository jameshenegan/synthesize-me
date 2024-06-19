import pandas as pd

def compute_obs_missing(series: pd.Series) -> str:
    """
    Compute the number and percentage of missing values in a pandas Series.

    Parameters:
    - series (pd.Series): The data series to analyze.

    Returns:
    - str: A formatted string showing the number and percentage of missing values.
    """
    # Calculate the number of missing values
    num_missing = series.isna().sum()
    
    # Calculate the proportion of missing values
    prop_missing = num_missing / len(series)
    
    # Format the percentage of missing values
    pct_missing = f'{prop_missing * 100:.2f}%'
    
    # Combine the number and percentage of missing values into a formatted string
    obs_missing = f'{num_missing} ({pct_missing})'
    
    return obs_missing
