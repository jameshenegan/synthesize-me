import pandas as pd
import os
from typing import List, Dict
from synthesize_me.generate_dd_obs.dataframe import make_dd_obs_data_for_table

def generate_dd_obs(path_to_input_folder_of_csv_files: str) -> pd.DataFrame:
    """
    Generate the dd_obs DataFrame based on the CSV files in the specified input folder.

    Parameters:
    - path_to_input_folder_of_csv_files (str): Path to the folder containing input CSV files.

    Returns:
    - pd.DataFrame: The generated dd_obs DataFrame containing observed data statistics for each variable.
    """
    # Initialize list to hold the dd_obs data for all tables in the input directory
    dd_obs_data: List[Dict] = []

    # Get and sort the list of files in the input folder
    list_of_files_in_input_folder = os.listdir(path_to_input_folder_of_csv_files)
    list_of_files_in_input_folder.sort()
    
    # Process each file in the input directory
    for file_name in list_of_files_in_input_folder:
        if file_name.endswith('.csv'):
            # Create a dictionary containing the dd_obs data for this table
            dd_obs_data += make_dd_obs_data_for_table(path_to_input_folder_of_csv_files, file_name)

    # Create DataFrame 
    dd_obs_df = pd.DataFrame(dd_obs_data)
    return dd_obs_df
