import numpy as np
import pandas as pd
import os

def generate_dd_obs(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize list to hold dd_obs data
    dd_obs_data = []

    # Process each file in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_dir, file_name)
            df = pd.read_csv(file_path)

            # Determine table name from file name
            table_name = os.path.splitext(file_name)[0]

            for var_name in df.columns:
                obs_datatype = 'Decimal'
                obs_mean = df[var_name].mean()
                obs_std = df[var_name].std()
                obs_min = df[var_name].min()
                obs_p_25 = df[var_name].quantile(0.25)
                obs_median = df[var_name].median()
                obs_p_75 = df[var_name].quantile(0.75)
                obs_max = df[var_name].max()
                
                dd_obs_data.append({
                    'table_name': table_name,
                    'var_name': var_name,
                    'obs_datatype': obs_datatype,
                    'obs_mean': obs_mean,
                    'obs_std': obs_std,
                    'obs_min': obs_min,
                    'obs_p_25': obs_p_25,
                    'obs_median': obs_median,
                    'obs_p_75': obs_p_75,
                    'obs_max': obs_max
                })

    # Create DataFrame and save to CSV
    dd_obs_df = pd.DataFrame(dd_obs_data)
    dd_obs_df.to_csv(os.path.join(output_dir, 'dd_obs.csv'), index=False)

    print(f"CSV file 'dd_obs.csv' created successfully in {output_dir}.")

if __name__ == '__main__':
    generate_dd_obs('input', 'metadata')
