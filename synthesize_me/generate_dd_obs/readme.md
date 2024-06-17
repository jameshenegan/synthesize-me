# `generate_dd_obs` Module

The `generate_dd_obs` module is responsible for creating the `dd_obs` DataFrame, which includes inferred data types and summary statistics for each variable in the input CSV files. This DataFrame is essential for understanding the structure and characteristics of the data, and it serves as the basis for generating the `dd_synth`.

## Functions

### `generate_dd_obs`

This function generates the `dd_obs` DataFrame by processing all CSV files in the specified input directory.

**Parameters:**

- `path_to_input_folder_of_csv_files` (str): The path to the directory containing the input CSV files.

**Returns:**

- `dd_obs_df` (pd.DataFrame): A DataFrame containing the inferred data types and summary statistics for each variable in the input CSV files.

**Example:**

```python
from synthesize_me.generate_dd_obs import generate_dd_obs

path_to_input_folder = 'path/to/input/folder'
dd_obs_df = generate_dd_obs(path_to_input_folder)
print(dd_obs_df)
```

### `make_dd_obs_data_for_table`

This helper function processes a single CSV file and generates summary statistics for each variable in the file.

**Parameters:**

- `input_dir` (str): The directory containing the input CSV file.
- `file_name` (str): The name of the CSV file.

**Returns:**

- `dd_obs_data` (list): A list of dictionaries, each containing summary statistics for a variable in the table.

## Summary Statistics

The `dd_obs` DataFrame includes the following columns for each variable:

- **table_name**: The name of the table containing the variable (derived from the CSV file name).
- **var_name**: The name of the variable.
- **obs_datatype**: The inferred data type of the variable (e.g., String, Decimal, Integer, NumberList, etc.).
- **obs_mean**: The mean value of the variable.
- **obs_std**: The standard deviation of the variable.
- **obs_min**: The minimum observed value of the variable.
- **obs_p_25**: The 25th percentile value of the variable.
- **obs_median**: The median value of the variable.
- **obs_p_75**: The 75th percentile value of the variable.
- **obs_max**: The maximum observed value of the variable.

## Example Usage

Here is an example of how to use the `generate_dd_obs` function to create a `dd_obs` DataFrame:

```python
from synthesize_me.generate_dd_obs import generate_dd_obs

# Define the path to the input folder containing CSV files
path_to_input_folder = 'path/to/input/folder'

# Generate the dd_obs DataFrame
dd_obs_df = generate_dd_obs(path_to_input_folder)

# Display the resulting DataFrame
print(dd_obs_df)
```

## How It Works

1. **Initialization**: The `generate_dd_obs` function initializes an empty list to hold the `dd_obs` data for all tables in the input directory.

2. **File Processing**: The function iterates over each file in the input directory. For each CSV file, it calls the `make_dd_obs_data_for_table` function.

3. **Data Aggregation**: The `make_dd_obs_data_for_table` function reads the CSV file into a DataFrame, infers the data type for each variable using the `guess_data_type` function, and computes summary statistics. These statistics are collected in a list of dictionaries.

4. **DataFrame Creation**: The collected data is then converted into a DataFrame (`dd_obs_df`), which is returned by the `generate_dd_obs` function.

## Dependencies

- `numpy`
- `pandas`
- `os`

Ensure you have these packages installed in your environment.

## Next Steps

### Additional summary statistics

Think about what other summary statistics we should add to the `dd_obs`.
