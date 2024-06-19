import os
import pandas as pd
from typing import List, Dict
from synthesize_me.generate_dd_obs.dataframe.series import make_dd_obs_entry_for_series

def make_dd_obs_data_for_table(input_dir: str, file_name: str) -> List[Dict]:
    """
    Generate the dd_obs data for a specific table (CSV file) in the input directory.

    Parameters:
    - input_dir (str): The directory containing the input CSV files.
    - file_name (str): The name of the CSV file to process.

    Returns:
    - List[Dict]: A list of dictionaries, each containing the dd_obs data for a variable in the table.
    """
    # Initialize list to hold the dd_obs data for the table in the input directory
    dd_obs_data: List[Dict] = []
    
    # Construct the full file path and read the CSV file into a DataFrame
    file_path = os.path.join(input_dir, file_name)    
    df = pd.read_csv(file_path)

    # Determine the table name from the file name
    table_name = os.path.splitext(file_name)[0]

    # Process each column (variable) in the DataFrame
    for var_name in df.columns:
        series = df[var_name]
        metadata = {"table_name": table_name, "var_name": var_name}
        dd_obs_entry = make_dd_obs_entry_for_series(series, metadata)
        dd_obs_data.append(dd_obs_entry)        
        
    return dd_obs_data
