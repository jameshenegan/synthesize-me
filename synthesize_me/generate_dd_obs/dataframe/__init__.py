import os

import pandas as pd 

from synthesize_me.generate_dd_obs.dataframe.series import make_dd_obs_entry_for_series


def make_dd_obs_data_for_table(input_dir, file_name):
    
    # Initialize list to hold the dd_obs data for table in input directory
    dd_obs_data = []
    
    file_path = os.path.join(input_dir, file_name)    
    df = pd.read_csv(file_path)

    # Determine table name from file name
    table_name = os.path.splitext(file_name)[0]

    for var_name in df.columns:
        series = df[var_name]
        metadata = {"table_name" : table_name, "var_name" : var_name}
        dd_obs_entry = make_dd_obs_entry_for_series(series, metadata)
        dd_obs_data.append(dd_obs_entry)        
        
    return dd_obs_data

