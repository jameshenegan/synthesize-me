import pandas as pd
import os

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

def synthesize_table_data(df, dd_synth_table):
    # Synthesize data based on the dd_synth_table
    synth_df = df.copy()
    for _, row in dd_synth_table.iterrows():
        var_name = row['var_name']
        if row['datatype'] == 'Decimal':
            synth_df[var_name] = synthesize_decimal_column(
                df[var_name],
                row['dispersion_amount'],
                row['winsorize_lower_limit'],
                row['winsorize_upper_limit']
            )
        # Add other data types synthesis as needed

    return synth_df

def synthesize_decimal_column(series, dispersion_amount, winsorize_lower_limit, winsorize_upper_limit):
    # Example synthesis logic for Decimal data type
    lower_bound = series.quantile(winsorize_lower_limit)
    upper_bound = series.quantile(winsorize_upper_limit)
    series = series.clip(lower=lower_bound, upper=upper_bound)
    noise = pd.Series([dispersion_amount] * len(series))
    return series + noise

# Add other synthesis functions as needed
