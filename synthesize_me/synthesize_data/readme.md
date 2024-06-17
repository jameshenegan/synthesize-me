# `synthesize_data` Module

The `synthesize_data` module is responsible for applying synthesis instructions to generate synthetic CSV files. This module processes the synthesis instructions from `dd_synth` and applies them to the input CSV files to create synthetic versions.

## Functions

### `create_csv_files_of_synth_data`

This function generates synthetic CSV files based on the synthesis instructions provided in `dd_synth`.

**Parameters:**

- `dd_synth` (pd.DataFrame): The DataFrame containing synthesis instructions for each variable.
- `path_to_input_folder_of_csv_files` (str): The path to the directory containing the input CSV files.
- `path_to_output_folder_of_csv_files` (str): The path to the directory where the synthetic CSV files will be saved.

**Example:**

```python
from synthesize_me.synthesize_data import create_csv_files_of_synth_data

# Define paths
input_folder = 'path/to/input/folder'
output_folder = 'path/to/output/folder'

# Load the dd_synth DataFrame
dd_synth = pd.read_csv('path/to/dd_synth.csv')

# Generate synthetic data
create_csv_files_of_synth_data(dd_synth, input_folder, output_folder)
```

## Next Steps

### NumberList

Come up with another method for synthesizing a columns of NumberList data type. Instead of changing to a random value, change to a neighboring value.

Think about how to store the metadata for this.

#### Documentation

Add documentation.

### Integer

Come up with at least one method to generate synthetic data for a variable that is of Integer data type.

Think about how to store the metadata for this.

#### Documentation

Add documentation.

### Decimal

Include alternative methods for synthesizing a variable that is of Decimal data type.

Think about how to store the metadata for this.

Ensure that synthesized data is in the range of the original data.

#### Documentation

Add documentation.
