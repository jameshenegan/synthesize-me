import argparse
import logging
from synthesize_me.generate_dd_obs import generate_dd_obs

def main(input_dir, output_file):
    """
    Generate the dd_obs DataFrame and save it to a CSV file.

    Parameters:
    input_dir (str): Directory containing the input CSV files.
    output_file (str): Path to save the generated dd_obs CSV file.
    """
    # Generate dd_obs DataFrame
    logging.info(f"Generating dd_obs from input directory: {input_dir}")
    dd_obs = generate_dd_obs(input_dir)

    # Save dd_obs to CSV
    logging.info(f"Saving dd_obs to output file: {output_file}")
    dd_obs.to_csv(output_file, index=False)
    logging.info("dd_obs generation and saving completed successfully.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate the dd_obs DataFrame and save it to a CSV file.')
    parser.add_argument('input_dir', type=str, help='Directory containing the input CSV files.')
    parser.add_argument('output_file', type=str, help='Path to save the generated dd_obs CSV file.')

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    main(args.input_dir, args.output_file)
