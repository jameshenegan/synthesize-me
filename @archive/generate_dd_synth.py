import pandas as pd
import os

def generate_dd_synth(input_dd_obs_path, output_dd_synth_path, blanket_default_params):
    # Read the dd_obs.csv file
    dd_obs_df = pd.read_csv(input_dd_obs_path)

    # Initialize list to hold dd_synth data
    dd_synth_data = []

    # Calculate dispersion_amount based on IQR and blanket_default_params
    for _, row in dd_obs_df.iterrows():
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

    # Create DataFrame and save to CSV
    dd_synth_df = pd.DataFrame(dd_synth_data)
    dd_synth_df.to_csv(output_dd_synth_path, index=False)

    print(f"CSV file 'dd_synth.csv' created successfully in {output_dd_synth_path}.")

if __name__ == '__main__':
    input_dd_obs_path = os.path.join('metadata', 'dd_obs.csv')
    output_dd_synth_path = os.path.join('metadata', 'dd_synth.csv')
    blanket_default_params = {
        "dispersion_factor": 0.05,
        "winsorize_lower_limit": 0.05,
        "winsorize_upper_limit": 0.95
    }

    generate_dd_synth(input_dd_obs_path, output_dd_synth_path, blanket_default_params)
