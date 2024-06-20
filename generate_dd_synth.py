import argparse
import logging
import pandas as pd
import numpy as np 

from synthesize_me.create_dd_synth import create_dd_synth

def main(input_file, output_file, dispersion_factor, winsorize_lower_limit, winsorize_upper_limit):
    """
    Generate the dd_synth DataFrame and save it to a CSV file.

    Parameters:
    input_file (str): Path to the dd_obs CSV file.
    output_file (str): Path to save the generated dd_synth CSV file.
    dispersion_factor (float): Default dispersion factor for the synthesis.
    winsorize_lower_limit (float): Default winsorize lower limit for the synthesis.
    winsorize_upper_limit (float): Default winsorize upper limit for the synthesis.
    """
    # Load dd_obs DataFrame
    logging.info(f"Loading dd_obs from file: {input_file}")
    dd_obs = pd.read_csv(input_file)

    # Set blanket default parameters
    blanket_default_params =  {
        "dispersion_factor": 0.05,
        "winsorize_lower_limit": 0.05,
        "winsorize_upper_limit": 0.95,
        "p_modify_number_list_val" : 0.15,
        "default_decimal_method" : "add_normal_noise",
        "default_integer_method" : "add_normal_noise_and_round",
        "default_numberlist_method" : "random_shuffle",
    }

    # Generate dd_synth DataFrame
    logging.info("Generating dd_synth with default parameters.")
    dd_synth = create_dd_synth(dd_obs, blanket_default_params)

    # Update certain rows of the dd_synth
    for i, row in dd_synth.iterrows():

        # Update the dd_synth for variables with a 'var_name' of 'id_number'
        if row['var_name'] == 'id_number':

            # Make it so these variables don't get synthesized
            dd_synth.at[i, 'should_be_synthesized'] = 0
            
            # Remove other information in the dd_synth for these variables
            values_to_remove = [c for c in dd_synth.columns if c not in [
                'table_name',
                'var_name',
                'should_be_synthesized'
                ]
            ]

            for v in values_to_remove:
                dd_synth.at[i, v] = np.nan

        if row['var_name'] == 'Normal_Mean5_SD2':
            dd_synth.at[i, 'method'] = 'winsorize_and_add_normal_noise'



    # Save dd_synth to CSV
    logging.info(f"Saving dd_synth to output file: {output_file}")
    dd_synth.to_csv(output_file, index=False)
    logging.info("dd_synth generation and saving completed successfully.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate the dd_synth DataFrame and save it to a CSV file.')
    parser.add_argument('input_file', type=str, help='Path to the dd_obs CSV file.')
    parser.add_argument('output_file', type=str, help='Path to save the generated dd_synth CSV file.')
    parser.add_argument('--dispersion_factor', type=float, default=0.05, help='Default dispersion factor for the synthesis.')
    parser.add_argument('--winsorize_lower_limit', type=float, default=0.05, help='Default winsorize lower limit for the synthesis.')
    parser.add_argument('--winsorize_upper_limit', type=float, default=0.95, help='Default winsorize upper limit for the synthesis.')

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    main(args.input_file, args.output_file, args.dispersion_factor, args.winsorize_lower_limit, args.winsorize_upper_limit)
