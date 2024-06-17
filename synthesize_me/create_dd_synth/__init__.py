import pandas as pd
from .decimal import handle_decimal
from .numberlist import handle_numberlist
from .integer import handle_integer

def create_dd_synth(dd_obs, blanket_default_params):    
    """
    Create the dd_synth DataFrame based on the dd_obs DataFrame and blanket default parameters.

    Parameters:
    - dd_obs: pd.DataFrame
        The observation data dictionary.
    - blanket_default_params: dict
        Default parameters for dispersion and winsorization.

    Returns:
    - pd.DataFrame
        The synthesized data dictionary.
    """

    # Initialize list to hold dd_synth data
    dd_synth_data = []

    # Process each row in dd_obs
    for _, row in dd_obs.iterrows():        
        datatype = row['obs_datatype']

        if datatype == 'Decimal':
            synth_row = handle_decimal(row, blanket_default_params)
        elif datatype == 'NumberList':
            synth_row = handle_numberlist(row, blanket_default_params)
        elif datatype == 'Integer':
            synth_row = handle_integer(row, blanket_default_params)
        else:
            # Add more data type handlers as needed
            synth_row = handle_default(row, blanket_default_params)

        dd_synth_data.append(synth_row)

    # Create DataFrame 
    dd_synth_df = pd.DataFrame(dd_synth_data)
    return dd_synth_df







def handle_default(row, blanket_default_params):
    """
    Handle the synthesis parameters for default data types.

    Parameters:
    - row: pd.Series
        The row from dd_obs.
    - blanket_default_params: dict
        Default parameters for dispersion and winsorization.

    Returns:
    - dict
        The synthesized row dictionary.
    """
    dispersion_amount = blanket_default_params['dispersion_factor'] * 1  # Adjust as needed
    winsorize_lower_limit = blanket_default_params['winsorize_lower_limit']
    winsorize_upper_limit = blanket_default_params['winsorize_upper_limit']

    return {
        'table_name': row['table_name'],
        'var_name': row['var_name'],
        'datatype': row['obs_datatype'],
        'dispersion_amount': dispersion_amount,
        'winsorize_lower_limit': winsorize_lower_limit,
        'winsorize_upper_limit': winsorize_upper_limit
    }
