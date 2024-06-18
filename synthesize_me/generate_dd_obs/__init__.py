import numpy as np
import pandas as pd
import os

from synthesize_me.generate_dd_obs.dataframe import make_dd_obs_data_for_table

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

