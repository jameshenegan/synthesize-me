import pandas as pd

def create_dd_synth(dd_obs, blanket_default_params):    

    # Initialize list to hold dd_synth data
    dd_synth_data = []

    # Calculate dispersion_amount based on IQR and blanket_default_params
    for _, row in dd_obs.iterrows():
        table_name = row['table_name']
        var_name = row['var_name']
        datatype = row['obs_datatype']
        iqr = row['obs_p_75'] - row['obs_p_25']
        dispersion_amount = blanket_default_params['dispersion_factor'] * iqr
        winsorize_lower_limit = blanket_default_params['winsorize_lower_limit']
        winsorize_upper_limit = blanket_default_params['winsorize_upper_limit']

        dd_synth_data.append({
            'table_name': table_name,
            'var_name': var_name,
            'datatype': datatype,
            'dispersion_amount': dispersion_amount,
            'winsorize_lower_limit': winsorize_lower_limit,
            'winsorize_upper_limit': winsorize_upper_limit
        })

    # Create DataFrame 
    dd_synth_df = pd.DataFrame(dd_synth_data)
    return dd_synth_df