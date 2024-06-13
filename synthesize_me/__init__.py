from synthesize_me.generate_dd_obs import generate_dd_obs
from synthesize_me.create_dd_synth import create_dd_synth
from synthesize_me.synthesize_data import create_csv_files_of_synth_data

def synthesize_folder_of_csv_files(
        path_to_input_folder_of_csv_files,
        path_to_output_folder_of_csv_files,
        dd_obs=None,
        dd_synth=None,
        blanket_default_params={
            "dispersion_factor": 0.05,
            "winsorize_lower_limit": 0.05,
            "winsorize_upper_limit": 0.95
        }
):
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
