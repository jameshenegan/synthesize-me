import pandas as pd
import os
from synthesize_me.compare import generate_comparison_plots

def main():
    # Paths to necessary files and directories
    path_to_dd_synth = "./example-data/metadata/dd_synth.csv"
    path_to_input_folder_of_csv_files = "./example-data/input"
    path_to_output_folder_of_csv_files = "./example-data/output"
    comparison_output_folder = "./example-data/comparison_plots"

    # Load dd_synth DataFrame
    dd_synth = pd.read_csv(path_to_dd_synth)
    
    # Generate comparison plots
    for table_name in dd_synth['table_name'].unique():
        original_file_path = os.path.join(path_to_input_folder_of_csv_files, f"{table_name}.csv")
        synthesized_file_path = os.path.join(path_to_output_folder_of_csv_files, f"{table_name}.csv")
        if os.path.exists(original_file_path) and os.path.exists(synthesized_file_path):
            original_df = pd.read_csv(original_file_path)
            synth_df = pd.read_csv(synthesized_file_path)
            generate_comparison_plots(original_df, synth_df, dd_synth[dd_synth['table_name'] == table_name], comparison_output_folder)

if __name__ == '__main__':
    main()
