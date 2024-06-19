from synthesize_me.generate_dd_obs.dataframe.series.guess_data_type import guess_data_type
from synthesize_me.generate_dd_obs.dataframe.series.compute_obs_missing import compute_obs_missing
import pandas as pd
from typing import Dict, Any

def make_dd_obs_entry_for_series(series: pd.Series, metadata: Dict[str, str]) -> Dict[str, Any]:
    """
    Generate the dd_obs entry for a specific series (variable) in the table.

    Parameters:
    - series (pd.Series): The data series to analyze.
    - metadata (Dict[str, str]): Metadata containing 'table_name' and 'var_name'.

    Returns:
    - Dict[str, Any]: A dictionary containing the dd_obs entry for the variable.
    """
    # Extract metadata
    table_name = metadata['table_name']
    var_name = metadata['var_name']

    # Compute basic statistics
    obs_numobs = series.dropna().shape[0]  # Number of non-missing observations
    obs_distinct = series.dropna().nunique()  # Number of distinct non-missing values
    obs_datatype = guess_data_type(series)  # Guess the data type
    obs_missing = compute_obs_missing(series)  # Compute the number and percentage of missing values

    # Initialize the dd_obs entry with basic metadata and statistics
    dd_obs_entry: Dict[str, Any] = {
        'table_name': table_name,
        'var_name': var_name,
        'obs_numobs': obs_numobs,
        'obs_distinct': obs_distinct,
        'obs_missing': obs_missing,
        'obs_datatype': obs_datatype,
    }

    # Add additional statistics based on the data type
    if obs_datatype in ['Integer', 'Decimal']:
        # Compute statistics relevant for numerical data types
        obs_mean = series.mean()
        obs_std = series.std()
        obs_min = series.min()
        obs_p_25 = series.quantile(0.25)
        obs_median = series.median()
        obs_p_75 = series.quantile(0.75)
        obs_max = series.max()

        # Add computed statistics to the dd_obs entry
        dd_obs_entry['obs_mean'] = obs_mean
        dd_obs_entry['obs_std'] = obs_std
        dd_obs_entry['obs_min'] = obs_min
        dd_obs_entry['obs_p_25'] = obs_p_25
        dd_obs_entry['obs_median'] = obs_median
        dd_obs_entry['obs_p_75'] = obs_p_75
        dd_obs_entry['obs_max'] = obs_max

    elif obs_datatype in ['StringList', 'NumberList']:
        # Compute permissible values for categorical or discrete data types
        obs_permissible_values = list(series.dropna().unique())
        obs_permissible_values.sort()

        # Add computed permissible values to the dd_obs entry
        dd_obs_entry['obs_permissible_values'] = obs_permissible_values

    return dd_obs_entry
