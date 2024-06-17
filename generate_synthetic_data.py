import pandas as pd
import logging
from synthesize_me import synthesize_folder_of_csv_files

def main():
    """
    Use the dd_synth generated during the example usage to synthesize data from input CSV files.
    """
    # Paths to necessary files and directories
    path_to_dd_synth = "./example-data/metadata/dd_synth.csv"
    path_to_input_folder_of_csv_files = "./example-data/input"
    path_to_output_folder_of_csv_files = "./example-data/output"

    # Load dd_synth DataFrame
    logging.info(f"Loading dd_synth from file: {path_to_dd_synth}")
    dd_synth = pd.read_csv(path_to_dd_synth)

    # Synthesize data using the loaded dd_synth
    logging.info("Synthesizing data using the provided dd_synth.")
    dd_obs, dd_synth = synthesize_folder_of_csv_files(
        path_to_input_folder_of_csv_files,
        path_to_output_folder_of_csv_files,
        dd_obs=None,
        dd_synth=dd_synth,
        blanket_default_params={
            "dispersion_factor": 0.05,
            "winsorize_lower_limit": 0.05,
            "winsorize_upper_limit": 0.95,
            "p_modify_number_list_val" : 0.15
        }
    )

if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Run the main function and print the dd_obs
    main()
    
