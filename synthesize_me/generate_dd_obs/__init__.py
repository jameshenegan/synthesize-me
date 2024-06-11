import numpy as np
import pandas as pd
import os

from synthesize_me.generate_dd_obs.guess_data_type import guess_data_type


def generate_dd_obs(path_to_input_folder_of_csv_files):
    # Initialize list to hold the dd_obs data for all tables in input directory
    dd_obs_data = []

    # Process each file in the input directory
    for file_name in os.listdir(path_to_input_folder_of_csv_files):
        if file_name.endswith('.csv'):        
            # Create a dictionary containing the dd_obs_data for this table
            dd_obs_data += make_dd_obs_data_for_table(path_to_input_folder_of_csv_files, file_name)

    # Create DataFrame 
    dd_obs_df = pd.DataFrame(dd_obs_data)
    return dd_obs_df


def make_dd_obs_data_for_table(input_dir, file_name):
    
    # Initialize list to hold the dd_obs data for table in input directory
    dd_obs_data = []
    
    file_path = os.path.join(input_dir, file_name)    
    df = pd.read_csv(file_path)

    # Determine table name from file name
    table_name = os.path.splitext(file_name)[0]

    for var_name in df.columns:
        obs_datatype = guess_data_type(df[var_name])
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
        
    return dd_obs_data
