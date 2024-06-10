def synthesize_folder_of_csv_files(
        path_to_input_folder_of_csv_files,
        path_to_output_folder_of_csv_files,
        dd_obs=None,
        dd_synth=None,
        blanket_default_params = {
            "dispersion_factor" : 0.05,
            "winsorize_lower_limit" : 0.05,
            "winsorize_upper_limit" : 0.95
        }        
):
    # If a dd_obs has not been provided, then
    # generate dd_obs (summary statistics) based on the input folder of CSV files
        
    if not dd_obs:
        dd_obs = generate_dd_obs(path_to_input_folder_of_csv_files)      

    # If a dd_synth has not been provided, then
    # create a dd_synth based on the dd_obs and the blanket_default_params .
    elif dd_obs and not dd_synth:
        dd_synth = create_dd_synth(dd_obs, blanket_default_params)        

    # Apply the dd_synth to the input folder of CSV files
    # to create CSV files of synthetic data in the output folder of CSV files
    create_csv_files_of_synth_data(
        dd_synth,
        path_to_input_folder_of_csv_files,
        path_to_output_folder_of_csv_files
        )
    
    # Return the dd_obs and the dd_synth
    return dd_obs, dd_synth


def generate_dd_obs(path_to_input_folder_of_csv_files):
    pass


def create_dd_synth(dd_obs):
    pass


def create_csv_files_of_synth_data(
        dd_synth,
        path_to_input_folder_of_csv_files,
        path_to_output_folder_of_csv_files
):
    pass