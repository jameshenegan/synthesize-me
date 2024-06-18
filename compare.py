         
import pandas as pd
import os
from synthesize_me.compare import generate_comparison_plots, compare_number_list_vars_for_table

def main():
    # Paths to necessary files and directories
    path_to_dd_synth = "./example-data/metadata/dd_synth.csv"
    path_to_input_folder_of_csv_files = "./example-data/input"
    path_to_output_folder_of_csv_files = "./example-data/output"
    comparison_output_folder = "./example-data/comparison_plots"
    path_to_output_of_number_list_comparison_metadata = "./example-data/comparison_csvs/number_lists.csv"

    # Load dd_synth DataFrame
    dd_synth = pd.read_csv(path_to_dd_synth)

    aggregated_number_list_comparison_data = []

    # Generate comparison plots
    for table_name in dd_synth['table_name'].unique():
        original_file_path = os.path.join(path_to_input_folder_of_csv_files, f"{table_name}.csv")
        synthesized_file_path = os.path.join(path_to_output_folder_of_csv_files, f"{table_name}.csv")

        if os.path.exists(original_file_path) and os.path.exists(synthesized_file_path):
            original_df = pd.read_csv(original_file_path)
            synth_df = pd.read_csv(synthesized_file_path)
            generate_comparison_plots(original_df, synth_df, dd_synth[dd_synth['table_name'] == table_name], comparison_output_folder)

            number_list_comparison_data_for_table = compare_number_list_vars_for_table(
                original_df, 
                synth_df,
                table_name, 
                 dd_synth[dd_synth['table_name'] == table_name])

            aggregated_number_list_comparison_data += number_list_comparison_data_for_table

    pd.DataFrame(aggregated_number_list_comparison_data).to_csv(path_to_output_of_number_list_comparison_metadata, index=False)

            
if __name__ == '__main__':
    main()
