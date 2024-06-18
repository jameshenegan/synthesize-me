import pandas as pd
import os
from .dataframe import synthesize_table_data

def create_csv_files_of_synth_data(
        dd_synth,
        path_to_input_folder_of_csv_files,
        path_to_output_folder_of_csv_files
):
    # Ensure the output directory exists
    if not os.path.exists(path_to_output_folder_of_csv_files):
        os.makedirs(path_to_output_folder_of_csv_files)

    # Process each file according to dd_synth
    for table_name in dd_synth['table_name'].unique():
        file_path = os.path.join(path_to_input_folder_of_csv_files, f"{table_name}.csv")
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            synth_df = synthesize_table_data(df, dd_synth[dd_synth['table_name'] == table_name])
            output_path = os.path.join(path_to_output_folder_of_csv_files, f"{table_name}.csv")
            synth_df.to_csv(output_path, index=False)

