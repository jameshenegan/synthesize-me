# `synthesize_me` Package

The `synthesize_me` package is designed to generate synthetic versions of CSV files. It provides functions to generate summary statistics, create synthesis instructions, and apply these instructions to generate synthetic data. The main functionality is encapsulated in the `synthesize_folder_of_csv_files` function.

## Functions

### `synthesize_folder_of_csv_files`

This function orchestrates the process of generating synthetic CSV files from an input folder. It can generate the necessary summary statistics and synthesis instructions if they are not provided.

**Parameters:**

- `path_to_input_folder_of_csv_files` (str): The path to the directory containing the input CSV files.
- `path_to_output_folder_of_csv_files` (str): The path to the directory where the synthetic CSV files will be saved.
- `dd_obs` (pd.DataFrame, optional): The DataFrame containing summary statistics for each variable. If not provided, it will be generated.
- `dd_synth` (pd.DataFrame, optional): The DataFrame containing synthesis instructions for each variable. If not provided, it will be created based on `dd_obs` and `blanket_default_params`.
- `blanket_default_params` (dict, optional): Default parameters for data synthesis. Default values are:
  - `dispersion_factor`: 0.05
  - `winsorize_lower_limit`: 0.05
  - `winsorize_upper_limit`: 0.95

**Returns:**

- `dd_obs` (pd.DataFrame): The DataFrame containing summary statistics for each variable.
- `dd_synth` (pd.DataFrame): The DataFrame containing synthesis instructions for each variable.

**Example:**

```python
from synthesize_me import synthesize_folder_of_csv_files

# Define paths
input_folder = 'path/to/input/folder'
output_folder = 'path/to/output/folder'

# Generate synthetic data
dd_obs, dd_synth = synthesize_folder_of_csv_files(input_folder, output_folder)
print(dd_obs)
print(dd_synth)
```

### `create_csv_files_of_synth_data`

This helper function applies the synthesis instructions from `dd_synth` to the input CSV files and generates synthetic CSV files in the output folder.

**Parameters:**

- `dd_synth` (pd.DataFrame): The DataFrame containing synthesis instructions for each variable.
- `path_to_input_folder_of_csv_files` (str): The path to the directory containing the input CSV files.
- `path_to_output_folder_of_csv_files` (str): The path to the directory where the synthetic CSV files will be saved.

## How It Works

1. **Generate or Use Provided `dd_obs`**: If `dd_obs` is not provided, the function generates it using the `generate_dd_obs` function, which computes summary statistics for each variable in the input CSV files.
2. **Create or Use Provided `dd_synth`**: If `dd_synth` is not provided, the function creates it using the `create_dd_synth` function, which applies the `blanket_default_params` to the summary statistics in `dd_obs`.
3. **Generate Synthetic CSV Files**: The function applies the synthesis instructions from `dd_synth` to the input CSV files, creating synthetic versions and saving them to the output folder.

## Dependencies

- `numpy`
- `pandas`
- `os`

Ensure you have these packages installed in your environment.

## Example Usage

Here is an example of how to use the `synthesize_folder_of_csv_files` function to generate synthetic CSV files:

```python
from synthesize_me import synthesize_folder_of_csv_files

# Define the paths to the input and output folders
input_folder = 'path/to/input/folder'
output_folder = 'path/to/output/folder'

# Generate the synthetic CSV files
dd_obs, dd_synth = synthesize_folder_of_csv_files(input_folder, output_folder)

# Display the resulting DataFrames
print(dd_obs)
print(dd_synth)
```
