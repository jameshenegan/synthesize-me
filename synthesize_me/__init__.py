from synthesize_me.generate_dd_obs import generate_dd_obs
from synthesize_me.create_dd_synth import create_dd_synth
from synthesize_me.synthesize_data import create_csv_files_of_synth_data
import pandas as pd
from typing import Optional, Tuple, Dict

def synthesize_folder_of_csv_files(
        path_to_input_folder_of_csv_files: str,
        path_to_output_folder_of_csv_files: str,
        dd_obs: Optional[pd.DataFrame] = None,
        dd_synth: Optional[pd.DataFrame] = None,
        blanket_default_params: Optional[Dict[str, float]] = None
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Synthesize a folder of CSV files by generating synthetic data based on the provided or generated
    data dictionary (dd_obs) and synthesis instructions (dd_synth).

    Parameters:
    - path_to_input_folder_of_csv_files (str): Path to the input folder containing CSV files.
    - path_to_output_folder_of_csv_files (str): Path to the output folder where synthetic CSV files will be saved.
    - dd_obs (Optional[pd.DataFrame]): Data dictionary of observed data statistics. If None, it will be generated.
    - dd_synth (Optional[pd.DataFrame]): Data dictionary of synthesis instructions. If None, it will be created.
    - blanket_default_params (Optional[Dict[str, float]]): Default parameters for synthesis. If None, default values are used.

    Returns:
    - Tuple[pd.DataFrame, pd.DataFrame]: The generated or provided dd_obs and dd_synth DataFrames.
    """
    if blanket_default_params is None:
        blanket_default_params = {
            "dispersion_factor": 0.05,
            "winsorize_lower_limit": 0.05,
            "winsorize_upper_limit": 0.95,
            "p_modify_number_list_val": 0.15,
            "default_decimal_method": "add_normal_noise",
            "default_integer_method": "add_normal_noise_and_round",
            "default_numberlist_method": "random_shuffle",
        }

    # If a dd_obs has not been provided, generate dd_obs
    if dd_obs is None:
        dd_obs = generate_dd_obs(path_to_input_folder_of_csv_files)

    # If a dd_synth has not been provided, create dd_synth
    if dd_synth is None:
        dd_synth = create_dd_synth(dd_obs, blanket_default_params)

    # Create synthetic CSV files
    create_csv_files_of_synth_data(
        dd_synth,
        path_to_input_folder_of_csv_files,
        path_to_output_folder_of_csv_files
    )

    # Return the dd_obs and the dd_synth
    return dd_obs, dd_synth
